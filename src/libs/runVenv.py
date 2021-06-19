import os


def down(shell):
    os.system(
        f'source {os.getcwd()}/venv/bin/activate;deactivate;exec {shell}')


def up(shell):
    os.system(f'source {os.getcwd()}/venv/bin/activate;exec {shell}')