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

3. Create 2 subnets for VPC
```redshift
$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.0.0/24 --availability-zone us-east-1e --dry-run --profile amazon-cli
 
An error occurred (DryRunOperation) when calling the CreateSubnet operation: Request would have succeeded, but DryRun flag is set.
 
$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.2.0/24 --availability-zone us-east-1c --dry-run --profile amazon-cli
 
An error occurred (DryRunOperation) when calling the CreateSubnet operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.0.0/24 --availability-zone us-east-1e --profile amazon-cli

$ aws ec2 create-subnet --vpc-id vpc-08f9545974e11ab62 --cidr-block 10.0.2.0/24 --availability-zone us-east-1c --profile amazon-cli
```

4. Add "dev_test" tag for 2 subnets
```
$ aws ec2 create-tags --resources subnet-vn5gcG7YPARwteVJ2 subnet-hoRE94lq9M9PI0uDj --tags Key=Name,Value=dev_test --profile amazon-cli
```

### Useful resources:
* [Amazon VPC](https://aws.amazon.com/vpc/)
* [Amazon CLI: VPC](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html#cli-aws-ec2)
* [Amazon AWS: VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)
* [Amazon CLI: Create tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html)
