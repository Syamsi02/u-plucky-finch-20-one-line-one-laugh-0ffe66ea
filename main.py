"""One Line, One Laugh -- a single funny line, written to /output/entry.txt.

The program is deterministic: it always writes the same line, with no
randomness, no network access and no third-party packages (stdlib only).
"""

import os

LINE = "I bought a plant to prove I could keep something alive. It died, but my excuses are thriving."

OUTPUT_PATH = "/output/entry.txt"


def write_line(path=OUTPUT_PATH):
    """Write the line to the output file, creating its directory if needed."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return LINE


def main():
    """Write the line and echo it, so the run is visible in the log too."""
    line = write_line()
    print(line)


if __name__ == "__main__":
    main()
