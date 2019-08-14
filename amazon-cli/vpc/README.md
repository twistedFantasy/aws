## Amazon VPC

1. Create new VPC
```
$ aws ec2 create-vpc --cidr-block 10.0.0.0/16 --dry-run --profile amazon-cli
An error occurred (DryRunOperation) when calling the CreateVpc operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-vpc --cidr-block 10.0.0.0/16 --profile amazon-cli
{
    "Vpc": {
        "CidrBlock": "10.0.0.0/16",
        "DhcpOptionsId": "dopt-fc649e99",
        "State": "pending",
        "VpcId": "vpc-08f9545974e11ab62",
        "OwnerId": "383820954082",
        "InstanceTenancy": "default",
        "Ipv6CidrBlockAssociationSet": [],
        "CidrBlockAssociationSet": [
            {
                "AssociationId": "vpc-cidr-assoc-0302a1fad188c9cab",
                "CidrBlock": "172.21.0.0/16",
                "CidrBlockState": {
                    "State": "associated"
                }
            }
        ],
        "IsDefault": false,
        "Tags": []
    }
}
```
2. Add "dev-test" tag using "VpcID" attribute value
```
$ aws ec2 create-tags --resources vpc-08f9545974e11ab62 --tags Key=Name,Value=dev-test --profile amazon-cli
```

3. Enable DNS resolution and DNS hostnames for VPC
```
$ aws ec2 modify-vpc-attribute --vpc-id vpc-08f9545974e11ab62 --enable-dns-hostnames --profile amazon-cli

$ aws ec2 modify-vpc-attribute --vpc-id vpc-08f9545974e11ab62 --enable-dns-support --profile amazon-cli
```

4. Create 2 private subnets for VPC
```
$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.1.0/24 --availability-zone us-east-1a --dry-run --profile amazon-cli
 
An error occurred (DryRunOperation) when calling the CreateSubnet operation: Request would have succeeded, but DryRun flag is set.
 
$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.2.0/24 --availability-zone us-east-1b --dry-run --profile amazon-cli
 
An error occurred (DryRunOperation) when calling the CreateSubnet operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.1.0/24 --availability-zone us-east-1a --profile amazon-cli
{
    "Subnet": {
        "AvailabilityZone": "us-east-1a",
        "AvailabilityZoneId": "use1-az6",
        "AvailableIpAddressCount": 251,
        "CidrBlock": "10.0.1.0/24",
        "DefaultForAz": false,
        "MapPublicIpOnLaunch": false,
        "State": "pending",
        "SubnetId": "subnet-MIm6AsKaiDIHbh464",
        "VpcId": "vpc-08f9545974e11ab62",
        "OwnerId": "091344251555",
        "AssignIpv6AddressOnCreation": false,
        "Ipv6CidrBlockAssociationSet": [],
        "SubnetArn": "arn:aws:ec2:us-east-1:091344251555:subnet/subnet-MIm6AsKaiDIHbh464"
    }
}

$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.2.0/24 --availability-zone us-east-1b --profile amazon-cli
{
    "Subnet": {
        "AvailabilityZone": "us-east-1b",
        "AvailabilityZoneId": "use1-az1",
        "AvailableIpAddressCount": 251,
        "CidrBlock": "10.0.2.0/24",
        "DefaultForAz": false,
        "MapPublicIpOnLaunch": false,
        "State": "pending",
        "SubnetId": "subnet-dy5V8R4UMH5DsOhfT",
        "VpcId": "vpc-08f9545974e11ab62",
        "OwnerId": "091344251555",
        "AssignIpv6AddressOnCreation": false,
        "Ipv6CidrBlockAssociationSet": [],
        "SubnetArn": "arn:aws:ec2:us-east-1:091344251555:subnet/subnet-dy5V8R4UMH5DsOhfT"
    }
}
```

