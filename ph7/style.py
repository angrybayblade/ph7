"""
This file is auto generated using scripts/render/style.py
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals


from typing_extensions import Literal, NotRequired, TypedDict

attributes = {
    "animation": "animation",
    "animation_play_state": "animation-play-state",
    "animation_name": "animation-name",
    "animation_fill_mode": "animation-fill-mode",
    "align_items": "align-items",
    "animation_duration": "animation-duration",
    "align_self": "align-self",
    "align_content": "align-content",
    "animation_direction": "animation-direction",
    "animation_iteration_count": "animation-iter-count",
    "all": "all",
    "animation_delay": "animation-delay",
    "animation_timing_function": "animation-timing-fn",
    "backface_visibility": "backface-visibility",
    "background_position": "background-position",
    "background_size": "background-size",
    "background": "background",
    "background_attachment": "background-attachment",
    "background_color": "background-color",
    "background_repeat": "background-repeat",
    "background_clip": "background-clip",
    "background_blend_mode": "background-blend-mode",
    "background_origin": "background-origin",
    "background_image": "background-image",
    "border": "border",
    "border_bottom": "border-bottom",
    "border_bottom_left_radius": "border-bottom-left-radius",
    "border_bottom_color": "border-bottom-color",
    "border_bottom_style": "border-bottom-style",
    "border_image_repeat": "border-image-repeat",
    "border_image": "border-image",
    "border_collapse": "border-collapse",
    "border_image_outset": "border-image-outset",
    "border_bottom_width": "border-bottom-width",
    "border_color": "border-color",
    "border_bottom_right_radius": "border-bottom-right-radius",
    "border_image_slice": "border-image-slice",
    "border_image_source": "border-image-source",
    "border_image_width": "border-image-width",
    "border_left_color": "border-left-color",
    "border_left_style": "border-left-style",
    "border_right_style": "border-right-style",
    "border_radius": "border-radius",
    "border_left": "border-left",
    "border_left_width": "border-left-width",
    "border_right_color": "border-right-color",
    "border_right": "border-right",
    "border_right_width": "border-right-width",
    "border_spacing": "border-spacing",
    "border_style": "border-style",
    "border_top": "border-top",
    "border_top_right_radius": "border-top-right-radius",
    "border_top_color": "border-top-color",
    "border_top_left_radius": "border-top-left-radius",
    "box_shadow": "box-shadow",
    "border_top_width": "border-top-width",
    "border_width": "border-width",
    "box_decoration_break": "box-decoration-break",
    "border_top_style": "border-top-style",
    "bottom": "bottom",
    "box_sizing": "box-sizing",
    "caption_side": "caption-side",
    "caret_color": "caret-color",
    "charset": "@charset",
    "clear": "clear",
    "column_count": "column-count",
    "clip": "clip",
    "column_rule": "column-rule",
    "column_gap": "column-gap",
    "clip_path": "clip-path",
    "color": "color",
    "column_fill": "column-fill",
    "column_rule_color": "column-rule-color",
    "column_rule_style": "column-rule-style",
    "column_rule_width": "column-rule-width",
    "column_span": "column-span",
    "column_width": "column-width",
    "columns": "columns",
    "content": "content",
    "counter_increment": "counter-increment",
    "direction": "direction",
    "counter_reset": "counter-reset",
    "display": "display",
    "empty_cells": "empty-cells",
    "filter": "filter",
    "cursor": "cursor",
    "flex": "flex",
    "flex_basis": "flex-basis",
    "flex_direction": "flex-direction",
    "flex_flow": "flex-flow",
    "flex_grow": "flex-grow",
    "flex_shrink": "flex-shrink",
    "font_family": "font-family",
    "float": "float",
    "font_face": "@font-face",
    "flex_wrap": "flex-wrap",
    "font": "font",
    "font_kerning": "font-kerning",
    "font_size": "font-size",
    "font_stretch": "font-stretch",
    "font_variant": "font-variant",
    "font_style": "font-style",
    "font_weight": "font-weight",
    "gap": "gap",
    "grid": "grid",
    "grid_auto_columns": "grid-auto-columns",
    "grid_auto_rows": "grid-auto-rows",
    "grid_area": "grid-area",
    "grid_column": "grid-column",
    "grid_auto_flow": "grid-auto-flow",
    "grid_column_end": "grid-column-end",
    "grid_column_gap": "grid-column-gap",
    "grid_gap": "grid-gap",
    "grid_column_start": "grid-column-start",
    "grid_row_end": "grid-row-end",
    "grid_row": "grid-row",
    "grid_row_gap": "grid-row-gap",
    "grid_template_areas": "grid-template-areas",
    "grid_template": "grid-template",
    "height": "height",
    "grid_template_columns": "grid-template-columns",
    "grid_row_start": "grid-row-start",
    "grid_template_rows": "grid-template-rows",
    "hyphens": "hyphens",
    "justify_content": "justify-content",
    "keyframes": "@keyframes",
    "left": "left",
    "letter_spacing": "letter-spacing",
    "line_height": "line-height",
    "list_style_image": "list-style-image",
    "list_style": "list-style",
    "margin": "margin",
    "margin_bottom": "margin-bottom",
    "list_style_position": "list-style-position",
    "list_style_type": "list-style-type",
    "margin_left": "margin-left",
    "margin_right": "margin-right",
    "margin_top": "margin-top",
    "max_width": "max-width",
    "max_height": "max-height",
    "media": "@media",
    "min_height": "min-height",
    "min_width": "min-width",
    "opacity": "opacity",
    "outline": "outline",
    "object_position": "object-position",
    "order": "order",
    "object_fit": "object-fit",
    "outline_color": "outline-color",
    "outline_offset": "outline-offset",
    "outline_style": "outline-style",
    "outline_width": "outline-width",
    "overflow_x": "overflow-x",
    "overflow_y": "overflow-y",
    "overflow": "overflow",
    "padding_left": "padding-left",
    "padding_bottom": "padding-bottom",
    "padding_top": "padding-top",
    "padding": "padding",
    "padding_right": "padding-right",
    "page_break_after": "page-break-after",
    "page_break_before": "page-break-before",
    "page_break_inside": "page-break-inside",
    "perspective": "perspective",
    "position": "position",
    "pointer_events": "pointer-events",
    "perspective_origin": "perspective-origin",
    "quotes": "quotes",
    "right": "right",
    "row_gap": "row-gap",
    "text_align": "text-align",
    "scroll_behavior": "scroll-behavior",
    "table_layout": "table-layout",
    "text_align_last": "text-align-last",
    "text_decoration": "text-decoration",
    "text_decoration_color": "text-decoration-color",
    "text_decoration_line": "text-decoration-line",
    "text_indent": "text-indent",
    "text_decoration_style": "text-decoration-style",
    "text_justify": "text-justify",
    "text_shadow": "text-shadow",
    "text_overflow": "text-overflow",
    "text_transform": "text-transform",
    "top": "top",
    "transform_origin": "transform-origin",
    "transform": "transform",
    "transform_style": "transform-style",
    "transition": "transition",
    "transition_duration": "transition-duration",
    "transition_delay": "transition-delay",
    "transition_property": "transition-property",
    "transition_timing_function": "transition-timing-function",
    "user_select": "user-select",
    "width": "width",
    "word_break": "word-break",
    "visibility": "visibility",
    "word_spacing": "word-spacing",
    "white_space": "white-space",
    "vertical_align": "vertical-align",
    "word_wrap": "word-wrap",
    "z_index": "z-index",
    "writing_mode": "writing-mode",
}


class Style(TypedDict):
    """CSS Properties"""

    animation: NotRequired[  # type: ignore
        Literal[
            "animation-name",
            "animation-duration",
            "animation-timing-function",
            "animation-delay",
            "animation-iteration-count",
            "animation-direction",
            "animation-fill-mode",
            "animation-play-state",
            str,
        ]
    ]
    """No syntax rule available"""

    animation_play_state: NotRequired[  # type: ignore
        Literal["paused", "running", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    animation_name: NotRequired[  # type: ignore
        Literal["keyframename", "none", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    animation_fill_mode: NotRequired[  # type: ignore
        Literal["none", "forwards", "backwards", "both", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    align_items: NotRequired[  # type: ignore
        Literal[
            "stretch",
            "center",
            "flex-start",
            "flex-end",
            "baseline",
            "initial",
            "inherit",
            str,
        ]
    ]
    """align-items: stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    animation_duration: NotRequired[  # type: ignore
        Literal["time", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    align_self: NotRequired[  # type: ignore
        Literal[
            "auto",
            "stretch",
            "center",
            "flex-start",
            "flex-end",
            "baseline",
            "initial",
            "inherit",
            str,
        ]
    ]
    """align-self: auto | stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    align_content: NotRequired[  # type: ignore
        Literal[
            "stretch",
            "center",
            "flex-start",
            "flex-end",
            "space-between",
            "space-around",
            "initial",
            "inherit",
            str,
        ]
    ]
    """align-content: stretch | center | flex-start |flex-end | space-between |space-around | initial | inherit;"""

    animation_direction: NotRequired[  # type: ignore
        Literal[
            "normal",
            "reverse",
            "alternate",
            "alternate-reverse",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    animation_iteration_count: NotRequired[  # type: ignore
        Literal["number", "infinite", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    all: NotRequired[Literal["initial", "inherit", "unset", str]]  # type: ignore
    """No syntax rule available"""

    animation_delay: NotRequired[  # type: ignore
        Literal["time", "initial", "inherit", str]
    ]
    """animation-delay: time | initial | inherit;"""

    animation_timing_function: NotRequired[  # type: ignore
        Literal[
            "linear",
            "ease",
            "ease-in",
            "ease-out",
            "ease-in-out",
            "step-start",
            "step-end",
            "steps(int,start|end)",
            "cubic-bezier(n,n,n,n)",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    backface_visibility: NotRequired[  # type: ignore
        Literal["visible", "hidden", "initial", "inherit", str]
    ]
    """backface-visibility: visible | hidden | initial | inherit;"""

    background_position: NotRequired[  # type: ignore
        Literal[
            "left top",
            "left center",
            "left bottom",
            "right top",
            "right center",
            "right bottom",
            "center top",
            "center center",
            "center bottom",
            "initial",
            "inherit",
            str,
        ]
    ]
    """background-position: value | x% y% |xpos ypos | initial | inherit"""

    background_size: NotRequired[  # type: ignore
        Literal[
            "auto",
            "length",
            "percentage",
            "cover",
            "contain",
            "initial",
            "inherit",
            str,
        ]
    ]
    """background-size: auto | length | cover |contain | initial | inherit;"""

    background: NotRequired[  # type: ignore
        Literal[
            "background-color",
            "background-image",
            "background-position",
            "background-size",
            "background-repeat",
            "background-origin",
            "background-clip",
            "background-attachment",
            "initial",
            "inherit",
            str,
        ]
    ]
    """background: bg-color bg-image position/bg-size bg-repeatbg-origin bg-clip bg-attachment | initial | inherit;"""

    background_attachment: NotRequired[  # type: ignore
        Literal["scroll", "fixed", "local", "initial", "inherit", str]
    ]
    """background-attachment: scroll | fixed | local |initial | inherit;"""

    background_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """background-color: color | transparent | initial | inherit;"""

    background_repeat: NotRequired[  # type: ignore
        Literal[
            "repeat",
            "repeat-x",
            "repeat-y",
            "no-repeat",
            "space",
            "round",
            "initial",
            "inherit",
            str,
        ]
    ]
    """background-repeat: repeat | repeat-x | repeat-y |no-repeat | initial | inherit;"""

    background_clip: NotRequired[  # type: ignore
        Literal["content-box", "padding-box", "border-box", "initial", "inherit", str]
    ]
    """background-clip: border-box | padding-box |content-box | initial | inherit;"""

    background_blend_mode: NotRequired[  # type: ignore
        Literal[
            "normal",
            "multiply",
            "screen",
            "overlay",
            "darken",
            "lighten",
            "color-dodge",
            "saturation",
            "color",
            "luminosity",
            str,
        ]
    ]
    """background-blend-mode: normal | multiply | screen | overlay | darken |lighten | color-dodge | saturation | color |luminosity;"""

    background_origin: NotRequired[  # type: ignore
        Literal["padding-box", "border-box", "content-box", "initial", "inherit", str]
    ]
    """background-origin: padding-box | border-box |content-box | initial | inherit;"""

    background_image: NotRequired[  # type: ignore
        Literal[
            "url",
            "none",
            "linear-gradient()",
            "radial-gradient()",
            "repeating-linear-gradient()",
            "repeating-radial-gradient()",
            "inherit",
            str,
        ]
    ]
    """background-image: url(url) | none | linear-gradient() | radial-gradient() |repeating-linear-gradient() | repeating-radial-gradient() |inherit;"""

    border: NotRequired[  # type: ignore
        Literal[
            "border-width", "border-style", "border-color", "initial", "inherit", str
        ]
    ]
    """border: border-width border-style border-color |initial | inherit;"""

    border_bottom: NotRequired[  # type: ignore
        Literal[
            "border-width", "border-style", "border-color", "initial", "inherit", str
        ]
    ]
    """border-bottom: border-width border-style border-color |initial | inherit;"""

    border_bottom_left_radius: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """border-bottom-left-radius: length | length% |initial | inherit;"""

    border_bottom_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """border-bottom-color: color | transparent |initial | inherit;"""

    border_bottom_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    border_image_repeat: NotRequired[  # type: ignore
        Literal["stretch", "repeat", "round", "space", "initial", "inherit", str]
    ]
    """border-image-repeat: stretch | repeat |round | initial | inherit;"""

    border_image: NotRequired[  # type: ignore
        Literal[
            "border-image-source",
            "border-image-slice",
            "border-image-width",
            "border-image-outset",
            "border-image-repeat",
            "initial",
            "inherit",
            str,
        ]
    ]
    """border-image: URL slice width outset repeat |initial | inherit;"""

    border_collapse: NotRequired[  # type: ignore
        Literal["separate", "collapse", "initial", "inherit", str]
    ]
    """border-collapse: separate | collapse | initial | inherit;"""

    border_image_outset: NotRequired[  # type: ignore
        Literal["length", "number", "initial", "inherit", str]
    ]
    """border-image-outset: length | number |initial | inherit;"""

    border_bottom_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    border_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """border-color: color | transparent | initial | inherit;"""

    border_bottom_right_radius: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """border-bottom-right-radius: length | length% | initial | inherit;"""

    border_image_slice: NotRequired[  # type: ignore
        Literal["number", "%", "fill", "initial", "inherit", str]
    ]
    """border-image-slice: number | % |fill | initial | inherit;"""

    border_image_source: NotRequired[  # type: ignore
        Literal["none", "image", "initial", "inherit", str]
    ]
    """border-image-source: none | image | initial | inherit;"""

    border_image_width: NotRequired[  # type: ignore
        Literal["length", "number", "%", "auto", "initial", "inherit", str]
    ]
    """border-image-width: number | % | auto | initial | inherit;"""

    border_left_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """border-left-color: color | transparent | initial | inherit;"""

    border_left_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    border_right_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    border_radius: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    border_left: NotRequired[  # type: ignore
        Literal[
            "border-width", "border-style", "border-color", "initial", "inherit", str
        ]
    ]
    """border-left: border-width border-style border-color |initial | inherit;"""

    border_left_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    border_right_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """border-right-color: color | transparent | initial | inherit;"""

    border_right: NotRequired[  # type: ignore
        Literal[
            "border-width", "border-style", "border-color", "initial", "inherit", str
        ]
    ]
    """border-right: border-width border-style border-color |initial | inherit;"""

    border_right_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    border_spacing: NotRequired[  # type: ignore
        Literal["length length", "initial", "inherit", str]
    ]
    """border-spacing: length | initial | inherit;"""

    border_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    border_top: NotRequired[  # type: ignore
        Literal[
            "border-width", "border-style", "border-color", "initial", "inherit", str
        ]
    ]
    """border-top: border-width border-style border-color |initial | inherit;"""

    border_top_right_radius: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """border-top-right-radius: length | length% | initial | inherit;"""

    border_top_color: NotRequired[  # type: ignore
        Literal["color", "transparent", "initial", "inherit", str]
    ]
    """border-top-color: color | transparent | initial | inherit;"""

    border_top_left_radius: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """border-top-left-radius: length | length% | initial | inherit;"""

    box_shadow: NotRequired[  # type: ignore
        Literal[
            "none",
            "h-offset",
            "v-offset",
            "blur",
            "spread",
            "color",
            "inset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """box-shadow: none | h-offset v-offset blur spread color |inset | initial | inherit;"""

    border_top_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """No syntax rule available"""

    border_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """border-width: medium | thin | thick |length | initial | inherit;"""

    box_decoration_break: NotRequired[  # type: ignore
        Literal["slice", "clone", "initial", "inherit", str]
    ]
    """box-decoration-break: slice | clone |initial | inherit | unset;"""

    border_top_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    bottom: NotRequired[  # type: ignore
        Literal["auto", "length", "%", "initial", "inherit", str]
    ]
    """bottom: auto | length | initial | inherit;"""

    box_sizing: NotRequired[  # type: ignore
        Literal["content-box", "border-box", "initial", "inherit", str]
    ]
    """box-sizing: content-box | border-box | initial | inherit;"""

    caption_side: NotRequired[  # type: ignore
        Literal["bottom", "top", "initial", "inherit", str]
    ]
    """caption-side: top | bottom | initial | inherit;"""

    caret_color: NotRequired[  # type: ignore
        Literal["auto", "color", "transparent", str]
    ]
    """caret-color: auto | color | transparent;"""

    charset: NotRequired[Literal["charset", str]]  # type: ignore
    """@charset "charset";"""

    clear: NotRequired[  # type: ignore
        Literal["none", "left", "right", "both", "initial", "inherit", str]
    ]
    """clear: none | left | right | both |initial | inherit;"""

    column_count: NotRequired[  # type: ignore
        Literal["number", "auto", "initial", "inherit", str]
    ]
    """column-count: number | auto | initial | inherit;"""

    clip: NotRequired[  # type: ignore
        Literal["auto", "shape", "initial", "inherit", str]
    ]
    """clip: auto | shape | initial | inherit;"""

    column_rule: NotRequired[  # type: ignore
        Literal[
            "column-rule-width ",
            "column-rule-style ",
            "column-rule-color ",
            "initial",
            "inherit",
            str,
        ]
    ]
    """column-rule: column-rule-widthcolumn-rule-stylecolumn-rule-color |initial | inherit;"""

    column_gap: NotRequired[  # type: ignore
        Literal["length", "normal", "initial", "inherit", str]
    ]
    """column-gap: length | normal | initial | inherit;"""

    clip_path: NotRequired[  # type: ignore
        Literal[
            "none",
            "basic-shape",
            "margin-box",
            "border-box",
            "padding-box",
            "content-box",
            "fill-box",
            "stroke-box",
            "clip-source",
            "view-box",
            str,
        ]
    ]
    """clip-path: clip-source | basic-shape | margin-box |border-box | padding-box | content-box |fill-box | stroke-box | view-box | none;"""

    color: NotRequired[Literal["color", "initial", "inherit", str]]  # type: ignore
    """color: color | initial | inherit;"""

    column_fill: NotRequired[  # type: ignore
        Literal["balance", "auto", "initial", "inherit", str]
    ]
    """column-fill: balance | auto | initial | inherit;"""

    column_rule_color: NotRequired[  # type: ignore
        Literal["color", "initial", "inherit", str]
    ]
    """column-rule-color: color | initial | inherit;"""

    column_rule_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """column-rule-style: none | hidden | dotted |dashed | solid | double |groove | ridge | inset |outset | initial | inherit;"""

    column_rule_width: NotRequired[  # type: ignore
        Literal["length", "medium", "thin", "thick", "initial", "inherit", str]
    ]
    """column-rule-width: length |medium | thin | thick |initial | inherit;"""

    column_span: NotRequired[  # type: ignore
        Literal["none", "all", "initial", "inherit", str]
    ]
    """column-span: none | all |initial | inherit;"""

    column_width: NotRequired[  # type: ignore
        Literal["auto", "length", "initial", "inherit", str]
    ]
    """column-width: auto | length |initial | inherit;"""

    columns: NotRequired[  # type: ignore
        Literal["auto", "column-width", "column-count", "initial", "inherit", str]
    ]
    """columns: auto | column-width column-count |initial | inherit;"""

    content: NotRequired[  # type: ignore
        Literal[
            "normal",
            "none",
            "counter",
            "attr(attribute)",
            "string",
            "open-quote",
            "close-quote",
            "no-open-quote",
            "no-close-quote",
            "url(url)",
            "initial",
            "inherit",
            str,
        ]
    ]
    """content: normal | none | counter | attr | string |open-quote | close-quote | no-open-quote |no-close-quote | url | initial | inherit;"""

    counter_increment: NotRequired[  # type: ignore
        Literal["none", "name number", "initial", "inherit", str]
    ]
    """counter-increment: none | name number |initial | inherit;"""

    direction: NotRequired[  # type: ignore
        Literal["ltr", "rtl", "initial", "inherit", str]
    ]
    """direction: ltr | rtl | initial | inherit;"""

    counter_reset: NotRequired[  # type: ignore
        Literal["none", "name number", "initial", "inherit", str]
    ]
    """counter-reset: none | name number | initial | inherit;"""

    display: NotRequired[  # type: ignore
        Literal[
            "inline",
            "block",
            "contents",
            "flex",
            "grid",
            "inline-block",
            "inline-flex",
            "inline-grid",
            "inline-table",
            "list-item",
            "run-in",
            "table",
            "table-caption",
            "table-column-group",
            "table-header-group",
            "table-footer-group",
            "table-row-group",
            "table-cell",
            "table-column",
            "table-row",
            "none",
            "initial",
            "inherit",
            str,
        ]
    ]
    """display: value"""

    empty_cells: NotRequired[  # type: ignore
        Literal["show", "hide", "initial", "inherit", str]
    ]
    """empty-cells: show | hide | initial | inherit;"""

    filter: NotRequired[  # type: ignore
        Literal[
            "none",
            "blur(px)",
            "brightness(%)",
            "contrast(%)",
            "drop-shadow(h-shadow,v-shadow,blur,spread,color)",
            "grayscale(%)",
            "hue-rotate(deg)",
            "invert(%)",
            "opacity(%)",
            "saturate(%)",
            "sepia(%)",
            "url(xml-file)",
            "initial",
            "inherit",
            str,
        ]
    ]
    """filter: none | blur() | brightness() | contrast() |drop-shadow() | grayscale() | hue-rotate() |invert() | opacity() | saturate() |sepia() | url();"""

    cursor: NotRequired[  # type: ignore
        Literal[
            "alias",
            "all-scroll",
            "auto",
            "cell",
            "context-menu",
            "col-resize",
            "copy",
            "crosshair",
            "default",
            "e-resize",
            "ew-resize",
            "grab",
            "grabbing",
            "help",
            "move",
            "n-resize",
            "ne-resize",
            "nesw-resize",
            "ns-resize",
            "nw-resize",
            "nwse-resize",
            "no-drop",
            "none",
            "not-allowed",
            "pointer",
            "progress",
            "row-resize",
            "s-resize",
            "se-resize",
            "sw-resize",
            "text",
            "URL",
            "vertical-text",
            "w-resize",
            "wait",
            "zoom-in",
            "zoom-out",
            "initial",
            "inherit",
            str,
        ]
    ]
    """cursor: value;"""

    flex: NotRequired[  # type: ignore
        Literal[
            "flex-grow",
            "flex-shrink",
            "flex-basis",
            "auto",
            "none",
            "initial",
            "inherit",
            str,
        ]
    ]
    """flex: flex-grow flex-shrink flex-basis |auto | initial | inherit;"""

    flex_basis: NotRequired[  # type: ignore
        Literal["auto", "length", "initial", "inherit", str]
    ]
    """flex-basis: auto | length | initial | inherit;"""

    flex_direction: NotRequired[  # type: ignore
        Literal[
            "row", "row-reverse", "column", "column-reverse", "initial", "inherit", str
        ]
    ]
    """flex-direction: row | row-reverse | column |column-reverse | initial |inherit;"""

    flex_flow: NotRequired[  # type: ignore
        Literal["flex-direction", "flex-wrap", "initial", "inherit", str]
    ]
    """flex-flow: flex-direction flex-wrap |initial | inherit;"""

    flex_grow: NotRequired[Literal["number", "initial", "inherit", str]]  # type: ignore
    """flex-grow: number | initial | inherit;"""

    flex_shrink: NotRequired[  # type: ignore
        Literal["number", "initial", "inherit", str]
    ]
    """flex-shrink: number | initial | inherit;"""

    font_family: NotRequired[  # type: ignore
        Literal[
            "Arial, Arial, Helvetica, sans-serif",
            "Courier New, Courier New, monospace",
            "Georgia, serif",
            "Lucida Console, Monaco, monospace",
            "Lucida Sans Unicode, Lucida Grande, sans-serif",
            "Palatino Linotype, Book Antiqua, Palatino, serif",
            "Tahoma, Geneva, sans-serif",
            "Times New Roman, Times New Roman, Times, serif",
            "Trebuchet MS, Trebuchet MS, sans-serif",
            "Verdana, Verdana, Geneva, sans-serif",
            str,
        ]
    ]
    """font-family: family-name | generic-family |initial | inherit;"""

    float: NotRequired[  # type: ignore
        Literal["none", "left", "right", "initial", "inherit", str]
    ]
    """float: none | left | right | initial | inherit;"""

    font_face: NotRequired[  # type: ignore
        Literal[
            "font-family",
            "src",
            "font-stretch",
            "font-style",
            "font-weight",
            "unicode-range",
            str,
        ]
    ]
    """@font-face { font-properties }"""

    flex_wrap: NotRequired[  # type: ignore
        Literal["nowrap", "wrap", "wrap-reverse", "initial", "inherit", str]
    ]
    """flex-wrap: nowrap | wrap | wrap-reverse |initial | inherit;"""

    font: NotRequired[  # type: ignore
        Literal[
            "font-style",
            "font-variant",
            "font-weight",
            "font-size",
            "font-family",
            "inherit",
            "Built in browser fonts",
            "caption",
            "icon",
            "menu",
            "message-box",
            "small-caption",
            "status-bar",
            "initial",
            str,
        ]
    ]
    """No syntax rule available"""

    font_kerning: NotRequired[Literal["auto", "normal", "none", str]]  # type: ignore
    """font-kerning: auto | normal | none;"""

    font_size: NotRequired[  # type: ignore
        Literal[
            "medium",
            "xx-small",
            "x-small",
            "small",
            "large",
            "x-large",
            "xx-large",
            "smaller",
            "larger",
            "length",
            "%",
            "initial",
            "inherit",
            str,
        ]
    ]
    """font-size: medium | xx-small | x-small | small |large | x-large | xx-large | smaller |larger | length | initial | inherit;"""

    font_stretch: NotRequired[  # type: ignore
        Literal[
            "ultra-condensed",
            "extra-condensed",
            "condensed",
            "semi-condensed",
            "normal",
            "semi-expanded",
            "expanded",
            "extra-expanded",
            "ultra-expanded",
            "initial",
            "inherit",
            str,
        ]
    ]
    """font-stretch: ultra-condensed | extra-condensed |condensed | semi-condensed | normal |semi-expanded | expanded | extra-expanded |ultra-expanded | initial | inherit;"""

    font_variant: NotRequired[  # type: ignore
        Literal["normal", "small-caps", "initial", "inherit", str]
    ]
    """font-variant: normal | small-caps |initial | inherit;"""

    font_style: NotRequired[  # type: ignore
        Literal["normal", "italic", "oblique", "initial", "inherit", str]
    ]
    """font-style: normal | italic | oblique |initial | inherit;"""

    font_weight: NotRequired[  # type: ignore
        Literal[
            "normal",
            "bold",
            "bolder",
            "lighter",
            "100",
            "200",
            "300",
            "400",
            "500",
            "600",
            "700",
            "800",
            "900",
            "initial",
            "inherit",
            str,
        ]
    ]
    """font-weight: normal | bold | bolder | lighter |number | initial | inherit;"""

    gap: NotRequired[  # type: ignore
        Literal["length", "normal", "initial", "inherit", str]
    ]
    """gap: length | normal | initial | inherit;"""

    grid: NotRequired[Literal["none", "initial", "inherit", str]]  # type: ignore
    """
    grid: none |grid-template-rows / grid-template-columns |grid-template-areas |
    grid-template-rows / [grid-auto-flow] grid-auto-columns |
    [grid-auto-flow] grid-auto-rows / grid-template-columns |initial | inherit;
    """

    grid_auto_columns: NotRequired[  # type: ignore
        Literal[
            "auto", "min-content", "max-content", "minmax(min.max)", "length", "%", str
        ]
    ]
    """grid-auto-columns: auto | min-content | max-content |minmax() | length | %;"""

    grid_auto_rows: NotRequired[  # type: ignore
        Literal[
            "auto", "max-content", "min-content", "minmax(min.max)", "length", "%", str
        ]
    ]
    """grid-auto-columns: auto | max-content | min-content |minmax | length | %;"""

    grid_area: NotRequired[  # type: ignore
        Literal[
            "grid-row-start",
            "grid-column-start",
            "grid-row-end",
            "grid-column-end",
            "itemname",
            str,
        ]
    ]
    """grid-area: grid-row-start / grid-column-start /grid-row-end / grid-column-end |itemname;"""

    grid_column: NotRequired[  # type: ignore
        Literal["grid-column-start", "grid-column-end", "span n", str]
    ]
    """grid-column: grid-column-start  [grid-column-end | span n] ;"""

    grid_auto_flow: NotRequired[  # type: ignore
        Literal["row", "column", "dense", "row dense", "column dense", str]
    ]
    """grid-auto-flow: row | column | dense |row dense | column dense;"""

    grid_column_end: NotRequired[  # type: ignore
        Literal["auto", "column", "span n", str]
    ]
    """grid-column-end: auto | column | span n;"""

    grid_column_gap: NotRequired[Literal["length", str]]  # type: ignore
    """grid-column-gap: length;"""

    grid_gap: NotRequired[  # type: ignore
        Literal["grid-row-gap", "grid-column-gap", str]
    ]
    """grid-gap: grid-row-gap grid-column-gap;"""

    grid_column_start: NotRequired[  # type: ignore
        Literal["auto", "column", "span n", str]
    ]
    """grid-column-start: auto | column | span n;"""

    grid_row_end: NotRequired[Literal["auto", "span n", "row", str]]  # type: ignore
    """grid-row-end: auto | span n | row-line;"""

    grid_row: NotRequired[  # type: ignore
        Literal["grid-row-start", "grid-row-end", "span n", str]
    ]
    """grid-row: grid-row-start  [grid-row-end | span n] ;"""

    grid_row_gap: NotRequired[Literal["length", str]]  # type: ignore
    """grid-row-gap: length;"""

    grid_template_areas: NotRequired[Literal["none", "areanames", str]]  # type: ignore
    """grid-template-areas: none | areanames;"""

    grid_template: NotRequired[  # type: ignore
        Literal[
            "none",
            "grid-template-rows",
            "grid-template-columns",
            "grid-template-areas",
            "initial",
            "inherit",
            str,
        ]
    ]
    """grid-template: none | grid-template-rows / grid-template-columns |grid-template-areas | initial | inherit;"""

    height: NotRequired[  # type: ignore
        Literal["auto", "length", "%", "initial", "inherit", str]
    ]
    """height: auto | length | initial | inherit;"""

    grid_template_columns: NotRequired[  # type: ignore
        Literal[
            "none",
            "auto",
            "max-content",
            "min-content",
            "length",
            "initial",
            "inherit",
            str,
        ]
    ]
    """grid-template-columns: none | auto | max-content |min-content | length | initial | inherit;"""

    grid_row_start: NotRequired[Literal["auto", "span n", "row", str]]  # type: ignore
    """grid-row-start: auto | span n | row-line;"""

    grid_template_rows: NotRequired[  # type: ignore
        Literal[
            "none",
            "auto",
            "max-content",
            "min-content",
            "length",
            "initial",
            "inherit",
            str,
        ]
    ]
    """grid-template-rows: none | auto | max-content |min-content | length | initial | inherit;"""

    hyphens: NotRequired[  # type: ignore
        Literal["none", "manual", "auto", "initial", "inherit", str]
    ]
    """hyphens: none | manual | auto | initial | inherit;"""

    justify_content: NotRequired[  # type: ignore
        Literal[
            "flex-start",
            "flex-end",
            "center",
            "space-between",
            "space-around",
            "initial",
            "inherit",
            str,
        ]
    ]
    """justify-content: flex-start | flex-end | center | space-between |space-around | initial | inherit;"""

    keyframes: NotRequired[  # type: ignore
        Literal["animation-name", "keyframes-selector", "css-styles", str]
    ]
    """@keyframes animation-name {keyframes-selector { css-styles; }}"""

    left: NotRequired[  # type: ignore
        Literal["auto", "length", "%", "initial", "inherit", str]
    ]
    """left: auto | length | initial | inherit;"""

    letter_spacing: NotRequired[  # type: ignore
        Literal["normal", "length", "initial", "inherit", str]
    ]
    """letter-spacing: normal | length | initial | inherit;"""

    line_height: NotRequired[  # type: ignore
        Literal["normal", "number", "length", "%", "initial", "inherit", str]
    ]
    """line-height: normal | number | length |initial | inherit;"""

    list_style_image: NotRequired[  # type: ignore
        Literal["none", "url", "initial", "inherit", str]
    ]
    """list-style-image: none | url | initial | inherit;"""

    list_style: NotRequired[  # type: ignore
        Literal[
            "list-style-type",
            "list-style-position",
            "list-style-image",
            "initial",
            "inherit",
            str,
        ]
    ]
    """list-style: list-style-type list-style-position list-style-image |initial | inherit;"""

    margin: NotRequired[  # type: ignore
        Literal["length", "%", "auto", "initial", "inherit", str]
    ]
    """margin: length | auto | initial | inherit;"""

    margin_bottom: NotRequired[  # type: ignore
        Literal["length", "%", "auto", "initial", "inherit", str]
    ]
    """margin-bottom: length | auto | initial | inherit;"""

    list_style_position: NotRequired[  # type: ignore
        Literal["inside", "outside", "initial", "inherit", str]
    ]
    """list-style-position: inside | outside | initial | inherit;"""

    list_style_type: NotRequired[  # type: ignore
        Literal[
            "disc",
            "armenian",
            "circle",
            "cjk-ideographic",
            "decimal",
            "decimal-leading-zero",
            "georgian",
            "hebrew",
            "hiragana",
            "hiragana-iroha",
            "katakana",
            "katakana-iroha",
            "lower-alpha",
            "lower-greek",
            "lower-latin",
            "lower-roman",
            "none",
            "square",
            "upper-alpha",
            "upper-greek",
            "upper-latin",
            "upper-roman",
            "initial",
            "inherit",
            str,
        ]
    ]
    """list-style-type: value;"""

    margin_left: NotRequired[  # type: ignore
        Literal["length", "%", "auto", "initial", "inherit", str]
    ]
    """margin-left: length | auto | initial | inherit;"""

    margin_right: NotRequired[  # type: ignore
        Literal["length", "%", "auto", "initial", "inherit", str]
    ]
    """margin-right: length | auto | initial | inherit;"""

    margin_top: NotRequired[  # type: ignore
        Literal["length", "%", "auto", "initial", "inherit", str]
    ]
    """margin-top: length | auto | initial | inherit;"""

    max_width: NotRequired[  # type: ignore
        Literal["none", "length", "%", "initial", "inherit", str]
    ]
    """max-width: none | length | initial | inherit;"""

    max_height: NotRequired[  # type: ignore
        Literal["none", "length", "%", "initial", "inherit", str]
    ]
    """max-height: none | length | initial | inherit;"""

    media: NotRequired[Literal["all", "print", "screen", "speech", str]]  # type: ignore
    """@media not | only mediatype and(mediafeature and | or | not mediafeature) {CSS-Code;}"""

    min_height: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """min-height: length | initial | inherit;"""

    min_width: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """min-width: length | initial | inherit;"""

    opacity: NotRequired[Literal["number", "initial", "inherit", str]]  # type: ignore
    """opacity: number | initial | inherit;"""

    outline: NotRequired[  # type: ignore
        Literal[
            "outline-width", "outline-style", "outline-color", "initial", "inherit", str
        ]
    ]
    """outline: outline-width outline-style outline-color | initial | inherit;"""

    object_position: NotRequired[  # type: ignore
        Literal["position", "initial", "inherit", str]
    ]
    """object-position: position | initial | inherit;"""

    order: NotRequired[Literal["number", "initial", "inherit", str]]  # type: ignore
    """order: number | initial | inherit;"""

    object_fit: NotRequired[  # type: ignore
        Literal[
            "fill", "contain", "cover", "scale-down", "none", "initial", "inherit", str
        ]
    ]
    """object-fit: fill | contain | cover | scale-down |none | initial | inherit;"""

    outline_color: NotRequired[  # type: ignore
        Literal["invert", "color", "initial", "inherit", str]
    ]
    """outline-color: invert | color | transparent |initial | inherit;"""

    outline_offset: NotRequired[  # type: ignore
        Literal["length", "initial", "inherit", str]
    ]
    """outline-offset: length | initial | inherit;"""

    outline_style: NotRequired[  # type: ignore
        Literal[
            "none",
            "hidden",
            "dotted",
            "dashed",
            "solid",
            "double",
            "groove",
            "ridge",
            "inset",
            "outset",
            "initial",
            "inherit",
            str,
        ]
    ]
    """outline-style: none | hidden | dotted | dashed |solid | double | groove | ridge |inset | outset | initial | inherit;"""

    outline_width: NotRequired[  # type: ignore
        Literal["medium", "thin", "thick", "length", "initial", "inherit", str]
    ]
    """outline-width: medium | thin | thick |length | initial | inherit;"""

    overflow_x: NotRequired[  # type: ignore
        Literal["visible", "hidden", "scroll", "auto", "initial", "inherit", str]
    ]
    """overflow-x: visible | hidden | scroll |auto | initial | inherit;"""

    overflow_y: NotRequired[  # type: ignore
        Literal["visible", "hidden", "scroll", "auto", "initial", "inherit", str]
    ]
    """overflow-y: visible | hidden | scroll |auto | initial | inherit;"""

    overflow: NotRequired[  # type: ignore
        Literal["visible", "hidden", "scroll", "auto", "initial", "inherit", str]
    ]
    """overflow: visible | hidden | scroll |auto | initial | inherit;"""

    padding_left: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """padding-left: length | initial | inherit;"""

    padding_bottom: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """padding-bottom: length | initial | inherit;"""

    padding_top: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """padding-top: length | initial | inherit;"""

    padding: NotRequired[Literal["length", "initial", "inherit", str]]  # type: ignore
    """padding: length | initial | inherit;"""

    padding_right: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """padding-right: length | initial | inherit;"""

    page_break_after: NotRequired[  # type: ignore
        Literal["auto", "always", "avoid", "left", "right", "initial", "inherit", str]
    ]
    """page-break-after: auto | always | avoid | left |right | initial | inherit;"""

    page_break_before: NotRequired[  # type: ignore
        Literal["auto", "always", "avoid", "left", "right", "initial", "inherit", str]
    ]
    """page-break-before: auto | always | avoid | left |right | initial | inherit;"""

    page_break_inside: NotRequired[  # type: ignore
        Literal["auto", "avoid", "initial", "inherit", str]
    ]
    """page-break-inside: auto | avoid |initial | inherit;"""

    perspective: NotRequired[  # type: ignore
        Literal["length", "none", "initial", "inherit", str]
    ]
    """perspective: length | none | initial | inherit;"""

    position: NotRequired[  # type: ignore
        Literal[
            "static",
            "relative",
            "absolute",
            "fixed",
            "sticky",
            "initial",
            "inherit",
            str,
        ]
    ]
    """position: static | absolute | fixed | relative |sticky | initial | inherit;"""

    pointer_events: NotRequired[  # type: ignore
        Literal[
            "auto",
            "none",
            "visiblePainted",
            "visibleFill",
            "visibleStroke",
            "visible",
            "painted",
            "fill",
            "stroke",
            "all",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    perspective_origin: NotRequired[  # type: ignore
        Literal["x-axis", "y-axis", "initial", "inherit", str]
    ]
    """perspective-origin: x-axis y-axis |initial | inherit;"""

    quotes: NotRequired[  # type: ignore
        Literal["none", "[string string]+", "initial", "inherit", str]
    ]
    """quotes: none | [string string]+ |initial | inherit;"""

    right: NotRequired[  # type: ignore
        Literal["auto", "length", "%", "initial", "inherit", str]
    ]
    """right: auto | length | initial | inherit;"""

    row_gap: NotRequired[  # type: ignore
        Literal["length", "normal", "initial", "inherit", str]
    ]
    """row-gap: length | normal | initial | inherit;"""

    text_align: NotRequired[  # type: ignore
        Literal["left", "right", "center", "justify", "initial", "inherit", str]
    ]
    """text-align: left | right | center |justify | initial | inherit;"""

    scroll_behavior: NotRequired[  # type: ignore
        Literal["auto", "smooth", "initial", "inherit", str]
    ]
    """scroll-behavior: auto | smooth | initial | inherit;"""

    table_layout: NotRequired[  # type: ignore
        Literal["auto", "fixed", "initial", "inherit", str]
    ]
    """table-layout: auto | fixed | initial | inherit;"""

    text_align_last: NotRequired[  # type: ignore
        Literal[
            "auto",
            "left",
            "right",
            "center",
            "justify",
            "start",
            "end",
            "initial",
            "inherit",
            str,
        ]
    ]
    """text-align-last: auto | left | right | center |justify | start | end |initial | inherit;"""

    text_decoration: NotRequired[  # type: ignore
        Literal[
            "none",
            "text-decoration-line",
            "text-decoration-color",
            "text-decoration-style",
            "initial",
            "inherit",
            str,
        ]
    ]
    """text-decoration: none |text-decoration-line text-decoration-colortext-decoration-style | initial | inherit;"""

    text_decoration_color: NotRequired[  # type: ignore
        Literal["color", "initial", "inherit", str]
    ]
    """text-decoration-color: color | initial | inherit;"""

    text_decoration_line: NotRequired[  # type: ignore
        Literal[
            "none", "underline", "overline", "line-through", "initial", "inherit", str
        ]
    ]
    """text-decoration-line: none | underline |overline | line-through |initial | inherit;"""

    text_indent: NotRequired[  # type: ignore
        Literal["length", "%", "initial", "inherit", str]
    ]
    """text-indent: length | initial | inherit;"""

    text_decoration_style: NotRequired[  # type: ignore
        Literal[
            "solid", "double", "dotted", "dashed", "wavy", "initial", "inherit", str
        ]
    ]
    """text-decoration-style: solid | double | dotted |dashed | wavy | initial | inherit;"""

    text_justify: NotRequired[  # type: ignore
        Literal["none", "auto", "inter-word", "trim", "initial", "inherit", str]
    ]
    """text-justify: auto | inter-word |none | initial | inherit;"""

    text_shadow: NotRequired[  # type: ignore
        Literal[
            "none",
            "x-offset",
            "y-offset",
            "blur-radius",
            "color",
            "initial",
            "inherit",
            str,
        ]
    ]
    """text-shadow: x-offset y-offset blur-radius color |none | initial | inherit;"""

    text_overflow: NotRequired[  # type: ignore
        Literal["clip", "ellipsis", "string", "initial", "inherit", str]
    ]
    """text-overflow: clip | ellipsis | string |initial | inherit;"""

    text_transform: NotRequired[  # type: ignore
        Literal[
            "none", "capitalize", "uppercase", "lowercase", "initial", "inherit", str
        ]
    ]
    """text-transform: none | capitalize | uppercase |lowercase | initial | inherit;"""

    top: NotRequired[  # type: ignore
        Literal["auto", "length", "%", "initial", "inherit", str]
    ]
    """top: auto | length | initial | inherit;"""

    transform_origin: NotRequired[  # type: ignore
        Literal["x-axis", "y-axis", "z-axis", "initial", "inherit", str]
    ]
    """transform-origin: x-axis y-axis z-axis |initial | inherit;"""

    transform: NotRequired[  # type: ignore
        Literal[
            "none",
            "translate(x,y)",
            "translateX(x)",
            "translateY(y)",
            "scale(x,y)",
            "scaleX(x)",
            "scaleY(y)",
            "rotate(angle)",
            "skew(x-angle,y-angle)",
            "skewX(angle)",
            "skewY(angle)",
            "matrix(n,n,n,n,n,n)",
            "initial",
            "inherit",
            str,
        ]
    ]
    """transform: none | transform-functions |initial | inherit;"""

    transform_style: NotRequired[  # type: ignore
        Literal["flat", "preserve-3d", "initial", "inherit", str]
    ]
    """transform-style: flat | preserve-3d | initial | inherit;"""

    transition: NotRequired[  # type: ignore
        Literal[
            "transition-property",
            "transition-duration",
            "transition-timing-function",
            "transition-delay",
            "initial",
            "inherit",
            str,
        ]
    ]
    """transition: property duration timing-function delay |initial | inherit;"""

    transition_duration: NotRequired[  # type: ignore
        Literal["time", "initial", "inherit", str]
    ]
    """transition-duration: time | initial | inherit;"""

    transition_delay: NotRequired[  # type: ignore
        Literal["time", "initial", "inherit", str]
    ]
    """transition-delay: time | initial | inherit;"""

    transition_property: NotRequired[  # type: ignore
        Literal["none", "all", "properties", "initial", "inherit", str]
    ]
    """transition-property: none | all | properties |initial | inherit;"""

    transition_timing_function: NotRequired[  # type: ignore
        Literal[
            "ease",
            "linear",
            "ease-in",
            "ease-out",
            "ease-in-out",
            "step-start",
            "step-end",
            "steps(int,start|end)",
            "cubic-bezier(n,n,n,n)",
            "initial",
            "inherit",
            str,
        ]
    ]
    """No syntax rule available"""

    user_select: NotRequired[  # type: ignore
        Literal["auto", "none", "text", "all", str]
    ]
    """user-select: auto | none | text | all;"""

    width: NotRequired[  # type: ignore
        Literal["auto", "length", "initial", "inherit", str]
    ]
    """width: auto | length | initial | inherit;"""

    word_break: NotRequired[  # type: ignore
        Literal[
            "normal", "break-all", "keep-all", "break-word", "initial", "inherit", str
        ]
    ]
    """word-break: normal | break-all | keep-all |break-word | initial | inherit;"""

    visibility: NotRequired[  # type: ignore
        Literal["visible", "hidden", "collapse", "initial", "inherit", str]
    ]
    """visibility: visible | hidden | collapse |initial | inherit;"""

    word_spacing: NotRequired[  # type: ignore
        Literal["normal", "length", "initial", "inherit", str]
    ]
    """word-spacing: normal | length | initial | inherit;"""

    white_space: NotRequired[  # type: ignore
        Literal[
            "normal", "nowrap", "pre", "pre-line", "pre-wrap", "initial", "inherit", str
        ]
    ]
    """white-space: normal | nowrap | pre |pre-line | pre-wrap | initial | inherit;"""

    vertical_align: NotRequired[  # type: ignore
        Literal[
            "baseline",
            "length",
            "%",
            "sub",
            "super",
            "top",
            "text-top",
            "middle",
            "bottom",
            "text-bottom",
            "initial",
            "inherit",
            str,
        ]
    ]
    """vertical-align: baseline | length | sub | super |top | text-top | middle | bottom |text-bottom | initial | inherit;"""

    word_wrap: NotRequired[  # type: ignore
        Literal["normal", "break-word", "initial", "inherit", str]
    ]
    """word-wrap: normal | break-word | initial | inherit;"""

    z_index: NotRequired[  # type: ignore
        Literal["auto", "number", "initial", "inherit", str]
    ]
    """z-index: auto | number | initial | inherit;"""

    writing_mode: NotRequired[  # type: ignore
        Literal["horizontal-tb", "vertical-rl", "vertical-lr", str]
    ]
    """writing-mode: horizontal-tb | vertical-rl | vertical-lr;"""
