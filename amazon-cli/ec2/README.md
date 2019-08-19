## Amazon EC2
1. Allocate new Elastic IP address
```
$ aws ec2 allocate-address --domain vpc --dry-run --profile amazon-cli

An error occurred (DryRunOperation) when calling the AllocateAddress operation: Request would have succeeded, but DryRun flag is set.

$ aws ec2 allocate-address --domain vpc --profile amazon-cli
```
2. Create new key pair
```
$ aws ec2 create-key-pair --key-name test --profile amazon-cli

OR

$ aws ec2 create-key-pair --key-name test --query 'KeyMaterial' --output text > MyKeyPair.pem
```

3. Create new EC2 instance
```
$ aws ec2 run-instances --key-name test --image-id ami-12c5w57b --instance-type t2.micro --security-group-ids sg-05cb7c25b43343ff8 \
 --subnet-id subnet-MIm6AsKaiDIHbh464 --no-ebs-optimized --count 1 --dry-run  --profile amazon-cli
```

3. Assosiate Elastic IP address with newly created EC2 instance
```
$ aws ec2 associate-address --allocation-id eipalloc-1zPjStq7J086bKuV --instance-id i-FfUyMlxG7wClkAnz --dry-run --profile amazon-cli
```
