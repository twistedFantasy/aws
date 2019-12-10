1. Install Node.js & npm
* Node.js (>= 8.11.x)
* You must specify both your credentials and an AWS Region to use the AWS CDK CLI;, as described in Specifying Your Credentials and Region.

2. Install AWS CDK
```
# npm install -g aws-cdk
```

3. Check installed version of AWS CDK
```
$ cdk --version
```

4. Install or update your language dependencies
```
$ pip3 install --upgrade aws-cdk.core
$ pip3 install aws-cdk.aws-ec2
```

5. Configure new profile
```
$ aws configure --profile amazon-cli
```

6. Init default python project
```
$ cdk init --language python
```
