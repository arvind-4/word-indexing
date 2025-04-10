"""The script creates an index of words from text files in a specified directory."""

import pathlib
import re


def remove_special_characters_and_numbers(word: str) -> str:
    """Remove special characters and numbers from a word."""
    return re.sub(r"[^a-zA-Z]", "", word)


def create_index(page_files: list[str], exclude_file: str, index_file: str) -> None:
    """Create an index of words from the given page files, excluding specified words."""
    excluded_words = set()
    with pathlib.Path.open(exclude_file) as f:
        for line in f:
            excluded_words.update(line.strip().split())

    word_index = {}
    for page_file in page_files:
        page_number = pathlib.Path(page_file).stem.split("-")[-1][-1]
        with pathlib.Path.open(page_file) as f:
            for line in f:
                words = line.strip().lower().split()
                for word in words:
                    new_word = remove_special_characters_and_numbers(word)
                    if new_word and new_word not in excluded_words:
                        if new_word not in word_index:
                            word_index[new_word] = set()
                        word_index[new_word].add(page_number)

    with pathlib.Path.open(index_file, "w") as f:
        f.write("Word : Page Numbers\n")
        f.write("--------------\n\n")
        for word, pages in sorted(word_index.items()):
            f.write(f"{word} : {', '.join(sorted(pages))}\n")


def main() -> None:
    """Execute the main function of the script."""
    base_dir = pathlib.Path(__file__).parent
    page_dir = base_dir / "pages"
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True, parents=True)
    page_files = [str(file) for file in page_dir.glob("Page*.txt")]
    index_file = output_dir / "index.txt"
    exclude_file = page_dir / "exclude" / "exclude-words.txt"

    create_index(page_files, exclude_file, index_file)


if __name__ == "__main__":
    main()
