#!/usr/bin/env python3

import os

from aws_cdk import core

from open.open_stack import OpenStack


if os.environ.get("ENV") and os.environ["ENV"] in ['stg', 'prod']:
    app = core.App()
    OpenStack(app, f'open-cdk-{os.environ["ENV"]}', app_env=os.environ["ENV"], env={'region': 'us-east-2'})
    app.synth()
else:
    raise Exception("No ENV value was specified, supported options: stg, prod")


