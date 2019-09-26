## Amazon Redshift

1. Create new Cluster Subnet Group
```
$ aws redshift create-cluster-subnet-group --cluster-subnet-group-name test-group --description "Test description" \
--subnet-ids subnet-763fdd1c subnet-937wfg4t --tags Key=Name,Value=dev_test --profile amazon-cli
```

2. Get list of all Amazon Redshift clusters 
```
$ aws redshift describe-clusters --profile amazon-cli
```

3. Get list of snapshots for selected cluster
```
$ aws redshift describe-cluster-snapshots --cluster-identifier redshift-cluster-1 --profile amazon-cli
```

4. Create new Redshift cluster from "test-snapshot1" and attach it to 2 Amazon AWS Security Groups
```
$ aws redshift restore-from-cluster-snapshot --cluster-identifier "redshift-cluster-new" --availability-zone us-east-1a \
--snapshot-identifier "test-snapshot1" --cluster-subnet-group-name test-group \
--publicly-accessible --kms-key-id 43t54-36537-7235-43264-65476 --iam-roles "arn:aws:iam::4354472452352:role/Test-Role" \
 --vpc-security-group-ids "sg-02d7cb65523cbcd4b" "sg-0f02e468dcab4200e" --profile amazon-cli
```

5. Modify existing Amazon Redshift cluster and attach it to 2 new Amazon AWS Security Groups
```
$ aws redshift modify-cluster --cluster-identifier "redshift-cluster-1" --cluster-security-groups \
  "sg-e9v92MoEMtvohlh6G" "sg-aTYFJUvdWUaD09CGD" --profile amazon-cli
```

6. Delete existing Amazon Redshift cluster
```
$ aws redshift delete-cluster --cluster-identifier "redshift-cluster-1" \
  --skip-final-cluster-snapshot --profile "amazon-cli"
```

Useful resources:
### Useful Resources
* [Amazon Redshift](https://aws.amazon.com/redshift/)
* [Amazon CLI: Redshift](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html)
* [Amazon CLI: Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/getting-started-cli.html)
