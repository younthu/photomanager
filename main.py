import click
from pathlib import Path


def walk_folder(folder):
    p = Path(folder)
    types = ["**/*.jpg", "**/*.jpeg", "**/*.png", "**/*.gif"]
    return [x for t in types for x in p.glob(t) ]

@click.command()
@click.option("--path", default=".", prompt="the folder to scan")
def photomanager(path):
    print( walk_folder(path))

if __name__ == "__main__":
    photomanager()
    