## Amazon CodeDeploy
1. Create application
```
$ aws deploy create-application --application-name TestApp --compute-platform Server --profile amazon-cli
{
  "applicationId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
}
```

2. Create deployment group for application
```
$ aws deploy create-deployment-group --application-name TestApp --deployment-group-name TestGroup \
 --deployment-config-name CodeDeployDefault.OneAtATime --ec2-tag-filters Key=Name,Value=TestDemoEC2,Type=KEY_AND_VALUE \
 --service-role-arn arn:aws:iam::124394173572:role/CodeDeployServiceRole --profile amazon-cli
```

### Useful Resources
* [Amazon CodeDeploy](https://aws.amazon.com/codedeploy/)
* [Amazon CLI: CodeDeploy](https://docs.aws.amazon.com/cli/latest/reference/deploy/index.html)
