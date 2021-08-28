
def format_duration(seconds):
    if seconds == 0: return 'now'

    y, d, h, m, s = 0, 0, 0, 0, seconds

    while True:
        if s >= 60:
            m += int(s / 60)
            s %= 60

        elif m >= 60:
            h += int(m / 60)
            m %= 60

        elif h >= 24:
            d += int(h / 24)
            h %= 24

        elif d >= 365:
            y += int(d / 365)
            d %= 365
        else:
            break

    units = [
        ['year', 'years'], ['day', 'days'], ['hour', 'hours'],
        ['minute', 'minutes'], ['second', 'seconds']
    ]

    time_units = []

    for (i, d) in enumerate([y, d, h, m, s]):
        if d:
            time_units.append("%s %s" % (d, units[i][d>1]))

    return [
        "{}",
        "{} and {}",
        "{}, {} and {}",
        "{}, {}, {} and {}",
        "{}, {}, {}, {} and {}",
    ][min(len(time_units)-1, 5)].format(*time_units)

    # if len(time_units) == 1:
    #     return time_units[0]
    # elif len(time_units) == 2:
    #     return "{} and {}".format(*time_units)
    # elif len(time_units) == 3:
    #     return "{}, {}"


if __name__ == '__main__':
    print(format_duration(3662))
