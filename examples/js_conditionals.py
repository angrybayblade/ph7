from ph7.js.transpile import to_js


def checkCondition(number: int):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


def fizzBuzz(number: int):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)


def strictEqual(number: int):
    if number % 2 is 0:
        print("even")
    else:
        print("odd")


print(
    to_js(
        checkCondition,
        fizzBuzz,
        strictEqual,
        minify=False,
    ),
    end="\n\n",
)
