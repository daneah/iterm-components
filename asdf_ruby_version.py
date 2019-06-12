import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description="Ruby version",
        detailed_description="Show ruby version using asdf",
        exemplar="💎 2.5.3",
        update_cadence=None,
        identifier="me.hgal.iterm-components.ruby-version",
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def coro(
            knobs,
            version = iterm2.Reference("user.asdfRubyVersion?")):
        if version:
            return f'💎 {version}'
        else:
            return "❌"

    await component.async_register(connection, coro)

iterm2.run_forever(main)
