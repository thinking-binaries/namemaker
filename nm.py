# nm.py  26/09/2016  D.J.Whale
# Originally written in java 08/05/2006

def load(filename):
    """Read words from a words file, into sections.
    # is a comment
    = is a section break
    any other lines are words
    """
    sections = []
    f = open(filename)
    while True:
        line = f.readline()
        line = line.strip()
        if line == "": break

        if line.startswith('#'):
            pass # ignore comments

        elif line.startswith('='):
            # start a new section
            sections.append([])
        else:
            # it's a word, add to present section
            (sections[len(sections)-1]).append(line)
    f.close()

    return sections


def ssv(words):
    """Convert a words list into space separated values"""
    line = ""
    for w in words:
        if len(line) != 0:
            line += ' '
        line += w
    return line


def generate(prefix, sections, index):
    """Generate combinations of words recursively, one from each section"""
    section = sections[index]
    for w in section:
        if not w in prefix:
            # Gross memory growth, but input file is small so it's good enough
            phrase = []
            for w2 in prefix:
                phrase.append(w2)
            phrase.append(w)
            if index < len(sections)-1:
                generate(phrase, sections, index+1)
            else:
                print(ssv(phrase))


if __name__ == "__main__":
    sections = load("words.txt")
    generate([], sections, 0)

# END



