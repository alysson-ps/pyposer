from pip._internal.cli.main import main
import subprocess
import json
import os
import re
import sys


# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enablePrint():
    sys.stdout = sys.__stdout__


def install(package, dev=False, quiet=False):
    if dev == False:
        if quiet == True:
            blockPrint()
            okay = main([
                'install',
                f'--target={os.getcwd()}/venv/lib/python3.9/site-packages',
                package
            ])
            enablePrint()
        else:
            okay = main([
                'install',
                f'--target={os.getcwd()}/venv/lib/python3.9/site-packages',
                package
            ])
            # okay = subprocess.Popen(f"pip install {package}", shell=True).wait()

        if okay == 0:
            cmd = f"pip freeze | grep {package}"
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            version = result.stdout.read().decode().replace('\n', '')
            with open('pyposer.json', 'r+') as f:
                data = json.load(f)
                data['dependencies'].update(
                    {package: re.sub("[^0-9^.]", "", version)})
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
    else:
        okay = main([
            'install',
            f'--target={os.getcwd()}/venv/lib/python3.9/site-packages', package
        ])

        if okay == 0:
            cmd = f"pip freeze | grep {package}"
            result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            version = result.stdout.read().decode().replace('\n', '')
            with open('pyposer.json', 'r+') as f:
                data = json.load(f)
                data['devDependencies'].update(
                    {package: re.sub("[^0-9^.]", "", version)})
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()


def remove(package, quiet=False):
    if quiet == True:
        blockPrint()
        okay = subprocess.run(["pip", "uninstall", package, "-y"],
                              stderr=subprocess.PIPE).returncode
        enablePrint()
    else:
        okay = subprocess.run(["pip", "uninstall", package, "-y"],
                              stderr=subprocess.PIPE).returncode
    if okay == 0:
        with open('pyposer.json', 'r+') as f:
            data = json.load(f)
            if data['dependencies'][package]:
                del data['dependencies'][package]
            elif data['devDependencies'][package]:
                del data['devDependencies'][package]

            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()