import json
import logging
import sys

import argparse
import boto3


def print_instances(the_instances):
    # Your default security group does not allow incoming SSH traffic by default.
    for i in the_instances:
        current_state = i.state['Name']
        log.info("Instance {}/{}: {} [{}] ssh-key={} ".format(i.instance_type, i.image_id, i.id, current_state, i.key_name))
        if current_state != "terminated":
            log.debug("  ssh ec2-user@{} / {} ({})".format(i.public_dns_name, i.public_ip_address, i.private_ip_address))
            log.debug("  security groups: {}".format(i.security_groups))
            log.debug("  [{}] root storage is {}".format(i.root_device_type, i.root_device_name))


def get_running_instances():
    return ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


def get_all_instances():
    return ec2.instances.filter()


def get_ssh_security_group():
    ssh_group = None
    all_vpcs = ec2_client.describe_vpcs()
    for vpc in all_vpcs['Vpcs']:
        if vpc['IsDefault']:
            default_vpc = vpc

    all_sec_groups = ec2_client.describe_security_groups()
    # VPC = ec2.Vpc(default_vpc.VpcId)

    for grp in all_sec_groups['SecurityGroups']:
        for permission in grp['IpPermissions']:
            if 'ToPort' in permission and 22 == permission['ToPort']:
                ssh_group = grp

    my_security_group = ec2.SecurityGroup(ssh_group['GroupId'])
    # might be useful
    # my_security_group.id
    # my_security_group.vpc_id
    return [my_security_group.group_name]


if __name__ == "__main__":
    # todo select AMI instance type
    # todo instance type ???
    # todo object(s)
    # todo add new security group which allows SSH
    # todo check ResponseMetadata
    # todo IPv6 support

    logging.basicConfig(format='%(asctime)-15s %(funcName)s %(message)s')
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    # log.addHandler(logging.StreamHandler(stream=sys.stdout))

    instances = None
    # magic by default
    option = sys.argv[1] if len(sys.argv) > 1 else "magic"

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--action", type=str, default="list-all", choices=["list-all", "list-running", "start", "stop"],
                            help="perform one of the actions presented")
    arg_parser.add_argument("-v", help="run with debug logging", action="store_true")  # todo check if it actually works, optional

    my_args = arg_parser.parse_args()

    log.info("action selected [{}]".format(my_args.action))

    # todo list-all is default
    # todo start / stop - can take optional pem
    # todo key - can take optional filename
    # todo default filename needs to be set
    #
    # todo create - can take # of instances (not yet)

    ami_image = 'ami-6869aa05'  # amazon 2016.03.3
    ec2 = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    image = ec2.Image(ami_image)
    log.debug("AMI name= {} [{}]".format(image.name, image.virtualization_type))
    log.debug("block device= {}".format(image.block_device_mappings))

    # region see/select
    regions = ec2_client.describe_regions()
    log.debug("regions {}".format(json.dumps(regions, indent=2)))

    if option == "magic":
        # todo check_if_allow_ssh_group_is_present
        log.info("ssh group = {}".format(get_ssh_security_group()))

    if my_args.action == "start":
        se_groups = get_ssh_security_group()
        instances = ec2.create_instances(ImageId=ami_image, MinCount=1, MaxCount=1, InstanceType='t2.micro',
                                         KeyName='temp_key', Monitoring={'Enabled': False}, SecurityGroups=se_groups)
        print_instances(instances)

    elif option == "stop":
        # ids = ['instance-id-1', 'instance-id-2', ...]
        my_instances = get_running_instances()
        # ec2_client.stop_instances(InstanceIds=my_instances)
        # ec2_client.terminate_instances(InstanceIds=my_instances)
        my_instances_ids = [i.id for i in my_instances]
        ec2.instances.filter(InstanceIds=my_instances_ids).stop()
        ec2.instances.filter(InstanceIds=my_instances_ids).terminate()

    elif my_args.action == "list-all":
        # Boto 3:  # Use the filter() method of the instances collection to retrieve
        # all running EC2 instances.
        all_instances = get_all_instances()
        print_instances(all_instances)

    elif my_args.action == "list-running":
        run_instances = get_running_instances()
        print_instances(run_instances)

    elif option == "keypair":
        key_name = 'temp_key'
        keypair = ec2_client.create_key_pair(KeyName=key_name)
        private_key = keypair['KeyMaterial']
        fingerprint_key = keypair['KeyFingerprint']
        # save private key to a file
        with open('{}.pem'.format(key_name), "wt") as private_key_file:
            private_key_file.write(private_key)
            # '-----BEGIN RSA PRIVATE KEY-----
