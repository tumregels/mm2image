import argparse


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
        nargs="*",
        metavar="FILENAME",
        help="file name(s) of mermaid diagram(s)",
    )
    parser.add_argument(
        "-c", "--clean", action="store_true", help="Clean all previous images"
    )
    return parser
