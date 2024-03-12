from ph7 import CSSObject


class flex_center(CSSObject):
    display = "flex"
    align_items = "center"
    justify_content = "center"


class textbox(flex_center):
    height = "100vh"
    width = "100vw"

    class text(CSSObject):
        font_size = "12px"
        font_weight = "500"
        font_family = "Lucida Console, Monaco, monospace"


print(textbox())
