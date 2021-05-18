from sys import argv
import click
import os

import libs.initialPyposer as init_run
import libs.colors as colors

_VERSION = '1.0.0'
_FIRST_ARG = argv[1]


@click.command()
@click.option("-y",
              "--yes",
              is_flag=True,
              help="Set default values in pyposer.json")
def init(yes):
    click.echo(init_run.createPyposer(click, yes))


@click.command(help="teste")
@click.option("-D", "--dev", is_flag=True, help="install how devDependencies")
def add(dev):
    click.echo(f"Init repo {dev}")


@click.group()
def group():
    pass


group.add_command(init)
group.add_command(add)

if __name__ == '__main__':
    print(
        f"{colors.BOLD}{__file__.split('/')[-1]} {_FIRST_ARG} {_VERSION}{colors.ENDC}"
    )
    # group()