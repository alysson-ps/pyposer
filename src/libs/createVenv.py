import os
import shutil
from virtualenv import cli_run, run


def create():
    cli_run(['venv'])
    for lib in [
            'click', 'virtualenv', 'six', 'filelock', 'appdirs', 'distlib'
    ]:
        if os.path.exists(f'/usr/lib/python3.9/site-packages/{lib}'):

            shutil.copytree(
                f'/usr/lib/python3.9/site-packages/{lib}',
                f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}')
        else:
            shutil.copyfile(
                f'/usr/lib/python3.9/site-packages/{lib}.py',
                f'{os.getcwd()}/venv/lib/python3.9/site-packages/{lib}.py')