5. Add "dev_test_public" and "dev_test_private" tags for 2 subnets
```
$ aws ec2 create-tags --resources subnet-MIm6AsKaiDIHbh464 --tags Key=Name,Value=dev_test_public --profile amazon-cli

$ aws ec2 create-tags --resources subnet-dy5V8R4UMH5DsOhfT --tags Key=Name,Value=dev_test_private --profile amazon-cli
```

6. Create Internet Gateway for public subnet
```
$ aws ec2 create-internet-gateway --dry-run --profile amazon-cli

An error occurred (DryRunOperation) when calling the CreateInternetGateway operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-internet-gateway --profile amazon-cli
{
    "InternetGateway": {
        "Attachments": [],
        "InternetGatewayId": "igw-DrQeEv8y2Gnqp1j1U",
        "Tags": []
    }
}
```

7. Add "dev_test" tag to internet gateway
```
$ aws ec2 create-tags --resources igw-DrQeEv8y2Gnqp1j1U --tags Key=Name,Value=dev_test --profile amazon-cli
```

8. Attach internet gateway to VPC
```
$ aws ec2 attach-internet-gateway --internet-gateway-id igw-DrQeEv8y2Gnqp1j1U --vpc-id vpc-08f9545974e11ab62 --dry-run --profile amazon-cli 

An error occurred (DryRunOperation) when calling the AttachInternetGateway operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 attach-internet-gateway --internet-gateway-id igw-DrQeEv8y2Gnqp1j1U --vpc-id vpc-08f9545974e11ab62 --profile amazon-cli 
```

9. Create route table for public subnet
```
$ aws ec2 create-route-table --vpc-id vpc-08f9545974e11ab62 --dry-run --profile amazon-cli

An error occurred (DryRunOperation) when calling the CreateRouteTable operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-route-table --vpc-id vpc-08f9545974e11ab62 --profile amazon-cli
{
    "RouteTable": {
        "Associations": [],
        "PropagatingVgws": [],
        "RouteTableId": "rtb-ovDUnWTdsWhAoSD1W",
        "Routes": [
            {
                "DestinationCidrBlock": "10.0.0.0/16",
                "GatewayId": "local",
                "Origin": "CreateRouteTable",
                "State": "active"
            }
        ],
        "Tags": [],
        "VpcId": "vpc-08f9545974e11ab62",
        "OwnerId": "091344251555"
    }
}
```

10. Add "dev_test_public" tag to route table
```
$ aws ec2 create-tags --resources rtb-ovDUnWTdsWhAoSD1W --tags Key=Name,Value=dev_test_public --profile amazon-cli
```

11. Create new route in route table to enable internet access
```
$ aws ec2 create-route --route-table-id rtb-ovDUnWTdsWhAoSD1W --destination-cidr-block 0.0.0.0/0 --gateway-id igw-DrQeEv8y2Gnqp1j1U --dry-run --profile amazon-cli

An error occurred (DryRunOperation) when calling the ReplaceRoute operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-route --route-table-id rtb-ovDUnWTdsWhAoSD1W --destination-cidr-block 0.0.0.0/0 --gateway-id igw-DrQeEv8y2Gnqp1j1U --profile amazon-cli
{
    "Return": true
}
```
12. Associate route table with public access to subnet to make it public
```
$ aws ec2 associate-route-table --route-table-id rtb-ovDUnWTdsWhAoSD1W --subnet-id subnet-MIm6AsKaiDIHbh464 --dry-run --profile amazon-cli

An error occurred (DryRunOperation) when calling the AssociateRouteTable operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 associate-route-table --route-table-id rtb-ovDUnWTdsWhAoSD1W --subnet-id subnet-MIm6AsKaiDIHbh464 --profile amazon-cli
{
    "AssociationId": "rtbassoc-quouVgtoo6yK05h2u"
}
```

### Useful resources:
* [Amazon VPC](https://aws.amazon.com/vpc/)
* [Amazon CLI: VPC](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html#cli-aws-ec2)
* [Amazon AWS: VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
* [Amazon CLI: Create tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html)
