target = list(input())


def respond(red,yellow,green):
    if red >= 3:
        print("nakhor lite")
    elif red >= 2 and yellow >= 2:
        print("nakhor lite")
    elif green == 0:
        print("nakhor lite")
    else:
        print("rahat baash")


def analysis(target_list):
    r = 0
    g = 0
    y = 0
    for i in target_list:
        if i == "G":
            g += 1
        elif i == "R":
            r += 1
        else:
            y += 1
    respond(r,y,g)


analysis(target)
