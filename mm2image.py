import base64
from pathlib import Path
from pprint import pprint

import requests


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
    filename = "file1.mm"
    file = Path(filename)
    text = file.read_text()
    mm(text, save_as=file.stem + ".png")


if __name__ == '__main__':
    main()
