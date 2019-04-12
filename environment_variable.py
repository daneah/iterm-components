import asyncio
import os

import iterm2


ENV_VAR_KNOB_NAME = 'ENV_VAR'


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Environment variable',
        detailed_description='Show the current value of an environment variable',
        exemplar='SOME_ENV_VAR=foo',
        update_cadence=3,
        identifier='engineering.dane.iterm-components.environment-variable',
        knobs=[
            iterm2.StringKnob('Variable name', 'SOME_ENV_VAR', 'SOME_ENV_VAR', ENV_VAR_KNOB_NAME),
        ],
    )

    @iterm2.StatusBarRPC
    async def env_var_coroutine(knobs):
        env_var_name = knobs[ENV_VAR_KNOB_NAME]
        return f'{env_var_name}={os.getenv(env_var_name, "")}'

    await component.async_register(connection, env_var_coroutine)

iterm2.run_forever(main)
