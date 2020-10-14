import click
from pathlib import Path


def walk_folder(folder):
    p = Path(folder).expanduser() # expanduser to translate path such as ~/Desktop, ~/Downloads.
    print(p)
    types = ["**/*.jpg", "**/*.jpeg", "**/*.png", "**/*.gif"]
    return [(file, file.stat().st_size) for t in types for file in p.glob(t) ]

@click.command()
@click.option("--path", default=".", prompt="the folder to scan")
def photomanager(path):
    print( walk_folder(path))

if __name__ == "__main__":
    photomanager()
    