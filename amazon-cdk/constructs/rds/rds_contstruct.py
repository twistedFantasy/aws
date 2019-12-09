from aws_cdk import (
    aws_ec2 as ec2,
    aws_rds as rds,
    core,
)
from aws_cdk.aws_ssm import StringParameter as Param


class RDSConstruct(core.Construct):

    @property
    def object(self):
        return self._rds

    def __init__(self, scope: core.Construct, id: str, *, app_env: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        security_group_params = {
            'security_group_name': f'rds-{app_env}-test-security-group',
            'description': f'security group for rds test({app_env})',
            'vpc': vpc,
        }
        security_group = ec2.SecurityGroup(self, 'security-group', **security_group_params)
        security_group.add_ingress_rule(peer=ec2.Peer.ipv4("54.125.156.2/32"),
                                        connection=ec2.Port(
                                            string_representation='random office',
                                            protocol=ec2.Protocol.TCP,
                                            from_port=5432,
                                            to_port=5432,
                                        ))

        password = Param.value_for_string_parameter(self, f'/{app_env}/test/DATABASE_PASSWORD')
        rds_params = {
            'engine': rds.DatabaseInstanceEngine.POSTGRES,
            'database_name': Param.value_for_string_parameter(self, f'/{app_env}/test/DATABASE_NAME'),
            'master_username': Param.value_for_string_parameter(self, f'/{app_env}/test/DATABASE_USER'),
            'master_user_password': core.SecretValue.plain_text(password),
            'instance_class': ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            'instance_identifier': f'{app_env}-test',
            'backup_retention': core.Duration.days(7),
            'delete_automated_backups': True,
            'security_groups': [security_group],
            'storage_type': rds.StorageType.GP2,
            'allocated_storage': 20,
            'engine_version': '11.5',
            'vpc': vpc,
        }
        self._rds = rds.DatabaseInstance(self, 'rds', **rds_params)
