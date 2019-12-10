from aws_cdk import (
    core,
)

from open.iam_construct import IAMConstruct
from open.vpc_construct import VPCConstruct
from open.ecs_construct import ECSConstruct
from open.ecr_construct import ECRConstruct
from open.rds_construct import RDSConstruct


class OpenStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, *, app_env: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        IAMConstruct(self, 'Open-IAM-Construct', app_env=app_env)
        vpc = VPCConstruct(self, 'Open-VPC-Construct', app_env=app_env)
        rds = RDSConstruct(self, 'Open-RDS-Construct', app_env=app_env, vpc=vpc.object)
        ecr = ECRConstruct(self, 'Open-ECR-Construct', app_env=app_env)
        params = {
            'app_env': app_env,
            'vpc': vpc.object,
            'rds': rds.object,
            'repository': ecr.object,
        }
        ECSConstruct(self, 'Open-ECS-Construct', **params)
