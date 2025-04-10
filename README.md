# Word Indexing

## Challenge outline

"Create index of words in a book" is a standard question we ask as practical test for devteam candidates.

Time limit is 3 hours. But it can be extended.

The question is given in Assignment.txt.

Data for testing the program is present in Page1.txt, Page2.txt, Page3.txt & exclude-words.txt.

Correct answer for test data is present in index.txt.

[The Question](https://github.com/Arvind-4/Assignment/blob/main/assignment/question.txt)

## Requirements

- Python 3.12 or above
- uv


## Getting Started

- Clone the repo

```bash
mkdir -p ~/Dev/word-indexing
cd ~/Dev/word-indexing
git clone https://github.com/arvind-4/word-indexing.git .
```

- Install requirements (It's optional)

```bash
uv venv
uv sync
```

> If you are not using `uv`, Try installing from `requirements.txt` file

```bash
pip install -r requirements.txt
```

- Run it locally

```bash
uv run python src/main.py
```

Now compare it with the `expected-output/index.txt` file.
