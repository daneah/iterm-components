import asyncio
import json
import urllib.request

import iterm2


KNOB_NAME = 'GITHUB_REPO'


async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='GitHub stars',
        detailed_description='How many stars a GitHub repository has',
        exemplar='some-user/project ★ 103',
        update_cadence=300,
        identifier='engineering.dane.iterm-components.github-stars',
        knobs=[iterm2.StringKnob('Repository', 'some-user/project', 'some-user/project', KNOB_NAME)],
    )

    @iterm2.StatusBarRPC
    async def github_stars_coroutine(knobs):
        github_repo = knobs[KNOB_NAME]
        info_url = f'https://api.github.com/repos/{github_repo}'

        try:
            stars = json.loads(
                urllib.request.urlopen(info_url).read().decode()
            )['stargazers_count']
        except:
            raise RuntimeError(info_url)
        else:
            return f'{github_repo} ★ {stars}'

    await component.async_register(connection, github_stars_coroutine)

iterm2.run_forever(main)
