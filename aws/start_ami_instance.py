import boto3

if __name__ == "__main__":
    ami_image = 'ami-60b6c60a'  # Amazon Linux

    ec2 = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    image = ec2.Image(ami_image)
    print("AMI name= {} [{}]".format(image.name, image.virtualization_type))
    print("block device= {}".format(image.block_device_mappings))

    #
    keypair = ec2_client.create_key_pair(KeyName='temp_key')
    private_key = keypair['KeyMaterial']
    # save private key to a file
    with open('temp_key.pem', "wt") as private_key_file:
        private_key_file.write(private_key)
    # '-----BEGIN RSA PRIVATE KEY-----



    instance = ec2.instance(ami_image)

    # ec2 = boto3.EC2.ServiceResource()
    # ec2.create_instances(ImageId='ami-60b6c60a', MinCount=1, MaxCount=1)
    # start multiple instances - InstanceIds =
    # ec2_client = boto3.client('ec2')
