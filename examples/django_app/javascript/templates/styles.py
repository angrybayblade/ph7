from ph7 import CSSObject


class container(CSSObject):
    display = "flex"
    justify_content = "center"
    align_items = "center"
    flex_direction = "column"

    height = "100%"
    width = "100%"


class image(CSSObject):
    height = "200px"
    width = "400px"

    margin_bottom = "25px"
