from ph7 import CSSObject


class item(CSSObject):
    """Flex center."""

    height = "30px"
    width = "100%"

    margin_top = "5px"

    class _nth_child(CSSObject):
        """Nth child."""

        child = 1
        margin_top = "0px"

    class __before(CSSObject):
        """Before selector."""

        content = '">"'


print(item())
