import base64
import logging
import sys
from pathlib import Path

import requests

import mm2image.cli as cli
import mm2image.gui as gui

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def mm(diagram: str, save_as: str) -> str:
    logger.info(diagram)
    graph_bytes = diagram.encode("ascii")

    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/img/" + base64_string

    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        with open(save_as, "wb") as f:
            f.write(response.content)
    logger.info(url)
    return url


def main() -> None:
    try:
        parser = cli.create_parser()
        args = parser.parse_args()
    except SystemExit as e:
        if e.code == 0:
            sys.exit()
    else:
        if not args.filenames:
            parser = gui.create_parser()
            args = parser.parse_args()

    logger.info(f"String Arguments: {args.filenames}")
    logger.info(f"Boolean Argument: {args.clean}")

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
