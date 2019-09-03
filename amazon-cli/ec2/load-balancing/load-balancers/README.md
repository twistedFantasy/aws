## Amazon Load Balancers

1. Create new application load balancer
```
$ aws elbv2 create-load-balancer --name TestLoadBalancer --subnets subnet-MIm6AsKaiDIHbh464 \
--security-groups sg-05cb7c25b43343ff8 --scheme internet-facing --tags Key=Name,Value=dev_test \
--type application --ip-address-type ipv4 --profile amazon-cli
{
    "LoadBalancers": [
        {
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:195333857493:loadbalancer/app/TestLoadBalancer/4938wv9943q4b5tl",
            "DNSName": "TestLoadBalancer-2385943923.us-east-1.elb.amazonaws.com",
            "CanonicalHostedZoneId": "W29OVFFUYW6P8P",
            "CreatedTime": "2019-09-03T17:05:31.760Z",
            "LoadBalancerName": "TestLoadBalancer",
            "Scheme": "internet-facing",
            "VpcId": "vpc-08f9545974e11ab62",
            "State": {
                "Code": "provisioning"
            },
            "Type": "application",
            "AvailabilityZones": [
                {
                    "ZoneName": "us-east-1a",
                    "SubnetId": "subnet-MIm6AsKaiDIHbh464"
                },
                {
                    "ZoneName": "us-east-1b",
                    "SubnetId": "subnet-dy5V8R4UMH5DsOhfT"
                }
            ],
            "SecurityGroups": [
                "sg-05cb7c25b43343ff8"
            ],
            "IpAddressType": "ipv4"
        }
    ]
}
```

2. Create new listener for Application Load Balancer
```
$ aws elbv2 create-listener --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:195333857493:loadbalancer/app/TestLoadBalancer/4938wv9943q4b5tl \
--protocol HTTP --port 80 --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:195333857493:targetgroup/TestTargetGroup/0493e9485743921e \
--profile amazon-cli
{
    "Listeners": [
        {
            "ListenerArn": "arn:aws:elasticloadbalancing:us-east-1:195333857493:listener/app/TestLoadBalancer/4938wv9943q4b5tl/a32p4532b543p6yt",
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:195333857493:loadbalancer/app/TestLoadBalancer/4938wv9943q4b5tl",
            "Port": 80,
            "Protocol": "HTTP",
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:195333857493:targetgroup/TestTargetGroup/0493e9485743921e"
                }
            ]
        }
    ]
}
```

### Useful Resources
* [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
* [Amazon CLI: Elastic Load Balancing](https://docs.aws.amazon.com/cli/latest/reference/elbv2/index.html#cli-aws-elbv2)
* [Amazon CLI: Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html)
