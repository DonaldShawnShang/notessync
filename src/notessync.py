"""NotesSync CLI stub."""
import argparse


def main() -> None:
    ap = argparse.ArgumentParser(prog="notessync")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("index").add_argument("path")
    sub.add_parser("search").add_argument("query")
    sub.add_parser("sync").add_argument("--to")
    args = ap.parse_args()
    print(f"notessync {args.cmd}: ok")


if __name__ == "__main__":
    main()
