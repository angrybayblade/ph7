from ph7.js.transpile import to_js


def tryCatch():
    try:
        print("try something")
    except Exception as e:
        print(f"Error: {e}")


def tryCatchFinally():
    try:
        print("try something")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("finally")


def tryRaiseCatch():
    try:
        raise Exception("Some error")
    except Exception as e:
        print(f"Error: {e}")


print(
    to_js(
        tryCatch,
        tryCatchFinally,
        tryRaiseCatch,
        minify=False,
    ),
    end="\n\n",
)
