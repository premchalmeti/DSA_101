def find_missing(consecutive_chars):
    for i in range(len(consecutive_chars)-1):
        if (ord(consecutive_chars[i+1]) - ord(consecutive_chars[i])) > 1:
            return chr(ord(consecutive_chars[i+1]) - 1)


if __name__ == '__main__':
    print(find_missing(["O", "Q", "R", "S"]), 'is missing word')
