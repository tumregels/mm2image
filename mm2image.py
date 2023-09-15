import base64
from textwrap import dedent

from html2image import Html2Image


def mm(diagram: str, save_as: str) -> str:
    graph_bytes = diagram.encode("ascii")

    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = "https://mermaid.ink/img/" + base64_string

    hti = Html2Image()
    hti.screenshot(url=url, save_as=save_as)
    return url


def main() -> None:
    mm(dedent("""\
    graph LR;
        A--> B & C & D;
        B--> A & E;
        C--> A & E;
        E--> B & C & D;
    """), 'graph.png')


if __name__ == '__main__':
    main()
