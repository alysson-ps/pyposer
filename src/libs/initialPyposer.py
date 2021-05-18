import os
import subprocess
import json


def createPyposer(click, default=False):
    if default:
        name = os.path.abspath(os.getcwd()).split('/')[-1]
        version = "1.0.0"
        main = "src/index.js"
        remote = subprocess.Popen(
            "git remote get-url origin", shell=True,
            stdout=subprocess.PIPE).stdout.read().decode().replace('\n', '')
        username = subprocess.Popen(
            "git config --get user.name", shell=True,
            stdout=subprocess.PIPE).stdout.read().decode()
        email = subprocess.Popen(
            "git config --get user.email", shell=True,
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

        # click.echo(json.dumps(pyposer, indent=2))
        with open('pyposer.json', 'w') as file:
            try:
                file.write(json.dumps(pyposer, indent=2))
                return "Saved pyposer.json"
            except Exception as e:
                return e
    else:
        click.echo("false")
