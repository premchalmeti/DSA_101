
# in-eficient mthd
def _get_plain_string(sstring):	
	return str(filter(lambda ch: ch.isalnum(), sstring))


def _reverse(sstring):
	return sstring[::-1]


def _add_special_chars(rstring, ostring):
	tstring = ""
	ri = 0

	for (i, ch) in enumerate(ostring):
		if not ch.isalpha():
			tstring += ch
		else:
			tstring += rstring[ri]
			ri += 1

	return tstring


def reverse_ineficient(sstring):
	plain_string = _get_plain_string(sstring)
	reversed_string = _reverse(plain_string)
	return _add_special_chars(reversed_string, sstring)


def swap_ch(lpos, rpos, sstring):
	return sstring[:lpos] + sstring[rpos] + sstring[lpos+1:rpos] + sstring[lpos] + sstring[rpos+1:]

# eficient mthd
def reverse_eficient(sstring):
	l, r = 0, len(sstring)-1
	tstring = sstring

	while l < r:
		if not sstring[l].isalpha():
			l += 1
		elif not sstring[r].isalpha():
			r -= 1
		else:
			tstring = swap_ch(l, r, tstring)
			l += 1
			r -= 1

	return tstring

if __name__ == '__main__':
    name = "a!@bc&d"
    expected = 'd!@cb&a'

    m1 = reverse_ineficient(name)
    m2 = reverse_eficient(name)

    print "mtd 1: ", name, m1
    print "mtd 2: ", name, m2

    assert m1 == expected, "m1 failed"
    assert m2 == expected, "m2 failed"
