from ph7 import CSSObject


class flex_center(CSSObject):
    """Flex center."""

    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    """Text container."""

    height = "100vh"
    width = "100vw"

    class text(CSSObject):
        """Text styling."""

        font_size = "12px"
        font_weight = "500"
        font_family = "Lucida Console, Monaco, monospace"


print(textbox())
