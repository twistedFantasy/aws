## Amazon Target Groups

1. Create target group
```
$ aws elbv2 create-target-group --name TestTargetGroup --protocol HTTP --port 8080 --vpc-id vpc-08f9545974e11ab62 \
--health-check-protocol HTTP --health-check-port 8080 --health-check-enabled --health-check-path "/" \
--health-check-interval-seconds 30 --health-check-timeout-seconds 5 \
--healthy-threshold-count 5 --unhealthy-threshold-count 2 --target-type instance --profile amazon-cli
{
    "TargetGroups": [
        {
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:195333857493:targetgroup/TestTargetGroup/0493e9485743921e",
            "TargetGroupName": "TestTargetGroup",
            "Protocol": "HTTP",
            "Port": 8080,
            "VpcId": "vpc-08f9545974e11ab62",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckPort": "8080",
            "HealthCheckEnabled": true,
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 5,
            "HealthyThresholdCount": 5,
            "UnhealthyThresholdCount": 2,
            "HealthCheckPath": "/",
            "Matcher": {
                "HttpCode": "200"
            },
            "TargetType": "instance"
        }
    ]
}
```

2. Register new targets in target group
```
$ aws elbv2 register-targets --target-group-arn arn:aws:elasticloadbalancing:us-east-1:195333857493:targetgroup/TestTargetGroup/0493e9485743921e \
--targets --targets Id=i-1234567890abcdef0 Id=i-0abcdef1234567890 --profile amazon-cli
```

### Useful Resources
* [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
* [Amazon CLI: Elastic Load Balancing](https://docs.aws.amazon.com/cli/latest/reference/elbv2/index.html#cli-aws-elbv2)
