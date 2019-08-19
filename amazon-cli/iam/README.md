## Amazon IAM

1. Create new "TestRole" role for Amazon Redshift service
```
$ aws iam create-role --role-name "TestRole" --assume-role-policy-document file://trust.json --profile amazon-cli
```

2. Attach different polices(AmazonS3FullAccess, AmazonRedshiftFullAccess) for "TestRole"
```
$ aws iam attach-role-policy --role-name "TestRole" --policy-arn "arn:aws:iam::aws:policy/AmazonS3FullAccess" --profile amazon-cli
$ aws iam attach-role-policy --role-name "TestRole" --policy-arn "arn:aws:iam::aws:policy/AmazonRedshiftFullAccess" --profile amazon-cli
```

### Useful Resources
* [Amazon IAM](https://aws.amazon.com/iam/)
* [Amazon CLI: IAM](https://docs.aws.amazon.com/cli/latest/reference/iam/)
* [Back to School: Understanding the IAM Policy Grammar](https://aws.amazon.com/blogs/security/back-to-school-understanding-the-iam-policy-grammar/)
