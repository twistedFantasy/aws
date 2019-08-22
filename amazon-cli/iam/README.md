## Amazon IAM

1. Create new "TestUser" user
```
$ aws iam create-user --user-name test-user --tags Key=Name,Value=dev_test --profile amazon-cli
```

2. Create a new AWS secret access key and corresponding AWS access key ID 
```
$ aws iam create-access-key --user-name test-user --profile amazon-cli
```

3. Attach full access to AWS CodeDeploy policy to user
```
$ aws iam attach-user-policy --user-name test-user --policy-arn arn:aws:iam::aws:policy/AWSCodeDeployFullAccess \
 --profile amazon-cli
```

4. Add inline policy for "TestUser" with access to selected S3 bucket
```
$ aws iam put-user-policy --user-name test-user --policy-name TestS3Policy --policy-document file://s3_policy.json \
--profile amazon-cli
```

5. Create new "TestRole" role for Amazon Redshift service
```
$ aws iam create-role --role-name "TestRole" --assume-role-policy-document file://trust.json --profile amazon-cli
```

6. Attach different polices(AmazonS3FullAccess, AmazonRedshiftFullAccess) for "TestRole"
```
$ aws iam attach-role-policy --role-name "TestRole" --policy-arn "arn:aws:iam::aws:policy/AmazonS3FullAccess" --profile amazon-cli
$ aws iam attach-role-policy --role-name "TestRole" --policy-arn "arn:aws:iam::aws:policy/AmazonRedshiftFullAccess" --profile amazon-cli
```

### Useful Resources
* [Amazon IAM](https://aws.amazon.com/iam/)
* [Amazon CLI: IAM](https://docs.aws.amazon.com/cli/latest/reference/iam/)
* [Back to School: Understanding the IAM Policy Grammar](https://aws.amazon.com/blogs/security/back-to-school-understanding-the-iam-policy-grammar/)
