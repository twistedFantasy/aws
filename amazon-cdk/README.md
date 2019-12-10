## Configuration
* [CDK Installation](./readme/INSTALLATION.md)

## Overview
Constructs folder contain raw simple examples of constructs outside of cdk structure:
* low-level CFN Resources(<resource>_cfn_construct.py filename pattern)
* high-level(intend-based API) Resources(<resource>_construct.py filename pattern)
* high-level(patterns) Resources((<resource>_patterns_construct.py filename pattern))

On the same level with "constructs" folder there are full examples for different projects, for example, "ecs-rds-vpc"
folder contain fully runnable example of application which create custom Amazon VPC, Amazon RDS, Amazon ECR, Amazon ECS

Useful resources:<br/>
* [Amazon AWS Constructs](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html)