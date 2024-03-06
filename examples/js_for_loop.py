from ph7.js.transpile import to_js


def oddEven(n: int):
    for i in range(n):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")


def oddEvenStartEnd(start: int, end: int):
    for i in range(start, end):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")


def oddEvenStartEndStep(start: int, end: int, step: int):
    for i in range(start, end, step):
        if i % 2 is 0:
            print(i + " is even")
        else:
            print(i + " is odd")


print(
    to_js(
        oddEven,
        oddEvenStartEnd,
        oddEvenStartEndStep,
        minify=False,
    ),
    end="\n\n",
)
