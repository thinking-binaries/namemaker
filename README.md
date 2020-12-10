# namemaker
A simple tool to generate names for companies and websites, job titles, etc.

## What it does

This is a simple command line tool. It takes a file called `words.txt`
and creates a range of ordered phrases from a set of word lists.

## How to use it

1. store your words in the file `words.txt`.
Words are stored in sections, and a section start is marked by an
equals sign on a line of it's own. To get a good set of names, you
should have at least 2 sections. An example file is provided in this
project.

2. Run the tool:

`python nm.py`

3. Look at the output in the file `phrases.txt`

4. Add and remove words from the `words.txt` file.

You can temporarily disable words by preceeding them with a comment marker,
which is a hash (#) symbol.

5. keep adding and removing words in the sections and running the tool,
analysing the output in `phrases.txt` until you spot some phrases that you
like.


@whaleygeek

10 Dec 2020



