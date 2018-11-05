#!/usr/bin/env python3
"""
Retrieve and print words from a URL.

Usage:
    python3 words.py <URL>
"""
from urllib.request import urlopen
import sys


# sample url = 'http://sixty-north.com/c/t.txt'
def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    print('-' * 25)
    print(locals())
    print('-' * 25)
    return story_words


def print_items(items):
    """Print items on a single

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print each word from a text document from a URL

    Args:
        url: The URL of a UTF-8 text document.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # the 0th arg is always the module filename
