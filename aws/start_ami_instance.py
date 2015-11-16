from pprint import pprint

import boto3
import sys

if __name__ == "__main__":
    dry_run = True
    instances = None
    option = sys.argv[1] if len(sys.argv) > 1 else "nothing"
    ami_image = 'ami-60b6c60a'  # Amazon Linux

    ec2 = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    image = ec2.Image(ami_image)
    print("AMI name= {} [{}]".format(image.name, image.virtualization_type))
    print("block device= {}".format(image.block_device_mappings))

    if option == "start":
        # boto3 docs
        instances = ec2.create_instances(ImageId=ami_image, MinCount=1, MaxCount=1, InstanceType='t2.micro',
                                         KeyName='temp_key', Monitoring={'Enabled': True}, DryRun=dry_run)
        print(instances)
        for instance in instances:
            print(instance)

    if option == "stop":
        # ids = ['instance-id-1', 'instance-id-2', ...]
        ec2.instances.filter(InstanceIds=instances).stop()
        ec2.instances.filter(InstanceIds=instances).terminate()

        # instance = ec2.Instance('test-instance')
        # response = instance.start(DryRun=dry_run)
        # pprint(response)
        # response = ec2_client.start_instances(DryRun=dry_run, InstanceIds=["required"])

    if option == "list":
        # Boto 3:  # Use the filter() method of the instances collection to retrieve
        # all running EC2 instances.
        running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for instance in running_instances:
            print(instance.id, instance.instance_type)

        pprint(ec2_client.describe_instances())

    if option == "keypair":
        key_name = 'temp_key'
        keypair = ec2_client.create_key_pair(DryRun=dry_run, KeyName=key_name)
        private_key = keypair['KeyMaterial']
        # save private key to a file
        with open('{}.pem'.format(key_name), "wt") as private_key_file:
            private_key_file.write(private_key)
        # '-----BEGIN RSA PRIVATE KEY-----

