# Wordle Solver CLI

A simple CLI tool to find potential wordle solutions.

## Setup

```
pip install -r requirements.txt
python -m nltk.downloader brown
```

## Usage

Pass in a `pattern`, using underscores for unknown letters and known correct positional letters.<br>
Use the optional `-i` and `-e` flags to include and exclude letters respectively.

eg:

```
python wordle ___th -e sne -i o
```

[out]
```
=========================
Found 11 possible results
=========================
booth    broth    cloth    forth    froth
groth    loath    mouth    tooth    worth
youth
```
