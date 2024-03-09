from ph7.css import CSSObject


class flex_center(CSSObject):

    display = "flex"
    align_items = "center"
    justify_content = "center"


print(flex_center())