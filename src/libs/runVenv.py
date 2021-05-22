import os


async def down(shell):
    os.system(
        f'source {os.getcwd()}/venv/bin/activate;deactivate;exec {shell}')


async def up(shell):
    os.system(f'source {os.getcwd()}/venv/bin/activate;exec {shell}')