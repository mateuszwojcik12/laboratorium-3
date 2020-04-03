#!/usr/bin/python3

import collections
import logging
import math
import os
import re
import string
import unicodedata

from matplotlib import patches
from matplotlib import pyplot as plt
from sklearn import decomposition
from sklearn import manifold

DIRNAME = 'teksty'

ALPHANUMERIC = ''.join(
    chr(x) for x in range(0x250)
    if unicodedata.category(chr(x)) in ('Lu', 'Ll', 'Nd'))

TOKENIZE_RE = re.compile(
    r'[{0}]+(?:-[{0}]+)*|[.,;:!?]+'.format(ALPHANUMERIC),
    re.MULTILINE | re.UNICODE)

INTERESTING_TOKEN_SET = frozenset("""
    . ? ! ,
    a aby albo ale ani aż bo choć czy i jeśli lecz ni niech niż więc że żeby
    bez dla do ku jako na nad o od po pod przed przez przy u w we wkoło z ze za
    bardzo coraz dotąd dziś gdy jak kiedy kiedyś niegdyś nieraz nigdy potem
    razem sam stąd teraz tu tuż tyle tym tymczasem wnet wszystko wtem wtenczas
    się nie by co gdyby gdzie jakby jeszcze już ledwie może nawet niby
    przecież tak tam też to tylko właśnie zaraz znowu
""".split())

INTERESTING_TOKEN_LIST = sorted(INTERESTING_TOKEN_SET)

# Solarized palette, https://ethanschoonover.com/solarized/
COLORS = [
    '#b58900',  # Yellow.
    '#dc322f',  # Red.
    '#6c71c4',  # Violet.
    '#2aa198',  # Cyan.
    '#859900',  # Green.
    '#cb4b16',  # Orange.
    '#d33682',  # Magenta.
    '#268bd2',  # Blue.
]


def analyze(filename):
    counter = collections.Counter()
    with open(filename, 'rt') as file:
        logging.info('Processing %s', filename)
        contents = file.read().split(u'-----\r\nTa lektura,')[0]
        tokens = TOKENIZE_RE.findall(contents)
        # TU(5): Uzupełnić zgodnie z instrukcją.
    # TU(6): Uzupełnić zgodnie z instrukcją.
    return result


def split_filename(filename, colors):
    filename = filename.split('.txt')[0]
    author, book = filename.split('-', 1)
    book = book.replace('-', ' ')
    book = book[0].title() + book[1:]
    author = author.title()
    if author not in colors:
        colors[author] = COLORS[len(colors)]
    return author, colors[author], book


def plot(filenames, X, title):
    colors = {}
    for filename, (x, y) in zip(filenames, X):
        author, color, book = split_filename(filename, colors)
        plt.plot(x, y, marker='o', color=color, label=author)
        plt.annotate(xy=(x, y), s=book, color=color)
    plt.title(title)
    legend_handles = [
        patches.Circle((0.5, 0.5), color=x) for x in colors.values()]
    plt.legend(legend_handles, colors.keys(), loc='upper left')
    plt.show()


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(message)s')
    filenames = []
    X = []
    for filename in os.listdir(DIRNAME):
        filenames.append(filename)
        X.append(analyze(os.path.join(DIRNAME, filename)))

    plot(
        filenames,
        decomposition.PCA(n_components=2).fit_transform(X),
        'Principal component analysis')

    # TU(9): Narysować analogiczny do powyższego diagram
    # wyników analizy czynnikowej (n_components=2).

    # TU(10): Narysować analogiczny do powyższych diagram
    # wyników skalowania wielowymiarowego (n_components=2).


if __name__ == '__main__':
    main()