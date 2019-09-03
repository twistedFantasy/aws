## Amazon Redshift

1. Create hosted zone for domain
```
$ aws route53 create-hosted-zone --name test.com --caller-reference 2019-03-09-18:19 --hosted-zone-config Comment="command-line version" --profile amazon-cli
```

2. Create change-resource-record-sets-basic.json file with next content
```
{
  "Comment": "Create new subdomain record set",
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "subdomain.test.com",
        "Type": "A",
        "TTL": 60,
        "ResourceRecords": [
          {
            "Value": "5.339.235.220"
          }
        ]
      }
    }
  ]
}
```

3. Create new record set for subdomain. hosted-zone-id can be found in the url of Amazon AWS Console, https://console.aws.amazon.com/route53/home#resource-record-sets:W2KFJVY9WIOPO5
```
$ aws route53 change-resource-record-sets --hosted-zone-id W2KFJVY9WIOPO5 \
--change-batch file://change-resource-record-sets-basic.json --profile amazon-cli
```

4. Create change-resource-record-sets-alias.json file for Application Load Balancer with next content
```
{
  "Comment": "Create new subdomain record set",
  "Changes": [
    {
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "subdomain.test.com",
        "Type": "A",
        "TTL": 60,
        "AliasTarget": {
          "HostedZoneId": "W2KFJVY9WIOPO5",
          "DNSName": "TestLoadBalancer-2857499238.us-east-1.elb.amazonaws.com",
          "EvaluateTargetHealth": false
        }
      }
    }
  ]
}
```

5. Create new record set for subdomain2.
```
$ aws route53 change-resource-record-sets --hosted-zone-id W2KFJVY9WIOPO5 \
--change-batch file://change-resource-record-sets-alias.json --profile amazon-cli
```

### Useful Resources
* [Amazon Route53](https://aws.amazon.com/route53/)
* [Amazon CLI: Route53](https://docs.aws.amazon.com/cli/latest/reference/route53/index.html)
