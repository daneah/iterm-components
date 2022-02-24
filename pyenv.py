#!/usr/bin/env python

"""
To use this component, add the following to iterm2_print_user_vars:

    iterm2_set_user_var python_version $(pyenv_prompt_info)
"""

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
    async def pyenv_coroutine(knobs, python=iterm2.Reference('user.python_version?')):
        python = python or '☠️'
        return f'🐍 {python}'

    await component.async_register(connection, pyenv_coroutine)

iterm2.run_forever(main)
