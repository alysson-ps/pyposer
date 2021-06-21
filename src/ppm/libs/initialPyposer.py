import os
import subprocess
import json
from . import colors
from .install import install

_GIT_DIR = os.path.exists('.git')
_SHELL = os.environ['SHELL'].split('/')[-1]


def createPyposer(click, default=False):
    if default:
        name = os.path.abspath(os.getcwd()).split('/')[-1]
        version = "1.0.0"
        main = "src/index.js"
        if _GIT_DIR:
            remote = subprocess.Popen(
                "git remote get-url origin",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode().replace(
                    '\n', '')
            username = subprocess.Popen(
                "git config --get user.name",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode()
            email = subprocess.Popen(
                "git config --get user.email",
                shell=True,
                stdout=subprocess.PIPE).stdout.read().decode()
            author = f"{username} <{email}>".replace('\n', '')

            license = "MIT"
            scripts = {"teste": "echo 'teste'"}
            dependencies = {}
            devDependencies = {}

            pyposer = {
                "name": name,
                "version": version,
                "main": main,
                "remote": remote,
                "author": author,
                "license": license,
                "scripts": scripts,
                "dependencies": dependencies,
                "devDependencies": devDependencies
            }

        else:
            license = "MIT"
            scripts = {"teste": "echo 'teste'"}
            dependencies = {}
            devDependencies = {}

            pyposer = {
                "name": name,
                "version": version,
                "main": main,
                "license": license,
                "scripts": scripts,
                "dependencies": dependencies,
                "devDependencies": devDependencies
            }

        click.echo(
            f"{colors.YELLOW}warning{colors.ENDC} The yes flag has been set. This will automatically answer yes to all questions"
        )
        with open('pyposer.json', 'w') as file:
            try:
                file.write(json.dumps(pyposer, indent=2))
                click.echo(
                    f"{colors.GREEN}success{colors.ENDC} Saved pyposer.json")
            except Exception as e:
                return click.echo(f"{colors.RED}error{colors.ENDC} {e}")
    else:
        click.echo("false")
