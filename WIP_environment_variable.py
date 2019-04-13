import asyncio
import os

import iterm2


ENV_VAR_KNOB_NAME = 'ENV_VAR'
SHOW_NAME_KNOB_NAME = 'SHOW_NAME'


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Environment variable',
        detailed_description='Show the current value of an environment variable',
        exemplar='SOME_ENV_VAR=foo',
        update_cadence=3,
        identifier='engineering.dane.iterm-components.environment-variable',
        knobs=[
            iterm2.StringKnob('Variable name', 'SOME_ENV_VAR', 'SOME_ENV_VAR', ENV_VAR_KNOB_NAME),
            iterm2.CheckboxKnob('Show variable name', True, SHOW_NAME_KNOB_NAME)
        ],
    )

    @iterm2.StatusBarRPC
    async def env_var_coroutine(knobs):
        env_var_name = knobs[ENV_VAR_KNOB_NAME]
        show_name = knobs[SHOW_NAME_KNOB_NAME]
        prefix = f'{env_var_name}=' if show_name else ''
        return f'{prefix}{os.getenv(env_var_name, "")}'

    await component.async_register(connection, env_var_coroutine)

iterm2.run_forever(main)
