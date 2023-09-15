import base64
from pathlib import Path
from pprint import pprint

from html2image import Html2Image


def mm(diagram: str, save_as: str) -> str:
    pprint(diagram)
    graph_bytes = diagram.encode("ascii")

    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/img/" + base64_string

    hti = Html2Image()
    hti.screenshot(url=url, save_as=save_as)
    print(url)
    return url


def main() -> None:
    filename = "file1.mm"
    file = Path(filename)
    text = file.read_text()
    mm(text, save_as=file.stem + ".png")


if __name__ == '__main__':
    main()
