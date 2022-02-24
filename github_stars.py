#!/usr/bin/env python

import asyncio
import json
import urllib.request
from urllib.error import HTTPError

import iterm2

REPO_KNOB_NAME = 'GITHUB_REPO'
TOKEN_KNOB_NAME = 'GITHUB_TOKEN'

def human_number(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    suffix = ['', 'K', 'M'][magnitude]
    return f'{num:.1f}{suffix}' if magnitude else f'{num}'


async def main(connection):
    github_repo = None

    component = iterm2.StatusBarComponent(
        short_description='GitHub stars',
        detailed_description='How many stars a GitHub repository has',
        exemplar='daneah/iterm-components ★ 67',
        update_cadence=300,
        identifier='engineering.dane.iterm-components.github-stars',
        knobs=[
            iterm2.StringKnob('Repository', 'some-user/project', 'some-user/project', REPO_KNOB_NAME),
            iterm2.StringKnob('Personal access token', 'token value (optional, for rate limiting or private repos)', '', TOKEN_KNOB_NAME)
        ],
    )

    @iterm2.RPC
    async def onclick(session_id):
        proc = await asyncio.create_subprocess_shell(
            f'open https://github.com/{github_repo}',
            stdout= asyncio.subprocess.PIPE,
            stderr= asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()

    @iterm2.StatusBarRPC
    async def github_stars_coroutine(knobs):
        github_repo = knobs[REPO_KNOB_NAME]
        info_url = f'https://api.github.com/repos/{github_repo}'

        token = knobs[TOKEN_KNOB_NAME]
        if not token:
            return '🔐 Configure access token'

        try:
            request = urllib.request.Request(
                info_url,
                headers={'Authorization': f'token {token}'} if token else {},
            )
            stars = json.loads(
                urllib.request.urlopen(request).read().decode()
            )['stargazers_count']
            stars = human_number(stars)
        except HTTPError as e:
            if e.code == 404:
                return f'❓ Repository not found'
            elif e.code == 401:
                return '🔐 Invalid access token'

            raise
        else:
            return f'{github_repo} ★ {stars}'

    await component.async_register(connection, github_stars_coroutine, onclick=onclick)

iterm2.run_forever(main)
