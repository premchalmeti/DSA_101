
def lucky_numbers(name, dob):
    return ["1", "2", "3"]


if __name__ == '__main__':
    name = raw_input("Hey, what's your name?\n>>")
    dob = raw_input("Hi %s, Please tell us your DOB<dd/mm/yyyy>?\n>>" % name)
    lucky_numbers = lucky_numbers(name, dob)
    print(
        "Hi %s, Following are your lucky numbers\n%s" % (
            name, ", ".join(lucky_numbers)
        )
    )
