
def rev_title(text):
    return " ".join([wrd[::-1].title() for wrd in text.split()])


if __name__ == '__main__':
    txt = "mr. premkumar ashok chalmeti"
    print rev_title(txt)
