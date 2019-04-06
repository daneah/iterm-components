import asyncio

import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='rvm gemset',
        detailed_description='The currently active rvm gemset',
        exemplar='♦ gemset',
        update_cadence=2,
        identifier='engineering.dane.iterm-components.rvm-gemset',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def rvm_gemset_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            '${HOME}/.rvm/bin/rvm-prompt g',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()

        if stderr:
            return '♦ rvm not installed!'

        gemset = stdout.decode().strip().replace('@', '') or 'default'
        return f'♦ {gemset}'

    await component.async_register(connection, rvm_gemset_coroutine)

iterm2.run_forever(main)
