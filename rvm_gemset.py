"""
To use this component, add the following to iterm2_print_user_vars:

    iterm2_set_user_var ruby_version $(rvm-prompt g 2&> /dev/null)
"""

import asyncio

import iterm2


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='rvm gemset',
        detailed_description='The currently active rvm gemset',
        exemplar='💎 gemset',
        update_cadence=2,
        identifier='engineering.dane.iterm-components.rvm-gemset',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def rvm_gemset_coroutine(knobs, ruby=iterm2.Reference('user.ruby_version?')):
        ruby = ruby or 'default'
        ruby = ruby.replace('@', '') or 'default'
        return f'💎 {ruby}'

    await component.async_register(connection, rvm_gemset_coroutine)

iterm2.run_forever(main)
