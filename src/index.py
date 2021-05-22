#!/usr/bin/env python3
# coding=utf-8

from sys import argv
import click
import time
import subprocess
import json
import os
from pathlib import Path

import libs.initialPyposer as init_run
import libs.colors as colors
from libs.install import install as installPkg
from libs.execScript import execCmd
from libs.runVenv import down, up
from libs import createVenv

_VERSION = 'v1.0.0'
_FIRST_ARG = argv[1] if len(argv) > 1 else "install"
_SHELL = os.environ['SHELL'].split('/')[-1]
_HOME_DIR = str(Path.home())
_RCFILE = ".zshrc" if _SHELL == "zsh" else ".bashrc"
_BANNER = f"{colors.BOLD}{__file__.split('/')[-1]} {_FIRST_ARG} {_VERSION}{colors.ENDC}"
_PYPOSER_EXIST = os.path.exists('pyposer.json')


@click.command()
@click.option("-y",
              "--yes",
              is_flag=True,
              help="Set default values in pyposer.json")
def init(yes):
    createVenv.create()
    start_time = time.time()
    init_run.createPyposer(click, yes)
    click.echo(f"done in {time.time() - start_time:.2f}")


@click.command()
@click.option("-D", "--dev", is_flag=True, help="install how devDependencies")
@click.option("-q",
              "--quiet",
              is_flag=True,
              help="install how devDependencies")
@click.argument("libs", required=True, nargs=-1)
def add(dev, libs, quiet):
    start_time = time.time()
    for lib in libs:
        installPkg(lib, dev, quiet)
    click.echo(f"done in {time.time() - start_time:.2f}")


@click.command()
def activate():
    up(_SHELL)


@click.command()
def deactivate():
    down(_SHELL)


@click.command()
@click.argument("cmd", required=True)
def run(cmd):
    click.echo(f"{colors.BOLD}{colors.GREY}$ {execCmd(cmd)}{colors.ENDC}")
    os.system(execCmd(cmd))


@click.command()
def install():
    with open('pyposer.json') as f:
        pyposer = json.load(f)
        if bool(pyposer['dependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                install(False, [package], False)
        if bool(pyposer['devDependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                group.commands['add'].callback(True, [package], False)


@click.group()
def group():
    pass


group.add_command(init)
group.add_command(add)
group.add_command(run)
group.add_command(install)
group.add_command(activate)
group.add_command(deactivate)

if __name__ == '__main__':
    if not "activate" in _FIRST_ARG:
        print(_BANNER)
    if _PYPOSER_EXIST:
        if not _FIRST_ARG in list(group.commands.keys()):
            group.commands['run'].callback(_FIRST_ARG)
        if _FIRST_ARG == 'install':
            group.commands['install'].callback()
    else:
        group()