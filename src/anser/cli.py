import click

from anser.config import build_config
from anser.commands.init_anser import InitAnser
from anser.utils.path import build_config_path, get_absolute_path


@click.group()
def cli() -> None:
    return None


@cli.command(name='init')
@click.argument('path', required=False)
def init(path: str | None = None) -> None:
    InitAnser(get_absolute_path(path)).execute()


@cli.command(name='migration')
@click.option('--message', required=False)
@click.option('--config-path', required=False)
def migration(
    message: str | None = None,
    config_path: str | None = None,
) -> None:
    config = build_config(build_config_path(config_path))
    return None
