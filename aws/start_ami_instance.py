import sys

import boto3


def print_instances(the_instances):
    # debug

    # Your default security group does not allow incoming SSH traffic by default.
    for i in the_instances:
        print("-" * 50)
        current_state = i.state['Name']
        print("EC2 instance={} [{}] AMI={} ssh-key={} hypervisor={}".format(i.id, current_state, i.image_id, i.key_name, i.hypervisor))
        if current_state != "terminated":
            print("  connect: {} / {} ({})".format(i.public_dns_name, i.public_ip_address, i.private_ip_address))
            print("  security groups: {}".format(i.security_groups))
            print("  [{}] root storage is {}".format(i.root_device_type, i.root_device_name))


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
    # todo 1 region see/select
    # import pprint
    # pprint.pprint(ec2_client.describe_regions())

    # todo 2 instance type ???

    # todo 3 object(s)

    # todo 4 add new security group which allows SSH

    # todo 5 check ResponseMetadata
    instances = None
    # list by default
    option = sys.argv[1] if len(sys.argv) > 1 else "magic"

    ami_image = 'ami-60b6c60a'  # Amazon Linux

    ec2 = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    image = ec2.Image(ami_image)
    # print("AMI name= {} [{}]".format(image.name, image.virtualization_type))
    # print("block device= {}".format(image.block_device_mappings))

    if option == "magic":
        # todo check_if_allow_ssh_group_is_present
        default_vpc = None
        print(get_ssh_security_group())
        # todo create_group
        # todo get_group_name?!?

    if option == "start":
        se_groups = get_ssh_security_group()
        instances = ec2.create_instances(ImageId=ami_image, MinCount=1, MaxCount=1, InstanceType='t2.micro',
                                         KeyName='temp_key', Monitoring={'Enabled': False}, SecurityGroups=se_groups)
        print_instances(instances)

    if option == "stop":
        # ids = ['instance-id-1', 'instance-id-2', ...]
        my_instances = get_running_instances()
        # ec2_client.stop_instances(InstanceIds=my_instances)
        # ec2_client.terminate_instances(InstanceIds=my_instances)
        my_instances_ids = [i.id for i in my_instances]
        ec2.instances.filter(InstanceIds=my_instances_ids).stop()
        ec2.instances.filter(InstanceIds=my_instances_ids).terminate()

    if option == "list":
        # Boto 3:  # Use the filter() method of the instances collection to retrieve
        # all running EC2 instances.
        running_instances = get_all_instances()
        print_instances(running_instances)
        # debug
        # pprint(ec2_client.describe_instances())

    if option == "keypair":
        key_name = 'temp_key'
        keypair = ec2_client.create_key_pair(KeyName=key_name)
        private_key = keypair['KeyMaterial']
        # save private key to a file
        with open('{}.pem'.format(key_name), "wt") as private_key_file:
            private_key_file.write(private_key)
            # '-----BEGIN RSA PRIVATE KEY-----
