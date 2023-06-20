import os
import pathlib
import re
from typing import List


def remove_special_characters_and_numbers(word: str) -> str:
    return re.sub(r"[^a-zA-Z]", "", word)


def create_index(pageFiles: List[str], excludeFile: str, indexFile: str) -> None:
    excludedWords = set()
    with open(excludeFile, "r") as f:
        for line in f:
            excludedWords.update(line.strip().split())

    wordIndex = {}
    for pageFile in pageFiles:
        pageNumber = str(os.path.basename(pageFile).split(".")[0].split("Page")[1])
        with open(pageFile, "r") as f:
            for line in f:
                words = line.strip().lower().split()
                for word in words:
                    word = remove_special_characters_and_numbers(word)
                    if word and word not in excludedWords:
                        if word not in wordIndex:
                            wordIndex[word] = set()
                        wordIndex[word].add(pageNumber)

    with open(indexFile, "w") as f:
        f.write("Word : Page Numbers\n")
        f.write("--------------\n\n")
        for word, pages in sorted(wordIndex.items()):
            f.write(f'{word} : {", ".join(sorted(pages))}\n')


BASE_DIR = pathlib.Path(__file__).parent
PAGE_DIR = BASE_DIR / "pages"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

pageFiles = [str(file) for file in PAGE_DIR.glob("Page*.txt")]
indexFile = OUTPUT_DIR / "index.txt"
excludeFile = PAGE_DIR / "exclude" / "exclude-words.txt"


if __name__ == "__main__":
    create_index(pageFiles=pageFiles, excludeFile=excludeFile, indexFile=indexFile)
