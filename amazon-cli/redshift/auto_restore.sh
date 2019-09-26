#!/usr/bin/env bash

echo "Find latest available snapshot for Redshift"
LAST_SNAPSHOT=$(aws redshift describe-cluster-snapshots \
  --cluster-identifier "test-prod" \
  --query="reverse(sort_by(Snapshots, &SnapshotCreateTime))[0]|SnapshotIdentifier" \
  --output json \
  --profile "amazon-cli") && echo "Latest snapshot was successfully found: $LAST_SNAPSHOT"
$(echo "$LAST_SNAPSHOT" | tr -d '"')

echo "Delete DEV Redshift"
aws redshift delete-cluster --cluster-identifier "test-stg" --skip-final-cluster-snapshot --profile "amazon-cli" && echo "DEV Redshift was successfully deleted"

sleep 30m

echo "Restore DEV Redshift from latest PROD snapshot"
aws redshift restore-from-cluster-snapshot --cluster-identifier "test-stg" --snapshot-identifier $LAST_SNAPSHOT \
 --availability-zone "us-east-1a" --cluster-subnet-group-name "test-stg" --publicly-accessible --vpc-security-group-ids "sg-eAIgJO2NN7qKB7NpN" \
 --iam-roles "arn:aws:iam::162221448999:role/TestRole" "arn:aws:iam::162221448999:role/aws-service-role/redshift.amazonaws.com/TestRole2" --profile "amazon-cli" \
 && echo "DEV Redshift was successfully restored from latest PROD snapshot"
