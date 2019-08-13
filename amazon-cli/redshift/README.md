## Amazon Redshift

1. Get list of all Amazon Redshift clusters 
```
$ aws redshift describe-clusters --profile amazon-cli
```

2. Get list of snapshots for selected cluster
```
$ aws redshift describe-cluster-snapshots --cluster-identifier redshift-cluster-1 --profile amazon-cli
```

3. Create new Redshift cluster from "test-snapshot1" and attach it to 2 Amazon AWS Security Groups
```
$ aws redshift restore-from-cluster-snapshot --cluster-identifier "redshift-cluster-new" --snapshot-identifier "test-snapshot1"
 --vpc-security-group-ids "sg-02d7cb65523cbcd4b" "sg-0f02e468dcab4200e" --profile amazon-cli
```

4. Modify existing Amazon Redshift cluster and attach it to 2 new Amazon AWS Security Groups
```
aws redshift modify-cluster --cluster-identifier "redshift-cluster-1" --cluster-security-groups "sg-e9v92MoEMtvohlh6G" "sg-aTYFJUvdWUaD09CGD" --profile test
```

Useful resources:
### Useful Resources
* [Amazon Redshift](https://aws.amazon.com/redshift/)
* [Amazon CLI: Redshift](https://docs.aws.amazon.com/cli/latest/reference/redshift/index.html)
* [Amazon CLI: Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/getting-started-cli.html)
