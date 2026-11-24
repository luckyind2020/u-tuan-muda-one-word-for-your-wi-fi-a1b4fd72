"""One word for your Wi-Fi.

Reads the single-word entry from entry.txt and prints it.
The word is Schrodinger: the network is simultaneously connected
and not connected, full bars and no internet, until you observe it.
The entry lives in entry.txt so the word itself stays a one-word file.
"""

from pathlib import Path

ENTRY_FILE = "entry.txt"


def load_word(entry_path=None):
    here = Path(__file__).resolve().parent
    target = Path(entry_path) if entry_path else here / ENTRY_FILE
    return target.read_text(encoding="utf-8").strip()


def main():
    print(load_word())


if __name__ == "__main__":
    main()
