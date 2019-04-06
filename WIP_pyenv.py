import asyncio

import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='pyenv',
        detailed_description='The currently active Python',
        exemplar='🐍 3.7.2',
        update_cadence=2,
        identifier='engineering.dane.iterm-components.pyenv',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def pyenv_coroutine(knobs):
        proc = await asyncio.create_subprocess_shell(
            'pyenv local',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()

        if stderr:
            return stderr.decode().strip()

        env = stdout.decode().strip()
        return f'🐍 {env}'

    await component.async_register(connection, pyenv_coroutine)

iterm2.run_forever(main)
