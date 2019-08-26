## Amazon ElasticSearch Service

1. Create new elasticsearch domain
```
$ aws es create-elasticsearch-domain --domain-name test-domain --elasticsearch-version 5.5 \
--elasticsearch-cluster-config InstanceType=t2.small.elasticsearch,InstanceCount=1 \
--ebs-options EBSEnabled=true,VolumeType=standard,VolumeSize=10 \
--vpc-options SubnetIds=subnet-1a2a3a4a,SecurityGroupIds=sg-2a3a4a5a --profile amazon-cli
``` 

### Useful Resources
* [Amazon ElasticSearch Service](https://aws.amazon.com/elasticsearch-service/)
* [Amazon CLI: ElasticSearch Service](https://docs.aws.amazon.com/cli/latest/reference/es/index.html)
