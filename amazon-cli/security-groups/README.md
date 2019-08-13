## Amazon Security Groups

1. Create new Security Group
```
$ aws ec2 create-security-group --group-name dev-test --description "dev-test description" --vpc-id vpc-08f9545974e11ab62 --dry-run --profile amazon-cli
An error occurred (DryRunOperation) when calling the CreateSecurityGroup operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 create-security-group --group-name dev-test --description "dev-test description" --vpc-id vpc-08f9545974e11ab62 --profile amazon-cli
{
    "GroupId": "sg-05cb7c25b43343ff8"
}
```
2. Add "dev-test" tag using "GroupId" attribute value
```
$ aws ec2 create-tags --resources sg-05cb7c25b43343ff8 --tags Key=Name,Value=dev-test --profile amazon-cli
```
3. Modify ingress(inbound) rules for security group. Rule  changes  are propagated to instances within the security group as quickly as possible. However, a small delay might occur.
```
$ aws ec2 authorize-security-group-ingress --group-id sg-05cb7c25b43343ff8 --protocol tcp --port 3379 --cidr 0.0.0.0/0 --profile amazon-cli
```
4. Modify multiple ingress(inbound) rules in one command
```
$ aws ec2 authorize-security-group-ingress --group-id sg-05cb7c25b43343ff8 --ip-permissions IpProtocol=tcp,FromPort=3389,ToPort=3389,IpRanges='[{CidrIp=203.0.113.0/24,Description="RDP access from NY office"}]' IpProtocol=tcp,FromPort=3388,ToPort=3388,IpRanges='[{CidrIp=203.0.113.0/24,Description="Test description"}]' --profile amazon-cli
```
To modify egress(outbound) rules "authorize-security-group-egress" should be used which has the same syntax
5. To delete existing ingress(inbound) rule. To remove  a rule,  the  values that you specify (for example, ports) must match the existing rule's values exactly.
```
$ aws ec2 revoke-security-group-ingress --group-id sg-05cb7c25b43343ff8 --protocol tcp --port 3379 --cidr 0.0.0.0/0 --profile amazon-cli 
```
6. To delete multiple existing ingress(inboud) rules
```
$ aws ec2 revoke-security-group-ingress --group-id sg-05cb7c25b43343ff8 --ip-permissions IpProtocol=tcp,FromPort=3389,ToPort=3389,IpRanges='[{CidrIp=203.0.113.0/24,Description="RDP access from NY office"}]' IpProtocol=tcp,FromPort=3388,ToPort=3388,IpRanges='[{CidrIp=203.0.113.0/24,Description="Test description"}]' --profile amazon-cli
```

### Useful Resources
* [Amazon Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
* [Amazon CLI: Security Groups](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-sg.html)
* [Amazon CLI: Security Groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/index.html#cli-aws-ec2)
* [Amazon CLI: Create tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html)

