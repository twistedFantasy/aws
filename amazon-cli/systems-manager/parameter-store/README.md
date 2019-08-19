## Amazon Parameter Store
1. Create new parameter
```
$ aws ssm put-parameter --name /dev/test/TEST_PARAM_ID --description "Test description" 
--value "test_password" --type "String" --no-overwrite --tags Key=Name,Value=dev_test --profile amazon-cli
```

### Useful resources:
* [Amazon System Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
* [Amazon CLI: System Manager Parameter Store](https://docs.aws.amazon.com/cli/latest/reference/ssm/index.html#cli-aws-ssm)
