import random

import iterm2

GREETINGS = [
    'Hello, world!',
    '¡Hola mundo!',
    'Salamu, dunia!',
    'শুভেচ্ছা, বিশ্ব!',
    '问候，世界！',
    'Chào thế giới!',
    'Բարեւ աշխարհ!',
]

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Hello, world!',
        detailed_description='Says hello in a random language periodically',
        exemplar='¡Hola, mundo!',
        update_cadence=5,
        identifier='engineering.dane.iterm-components.sentinel',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def hello_world_coroutine(knobs):
        return random.choice(GREETINGS)

    await component.async_register(connection, hello_world_coroutine)

iterm2.run_forever(main)
