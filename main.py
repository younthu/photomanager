import click
import pprint
from pathlib import Path


def walk_folder(folder):
    p = Path(folder).expanduser() # expanduser to translate path such as ~/Desktop, ~/Downloads.
    print(p)
    types = ["**/*.jpg", "**/*.jpeg", "**/*.png", "**/*.gif"]
    return [(file, file.stat().st_size) for t in types for file in p.glob(t) ]

def pretty_print(images):
    pp = pprint.PrettyPrinter(depth=6)
    # sort
    sorted_images = sorted(images, key=lambda tup: tup[1])
    pp.pprint(sorted_images)
    
@click.command()
@click.option("--path", default=".", prompt="the folder to scan")
def photomanager(path):
    pretty_print( walk_folder(path))

if __name__ == "__main__":
    photomanager()
    