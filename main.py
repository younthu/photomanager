import click
from pathlib import Path

@click.command()
@click.option("--path", default=".", prompt="the folder to scan")
def photomanager(path):
    p = Path(path)
    print(p)
    file_list = [x for x in p.glob('**/*.jpg')]
    print( file_list)

if __name__ == "__main__":
    photomanager()
    