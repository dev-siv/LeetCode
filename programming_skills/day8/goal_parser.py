def interpret(command):
    return command.replace("()", "o").replace("(al)", "al")


if __name__ == "__main__":
    c = "(al)G(al)()()G"
    print(interpret(c))