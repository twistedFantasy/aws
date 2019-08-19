## Amazon Parameter Store
1. Create new parameter
```
$ aws ssm put-parameter --name /dev/test/TEST_PARAM_ID --description "Test description" 
--value "test_password" --type "String" --no-overwrite --tags Key=Name,Value=dev_test --profile amazon-cli
```
