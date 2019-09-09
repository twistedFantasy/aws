## Amazon CloudWatch

1.Create new log group for ECS DEV environment
```
$ aws logs create-log-group --log-group-name my-logs --tags Key=Name,Value=dev-test  --profile amazon-cli
```
2. Create log stream
```
$ aws logs create-log-stream --log-group-name my-logs --log-stream-name test-stream --profile amazon-cli
```

### Useful Resources
* [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
* [Amazon CLI: CloudWatch](https://docs.aws.amazon.com/cli/latest/reference/logs/index.html#cli-aws-logs)
