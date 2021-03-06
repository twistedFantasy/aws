from aws_cdk import (
    aws_logs as logs,
    core,
)


class LogsConstruct(core.Construct):

    @property
    def object(self):
        return self._logs

    def __init__(self, scope: core.Construct, id: str, *, app_env: str, **kwargs):
        super().__init__(scope, id, kwargs)

        params = {
            'log_group_name': f'open-{app_env}-ecs-log-group',
            'retention': logs.RetentionDays.ONE_MONTH,
        }
        self._logs = logs.LogGroup(self, 'open-log-group', **params)
