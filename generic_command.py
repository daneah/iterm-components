import asyncio

import iterm2


SCRIPT = 'SCRIPT'
PREFIX = 'PREFIX'

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Execute a user defined command',
        detailed_description='A component that displays the output of an arbitrary command with an optional prefix',
        exemplar='> hello world',
        update_cadence=7,
        identifier='engineering.dane.iterm-components.generic-command',
        knobs=[
           iterm2.StringKnob('Script', 'echo "hello world"', '', SCRIPT),
           iterm2.StringKnob('Prefix', '>', '', PREFIX)
        ],
    )

    @iterm2.StatusBarRPC
    async def generic_command_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            knobs[SCRIPT],
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        prefix = knobs[PREFIX]
        prefix = f'{prefix} ' if prefix else ''
        return f'{prefix}{stdout.decode().strip()}' if not stderr else 'Command failed!'

    await component.async_register(connection, generic_command_coroutine)

iterm2.run_forever(main)
