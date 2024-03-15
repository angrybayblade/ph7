from ph7 import CSSObject


class item(CSSObject):
    height = "30px"
    width = "100%"

    margin_top = "5px"

    class _nth_child(CSSObject, n=1):
        margin_top = "0px"

    class __before(CSSObject):
        content = '">"'


print(item())
