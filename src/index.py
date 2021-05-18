from sys import argv
import click
import time
import subprocess

import libs.initialPyposer as init_run
import libs.colors as colors
from libs.install import install

_VERSION = 'v1.0.0'
_FIRST_ARG = argv[1] if len(argv) > 1 else "install"


@click.command()
@click.option("-y",
              "--yes",
              is_flag=True,
              help="Set default values in pyposer.json")
def init(yes):
    start_time = time.time()
    init_run.createPyposer(click, yes)
    click.echo(f"done in {time.time() - start_time:.2f}")


@click.command(help="teste")
@click.option("-D", "--dev", is_flag=True, help="install how devDependencies")
@click.argument("libs", required=True, nargs=-1)
def add(dev, libs):
    start_time = time.time()
    for lib in libs:
        install(lib)
    click.echo(f"done in {time.time() - start_time:.2f}")


@click.command()
def activate():
    start_time = time.time()
    cmd = "source venv/bin/activate"
    subprocess.Popen(cmd, shell=True)
    click.echo(f"done in {time.time() - start_time:.2f}")


@click.group()
def group():
    pass


group.add_command(init)
group.add_command(add)
group.add_command(activate)

if __name__ == '__main__':
    print(
        f"{colors.BOLD}{__file__.split('/')[-1]} {_FIRST_ARG} {_VERSION}{colors.ENDC}"
    )
    group()