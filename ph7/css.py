"""
This file is auto generated using scripts/render/css.py
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

import typing as t

from typing_extensions import Literal

from ph7.style import attributes as css_attr


class CSSObject:
    """CSS class representation."""

    animation: Literal[
        "animation-name",
        "animation-duration",
        "animation-timing-function",
        "animation-delay",
        "animation-iteration-count",
        "animation-direction",
        "animation-fill-mode",
        "animation-play-state",
    ]
    """No syntax rule available"""

    animation_play_state: Literal["paused", "running", "initial", "inherit"]
    """No syntax rule available"""

    animation_name: Literal["keyframename", "none", "initial", "inherit"]
    """No syntax rule available"""

    animation_fill_mode: Literal[
        "none", "forwards", "backwards", "both", "initial", "inherit"
    ]
    """No syntax rule available"""

    align_items: Literal[
        "stretch", "center", "flex-start", "flex-end", "baseline", "initial", "inherit"
    ]
    """align-items: stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    animation_duration: Literal["time", "initial", "inherit"]
    """No syntax rule available"""

    align_self: Literal[
        "auto",
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "baseline",
        "initial",
        "inherit",
    ]
    """align-self: auto | stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    align_content: Literal[
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "space-between",
        "space-around",
        "initial",
        "inherit",
    ]
    """align-content: stretch | center | flex-start |flex-end | space-between |space-around | initial | inherit;"""

    animation_direction: Literal[
        "normal", "reverse", "alternate", "alternate-reverse", "initial", "inherit"
    ]
    """No syntax rule available"""

    animation_iteration_count: Literal["number", "infinite", "initial", "inherit"]
    """No syntax rule available"""

    all: Literal["initial", "inherit", "unset"]
    """No syntax rule available"""

    animation_delay: Literal["time", "initial", "inherit"]
    """animation-delay: time | initial | inherit;"""

    animation_timing_function: Literal[
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
    ]
    """No syntax rule available"""

    backface_visibility: Literal["visible", "hidden", "initial", "inherit"]
    """backface-visibility: visible | hidden | initial | inherit;"""

    background_position: Literal[
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
    ]
    """background-position: value | x% y% |xpos ypos | initial | inherit"""

    background_size: Literal[
        "auto", "length", "percentage", "cover", "contain", "initial", "inherit"
    ]
    """background-size: auto | length | cover |contain | initial | inherit;"""

    background: Literal[
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
    ]
    """background: bg-color bg-image position/bg-size bg-repeatbg-origin bg-clip bg-attachment | initial | inherit;"""

    background_attachment: Literal["scroll", "fixed", "local", "initial", "inherit"]
    """background-attachment: scroll | fixed | local |initial | inherit;"""

    background_color: Literal["color", "transparent", "initial", "inherit"]
    """background-color: color | transparent | initial | inherit;"""

    background_repeat: Literal[
        "repeat",
        "repeat-x",
        "repeat-y",
        "no-repeat",
        "space",
        "round",
        "initial",
        "inherit",
    ]
    """background-repeat: repeat | repeat-x | repeat-y |no-repeat | initial | inherit;"""

    background_clip: Literal[
        "content-box", "padding-box", "border-box", "initial", "inherit"
    ]
    """background-clip: border-box | padding-box |content-box | initial | inherit;"""

    background_blend_mode: Literal[
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
    ]
    """background-blend-mode: normal | multiply | screen | overlay | darken |lighten | color-dodge | saturation | color |luminosity;"""

    background_origin: Literal[
        "padding-box", "border-box", "content-box", "initial", "inherit"
    ]
    """background-origin: padding-box | border-box |content-box | initial | inherit;"""

    background_image: Literal[
        "url",
        "none",
        "linear-gradient()",
        "radial-gradient()",
        "repeating-linear-gradient()",
        "repeating-radial-gradient()",
        "inherit",
    ]
    """background-image: url(url) | none | linear-gradient() | radial-gradient() |repeating-linear-gradient() | repeating-radial-gradient() |inherit;"""

    border: Literal[
        "border-width", "border-style", "border-color", "initial", "inherit"
    ]
    """border: border-width border-style border-color |initial | inherit;"""

    border_bottom: Literal[
        "border-width", "border-style", "border-color", "initial", "inherit"
    ]
    """border-bottom: border-width border-style border-color |initial | inherit;"""

    border_bottom_left_radius: Literal["length", "%", "initial", "inherit"]
    """border-bottom-left-radius: length | length% |initial | inherit;"""

    border_bottom_color: Literal["color", "transparent", "initial", "inherit"]
    """border-bottom-color: color | transparent |initial | inherit;"""

    border_bottom_style: Literal[
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
    ]
    """No syntax rule available"""

    border_image_repeat: Literal[
        "stretch", "repeat", "round", "space", "initial", "inherit"
    ]
    """border-image-repeat: stretch | repeat |round | initial | inherit;"""

    border_image: Literal[
        "border-image-source",
        "border-image-slice",
        "border-image-width",
        "border-image-outset",
        "border-image-repeat",
        "initial",
        "inherit",
    ]
    """border-image: URL slice width outset repeat |initial | inherit;"""

    border_collapse: Literal["separate", "collapse", "initial", "inherit"]
    """border-collapse: separate | collapse | initial | inherit;"""

    border_image_outset: Literal["length", "number", "initial", "inherit"]
    """border-image-outset: length | number |initial | inherit;"""

    border_bottom_width: Literal[
        "medium", "thin", "thick", "length", "initial", "inherit"
    ]
    """No syntax rule available"""

    border_color: Literal["color", "transparent", "initial", "inherit"]
    """border-color: color | transparent | initial | inherit;"""

    border_bottom_right_radius: Literal["length", "%", "initial", "inherit"]
    """border-bottom-right-radius: length | length% | initial | inherit;"""

    border_image_slice: Literal["number", "%", "fill", "initial", "inherit"]
    """border-image-slice: number | % |fill | initial | inherit;"""

    border_image_source: Literal["none", "image", "initial", "inherit"]
    """border-image-source: none | image | initial | inherit;"""

    border_image_width: Literal["length", "number", "%", "auto", "initial", "inherit"]
    """border-image-width: number | % | auto | initial | inherit;"""

    border_left_color: Literal["color", "transparent", "initial", "inherit"]
    """border-left-color: color | transparent | initial | inherit;"""

    border_left_style: Literal[
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
    ]
    """No syntax rule available"""

    border_right_style: Literal[
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
    ]
    """No syntax rule available"""

    border_radius: Literal["length", "%", "initial", "inherit"]
    """No syntax rule available"""

    border_left: Literal[
        "border-width", "border-style", "border-color", "initial", "inherit"
    ]
    """border-left: border-width border-style border-color |initial | inherit;"""

    border_left_width: Literal[
        "medium", "thin", "thick", "length", "initial", "inherit"
    ]
    """No syntax rule available"""

    border_right_color: Literal["color", "transparent", "initial", "inherit"]
    """border-right-color: color | transparent | initial | inherit;"""

    border_right: Literal[
        "border-width", "border-style", "border-color", "initial", "inherit"
    ]
    """border-right: border-width border-style border-color |initial | inherit;"""

    border_right_width: Literal[
        "medium", "thin", "thick", "length", "initial", "inherit"
    ]
    """No syntax rule available"""

    border_spacing: Literal["length length", "initial", "inherit"]
    """border-spacing: length | initial | inherit;"""

    border_style: Literal[
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
    ]
    """No syntax rule available"""

    border_top: Literal[
        "border-width", "border-style", "border-color", "initial", "inherit"
    ]
    """border-top: border-width border-style border-color |initial | inherit;"""

    border_top_right_radius: Literal["length", "%", "initial", "inherit"]
    """border-top-right-radius: length | length% | initial | inherit;"""

    border_top_color: Literal["color", "transparent", "initial", "inherit"]
    """border-top-color: color | transparent | initial | inherit;"""

    border_top_left_radius: Literal["length", "%", "initial", "inherit"]
    """border-top-left-radius: length | length% | initial | inherit;"""

    box_shadow: Literal[
        "none",
        "h-offset",
        "v-offset",
        "blur",
        "spread",
        "color",
        "inset",
        "initial",
        "inherit",
    ]
    """box-shadow: none | h-offset v-offset blur spread color |inset | initial | inherit;"""

    border_top_width: Literal["medium", "thin", "thick", "length", "initial", "inherit"]
    """No syntax rule available"""

    border_width: Literal["medium", "thin", "thick", "length", "initial", "inherit"]
    """border-width: medium | thin | thick |length | initial | inherit;"""

    box_decoration_break: Literal["slice", "clone", "initial", "inherit"]
    """box-decoration-break: slice | clone |initial | inherit | unset;"""

    border_top_style: Literal[
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
    ]
    """No syntax rule available"""

    bottom: Literal["auto", "length", "%", "initial", "inherit"]
    """bottom: auto | length | initial | inherit;"""

    box_sizing: Literal["content-box", "border-box", "initial", "inherit"]
    """box-sizing: content-box | border-box | initial | inherit;"""

    caption_side: Literal["bottom", "top", "initial", "inherit"]
    """caption-side: top | bottom | initial | inherit;"""

    caret_color: Literal["auto", "color", "transparent"]
    """caret-color: auto | color | transparent;"""

    charset: Literal["charset"]
    """@charset "charset";"""

    clear: Literal["none", "left", "right", "both", "initial", "inherit"]
    """clear: none | left | right | both |initial | inherit;"""

    column_count: Literal["number", "auto", "initial", "inherit"]
    """column-count: number | auto | initial | inherit;"""

    clip: Literal["auto", "shape", "initial", "inherit"]
    """clip: auto | shape | initial | inherit;"""

    column_rule: Literal[
        "column-rule-width ",
        "column-rule-style ",
        "column-rule-color ",
        "initial",
        "inherit",
    ]
    """column-rule: column-rule-widthcolumn-rule-stylecolumn-rule-color |initial | inherit;"""

    column_gap: Literal["length", "normal", "initial", "inherit"]
    """column-gap: length | normal | initial | inherit;"""

    clip_path: Literal[
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
    ]
    """clip-path: clip-source | basic-shape | margin-box |border-box | padding-box | content-box |fill-box | stroke-box | view-box | none;"""

    color: Literal["color", "initial", "inherit"]
    """color: color | initial | inherit;"""

    column_fill: Literal["balance", "auto", "initial", "inherit"]
    """column-fill: balance | auto | initial | inherit;"""

    column_rule_color: Literal["color", "initial", "inherit"]
    """column-rule-color: color | initial | inherit;"""

    column_rule_style: Literal[
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
    ]
    """column-rule-style: none | hidden | dotted |dashed | solid | double |groove | ridge | inset |outset | initial | inherit;"""

    column_rule_width: Literal[
        "length", "medium", "thin", "thick", "initial", "inherit"
    ]
    """column-rule-width: length |medium | thin | thick |initial | inherit;"""

    column_span: Literal["none", "all", "initial", "inherit"]
    """column-span: none | all |initial | inherit;"""

    column_width: Literal["auto", "length", "initial", "inherit"]
    """column-width: auto | length |initial | inherit;"""

    columns: Literal["auto", "column-width", "column-count", "initial", "inherit"]
    """columns: auto | column-width column-count |initial | inherit;"""

    content: Literal[
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
    ]
    """content: normal | none | counter | attr | string |open-quote | close-quote | no-open-quote |no-close-quote | url | initial | inherit;"""

    counter_increment: Literal["none", "name number", "initial", "inherit"]
    """counter-increment: none | name number |initial | inherit;"""

    direction: Literal["ltr", "rtl", "initial", "inherit"]
    """direction: ltr | rtl | initial | inherit;"""

    counter_reset: Literal["none", "name number", "initial", "inherit"]
    """counter-reset: none | name number | initial | inherit;"""

    display: Literal[
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
    ]
    """display: value"""

    empty_cells: Literal["show", "hide", "initial", "inherit"]
    """empty-cells: show | hide | initial | inherit;"""

    filter: Literal[
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
    ]
    """filter: none | blur() | brightness() | contrast() |drop-shadow() | grayscale() | hue-rotate() |invert() | opacity() | saturate() |sepia() | url();"""

    cursor: Literal[
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
    ]
    """cursor: value;"""

    flex: Literal[
        "flex-grow", "flex-shrink", "flex-basis", "auto", "none", "initial", "inherit"
    ]
    """flex: flex-grow flex-shrink flex-basis |auto | initial | inherit;"""

    flex_basis: Literal["auto", "length", "initial", "inherit"]
    """flex-basis: auto | length | initial | inherit;"""

    flex_direction: Literal[
        "row", "row-reverse", "column", "column-reverse", "initial", "inherit"
    ]
    """flex-direction: row | row-reverse | column |column-reverse | initial |inherit;"""

    flex_flow: Literal["flex-direction", "flex-wrap", "initial", "inherit"]
    """flex-flow: flex-direction flex-wrap |initial | inherit;"""

    flex_grow: Literal["number", "initial", "inherit"]
    """flex-grow: number | initial | inherit;"""

    flex_shrink: Literal["number", "initial", "inherit"]
    """flex-shrink: number | initial | inherit;"""

    font_family: Literal[
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
    ]
    """font-family: family-name | generic-family |initial | inherit;"""

    float: Literal["none", "left", "right", "initial", "inherit"]
    """float: none | left | right | initial | inherit;"""

    font_face: Literal[
        "font-family",
        "src",
        "font-stretch",
        "font-style",
        "font-weight",
        "unicode-range",
    ]
    """@font-face { font-properties }"""

    flex_wrap: Literal["nowrap", "wrap", "wrap-reverse", "initial", "inherit"]
    """flex-wrap: nowrap | wrap | wrap-reverse |initial | inherit;"""

    font: Literal[
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
    ]
    """No syntax rule available"""

    font_kerning: Literal["auto", "normal", "none"]
    """font-kerning: auto | normal | none;"""

    font_size: Literal[
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
    ]
    """font-size: medium | xx-small | x-small | small |large | x-large | xx-large | smaller |larger | length | initial | inherit;"""

    font_stretch: Literal[
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
    ]
    """font-stretch: ultra-condensed | extra-condensed |condensed | semi-condensed | normal |semi-expanded | expanded | extra-expanded |ultra-expanded | initial | inherit;"""

    font_variant: Literal["normal", "small-caps", "initial", "inherit"]
    """font-variant: normal | small-caps |initial | inherit;"""

    font_style: Literal["normal", "italic", "oblique", "initial", "inherit"]
    """font-style: normal | italic | oblique |initial | inherit;"""

    font_weight: Literal[
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
    ]
    """font-weight: normal | bold | bolder | lighter |number | initial | inherit;"""

    gap: Literal["length", "normal", "initial", "inherit"]
    """gap: length | normal | initial | inherit;"""

    grid: Literal["none", "initial", "inherit"]
    """
    grid: none |grid-template-rows / grid-template-columns |grid-template-areas |
    grid-template-rows / [grid-auto-flow] grid-auto-columns |
    [grid-auto-flow] grid-auto-rows / grid-template-columns |initial | inherit;
    """

    grid_auto_columns: Literal[
        "auto", "min-content", "max-content", "minmax(min.max)", "length", "%"
    ]
    """grid-auto-columns: auto | min-content | max-content |minmax() | length | %;"""

    grid_auto_rows: Literal[
        "auto", "max-content", "min-content", "minmax(min.max)", "length", "%"
    ]
    """grid-auto-columns: auto | max-content | min-content |minmax | length | %;"""

    grid_area: Literal[
        "grid-row-start",
        "grid-column-start",
        "grid-row-end",
        "grid-column-end",
        "itemname",
    ]
    """grid-area: grid-row-start / grid-column-start /grid-row-end / grid-column-end |itemname;"""

    grid_column: Literal["grid-column-start", "grid-column-end", "span n"]
    """grid-column: grid-column-start  [grid-column-end | span n] ;"""

    grid_auto_flow: Literal["row", "column", "dense", "row dense", "column dense"]
    """grid-auto-flow: row | column | dense |row dense | column dense;"""

    grid_column_end: Literal["auto", "column", "span n"]
    """grid-column-end: auto | column | span n;"""

    grid_column_gap: Literal["length"]
    """grid-column-gap: length;"""

    grid_gap: Literal["grid-row-gap", "grid-column-gap"]
    """grid-gap: grid-row-gap grid-column-gap;"""

    grid_column_start: Literal["auto", "column", "span n"]
    """grid-column-start: auto | column | span n;"""

    grid_row_end: Literal["auto", "span n", "row"]
    """grid-row-end: auto | span n | row-line;"""

    grid_row: Literal["grid-row-start", "grid-row-end", "span n"]
    """grid-row: grid-row-start  [grid-row-end | span n] ;"""

    grid_row_gap: Literal["length"]
    """grid-row-gap: length;"""

    grid_template_areas: Literal["none", "areanames"]
    """grid-template-areas: none | areanames;"""

    grid_template: Literal[
        "none",
        "grid-template-rows",
        "grid-template-columns",
        "grid-template-areas",
        "initial",
        "inherit",
    ]
    """grid-template: none | grid-template-rows / grid-template-columns |grid-template-areas | initial | inherit;"""

    height: Literal["auto", "length", "%", "initial", "inherit"]
    """height: auto | length | initial | inherit;"""

    grid_template_columns: Literal[
        "none", "auto", "max-content", "min-content", "length", "initial", "inherit"
    ]
    """grid-template-columns: none | auto | max-content |min-content | length | initial | inherit;"""

    grid_row_start: Literal["auto", "span n", "row"]
    """grid-row-start: auto | span n | row-line;"""

    grid_template_rows: Literal[
        "none", "auto", "max-content", "min-content", "length", "initial", "inherit"
    ]
    """grid-template-rows: none | auto | max-content |min-content | length | initial | inherit;"""

    hyphens: Literal["none", "manual", "auto", "initial", "inherit"]
    """hyphens: none | manual | auto | initial | inherit;"""

    justify_content: Literal[
        "flex-start",
        "flex-end",
        "center",
        "space-between",
        "space-around",
        "initial",
        "inherit",
    ]
    """justify-content: flex-start | flex-end | center | space-between |space-around | initial | inherit;"""

    keyframes: Literal["animation-name", "keyframes-selector", "css-styles"]
    """@keyframes animation-name {keyframes-selector { css-styles; }}"""

    left: Literal["auto", "length", "%", "initial", "inherit"]
    """left: auto | length | initial | inherit;"""

    letter_spacing: Literal["normal", "length", "initial", "inherit"]
    """letter-spacing: normal | length | initial | inherit;"""

    line_height: Literal["normal", "number", "length", "%", "initial", "inherit"]
    """line-height: normal | number | length |initial | inherit;"""

    list_style_image: Literal["none", "url", "initial", "inherit"]
    """list-style-image: none | url | initial | inherit;"""

    list_style: Literal[
        "list-style-type",
        "list-style-position",
        "list-style-image",
        "initial",
        "inherit",
    ]
    """list-style: list-style-type list-style-position list-style-image |initial | inherit;"""

    margin: Literal["length", "%", "auto", "initial", "inherit"]
    """margin: length | auto | initial | inherit;"""

    margin_bottom: Literal["length", "%", "auto", "initial", "inherit"]
    """margin-bottom: length | auto | initial | inherit;"""

    list_style_position: Literal["inside", "outside", "initial", "inherit"]
    """list-style-position: inside | outside | initial | inherit;"""

    list_style_type: Literal[
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
    ]
    """list-style-type: value;"""

    margin_left: Literal["length", "%", "auto", "initial", "inherit"]
    """margin-left: length | auto | initial | inherit;"""

    margin_right: Literal["length", "%", "auto", "initial", "inherit"]
    """margin-right: length | auto | initial | inherit;"""

    margin_top: Literal["length", "%", "auto", "initial", "inherit"]
    """margin-top: length | auto | initial | inherit;"""

    max_width: Literal["none", "length", "%", "initial", "inherit"]
    """max-width: none | length | initial | inherit;"""

    max_height: Literal["none", "length", "%", "initial", "inherit"]
    """max-height: none | length | initial | inherit;"""

    media: Literal["all", "print", "screen", "speech"]
    """@media not | only mediatype and(mediafeature and | or | not mediafeature) {CSS-Code;}"""

    min_height: Literal["length", "%", "initial", "inherit"]
    """min-height: length | initial | inherit;"""

    min_width: Literal["length", "%", "initial", "inherit"]
    """min-width: length | initial | inherit;"""

    opacity: Literal["number", "initial", "inherit"]
    """opacity: number | initial | inherit;"""

    outline: Literal[
        "outline-width", "outline-style", "outline-color", "initial", "inherit"
    ]
    """outline: outline-width outline-style outline-color | initial | inherit;"""

    object_position: Literal["position", "initial", "inherit"]
    """object-position: position | initial | inherit;"""

    order: Literal["number", "initial", "inherit"]
    """order: number | initial | inherit;"""

    object_fit: Literal[
        "fill", "contain", "cover", "scale-down", "none", "initial", "inherit"
    ]
    """object-fit: fill | contain | cover | scale-down |none | initial | inherit;"""

    outline_color: Literal["invert", "color", "initial", "inherit"]
    """outline-color: invert | color | transparent |initial | inherit;"""

    outline_offset: Literal["length", "initial", "inherit"]
    """outline-offset: length | initial | inherit;"""

    outline_style: Literal[
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
    ]
    """outline-style: none | hidden | dotted | dashed |solid | double | groove | ridge |inset | outset | initial | inherit;"""

    outline_width: Literal["medium", "thin", "thick", "length", "initial", "inherit"]
    """outline-width: medium | thin | thick |length | initial | inherit;"""

    overflow_x: Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    """overflow-x: visible | hidden | scroll |auto | initial | inherit;"""

    overflow_y: Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    """overflow-y: visible | hidden | scroll |auto | initial | inherit;"""

    overflow: Literal["visible", "hidden", "scroll", "auto", "initial", "inherit"]
    """overflow: visible | hidden | scroll |auto | initial | inherit;"""

    padding_left: Literal["length", "%", "initial", "inherit"]
    """padding-left: length | initial | inherit;"""

    padding_bottom: Literal["length", "%", "initial", "inherit"]
    """padding-bottom: length | initial | inherit;"""

    padding_top: Literal["length", "%", "initial", "inherit"]
    """padding-top: length | initial | inherit;"""

    padding: Literal["length", "initial", "inherit"]
    """padding: length | initial | inherit;"""

    padding_right: Literal["length", "%", "initial", "inherit"]
    """padding-right: length | initial | inherit;"""

    page_break_after: Literal[
        "auto", "always", "avoid", "left", "right", "initial", "inherit"
    ]
    """page-break-after: auto | always | avoid | left |right | initial | inherit;"""

    page_break_before: Literal[
        "auto", "always", "avoid", "left", "right", "initial", "inherit"
    ]
    """page-break-before: auto | always | avoid | left |right | initial | inherit;"""

    page_break_inside: Literal["auto", "avoid", "initial", "inherit"]
    """page-break-inside: auto | avoid |initial | inherit;"""

    perspective: Literal["length", "none", "initial", "inherit"]
    """perspective: length | none | initial | inherit;"""

    position: Literal[
        "static", "relative", "absolute", "fixed", "sticky", "initial", "inherit"
    ]
    """position: static | absolute | fixed | relative |sticky | initial | inherit;"""

    pointer_events: Literal[
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
    ]
    """No syntax rule available"""

    perspective_origin: Literal["x-axis", "y-axis", "initial", "inherit"]
    """perspective-origin: x-axis y-axis |initial | inherit;"""

    quotes: Literal["none", "[string string]+", "initial", "inherit"]
    """quotes: none | [string string]+ |initial | inherit;"""

    right: Literal["auto", "length", "%", "initial", "inherit"]
    """right: auto | length | initial | inherit;"""

    row_gap: Literal["length", "normal", "initial", "inherit"]
    """row-gap: length | normal | initial | inherit;"""

    text_align: Literal["left", "right", "center", "justify", "initial", "inherit"]
    """text-align: left | right | center |justify | initial | inherit;"""

    scroll_behavior: Literal["auto", "smooth", "initial", "inherit"]
    """scroll-behavior: auto | smooth | initial | inherit;"""

    table_layout: Literal["auto", "fixed", "initial", "inherit"]
    """table-layout: auto | fixed | initial | inherit;"""

    text_align_last: Literal[
        "auto",
        "left",
        "right",
        "center",
        "justify",
        "start",
        "end",
        "initial",
        "inherit",
    ]
    """text-align-last: auto | left | right | center |justify | start | end |initial | inherit;"""

    text_decoration: Literal[
        "none",
        "text-decoration-line",
        "text-decoration-color",
        "text-decoration-style",
        "initial",
        "inherit",
    ]
    """text-decoration: none |text-decoration-line text-decoration-colortext-decoration-style | initial | inherit;"""

    text_decoration_color: Literal["color", "initial", "inherit"]
    """text-decoration-color: color | initial | inherit;"""

    text_decoration_line: Literal[
        "none", "underline", "overline", "line-through", "initial", "inherit"
    ]
    """text-decoration-line: none | underline |overline | line-through |initial | inherit;"""

    text_indent: Literal["length", "%", "initial", "inherit"]
    """text-indent: length | initial | inherit;"""

    text_decoration_style: Literal[
        "solid", "double", "dotted", "dashed", "wavy", "initial", "inherit"
    ]
    """text-decoration-style: solid | double | dotted |dashed | wavy | initial | inherit;"""

    text_justify: Literal["none", "auto", "inter-word", "trim", "initial", "inherit"]
    """text-justify: auto | inter-word |none | initial | inherit;"""

    text_shadow: Literal[
        "none", "x-offset", "y-offset", "blur-radius", "color", "initial", "inherit"
    ]
    """text-shadow: x-offset y-offset blur-radius color |none | initial | inherit;"""

    text_overflow: Literal["clip", "ellipsis", "string", "initial", "inherit"]
    """text-overflow: clip | ellipsis | string |initial | inherit;"""

    text_transform: Literal[
        "none", "capitalize", "uppercase", "lowercase", "initial", "inherit"
    ]
    """text-transform: none | capitalize | uppercase |lowercase | initial | inherit;"""

    top: Literal["auto", "length", "%", "initial", "inherit"]
    """top: auto | length | initial | inherit;"""

    transform_origin: Literal["x-axis", "y-axis", "z-axis", "initial", "inherit"]
    """transform-origin: x-axis y-axis z-axis |initial | inherit;"""

    transform: Literal[
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
    ]
    """transform: none | transform-functions |initial | inherit;"""

    transform_style: Literal["flat", "preserve-3d", "initial", "inherit"]
    """transform-style: flat | preserve-3d | initial | inherit;"""

    transition: Literal[
        "transition-property",
        "transition-duration",
        "transition-timing-function",
        "transition-delay",
        "initial",
        "inherit",
    ]
    """transition: property duration timing-function delay |initial | inherit;"""

    transition_duration: Literal["time", "initial", "inherit"]
    """transition-duration: time | initial | inherit;"""

    transition_delay: Literal["time", "initial", "inherit"]
    """transition-delay: time | initial | inherit;"""

    transition_property: Literal["none", "all", "properties", "initial", "inherit"]
    """transition-property: none | all | properties |initial | inherit;"""

    transition_timing_function: Literal[
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
    ]
    """No syntax rule available"""

    user_select: Literal["auto", "none", "text", "all"]
    """user-select: auto | none | text | all;"""

    width: Literal["auto", "length", "initial", "inherit"]
    """width: auto | length | initial | inherit;"""

    word_break: Literal[
        "normal", "break-all", "keep-all", "break-word", "initial", "inherit"
    ]
    """word-break: normal | break-all | keep-all |break-word | initial | inherit;"""

    visibility: Literal["visible", "hidden", "collapse", "initial", "inherit"]
    """visibility: visible | hidden | collapse |initial | inherit;"""

    word_spacing: Literal["normal", "length", "initial", "inherit"]
    """word-spacing: normal | length | initial | inherit;"""

    white_space: Literal[
        "normal", "nowrap", "pre", "pre-line", "pre-wrap", "initial", "inherit"
    ]
    """white-space: normal | nowrap | pre |pre-line | pre-wrap | initial | inherit;"""

    vertical_align: Literal[
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
    ]
    """vertical-align: baseline | length | sub | super |top | text-top | middle | bottom |text-bottom | initial | inherit;"""

    word_wrap: Literal["normal", "break-word", "initial", "inherit"]
    """word-wrap: normal | break-word | initial | inherit;"""

    z_index: Literal["auto", "number", "initial", "inherit"]
    """z-index: auto | number | initial | inherit;"""

    writing_mode: Literal["horizontal-tb", "vertical-rl", "vertical-lr"]
    """writing-mode: horizontal-tb | vertical-rl | vertical-lr;"""

    @classmethod
    def name(cls) -> str:
        """Name string."""
        return cls.__name__.replace("_", "-")

    @classmethod
    def properties(cls) -> t.Dict[str, str]:
        """Returns properties mapping."""
        properties = {}
        for base in cls.__bases__:
            if hasattr(base, "properties"):
                properties.update(base.properties())
        for prop, val in cls.__dict__.items():
            if isinstance(val, str) and not prop.startswith("__"):
                properties[css_attr[prop]] = val
        return properties

    @classmethod
    def subclasses(cls) -> t.List["CSSObject"]:
        """Returns the list of available subclasses."""
        cs = []
        for c in cls.__dict__.values():
            if hasattr(c, "properties"):
                cs.append(c)
        return cs


def _render(obj: CSSObject, parent: str, container: t.Dict) -> None:
    """Render CSS object."""
    container[f"{parent} .{obj.name()}"[1:]] = obj.properties()
    for subc in obj.subclasses():
        _render(
            obj=subc,
            parent=f"{parent} .{obj.name()}",
            container=container,
        )


def render(*objs: CSSObject, minify: bool = False) -> str:
    """Render CSS stylesheet."""
    sheet = ""
    container: t.Dict[str, t.Dict] = {}
    separator = "" if minify else " "
    newline = "" if minify else "\n"
    tab = "" if minify else "  "
    for obj in objs:
        _render(obj=obj, parent="", container=container)
    for cls in sorted(container):
        sheet += f"{cls}" + "{" + newline
        for prop, val in container[cls].items():
            sheet += f"{tab}{prop}:{separator}{val};{newline}"
        sheet += "}" + newline
    return sheet
