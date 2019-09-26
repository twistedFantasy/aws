#!/usr/bin/env bash

echo "Find latest available snapshot for RDS(PostgreSQL)"
LAST_SNAPSHOT=$(aws rds describe-db-snapshots \
  --db-instance-identifier="test-prod" \
  --query="reverse(sort_by(DBSnapshots, &SnapshotCreateTime))[0]|DBSnapshotIdentifier" \
  --output text \
  --profile "amazon-cli") && echo "Latest snapshot was successfully found: $LAST_SNAPSHOT"

echo "Delete DEV RDS"
aws rds delete-db-instance --db-instance-identifier "test-stg" --skip-final-snapshot --profile "amazon-cli" && echo "DEV RDS was successfully deleted"

sleep 20m

echo "Restore DEV RDS from latest PROD snapshot"
aws rds restore-db-instance-from-db-snapshot --db-instance-identifier  "test-stg" \
 --db-snapshot-identifier $LAST_SNAPSHOT \
 --db-instance-class "db.t2.micro" --publicly-accessible \
 --no-multi-az --tags Key=Name,Value="dev_test_rds" \
 --db-subnet-group-name "default-sg-nXAv6S8dWCvYQLBnS" \
 --vpc-security-group-ids  "sg-PDdXXSjQQaySo3I6Z" \
 --availability-zone "us-east-1a" \
 --profile amazon-cli && echo "DEV RDS was successfully restored from latest PROD snapshot"
