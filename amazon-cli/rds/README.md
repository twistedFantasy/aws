## Amazon RDS

1. Get information about provisioned Aurora DB clusters.
```
$ aws rds describe-db-clusters --profile amazon-cli
```

2. Get  information  about  DB cluster snapshots.
```
$ aws rds describe-db-cluster-snapshots --db-cluster-identifier myauroradbcluster --profile amazon-cli
```

3. Get  information about provisioned RDS instances.
```
$ aws rds describe-db-instances --profile amazon-cli
```

4. Get  information about DB snapshots.
```
$ aws rds describe-db-snapshots --db-instance-identifier myrdsdb --profile amazon-cli
```

5. Create a new DB cluster from a DB snapshot or DB cluster snapshot.
If  a  DB  snapshot is specified, the target DB cluster is created from
the source DB snapshot with a default configuration and  default  security group.
If a DB cluster snapshot is specified, the target DB cluster is created
from the source DB cluster restore point with the same configuration as
the  original source DB cluster, except that the new DB cluster is created with the default security group.
```
$ aws rds restore-db-cluster-from-snapshot --db-cluster-identifier newauroradbcluster --snapshot-identifier test-snapshot1
--profile amazon-cli
```

6. Create RDS Subnet Group
```
$ aws rds create-db-subnet-group --db-subnet-group-name default-sg-oEiVkV4rfJSbewOsk --db-subnet-group-description 
"Created from Amazon CLI" --subnet-ids subnet-vn5gcG7YPARwteVJ2 subnet-hoRE94lq9M9PI0uDj 
--tags Key=Name,Value=dev_test --profile amazon-cli
```

7. Create  a  new  DB instance from a DB snapshot. The target database is
created from the source database restore point with the most of  original
configuration  with  the default security group and the default DB
parameter group. By default, the new DB instance is created as  a  single-AZ
deployment  except  when  the instance is a SQL Server instance that has an
option group that is associated  with  mirroring;  in  this case,
the instance becomes a mirrored AZ deployment and not a single-AZ deployment.

```
$ aws rds restore-db-instance-from-db-snapshot --db-instance-identifier newrdsdb 
--db-snapshot-identifier rds:test-dev-2019-06-05-03-19 --db-instance-class db.t2.micro
--no-publicly-accessible --no-multi-az --tags Key=Name,Value=dev_test --db-subnet-group-name
 default-sg-oEiVkV4rfJSbewOsk --vpc-security-group-ids "sg-02d7cb65523cbcd4b" "sg-0f02e468dcab4200e" 
--profile amazon-cli
```

8. Modify a setting for an Amazon Aurora DB cluster. You can change one or 
more database configuration parameters by specifying  these  parameters
and  the  new  values  in  the  request.
```
$ aws rds modify-db-cluster --db-cluster-identifier myauroradbcluster  --apply-immediately --port 3307
--vpc-security-group-ids "sg-0f02e468dcab4200e" --profile amazon-cli 
```

9. Modifies  settings  for a DB instance. You can change one or more database
configuration parameters by specifying these  parameters  and  the new  values
in the request. To learn what modifications you can make to your DB instance,
call DescribeValidDBInstanceModifications before  you call ModifyDBInstance 
```
aws rds modify-db-instance --db-instance-identifier myrdsdb --apply-immediately --port 3307
--vpc-security-group-ids "sg-0f02e468dcab4200e" --profile amazon-cli
```

10. Delete existing Amazon RDS instance
```
$ aws rds delete-db-instance --db-instance-identifier "myauroradbcluster" \
  --skip-final-snapshot --profile "amazon-cli"
```

### Useful resources:
* [Amazon RDS](https://aws.amazon.com/rds/)
* [Amazon CLI: RDS](https://docs.aws.amazon.com/cli/latest/reference/rds/)
