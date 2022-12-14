import sys
from argparse import ArgumentParser
import nltk


def get_corpus():
    return {word.lower() for word in nltk.corpus.brown.words()}


def filter_numeric(words):
    return [word for word in words if not any(x.isdigit() for x in word)]


def print_results(results, cols=3):
    n_results = len(results)
    text = f'Found {n_results:,} possible {"result" if n_results == 1 else "results"}'
    print(f'\n{"="*len(text)}\n{text}\n{"="*len(text)}')
    for i in range(0, n_results, cols):
        indices = [i + x for x in range(cols) if i + x < n_results]
        print('    '.join([results[idx] for idx in indices]))


def return_candidates(pattern='_____', exclude=None, include=None, corpus=get_corpus(), include_numeric=False):
    if exclude is None:
        exclude = []
    if isinstance(exclude, str):
        exclude = list(exclude.lower())

    word_len = len(pattern)

    known = {i: x for i, x in enumerate(pattern) if x != '_'}

    candidates = [word for word in corpus
                  if len(word) == word_len
                  and not any(x in word.lower() for x in exclude)
                  and all(word[k] == v for k, v in known.items())]

    if include is not None:
        if isinstance(include, str):
            include = list(include.lower())
        candidates = [word for word in candidates if all(x in word for x in include)]

    if not include_numeric:
        candidates = filter_numeric(candidates)

    return sorted(candidates)


def parse_args(argv):
    parser = ArgumentParser()
    parser.add_argument('pattern',
                        help='Pattern to search for including known positionally correct letter. eg "___ch"',
                        type=str)

    parser.add_argument('-e', '--exclude',
                        help='A string list of letters known not be be in the word.',
                        required=False,
                        type=str,
                        default=None)

    parser.add_argument('-i', '--include',
                        help='A string list of letters known to be in the word, but position is unknown.',
                        required=False,
                        type=str,
                        default=None)

    parser.add_argument('-c', '--columns',
                        help='The number of columns to format printed results into.',
                        required=False,
                        default=5,
                        type=int)

    parser.add_argument('--include-numeric',
                        help='Includes words with numeric characters.',
                        required=False,
                        action='store_true')

    return parser.parse_args(argv)


def main(argv):
    args = parse_args(argv)
    results = return_candidates(args.pattern, exclude=args.exclude, include=args.include, include_numeric=args.include_numeric)
    print_results(results, args.columns)


if __name__ == "__main__":
    main(sys.argv[1:])
