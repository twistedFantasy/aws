1. Install Amazon CLI
```
$ pip3 install awscli --upgrade --user
```
Link: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

2. Configure Amazon CLI
2.1. Create new user in Amazon AWS IAM with needed permissions. Can have full access for all Amazon AWS resource:
"AdministratorAccess" policy. Or can be attached only policies for needed resources,
for example: AmazonVPCFullAccess, AmazonRedshiftFullAccess, AmazonEC2FullAccess, IAMFullAccess, etc...
2.2. Configure new "amazon-cli" profile. Credentials used below is not valid and provided like an example.
```
$ aws configure --profile amazon-cli
AWS Access Key ID [None]: AKIAI44QH8DHBEXAMPLE
AWS Secret Access Key [None]: je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: json
```
Link: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

* [Amazon Virtual Private Cloud(VPC)](./vpc/README.md)
* [Amazon Security Groups](./security-groups/README.md)
* [Amazon Redshift](./redshift/README.md)
* [Amazon Identity and Access Management(IAM)](./iam/README.md)
* [Amazon Relationship Database Service(RDS)](./rds/README.md)
