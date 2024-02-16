"""
This file is auto generated using scripts/render/style.py
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t

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

    animation: NotRequired[
        t.Union[
            str,
            Literal[
                "animation-name",
                "animation-duration",
                "animation-timing-function",
                "animation-delay",
                "animation-iteration-count",
                "animation-direction",
                "animation-fill-mode",
                "animation-play-state",
            ],
        ]
    ]
    """No syntax rule available"""

    animation_play_state: NotRequired[
        t.Union[str, Literal["paused", "running", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    animation_name: NotRequired[
        t.Union[str, Literal["keyframename", "none", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    animation_fill_mode: NotRequired[
        t.Union[
            str, Literal["none", "forwards", "backwards", "both", "initial", "inherit"]
        ]
    ]
    """No syntax rule available"""

    align_items: NotRequired[
        t.Union[
            str,
            Literal[
                "stretch",
                "center",
                "flex-start",
                "flex-end",
                "baseline",
                "initial",
                "inherit",
            ],
        ]
    ]
    """align-items: stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    animation_duration: NotRequired[t.Union[str, Literal["time", "initial", "inherit"]]]
    """No syntax rule available"""

    align_self: NotRequired[
        t.Union[
            str,
            Literal[
                "auto",
                "stretch",
                "center",
                "flex-start",
                "flex-end",
                "baseline",
                "initial",
                "inherit",
            ],
        ]
    ]
    """align-self: auto | stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    align_content: NotRequired[
        t.Union[
            str,
            Literal[
                "stretch",
                "center",
                "flex-start",
                "flex-end",
                "space-between",
                "space-around",
                "initial",
                "inherit",
            ],
        ]
    ]
    """align-content: stretch | center | flex-start |flex-end | space-between |space-around | initial | inherit;"""

    animation_direction: NotRequired[
        t.Union[
            str,
            Literal[
                "normal",
                "reverse",
                "alternate",
                "alternate-reverse",
                "initial",
                "inherit",
            ],
        ]
    ]
    """No syntax rule available"""

    animation_iteration_count: NotRequired[
        t.Union[str, Literal["number", "infinite", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    all: NotRequired[t.Union[str, Literal["initial", "inherit", "unset"]]]
    """No syntax rule available"""

    animation_delay: NotRequired[t.Union[str, Literal["time", "initial", "inherit"]]]
    """animation-delay: time | initial | inherit;"""

    animation_timing_function: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    backface_visibility: NotRequired[
        t.Union[str, Literal["visible", "hidden", "initial", "inherit"]]
    ]
    """backface-visibility: visible | hidden | initial | inherit;"""

    background_position: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """background-position: value | x% y% |xpos ypos | initial | inherit"""

    background_size: NotRequired[
        t.Union[
            str,
            Literal[
                "auto", "length", "percentage", "cover", "contain", "initial", "inherit"
            ],
        ]
    ]
    """background-size: auto | length | cover |contain | initial | inherit;"""

    background: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """background: bg-color bg-image position/bg-size bg-repeatbg-origin bg-clip bg-attachment | initial | inherit;"""

    background_attachment: NotRequired[
        t.Union[str, Literal["scroll", "fixed", "local", "initial", "inherit"]]
    ]
    """background-attachment: scroll | fixed | local |initial | inherit;"""

    background_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """background-color: color | transparent | initial | inherit;"""

    background_repeat: NotRequired[
        t.Union[
            str,
            Literal[
                "repeat",
                "repeat-x",
                "repeat-y",
                "no-repeat",
                "space",
                "round",
                "initial",
                "inherit",
            ],
        ]
    ]
    """background-repeat: repeat | repeat-x | repeat-y |no-repeat | initial | inherit;"""

    background_clip: NotRequired[
        t.Union[
            str,
            Literal["content-box", "padding-box", "border-box", "initial", "inherit"],
        ]
    ]
    """background-clip: border-box | padding-box |content-box | initial | inherit;"""

    background_blend_mode: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """background-blend-mode: normal | multiply | screen | overlay | darken |lighten | color-dodge | saturation | color |luminosity;"""

    background_origin: NotRequired[
        t.Union[
            str,
            Literal["padding-box", "border-box", "content-box", "initial", "inherit"],
        ]
    ]
    """background-origin: padding-box | border-box |content-box | initial | inherit;"""

    background_image: NotRequired[
        t.Union[
            str,
            Literal[
                "url",
                "none",
                "linear-gradient()",
                "radial-gradient()",
                "repeating-linear-gradient()",
                "repeating-radial-gradient()",
                "inherit",
            ],
        ]
    ]
    """background-image: url(url) | none | linear-gradient() | radial-gradient() |repeating-linear-gradient() | repeating-radial-gradient() |inherit;"""

    border: NotRequired[
        t.Union[
            str,
            Literal[
                "border-width", "border-style", "border-color", "initial", "inherit"
            ],
        ]
    ]
    """border: border-width border-style border-color |initial | inherit;"""

    border_bottom: NotRequired[
        t.Union[
            str,
            Literal[
                "border-width", "border-style", "border-color", "initial", "inherit"
            ],
        ]
    ]
    """border-bottom: border-width border-style border-color |initial | inherit;"""

    border_bottom_left_radius: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """border-bottom-left-radius: length | length% |initial | inherit;"""

    border_bottom_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """border-bottom-color: color | transparent |initial | inherit;"""

    border_bottom_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    border_image_repeat: NotRequired[
        t.Union[
            str, Literal["stretch", "repeat", "round", "space", "initial", "inherit"]
        ]
    ]
    """border-image-repeat: stretch | repeat |round | initial | inherit;"""

    border_image: NotRequired[
        t.Union[
            str,
            Literal[
                "border-image-source",
                "border-image-slice",
                "border-image-width",
                "border-image-outset",
                "border-image-repeat",
                "initial",
                "inherit",
            ],
        ]
    ]
    """border-image: URL slice width outset repeat |initial | inherit;"""

    border_collapse: NotRequired[
        t.Union[str, Literal["separate", "collapse", "initial", "inherit"]]
    ]
    """border-collapse: separate | collapse | initial | inherit;"""

    border_image_outset: NotRequired[
        t.Union[str, Literal["length", "number", "initial", "inherit"]]
    ]
    """border-image-outset: length | number |initial | inherit;"""

    border_bottom_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    border_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """border-color: color | transparent | initial | inherit;"""

    border_bottom_right_radius: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """border-bottom-right-radius: length | length% | initial | inherit;"""

    border_image_slice: NotRequired[
        t.Union[str, Literal["number", "%", "fill", "initial", "inherit"]]
    ]
    """border-image-slice: number | % |fill | initial | inherit;"""

    border_image_source: NotRequired[
        t.Union[str, Literal["none", "image", "initial", "inherit"]]
    ]
    """border-image-source: none | image | initial | inherit;"""

    border_image_width: NotRequired[
        t.Union[str, Literal["length", "number", "%", "auto", "initial", "inherit"]]
    ]
    """border-image-width: number | % | auto | initial | inherit;"""

    border_left_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """border-left-color: color | transparent | initial | inherit;"""

    border_left_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    border_right_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    border_radius: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    border_left: NotRequired[
        t.Union[
            str,
            Literal[
                "border-width", "border-style", "border-color", "initial", "inherit"
            ],
        ]
    ]
    """border-left: border-width border-style border-color |initial | inherit;"""

    border_left_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    border_right_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """border-right-color: color | transparent | initial | inherit;"""

    border_right: NotRequired[
        t.Union[
            str,
            Literal[
                "border-width", "border-style", "border-color", "initial", "inherit"
            ],
        ]
    ]
    """border-right: border-width border-style border-color |initial | inherit;"""

    border_right_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    border_spacing: NotRequired[
        t.Union[str, Literal["length length", "initial", "inherit"]]
    ]
    """border-spacing: length | initial | inherit;"""

    border_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    border_top: NotRequired[
        t.Union[
            str,
            Literal[
                "border-width", "border-style", "border-color", "initial", "inherit"
            ],
        ]
    ]
    """border-top: border-width border-style border-color |initial | inherit;"""

    border_top_right_radius: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """border-top-right-radius: length | length% | initial | inherit;"""

    border_top_color: NotRequired[
        t.Union[str, Literal["color", "transparent", "initial", "inherit"]]
    ]
    """border-top-color: color | transparent | initial | inherit;"""

    border_top_left_radius: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """border-top-left-radius: length | length% | initial | inherit;"""

    box_shadow: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """box-shadow: none | h-offset v-offset blur spread color |inset | initial | inherit;"""

    border_top_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """No syntax rule available"""

    border_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """border-width: medium | thin | thick |length | initial | inherit;"""

    box_decoration_break: NotRequired[
        t.Union[str, Literal["slice", "clone", "initial", "inherit"]]
    ]
    """box-decoration-break: slice | clone |initial | inherit | unset;"""

    border_top_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    bottom: NotRequired[
        t.Union[str, Literal["auto", "length", "%", "initial", "inherit"]]
    ]
    """bottom: auto | length | initial | inherit;"""

    box_sizing: NotRequired[
        t.Union[str, Literal["content-box", "border-box", "initial", "inherit"]]
    ]
    """box-sizing: content-box | border-box | initial | inherit;"""

    caption_side: NotRequired[
        t.Union[str, Literal["bottom", "top", "initial", "inherit"]]
    ]
    """caption-side: top | bottom | initial | inherit;"""

    caret_color: NotRequired[t.Union[str, Literal["auto", "color", "transparent"]]]
    """caret-color: auto | color | transparent;"""

    charset: NotRequired[t.Union[str, Literal["charset"]]]
    """@charset "charset";"""

    clear: NotRequired[
        t.Union[str, Literal["none", "left", "right", "both", "initial", "inherit"]]
    ]
    """clear: none | left | right | both |initial | inherit;"""

    column_count: NotRequired[
        t.Union[str, Literal["number", "auto", "initial", "inherit"]]
    ]
    """column-count: number | auto | initial | inherit;"""

    clip: NotRequired[t.Union[str, Literal["auto", "shape", "initial", "inherit"]]]
    """clip: auto | shape | initial | inherit;"""

    column_rule: NotRequired[
        t.Union[
            str,
            Literal[
                "column-rule-width ",
                "column-rule-style ",
                "column-rule-color ",
                "initial",
                "inherit",
            ],
        ]
    ]
    """column-rule: column-rule-widthcolumn-rule-stylecolumn-rule-color |initial | inherit;"""

    column_gap: NotRequired[
        t.Union[str, Literal["length", "normal", "initial", "inherit"]]
    ]
    """column-gap: length | normal | initial | inherit;"""

    clip_path: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """clip-path: clip-source | basic-shape | margin-box |border-box | padding-box | content-box |fill-box | stroke-box | view-box | none;"""

    color: NotRequired[t.Union[str, Literal["color", "initial", "inherit"]]]
    """color: color | initial | inherit;"""

    column_fill: NotRequired[
        t.Union[str, Literal["balance", "auto", "initial", "inherit"]]
    ]
    """column-fill: balance | auto | initial | inherit;"""

    column_rule_color: NotRequired[t.Union[str, Literal["color", "initial", "inherit"]]]
    """column-rule-color: color | initial | inherit;"""

    column_rule_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """column-rule-style: none | hidden | dotted |dashed | solid | double |groove | ridge | inset |outset | initial | inherit;"""

    column_rule_width: NotRequired[
        t.Union[str, Literal["length", "medium", "thin", "thick", "initial", "inherit"]]
    ]
    """column-rule-width: length |medium | thin | thick |initial | inherit;"""

    column_span: NotRequired[t.Union[str, Literal["none", "all", "initial", "inherit"]]]
    """column-span: none | all |initial | inherit;"""

    column_width: NotRequired[
        t.Union[str, Literal["auto", "length", "initial", "inherit"]]
    ]
    """column-width: auto | length |initial | inherit;"""

    columns: NotRequired[
        t.Union[
            str, Literal["auto", "column-width", "column-count", "initial", "inherit"]
        ]
    ]
    """columns: auto | column-width column-count |initial | inherit;"""

    content: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """content: normal | none | counter | attr | string |open-quote | close-quote | no-open-quote |no-close-quote | url | initial | inherit;"""

    counter_increment: NotRequired[
        t.Union[str, Literal["none", "name number", "initial", "inherit"]]
    ]
    """counter-increment: none | name number |initial | inherit;"""

    direction: NotRequired[t.Union[str, Literal["ltr", "rtl", "initial", "inherit"]]]
    """direction: ltr | rtl | initial | inherit;"""

    counter_reset: NotRequired[
        t.Union[str, Literal["none", "name number", "initial", "inherit"]]
    ]
    """counter-reset: none | name number | initial | inherit;"""

    display: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """display: value"""

    empty_cells: NotRequired[
        t.Union[str, Literal["show", "hide", "initial", "inherit"]]
    ]
    """empty-cells: show | hide | initial | inherit;"""

    filter: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """filter: none | blur() | brightness() | contrast() |drop-shadow() | grayscale() | hue-rotate() |invert() | opacity() | saturate() |sepia() | url();"""

    cursor: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """cursor: value;"""

    flex: NotRequired[
        t.Union[
            str,
            Literal[
                "flex-grow",
                "flex-shrink",
                "flex-basis",
                "auto",
                "none",
                "initial",
                "inherit",
            ],
        ]
    ]
    """flex: flex-grow flex-shrink flex-basis |auto | initial | inherit;"""

    flex_basis: NotRequired[
        t.Union[str, Literal["auto", "length", "initial", "inherit"]]
    ]
    """flex-basis: auto | length | initial | inherit;"""

    flex_direction: NotRequired[
        t.Union[
            str,
            Literal[
                "row", "row-reverse", "column", "column-reverse", "initial", "inherit"
            ],
        ]
    ]
    """flex-direction: row | row-reverse | column |column-reverse | initial |inherit;"""

    flex_flow: NotRequired[
        t.Union[str, Literal["flex-direction", "flex-wrap", "initial", "inherit"]]
    ]
    """flex-flow: flex-direction flex-wrap |initial | inherit;"""

    flex_grow: NotRequired[t.Union[str, Literal["number", "initial", "inherit"]]]
    """flex-grow: number | initial | inherit;"""

    flex_shrink: NotRequired[t.Union[str, Literal["number", "initial", "inherit"]]]
    """flex-shrink: number | initial | inherit;"""

    font_family: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """font-family: family-name | generic-family |initial | inherit;"""

    float: NotRequired[
        t.Union[str, Literal["none", "left", "right", "initial", "inherit"]]
    ]
    """float: none | left | right | initial | inherit;"""

    font_face: NotRequired[
        t.Union[
            str,
            Literal[
                "font-family",
                "src",
                "font-stretch",
                "font-style",
                "font-weight",
                "unicode-range",
            ],
        ]
    ]
    """@font-face { font-properties }"""

    flex_wrap: NotRequired[
        t.Union[str, Literal["nowrap", "wrap", "wrap-reverse", "initial", "inherit"]]
    ]
    """flex-wrap: nowrap | wrap | wrap-reverse |initial | inherit;"""

    font: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    font_kerning: NotRequired[t.Union[str, Literal["auto", "normal", "none"]]]
    """font-kerning: auto | normal | none;"""

    font_size: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """font-size: medium | xx-small | x-small | small |large | x-large | xx-large | smaller |larger | length | initial | inherit;"""

    font_stretch: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """font-stretch: ultra-condensed | extra-condensed |condensed | semi-condensed | normal |semi-expanded | expanded | extra-expanded |ultra-expanded | initial | inherit;"""

    font_variant: NotRequired[
        t.Union[str, Literal["normal", "small-caps", "initial", "inherit"]]
    ]
    """font-variant: normal | small-caps |initial | inherit;"""

    font_style: NotRequired[
        t.Union[str, Literal["normal", "italic", "oblique", "initial", "inherit"]]
    ]
    """font-style: normal | italic | oblique |initial | inherit;"""

    font_weight: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """font-weight: normal | bold | bolder | lighter |number | initial | inherit;"""

    gap: NotRequired[t.Union[str, Literal["length", "normal", "initial", "inherit"]]]
    """gap: length | normal | initial | inherit;"""

    grid: NotRequired[t.Union[str, Literal["none", "initial", "inherit"]]]
    """grid:
        none |grid-template-rows / grid-template-columns |grid-template-areas |
        grid-template-rows / [grid-auto-flow] grid-auto-columns |
        [grid-auto-flow] grid-auto-rows / grid-template-columns |
        initial | inherit;
    """

    grid_auto_columns: NotRequired[
        t.Union[
            str,
            Literal[
                "auto", "min-content", "max-content", "minmax(min.max)", "length", "%"
            ],
        ]
    ]
    """grid-auto-columns: auto | min-content | max-content |minmax() | length | %;"""

    grid_auto_rows: NotRequired[
        t.Union[
            str,
            Literal[
                "auto", "max-content", "min-content", "minmax(min.max)", "length", "%"
            ],
        ]
    ]
    """grid-auto-columns: auto | max-content | min-content |minmax | length | %;"""

    grid_area: NotRequired[
        t.Union[
            str,
            Literal[
                "grid-row-start",
                "grid-column-start",
                "grid-row-end",
                "grid-column-end",
                "itemname",
            ],
        ]
    ]
    """grid-area: grid-row-start / grid-column-start /grid-row-end / grid-column-end |itemname;"""

    grid_column: NotRequired[
        t.Union[str, Literal["grid-column-start", "grid-column-end", "span n"]]
    ]
    """grid-column: grid-column-start  [grid-column-end | span n] ;"""

    grid_auto_flow: NotRequired[
        t.Union[str, Literal["row", "column", "dense", "row dense", "column dense"]]
    ]
    """grid-auto-flow: row | column | dense |row dense | column dense;"""

    grid_column_end: NotRequired[t.Union[str, Literal["auto", "column", "span n"]]]
    """grid-column-end: auto | column | span n;"""

    grid_column_gap: NotRequired[t.Union[str, Literal["length"]]]
    """grid-column-gap: length;"""

    grid_gap: NotRequired[t.Union[str, Literal["grid-row-gap", "grid-column-gap"]]]
    """grid-gap: grid-row-gap grid-column-gap;"""

    grid_column_start: NotRequired[t.Union[str, Literal["auto", "column", "span n"]]]
    """grid-column-start: auto | column | span n;"""

    grid_row_end: NotRequired[t.Union[str, Literal["auto", "span n", "row"]]]
    """grid-row-end: auto | span n | row-line;"""

    grid_row: NotRequired[
        t.Union[str, Literal["grid-row-start", "grid-row-end", "span n"]]
    ]
    """grid-row: grid-row-start  [grid-row-end | span n] ;"""

    grid_row_gap: NotRequired[t.Union[str, Literal["length"]]]
    """grid-row-gap: length;"""

    grid_template_areas: NotRequired[t.Union[str, Literal["none", "areanames"]]]
    """grid-template-areas: none | areanames;"""

    grid_template: NotRequired[
        t.Union[
            str,
            Literal[
                "none",
                "grid-template-rows",
                "grid-template-columns",
                "grid-template-areas",
                "initial",
                "inherit",
            ],
        ]
    ]
    """grid-template: none | grid-template-rows / grid-template-columns |grid-template-areas | initial | inherit;"""

    height: NotRequired[
        t.Union[str, Literal["auto", "length", "%", "initial", "inherit"]]
    ]
    """height: auto | length | initial | inherit;"""

    grid_template_columns: NotRequired[
        t.Union[
            str,
            Literal[
                "none",
                "auto",
                "max-content",
                "min-content",
                "length",
                "initial",
                "inherit",
            ],
        ]
    ]
    """grid-template-columns: none | auto | max-content |min-content | length | initial | inherit;"""

    grid_row_start: NotRequired[t.Union[str, Literal["auto", "span n", "row"]]]
    """grid-row-start: auto | span n | row-line;"""

    grid_template_rows: NotRequired[
        t.Union[
            str,
            Literal[
                "none",
                "auto",
                "max-content",
                "min-content",
                "length",
                "initial",
                "inherit",
            ],
        ]
    ]
    """grid-template-rows: none | auto | max-content |min-content | length | initial | inherit;"""

    hyphens: NotRequired[
        t.Union[str, Literal["none", "manual", "auto", "initial", "inherit"]]
    ]
    """hyphens: none | manual | auto | initial | inherit;"""

    justify_content: NotRequired[
        t.Union[
            str,
            Literal[
                "flex-start",
                "flex-end",
                "center",
                "space-between",
                "space-around",
                "initial",
                "inherit",
            ],
        ]
    ]
    """justify-content: flex-start | flex-end | center | space-between |space-around | initial | inherit;"""

    keyframes: NotRequired[
        t.Union[str, Literal["animation-name", "keyframes-selector", "css-styles"]]
    ]
    """@keyframes animation-name {keyframes-selector { css-styles; }}"""

    left: NotRequired[
        t.Union[str, Literal["auto", "length", "%", "initial", "inherit"]]
    ]
    """left: auto | length | initial | inherit;"""

    letter_spacing: NotRequired[
        t.Union[str, Literal["normal", "length", "initial", "inherit"]]
    ]
    """letter-spacing: normal | length | initial | inherit;"""

    line_height: NotRequired[
        t.Union[str, Literal["normal", "number", "length", "%", "initial", "inherit"]]
    ]
    """line-height: normal | number | length |initial | inherit;"""

    list_style_image: NotRequired[
        t.Union[str, Literal["none", "url", "initial", "inherit"]]
    ]
    """list-style-image: none | url | initial | inherit;"""

    list_style: NotRequired[
        t.Union[
            str,
            Literal[
                "list-style-type",
                "list-style-position",
                "list-style-image",
                "initial",
                "inherit",
            ],
        ]
    ]
    """list-style: list-style-type list-style-position list-style-image |initial | inherit;"""

    margin: NotRequired[
        t.Union[str, Literal["length", "%", "auto", "initial", "inherit"]]
    ]
    """margin: length | auto | initial | inherit;"""

    margin_bottom: NotRequired[
        t.Union[str, Literal["length", "%", "auto", "initial", "inherit"]]
    ]
    """margin-bottom: length | auto | initial | inherit;"""

    list_style_position: NotRequired[
        t.Union[str, Literal["inside", "outside", "initial", "inherit"]]
    ]
    """list-style-position: inside | outside | initial | inherit;"""

    list_style_type: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """list-style-type: value;"""

    margin_left: NotRequired[
        t.Union[str, Literal["length", "%", "auto", "initial", "inherit"]]
    ]
    """margin-left: length | auto | initial | inherit;"""

    margin_right: NotRequired[
        t.Union[str, Literal["length", "%", "auto", "initial", "inherit"]]
    ]
    """margin-right: length | auto | initial | inherit;"""

    margin_top: NotRequired[
        t.Union[str, Literal["length", "%", "auto", "initial", "inherit"]]
    ]
    """margin-top: length | auto | initial | inherit;"""

    max_width: NotRequired[
        t.Union[str, Literal["none", "length", "%", "initial", "inherit"]]
    ]
    """max-width: none | length | initial | inherit;"""

    max_height: NotRequired[
        t.Union[str, Literal["none", "length", "%", "initial", "inherit"]]
    ]
    """max-height: none | length | initial | inherit;"""

    media: NotRequired[t.Union[str, Literal["all", "print", "screen", "speech"]]]
    """@media not | only mediatype and(mediafeature and | or | not mediafeature) {CSS-Code;}"""

    min_height: NotRequired[t.Union[str, Literal["length", "%", "initial", "inherit"]]]
    """min-height: length | initial | inherit;"""

    min_width: NotRequired[t.Union[str, Literal["length", "%", "initial", "inherit"]]]
    """min-width: length | initial | inherit;"""

    opacity: NotRequired[t.Union[str, Literal["number", "initial", "inherit"]]]
    """opacity: number | initial | inherit;"""

    outline: NotRequired[
        t.Union[
            str,
            Literal[
                "outline-width", "outline-style", "outline-color", "initial", "inherit"
            ],
        ]
    ]
    """outline: outline-width outline-style outline-color | initial | inherit;"""

    object_position: NotRequired[
        t.Union[str, Literal["position", "initial", "inherit"]]
    ]
    """object-position: position | initial | inherit;"""

    order: NotRequired[t.Union[str, Literal["number", "initial", "inherit"]]]
    """order: number | initial | inherit;"""

    object_fit: NotRequired[
        t.Union[
            str,
            Literal[
                "fill", "contain", "cover", "scale-down", "none", "initial", "inherit"
            ],
        ]
    ]
    """object-fit: fill | contain | cover | scale-down |none | initial | inherit;"""

    outline_color: NotRequired[
        t.Union[str, Literal["invert", "color", "initial", "inherit"]]
    ]
    """outline-color: invert | color | transparent |initial | inherit;"""

    outline_offset: NotRequired[t.Union[str, Literal["length", "initial", "inherit"]]]
    """outline-offset: length | initial | inherit;"""

    outline_style: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """outline-style: none | hidden | dotted | dashed |solid | double | groove | ridge |inset | outset | initial | inherit;"""

    outline_width: NotRequired[
        t.Union[str, Literal["medium", "thin", "thick", "length", "initial", "inherit"]]
    ]
    """outline-width: medium | thin | thick |length | initial | inherit;"""

    overflow_x: NotRequired[
        t.Union[
            str, Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
        ]
    ]
    """overflow-x: visible | hidden | scroll |auto | initial | inherit;"""

    overflow_y: NotRequired[
        t.Union[
            str, Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
        ]
    ]
    """overflow-y: visible | hidden | scroll |auto | initial | inherit;"""

    overflow: NotRequired[
        t.Union[
            str, Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
        ]
    ]
    """overflow: visible | hidden | scroll |auto | initial | inherit;"""

    padding_left: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """padding-left: length | initial | inherit;"""

    padding_bottom: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """padding-bottom: length | initial | inherit;"""

    padding_top: NotRequired[t.Union[str, Literal["length", "%", "initial", "inherit"]]]
    """padding-top: length | initial | inherit;"""

    padding: NotRequired[t.Union[str, Literal["length", "initial", "inherit"]]]
    """padding: length | initial | inherit;"""

    padding_right: NotRequired[
        t.Union[str, Literal["length", "%", "initial", "inherit"]]
    ]
    """padding-right: length | initial | inherit;"""

    page_break_after: NotRequired[
        t.Union[
            str,
            Literal["auto", "always", "avoid", "left", "right", "initial", "inherit"],
        ]
    ]
    """page-break-after: auto | always | avoid | left |right | initial | inherit;"""

    page_break_before: NotRequired[
        t.Union[
            str,
            Literal["auto", "always", "avoid", "left", "right", "initial", "inherit"],
        ]
    ]
    """page-break-before: auto | always | avoid | left |right | initial | inherit;"""

    page_break_inside: NotRequired[
        t.Union[str, Literal["auto", "avoid", "initial", "inherit"]]
    ]
    """page-break-inside: auto | avoid |initial | inherit;"""

    perspective: NotRequired[
        t.Union[str, Literal["length", "none", "initial", "inherit"]]
    ]
    """perspective: length | none | initial | inherit;"""

    position: NotRequired[
        t.Union[
            str,
            Literal[
                "static",
                "relative",
                "absolute",
                "fixed",
                "sticky",
                "initial",
                "inherit",
            ],
        ]
    ]
    """position: static | absolute | fixed | relative |sticky | initial | inherit;"""

    pointer_events: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    perspective_origin: NotRequired[
        t.Union[str, Literal["x-axis", "y-axis", "initial", "inherit"]]
    ]
    """perspective-origin: x-axis y-axis |initial | inherit;"""

    quotes: NotRequired[
        t.Union[str, Literal["none", "[string string]+", "initial", "inherit"]]
    ]
    """quotes: none | [string string]+ |initial | inherit;"""

    right: NotRequired[
        t.Union[str, Literal["auto", "length", "%", "initial", "inherit"]]
    ]
    """right: auto | length | initial | inherit;"""

    row_gap: NotRequired[
        t.Union[str, Literal["length", "normal", "initial", "inherit"]]
    ]
    """row-gap: length | normal | initial | inherit;"""

    text_align: NotRequired[
        t.Union[
            str, Literal["left", "right", "center", "justify", "initial", "inherit"]
        ]
    ]
    """text-align: left | right | center |justify | initial | inherit;"""

    scroll_behavior: NotRequired[
        t.Union[str, Literal["auto", "smooth", "initial", "inherit"]]
    ]
    """scroll-behavior: auto | smooth | initial | inherit;"""

    table_layout: NotRequired[
        t.Union[str, Literal["auto", "fixed", "initial", "inherit"]]
    ]
    """table-layout: auto | fixed | initial | inherit;"""

    text_align_last: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """text-align-last: auto | left | right | center |justify | start | end |initial | inherit;"""

    text_decoration: NotRequired[
        t.Union[
            str,
            Literal[
                "none",
                "text-decoration-line",
                "text-decoration-color",
                "text-decoration-style",
                "initial",
                "inherit",
            ],
        ]
    ]
    """text-decoration: none |text-decoration-line text-decoration-colortext-decoration-style | initial | inherit;"""

    text_decoration_color: NotRequired[
        t.Union[str, Literal["color", "initial", "inherit"]]
    ]
    """text-decoration-color: color | initial | inherit;"""

    text_decoration_line: NotRequired[
        t.Union[
            str,
            Literal[
                "none", "underline", "overline", "line-through", "initial", "inherit"
            ],
        ]
    ]
    """text-decoration-line: none | underline |overline | line-through |initial | inherit;"""

    text_indent: NotRequired[t.Union[str, Literal["length", "%", "initial", "inherit"]]]
    """text-indent: length | initial | inherit;"""

    text_decoration_style: NotRequired[
        t.Union[
            str,
            Literal[
                "solid", "double", "dotted", "dashed", "wavy", "initial", "inherit"
            ],
        ]
    ]
    """text-decoration-style: solid | double | dotted |dashed | wavy | initial | inherit;"""

    text_justify: NotRequired[
        t.Union[
            str, Literal["none", "auto", "inter-word", "trim", "initial", "inherit"]
        ]
    ]
    """text-justify: auto | inter-word |none | initial | inherit;"""

    text_shadow: NotRequired[
        t.Union[
            str,
            Literal[
                "none",
                "x-offset",
                "y-offset",
                "blur-radius",
                "color",
                "initial",
                "inherit",
            ],
        ]
    ]
    """text-shadow: x-offset y-offset blur-radius color |none | initial | inherit;"""

    text_overflow: NotRequired[
        t.Union[str, Literal["clip", "ellipsis", "string", "initial", "inherit"]]
    ]
    """text-overflow: clip | ellipsis | string |initial | inherit;"""

    text_transform: NotRequired[
        t.Union[
            str,
            Literal[
                "none", "capitalize", "uppercase", "lowercase", "initial", "inherit"
            ],
        ]
    ]
    """text-transform: none | capitalize | uppercase |lowercase | initial | inherit;"""

    top: NotRequired[t.Union[str, Literal["auto", "length", "%", "initial", "inherit"]]]
    """top: auto | length | initial | inherit;"""

    transform_origin: NotRequired[
        t.Union[str, Literal["x-axis", "y-axis", "z-axis", "initial", "inherit"]]
    ]
    """transform-origin: x-axis y-axis z-axis |initial | inherit;"""

    transform: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """transform: none | transform-functions |initial | inherit;"""

    transform_style: NotRequired[
        t.Union[str, Literal["flat", "preserve-3d", "initial", "inherit"]]
    ]
    """transform-style: flat | preserve-3d | initial | inherit;"""

    transition: NotRequired[
        t.Union[
            str,
            Literal[
                "transition-property",
                "transition-duration",
                "transition-timing-function",
                "transition-delay",
                "initial",
                "inherit",
            ],
        ]
    ]
    """transition: property duration timing-function delay |initial | inherit;"""

    transition_duration: NotRequired[
        t.Union[str, Literal["time", "initial", "inherit"]]
    ]
    """transition-duration: time | initial | inherit;"""

    transition_delay: NotRequired[t.Union[str, Literal["time", "initial", "inherit"]]]
    """transition-delay: time | initial | inherit;"""

    transition_property: NotRequired[
        t.Union[str, Literal["none", "all", "properties", "initial", "inherit"]]
    ]
    """transition-property: none | all | properties |initial | inherit;"""

    transition_timing_function: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """No syntax rule available"""

    user_select: NotRequired[t.Union[str, Literal["auto", "none", "text", "all"]]]
    """user-select: auto | none | text | all;"""

    width: NotRequired[t.Union[str, Literal["auto", "length", "initial", "inherit"]]]
    """width: auto | length | initial | inherit;"""

    word_break: NotRequired[
        t.Union[
            str,
            Literal[
                "normal", "break-all", "keep-all", "break-word", "initial", "inherit"
            ],
        ]
    ]
    """word-break: normal | break-all | keep-all |break-word | initial | inherit;"""

    visibility: NotRequired[
        t.Union[str, Literal["visible", "hidden", "collapse", "initial", "inherit"]]
    ]
    """visibility: visible | hidden | collapse |initial | inherit;"""

    word_spacing: NotRequired[
        t.Union[str, Literal["normal", "length", "initial", "inherit"]]
    ]
    """word-spacing: normal | length | initial | inherit;"""

    white_space: NotRequired[
        t.Union[
            str,
            Literal[
                "normal", "nowrap", "pre", "pre-line", "pre-wrap", "initial", "inherit"
            ],
        ]
    ]
    """white-space: normal | nowrap | pre |pre-line | pre-wrap | initial | inherit;"""

    vertical_align: NotRequired[
        t.Union[
            str,
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
            ],
        ]
    ]
    """vertical-align: baseline | length | sub | super |top | text-top | middle | bottom |text-bottom | initial | inherit;"""

    word_wrap: NotRequired[
        t.Union[str, Literal["normal", "break-word", "initial", "inherit"]]
    ]
    """word-wrap: normal | break-word | initial | inherit;"""

    z_index: NotRequired[t.Union[str, Literal["auto", "number", "initial", "inherit"]]]
    """z-index: auto | number | initial | inherit;"""

    writing_mode: NotRequired[
        t.Union[str, Literal["horizontal-tb", "vertical-rl", "vertical-lr"]]
    ]
    """writing-mode: horizontal-tb | vertical-rl | vertical-lr;"""
