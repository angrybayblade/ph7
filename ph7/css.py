"""
This file is auto generated using scripts/render/css.py
"""

# pylint: disable=line-too-long,too-many-lines,redefined-outer-name,redefined-builtin,invalid-name,too-many-locals

from typing_extensions import Literal

from ph7.core.css import CSSNode, to_css


class CSSObject(CSSNode):
    """CSS class representation."""

    animation: Literal[  # type: ignore
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
    """No syntax rule available"""

    animation_play_state: Literal[  # type: ignore
        "paused", "running", "initial", "inherit", str
    ]
    """No syntax rule available"""

    animation_name: Literal[  # type: ignore
        "keyframename", "none", "initial", "inherit", str
    ]
    """No syntax rule available"""

    animation_fill_mode: Literal[  # type: ignore
        "none", "forwards", "backwards", "both", "initial", "inherit", str
    ]
    """No syntax rule available"""

    align_items: Literal[  # type: ignore
        "stretch",
        "center",
        "flex-start",
        "flex-end",
        "baseline",
        "initial",
        "inherit",
        str,
    ]
    """align-items: stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    animation_duration: Literal["time", "initial", "inherit", str]  # type: ignore
    """No syntax rule available"""

    align_self: Literal[  # type: ignore
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
    """align-self: auto | stretch | center | flex-start |flex-end | baseline | initial | inherit;"""

    align_content: Literal[  # type: ignore
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
    """align-content: stretch | center | flex-start |flex-end | space-between |space-around | initial | inherit;"""

    animation_direction: Literal[  # type: ignore
        "normal", "reverse", "alternate", "alternate-reverse", "initial", "inherit", str
    ]
    """No syntax rule available"""

    animation_iteration_count: Literal[  # type: ignore
        "number", "infinite", "initial", "inherit", str
    ]
    """No syntax rule available"""

    all: Literal["initial", "inherit", "unset", str]  # type: ignore
    """No syntax rule available"""

    animation_delay: Literal["time", "initial", "inherit", str]  # type: ignore
    """animation-delay: time | initial | inherit;"""

    animation_timing_function: Literal[  # type: ignore
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
    """No syntax rule available"""

    backface_visibility: Literal[  # type: ignore
        "visible", "hidden", "initial", "inherit", str
    ]
    """backface-visibility: visible | hidden | initial | inherit;"""

    background_position: Literal[  # type: ignore
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
    """background-position: value | x% y% |xpos ypos | initial | inherit"""

    background_size: Literal[  # type: ignore
        "auto", "length", "percentage", "cover", "contain", "initial", "inherit", str
    ]
    """background-size: auto | length | cover |contain | initial | inherit;"""

    background: Literal[  # type: ignore
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
    """background: bg-color bg-image position/bg-size bg-repeatbg-origin bg-clip bg-attachment | initial | inherit;"""

    background_attachment: Literal[  # type: ignore
        "scroll", "fixed", "local", "initial", "inherit", str
    ]
    """background-attachment: scroll | fixed | local |initial | inherit;"""

    background_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """background-color: color | transparent | initial | inherit;"""

    background_repeat: Literal[  # type: ignore
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
    """background-repeat: repeat | repeat-x | repeat-y |no-repeat | initial | inherit;"""

    background_clip: Literal[  # type: ignore
        "content-box", "padding-box", "border-box", "initial", "inherit", str
    ]
    """background-clip: border-box | padding-box |content-box | initial | inherit;"""

    background_blend_mode: Literal[  # type: ignore
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
    """background-blend-mode: normal | multiply | screen | overlay | darken |lighten | color-dodge | saturation | color |luminosity;"""

    background_origin: Literal[  # type: ignore
        "padding-box", "border-box", "content-box", "initial", "inherit", str
    ]
    """background-origin: padding-box | border-box |content-box | initial | inherit;"""

    background_image: Literal[  # type: ignore
        "url",
        "none",
        "linear-gradient()",
        "radial-gradient()",
        "repeating-linear-gradient()",
        "repeating-radial-gradient()",
        "inherit",
        str,
    ]
    """background-image: url(url) | none | linear-gradient() | radial-gradient() |repeating-linear-gradient() | repeating-radial-gradient() |inherit;"""

    border: Literal[  # type: ignore
        "border-width", "border-style", "border-color", "initial", "inherit", str
    ]
    """border: border-width border-style border-color |initial | inherit;"""

    border_bottom: Literal[  # type: ignore
        "border-width", "border-style", "border-color", "initial", "inherit", str
    ]
    """border-bottom: border-width border-style border-color |initial | inherit;"""

    border_bottom_left_radius: Literal[  # type: ignore
        "length", "%", "initial", "inherit", str
    ]
    """border-bottom-left-radius: length | length% |initial | inherit;"""

    border_bottom_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """border-bottom-color: color | transparent |initial | inherit;"""

    border_bottom_style: Literal[  # type: ignore
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
    """No syntax rule available"""

    border_image_repeat: Literal[  # type: ignore
        "stretch", "repeat", "round", "space", "initial", "inherit", str
    ]
    """border-image-repeat: stretch | repeat |round | initial | inherit;"""

    border_image: Literal[  # type: ignore
        "border-image-source",
        "border-image-slice",
        "border-image-width",
        "border-image-outset",
        "border-image-repeat",
        "initial",
        "inherit",
        str,
    ]
    """border-image: URL slice width outset repeat |initial | inherit;"""

    border_collapse: Literal[  # type: ignore
        "separate", "collapse", "initial", "inherit", str
    ]
    """border-collapse: separate | collapse | initial | inherit;"""

    border_image_outset: Literal[  # type: ignore
        "length", "number", "initial", "inherit", str
    ]
    """border-image-outset: length | number |initial | inherit;"""

    border_bottom_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """No syntax rule available"""

    border_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """border-color: color | transparent | initial | inherit;"""

    border_bottom_right_radius: Literal[  # type: ignore
        "length", "%", "initial", "inherit", str
    ]
    """border-bottom-right-radius: length | length% | initial | inherit;"""

    border_image_slice: Literal[  # type: ignore
        "number", "%", "fill", "initial", "inherit", str
    ]
    """border-image-slice: number | % |fill | initial | inherit;"""

    border_image_source: Literal[  # type: ignore
        "none", "image", "initial", "inherit", str
    ]
    """border-image-source: none | image | initial | inherit;"""

    border_image_width: Literal[  # type: ignore
        "length", "number", "%", "auto", "initial", "inherit", str
    ]
    """border-image-width: number | % | auto | initial | inherit;"""

    border_left_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """border-left-color: color | transparent | initial | inherit;"""

    border_left_style: Literal[  # type: ignore
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
    """No syntax rule available"""

    border_right_style: Literal[  # type: ignore
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
    """No syntax rule available"""

    border_radius: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """No syntax rule available"""

    border_left: Literal[  # type: ignore
        "border-width", "border-style", "border-color", "initial", "inherit", str
    ]
    """border-left: border-width border-style border-color |initial | inherit;"""

    border_left_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """No syntax rule available"""

    border_right_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """border-right-color: color | transparent | initial | inherit;"""

    border_right: Literal[  # type: ignore
        "border-width", "border-style", "border-color", "initial", "inherit", str
    ]
    """border-right: border-width border-style border-color |initial | inherit;"""

    border_right_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """No syntax rule available"""

    border_spacing: Literal["length length", "initial", "inherit", str]  # type: ignore
    """border-spacing: length | initial | inherit;"""

    border_style: Literal[  # type: ignore
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
    """No syntax rule available"""

    border_top: Literal[  # type: ignore
        "border-width", "border-style", "border-color", "initial", "inherit", str
    ]
    """border-top: border-width border-style border-color |initial | inherit;"""

    border_top_right_radius: Literal[  # type: ignore
        "length", "%", "initial", "inherit", str
    ]
    """border-top-right-radius: length | length% | initial | inherit;"""

    border_top_color: Literal[  # type: ignore
        "color", "transparent", "initial", "inherit", str
    ]
    """border-top-color: color | transparent | initial | inherit;"""

    border_top_left_radius: Literal[  # type: ignore
        "length", "%", "initial", "inherit", str
    ]
    """border-top-left-radius: length | length% | initial | inherit;"""

    box_shadow: Literal[  # type: ignore
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
    """box-shadow: none | h-offset v-offset blur spread color |inset | initial | inherit;"""

    border_top_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """No syntax rule available"""

    border_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """border-width: medium | thin | thick |length | initial | inherit;"""

    box_decoration_break: Literal[  # type: ignore
        "slice", "clone", "initial", "inherit", str
    ]
    """box-decoration-break: slice | clone |initial | inherit | unset;"""

    border_top_style: Literal[  # type: ignore
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
    """No syntax rule available"""

    bottom: Literal["auto", "length", "%", "initial", "inherit", str]  # type: ignore
    """bottom: auto | length | initial | inherit;"""

    box_sizing: Literal[  # type: ignore
        "content-box", "border-box", "initial", "inherit", str
    ]
    """box-sizing: content-box | border-box | initial | inherit;"""

    caption_side: Literal["bottom", "top", "initial", "inherit", str]  # type: ignore
    """caption-side: top | bottom | initial | inherit;"""

    caret_color: Literal["auto", "color", "transparent", str]  # type: ignore
    """caret-color: auto | color | transparent;"""

    charset: Literal["charset", str]  # type: ignore
    """@charset "charset";"""

    clear: Literal[  # type: ignore
        "none", "left", "right", "both", "initial", "inherit", str
    ]
    """clear: none | left | right | both |initial | inherit;"""

    column_count: Literal["number", "auto", "initial", "inherit", str]  # type: ignore
    """column-count: number | auto | initial | inherit;"""

    clip: Literal["auto", "shape", "initial", "inherit", str]  # type: ignore
    """clip: auto | shape | initial | inherit;"""

    column_rule: Literal[  # type: ignore
        "column-rule-width ",
        "column-rule-style ",
        "column-rule-color ",
        "initial",
        "inherit",
        str,
    ]
    """column-rule: column-rule-widthcolumn-rule-stylecolumn-rule-color |initial | inherit;"""

    column_gap: Literal["length", "normal", "initial", "inherit", str]  # type: ignore
    """column-gap: length | normal | initial | inherit;"""

    clip_path: Literal[  # type: ignore
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
    """clip-path: clip-source | basic-shape | margin-box |border-box | padding-box | content-box |fill-box | stroke-box | view-box | none;"""

    color: Literal["color", "initial", "inherit", str]  # type: ignore
    """color: color | initial | inherit;"""

    column_fill: Literal["balance", "auto", "initial", "inherit", str]  # type: ignore
    """column-fill: balance | auto | initial | inherit;"""

    column_rule_color: Literal["color", "initial", "inherit", str]  # type: ignore
    """column-rule-color: color | initial | inherit;"""

    column_rule_style: Literal[  # type: ignore
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
    """column-rule-style: none | hidden | dotted |dashed | solid | double |groove | ridge | inset |outset | initial | inherit;"""

    column_rule_width: Literal[  # type: ignore
        "length", "medium", "thin", "thick", "initial", "inherit", str
    ]
    """column-rule-width: length |medium | thin | thick |initial | inherit;"""

    column_span: Literal["none", "all", "initial", "inherit", str]  # type: ignore
    """column-span: none | all |initial | inherit;"""

    column_width: Literal["auto", "length", "initial", "inherit", str]  # type: ignore
    """column-width: auto | length |initial | inherit;"""

    columns: Literal[  # type: ignore
        "auto", "column-width", "column-count", "initial", "inherit", str
    ]
    """columns: auto | column-width column-count |initial | inherit;"""

    content: Literal[  # type: ignore
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
    """content: normal | none | counter | attr | string |open-quote | close-quote | no-open-quote |no-close-quote | url | initial | inherit;"""

    counter_increment: Literal[  # type: ignore
        "none", "name number", "initial", "inherit", str
    ]
    """counter-increment: none | name number |initial | inherit;"""

    direction: Literal["ltr", "rtl", "initial", "inherit", str]  # type: ignore
    """direction: ltr | rtl | initial | inherit;"""

    counter_reset: Literal[  # type: ignore
        "none", "name number", "initial", "inherit", str
    ]
    """counter-reset: none | name number | initial | inherit;"""

    display: Literal[  # type: ignore
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
    """display: value"""

    empty_cells: Literal["show", "hide", "initial", "inherit", str]  # type: ignore
    """empty-cells: show | hide | initial | inherit;"""

    filter: Literal[  # type: ignore
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
    """filter: none | blur() | brightness() | contrast() |drop-shadow() | grayscale() | hue-rotate() |invert() | opacity() | saturate() |sepia() | url();"""

    cursor: Literal[  # type: ignore
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
    """cursor: value;"""

    flex: Literal[  # type: ignore
        "flex-grow",
        "flex-shrink",
        "flex-basis",
        "auto",
        "none",
        "initial",
        "inherit",
        str,
    ]
    """flex: flex-grow flex-shrink flex-basis |auto | initial | inherit;"""

    flex_basis: Literal["auto", "length", "initial", "inherit", str]  # type: ignore
    """flex-basis: auto | length | initial | inherit;"""

    flex_direction: Literal[  # type: ignore
        "row", "row-reverse", "column", "column-reverse", "initial", "inherit", str
    ]
    """flex-direction: row | row-reverse | column |column-reverse | initial |inherit;"""

    flex_flow: Literal[  # type: ignore
        "flex-direction", "flex-wrap", "initial", "inherit", str
    ]
    """flex-flow: flex-direction flex-wrap |initial | inherit;"""

    flex_grow: Literal["number", "initial", "inherit", str]  # type: ignore
    """flex-grow: number | initial | inherit;"""

    flex_shrink: Literal["number", "initial", "inherit", str]  # type: ignore
    """flex-shrink: number | initial | inherit;"""

    font_family: Literal[  # type: ignore
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
    """font-family: family-name | generic-family |initial | inherit;"""

    float: Literal["none", "left", "right", "initial", "inherit", str]  # type: ignore
    """float: none | left | right | initial | inherit;"""

    font_face: Literal[  # type: ignore
        "font-family",
        "src",
        "font-stretch",
        "font-style",
        "font-weight",
        "unicode-range",
        str,
    ]
    """@font-face { font-properties }"""

    flex_wrap: Literal[  # type: ignore
        "nowrap", "wrap", "wrap-reverse", "initial", "inherit", str
    ]
    """flex-wrap: nowrap | wrap | wrap-reverse |initial | inherit;"""

    font: Literal[  # type: ignore
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
    """No syntax rule available"""

    font_kerning: Literal["auto", "normal", "none", str]  # type: ignore
    """font-kerning: auto | normal | none;"""

    font_size: Literal[  # type: ignore
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
    """font-size: medium | xx-small | x-small | small |large | x-large | xx-large | smaller |larger | length | initial | inherit;"""

    font_stretch: Literal[  # type: ignore
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
    """font-stretch: ultra-condensed | extra-condensed |condensed | semi-condensed | normal |semi-expanded | expanded | extra-expanded |ultra-expanded | initial | inherit;"""

    font_variant: Literal[  # type: ignore
        "normal", "small-caps", "initial", "inherit", str
    ]
    """font-variant: normal | small-caps |initial | inherit;"""

    font_style: Literal[  # type: ignore
        "normal", "italic", "oblique", "initial", "inherit", str
    ]
    """font-style: normal | italic | oblique |initial | inherit;"""

    font_weight: Literal[  # type: ignore
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
    """font-weight: normal | bold | bolder | lighter |number | initial | inherit;"""

    gap: Literal["length", "normal", "initial", "inherit", str]  # type: ignore
    """gap: length | normal | initial | inherit;"""

    grid: Literal["none", "initial", "inherit", str]  # type: ignore
    """
    grid: none |grid-template-rows / grid-template-columns |
    grid-template-areas |grid-template-rows / [grid-auto-flow] grid-auto-columns |
    [grid-auto-flow] grid-auto-rows / grid-template-columns |initial | inherit;
    """

    grid_auto_columns: Literal[  # type: ignore
        "auto", "min-content", "max-content", "minmax(min.max)", "length", "%", str
    ]
    """grid-auto-columns: auto | min-content | max-content |minmax() | length | %;"""

    grid_auto_rows: Literal[  # type: ignore
        "auto", "max-content", "min-content", "minmax(min.max)", "length", "%", str
    ]
    """grid-auto-columns: auto | max-content | min-content |minmax | length | %;"""

    grid_area: Literal[  # type: ignore
        "grid-row-start",
        "grid-column-start",
        "grid-row-end",
        "grid-column-end",
        "itemname",
        str,
    ]
    """grid-area: grid-row-start / grid-column-start /grid-row-end / grid-column-end |itemname;"""

    grid_column: Literal[  # type: ignore
        "grid-column-start", "grid-column-end", "span n", str
    ]
    """grid-column: grid-column-start  [grid-column-end | span n] ;"""

    grid_auto_flow: Literal[  # type: ignore
        "row", "column", "dense", "row dense", "column dense", str
    ]
    """grid-auto-flow: row | column | dense |row dense | column dense;"""

    grid_column_end: Literal["auto", "column", "span n", str]  # type: ignore
    """grid-column-end: auto | column | span n;"""

    grid_column_gap: Literal["length", str]  # type: ignore
    """grid-column-gap: length;"""

    grid_gap: Literal["grid-row-gap", "grid-column-gap", str]  # type: ignore
    """grid-gap: grid-row-gap grid-column-gap;"""

    grid_column_start: Literal["auto", "column", "span n", str]  # type: ignore
    """grid-column-start: auto | column | span n;"""

    grid_row_end: Literal["auto", "span n", "row", str]  # type: ignore
    """grid-row-end: auto | span n | row-line;"""

    grid_row: Literal["grid-row-start", "grid-row-end", "span n", str]  # type: ignore
    """grid-row: grid-row-start  [grid-row-end | span n] ;"""

    grid_row_gap: Literal["length", str]  # type: ignore
    """grid-row-gap: length;"""

    grid_template_areas: Literal["none", "areanames", str]  # type: ignore
    """grid-template-areas: none | areanames;"""

    grid_template: Literal[  # type: ignore
        "none",
        "grid-template-rows",
        "grid-template-columns",
        "grid-template-areas",
        "initial",
        "inherit",
        str,
    ]
    """grid-template: none | grid-template-rows / grid-template-columns |grid-template-areas | initial | inherit;"""

    height: Literal["auto", "length", "%", "initial", "inherit", str]  # type: ignore
    """height: auto | length | initial | inherit;"""

    grid_template_columns: Literal[  # type: ignore
        "none",
        "auto",
        "max-content",
        "min-content",
        "length",
        "initial",
        "inherit",
        str,
    ]
    """grid-template-columns: none | auto | max-content |min-content | length | initial | inherit;"""

    grid_row_start: Literal["auto", "span n", "row", str]  # type: ignore
    """grid-row-start: auto | span n | row-line;"""

    grid_template_rows: Literal[  # type: ignore
        "none",
        "auto",
        "max-content",
        "min-content",
        "length",
        "initial",
        "inherit",
        str,
    ]
    """grid-template-rows: none | auto | max-content |min-content | length | initial | inherit;"""

    hyphens: Literal[  # type: ignore
        "none", "manual", "auto", "initial", "inherit", str
    ]
    """hyphens: none | manual | auto | initial | inherit;"""

    justify_content: Literal[  # type: ignore
        "flex-start",
        "flex-end",
        "center",
        "space-between",
        "space-around",
        "initial",
        "inherit",
        str,
    ]
    """justify-content: flex-start | flex-end | center | space-between |space-around | initial | inherit;"""

    keyframes: Literal[  # type: ignore
        "animation-name", "keyframes-selector", "css-styles", str
    ]
    """@keyframes animation-name {keyframes-selector { css-styles; }}"""

    left: Literal["auto", "length", "%", "initial", "inherit", str]  # type: ignore
    """left: auto | length | initial | inherit;"""

    letter_spacing: Literal[  # type: ignore
        "normal", "length", "initial", "inherit", str
    ]
    """letter-spacing: normal | length | initial | inherit;"""

    line_height: Literal[  # type: ignore
        "normal", "number", "length", "%", "initial", "inherit", str
    ]
    """line-height: normal | number | length |initial | inherit;"""

    list_style_image: Literal["none", "url", "initial", "inherit", str]  # type: ignore
    """list-style-image: none | url | initial | inherit;"""

    list_style: Literal[  # type: ignore
        "list-style-type",
        "list-style-position",
        "list-style-image",
        "initial",
        "inherit",
        str,
    ]
    """list-style: list-style-type list-style-position list-style-image |initial | inherit;"""

    margin: Literal["length", "%", "auto", "initial", "inherit", str]  # type: ignore
    """margin: length | auto | initial | inherit;"""

    margin_bottom: Literal[  # type: ignore
        "length", "%", "auto", "initial", "inherit", str
    ]
    """margin-bottom: length | auto | initial | inherit;"""

    list_style_position: Literal[  # type: ignore
        "inside", "outside", "initial", "inherit", str
    ]
    """list-style-position: inside | outside | initial | inherit;"""

    list_style_type: Literal[  # type: ignore
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
    """list-style-type: value;"""

    margin_left: Literal[  # type: ignore
        "length", "%", "auto", "initial", "inherit", str
    ]
    """margin-left: length | auto | initial | inherit;"""

    margin_right: Literal[  # type: ignore
        "length", "%", "auto", "initial", "inherit", str
    ]
    """margin-right: length | auto | initial | inherit;"""

    margin_top: Literal[  # type: ignore
        "length", "%", "auto", "initial", "inherit", str
    ]
    """margin-top: length | auto | initial | inherit;"""

    max_width: Literal["none", "length", "%", "initial", "inherit", str]  # type: ignore
    """max-width: none | length | initial | inherit;"""

    max_height: Literal[  # type: ignore
        "none", "length", "%", "initial", "inherit", str
    ]
    """max-height: none | length | initial | inherit;"""

    media: Literal["all", "print", "screen", "speech", str]  # type: ignore
    """@media not | only mediatype and(mediafeature and | or | not mediafeature) {CSS-Code;}"""

    min_height: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """min-height: length | initial | inherit;"""

    min_width: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """min-width: length | initial | inherit;"""

    opacity: Literal["number", "initial", "inherit", str]  # type: ignore
    """opacity: number | initial | inherit;"""

    outline: Literal[  # type: ignore
        "outline-width", "outline-style", "outline-color", "initial", "inherit", str
    ]
    """outline: outline-width outline-style outline-color | initial | inherit;"""

    object_position: Literal["position", "initial", "inherit", str]  # type: ignore
    """object-position: position | initial | inherit;"""

    order: Literal["number", "initial", "inherit", str]  # type: ignore
    """order: number | initial | inherit;"""

    object_fit: Literal[  # type: ignore
        "fill", "contain", "cover", "scale-down", "none", "initial", "inherit", str
    ]
    """object-fit: fill | contain | cover | scale-down |none | initial | inherit;"""

    outline_color: Literal["invert", "color", "initial", "inherit", str]  # type: ignore
    """outline-color: invert | color | transparent |initial | inherit;"""

    outline_offset: Literal["length", "initial", "inherit", str]  # type: ignore
    """outline-offset: length | initial | inherit;"""

    outline_style: Literal[  # type: ignore
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
    """outline-style: none | hidden | dotted | dashed |solid | double | groove | ridge |inset | outset | initial | inherit;"""

    outline_width: Literal[  # type: ignore
        "medium", "thin", "thick", "length", "initial", "inherit", str
    ]
    """outline-width: medium | thin | thick |length | initial | inherit;"""

    overflow_x: Literal[  # type: ignore
        "visible", "hidden", "scroll", "auto", "initial", "inherit", str
    ]
    """overflow-x: visible | hidden | scroll |auto | initial | inherit;"""

    overflow_y: Literal[  # type: ignore
        "visible", "hidden", "scroll", "auto", "initial", "inherit", str
    ]
    """overflow-y: visible | hidden | scroll |auto | initial | inherit;"""

    overflow: Literal[  # type: ignore
        "visible", "hidden", "scroll", "auto", "initial", "inherit", str
    ]
    """overflow: visible | hidden | scroll |auto | initial | inherit;"""

    padding_left: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """padding-left: length | initial | inherit;"""

    padding_bottom: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """padding-bottom: length | initial | inherit;"""

    padding_top: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """padding-top: length | initial | inherit;"""

    padding: Literal["length", "initial", "inherit", str]  # type: ignore
    """padding: length | initial | inherit;"""

    padding_right: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """padding-right: length | initial | inherit;"""

    page_break_after: Literal[  # type: ignore
        "auto", "always", "avoid", "left", "right", "initial", "inherit", str
    ]
    """page-break-after: auto | always | avoid | left |right | initial | inherit;"""

    page_break_before: Literal[  # type: ignore
        "auto", "always", "avoid", "left", "right", "initial", "inherit", str
    ]
    """page-break-before: auto | always | avoid | left |right | initial | inherit;"""

    page_break_inside: Literal[  # type: ignore
        "auto", "avoid", "initial", "inherit", str
    ]
    """page-break-inside: auto | avoid |initial | inherit;"""

    perspective: Literal["length", "none", "initial", "inherit", str]  # type: ignore
    """perspective: length | none | initial | inherit;"""

    position: Literal[  # type: ignore
        "static", "relative", "absolute", "fixed", "sticky", "initial", "inherit", str
    ]
    """position: static | absolute | fixed | relative |sticky | initial | inherit;"""

    pointer_events: Literal[  # type: ignore
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
    """No syntax rule available"""

    perspective_origin: Literal[  # type: ignore
        "x-axis", "y-axis", "initial", "inherit", str
    ]
    """perspective-origin: x-axis y-axis |initial | inherit;"""

    quotes: Literal[  # type: ignore
        "none", "[string string]+", "initial", "inherit", str
    ]
    """quotes: none | [string string]+ |initial | inherit;"""

    right: Literal["auto", "length", "%", "initial", "inherit", str]  # type: ignore
    """right: auto | length | initial | inherit;"""

    row_gap: Literal["length", "normal", "initial", "inherit", str]  # type: ignore
    """row-gap: length | normal | initial | inherit;"""

    text_align: Literal[  # type: ignore
        "left", "right", "center", "justify", "initial", "inherit", str
    ]
    """text-align: left | right | center |justify | initial | inherit;"""

    scroll_behavior: Literal[  # type: ignore
        "auto", "smooth", "initial", "inherit", str
    ]
    """scroll-behavior: auto | smooth | initial | inherit;"""

    table_layout: Literal["auto", "fixed", "initial", "inherit", str]  # type: ignore
    """table-layout: auto | fixed | initial | inherit;"""

    text_align_last: Literal[  # type: ignore
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
    """text-align-last: auto | left | right | center |justify | start | end |initial | inherit;"""

    text_decoration: Literal[  # type: ignore
        "none",
        "text-decoration-line",
        "text-decoration-color",
        "text-decoration-style",
        "initial",
        "inherit",
        str,
    ]
    """text-decoration: none |text-decoration-line text-decoration-colortext-decoration-style | initial | inherit;"""

    text_decoration_color: Literal["color", "initial", "inherit", str]  # type: ignore
    """text-decoration-color: color | initial | inherit;"""

    text_decoration_line: Literal[  # type: ignore
        "none", "underline", "overline", "line-through", "initial", "inherit", str
    ]
    """text-decoration-line: none | underline |overline | line-through |initial | inherit;"""

    text_indent: Literal["length", "%", "initial", "inherit", str]  # type: ignore
    """text-indent: length | initial | inherit;"""

    text_decoration_style: Literal[  # type: ignore
        "solid", "double", "dotted", "dashed", "wavy", "initial", "inherit", str
    ]
    """text-decoration-style: solid | double | dotted |dashed | wavy | initial | inherit;"""

    text_justify: Literal[  # type: ignore
        "none", "auto", "inter-word", "trim", "initial", "inherit", str
    ]
    """text-justify: auto | inter-word |none | initial | inherit;"""

    text_shadow: Literal[  # type: ignore
        "none",
        "x-offset",
        "y-offset",
        "blur-radius",
        "color",
        "initial",
        "inherit",
        str,
    ]
    """text-shadow: x-offset y-offset blur-radius color |none | initial | inherit;"""

    text_overflow: Literal[  # type: ignore
        "clip", "ellipsis", "string", "initial", "inherit", str
    ]
    """text-overflow: clip | ellipsis | string |initial | inherit;"""

    text_transform: Literal[  # type: ignore
        "none", "capitalize", "uppercase", "lowercase", "initial", "inherit", str
    ]
    """text-transform: none | capitalize | uppercase |lowercase | initial | inherit;"""

    top: Literal["auto", "length", "%", "initial", "inherit", str]  # type: ignore
    """top: auto | length | initial | inherit;"""

    transform_origin: Literal[  # type: ignore
        "x-axis", "y-axis", "z-axis", "initial", "inherit", str
    ]
    """transform-origin: x-axis y-axis z-axis |initial | inherit;"""

    transform: Literal[  # type: ignore
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
    """transform: none | transform-functions |initial | inherit;"""

    transform_style: Literal[  # type: ignore
        "flat", "preserve-3d", "initial", "inherit", str
    ]
    """transform-style: flat | preserve-3d | initial | inherit;"""

    transition: Literal[  # type: ignore
        "transition-property",
        "transition-duration",
        "transition-timing-function",
        "transition-delay",
        "initial",
        "inherit",
        str,
    ]
    """transition: property duration timing-function delay |initial | inherit;"""

    transition_duration: Literal["time", "initial", "inherit", str]  # type: ignore
    """transition-duration: time | initial | inherit;"""

    transition_delay: Literal["time", "initial", "inherit", str]  # type: ignore
    """transition-delay: time | initial | inherit;"""

    transition_property: Literal[  # type: ignore
        "none", "all", "properties", "initial", "inherit", str
    ]
    """transition-property: none | all | properties |initial | inherit;"""

    transition_timing_function: Literal[  # type: ignore
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
    """No syntax rule available"""

    user_select: Literal["auto", "none", "text", "all", str]  # type: ignore
    """user-select: auto | none | text | all;"""

    width: Literal["auto", "length", "initial", "inherit", str]  # type: ignore
    """width: auto | length | initial | inherit;"""

    word_break: Literal[  # type: ignore
        "normal", "break-all", "keep-all", "break-word", "initial", "inherit", str
    ]
    """word-break: normal | break-all | keep-all |break-word | initial | inherit;"""

    visibility: Literal[  # type: ignore
        "visible", "hidden", "collapse", "initial", "inherit", str
    ]
    """visibility: visible | hidden | collapse |initial | inherit;"""

    word_spacing: Literal["normal", "length", "initial", "inherit", str]  # type: ignore
    """word-spacing: normal | length | initial | inherit;"""

    white_space: Literal[  # type: ignore
        "normal", "nowrap", "pre", "pre-line", "pre-wrap", "initial", "inherit", str
    ]
    """white-space: normal | nowrap | pre |pre-line | pre-wrap | initial | inherit;"""

    vertical_align: Literal[  # type: ignore
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
    """vertical-align: baseline | length | sub | super |top | text-top | middle | bottom |text-bottom | initial | inherit;"""

    word_wrap: Literal[  # type: ignore
        "normal", "break-word", "initial", "inherit", str
    ]
    """word-wrap: normal | break-word | initial | inherit;"""

    z_index: Literal["auto", "number", "initial", "inherit", str]  # type: ignore
    """z-index: auto | number | initial | inherit;"""

    writing_mode: Literal[  # type: ignore
        "horizontal-tb", "vertical-rl", "vertical-lr", str
    ]
    """writing-mode: horizontal-tb | vertical-rl | vertical-lr;"""

    def __str__(self) -> str:
        """String representation."""
        return to_css(self)

    __repr__ = __str__
