def decryptPassword(s):
    # Write your code here
    org_string = list(s)
    i = 0
    o_len = len(s)

    while i < o_len:
        if s[i].isdigit() and s[i] != '0':
            org_place = "".join(org_string).rindex('0')
            org_string[org_place] = s[i]
            # org_string.pop(i)
            org_string[i] = '#'
        elif s[i].isupper():
            org_string[i] = s[i+1]
            org_string[i+1] = s[i]
            # org_string.pop(i+2)
            org_string[i+2] = '#'
        i += 1

    print(''.join([c for c in org_string if c!='#']))
    return ""


if __name__ == '__main__':
    print(decryptPassword('51Pa*0Lp*0e'))

