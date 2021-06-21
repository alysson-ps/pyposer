#!/usr/bin/python3
# coding=utf-8

from sys import argv, exit
import click
import time
import subprocess
import json
import os
from pathlib import Path

import libs.initialPyposer as init_run
import libs.colors as colors
from libs.install import install as installPkg, remove as removePkg
from libs.execScript import execCmd
from libs.runVenv import down, up
from libs import createVenv

_VERSION = 'v0.1.0'
_FIRST_ARG = argv[1] if len(argv) > 1 else "install"
_SHELL = os.environ['SHELL'].split('/')[-1]
_HOME_DIR = str(Path.home())
_RCFILE = ".zshrc" if _SHELL == "zsh" else ".bashrc"
_BANNER = f"{colors.BOLD}{__file__.split('/')[-1]} {_FIRST_ARG} {_VERSION}{colors.ENDC}"
_PYPOSER_EXIST = os.path.exists('pyposer.json')


def print_version(ctx, param, value):
    if value:
        click.echo(_VERSION)
        exit()
    else:
        pass


@click.group()
@click.option("-v", "--version", is_flag=True, callback=print_version)
def group(version):
    pass


@group.command()
@click.option("-y",
              "--yes",
              is_flag=True,
              help="Set default values in pyposer.json")
def init(yes):
    createVenv.create()
    start_time = time.time()
    init_run.createPyposer(click, yes)
    click.echo(f"done in {time.time() - start_time:.2f}")


@group.command()
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


@group.command()
@click.option("-q",
              "--quiet",
              is_flag=True,
              help="install how devDependencies")
@click.argument("libs", required=True, nargs=-1)
def remove(libs, quiet):
    start_time = time.time()
    for lib in libs:
        removePkg(lib, quiet)
    click.echo(f"done in {time.time() - start_time:.2f}")


@group.command()
def activate():
    up(_SHELL)


@group.command()
def deactivate():
    down(_SHELL)


@group.command()
@click.argument("cmd", required=True)
def run(cmd):
    click.echo(f"{colors.BOLD}{colors.GREY}$ {execCmd(cmd)}{colors.ENDC}")
    os.system(execCmd(cmd))


@group.command()
def install():
    with open('pyposer.json') as f:
        pyposer = json.load(f)
        if bool(pyposer['dependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                installPkg(package)
        if bool(pyposer['devDependencies']):
            for pkg in list(pyposer['dependencies'].items()):
                package = f'{pkg[0]}=={pkg[1]}'
                group.commands['add'].callback(package, True, False)


def main():
    if "-" in _FIRST_ARG:
        pass
    elif not "activate" in _FIRST_ARG:
        print(_BANNER)
    if _PYPOSER_EXIST:
        if not _FIRST_ARG in list(
                group.commands.keys()) and not "-" in _FIRST_ARG:
            group.commands['run'].callback(_FIRST_ARG)
            exit()
        if _FIRST_ARG == 'install':
            group.commands['install'].callback()
            exit()
    group()


if __name__ == '__main__':
    main()