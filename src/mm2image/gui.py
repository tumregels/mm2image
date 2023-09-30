from gooey import Gooey, GooeyParser


@Gooey(program_name="mm2image")
def create_parser() -> GooeyParser:
    parser = GooeyParser(description="Generate mermaid diagrams")
    parser.add_argument(
        "filenames",
        nargs="+",
        metavar="FILENAME",
        help="file name(s) of mermaid diagram(s)",
        widget="MultiFileChooser"
    )
    parser.add_argument(
        "-c", "--clean", action="store_true", help="Clean all previous images"
    )
    return parser