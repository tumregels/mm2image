import argparse
import base64
from pathlib import Path
from pprint import pprint

import requests


def create_parser() -> argparse.ArgumentParser:
    """
    >>> parser = create_parser()
    >>> args = parser.parse_args('file1.mm file2.mm --clean'.split())
    >>> args.filenames
    ['file1.mm', 'file2.mm']
    >>> args.clean
    True
    """
    parser = argparse.ArgumentParser(description="Generate mermaid diagrams")
    parser.add_argument(
        "filenames",
        nargs="+",
        metavar="FILENAME",
        help="file name(s) of mermaid diagram(s)",
    )
    parser.add_argument(
        "-c", "--clean", action="store_true", help="Clean all previous images"
    )
    return parser


def mm(diagram: str, save_as: str) -> str:
    pprint(diagram)
    graph_bytes = diagram.encode("ascii")

    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/img/" + base64_string

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(save_as, "wb") as f:
            f.write(response.content)
    print(url)
    return url


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    print("String Arguments:", args.filenames)
    print("Boolean Argument:", args.clean)

    for filename in args.filenames:
        diag_file = Path(filename)
        image_file = Path(diag_file.stem + ".png")
        if diag_file.is_file():
            if image_file.is_file() and args.clean:
                image_file.unlink()
            text = diag_file.read_text()
            mm(text, save_as=image_file.as_posix())


if __name__ == '__main__':
    main()
