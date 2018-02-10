"""
    pygclip.colors
    ~~~~~~~~~~~~~~

    Color-related functions.

    :copyright: © 2018 by Bryan Lee McKelvey.
    :license: MIT, see LICENSE for more details.
"""

from typing import Tuple

RGB = Tuple[int, int, int]


def _hex_to_rgb(hex_color: str) -> RGB:
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def _rgb_to_hex(rgb: RGB) -> str:
    return '#{:02x}{:02x}{:02x}'.format(*rgb)


def _darken_rgb(rgb: RGB, factor: float) -> RGB:
    return tuple(int(x * (1 - factor)) for x in rgb)


def darken_color(hex_color: str, factor: float) -> str:
    return _rgb_to_hex(_darken_rgb(_hex_to_rgb(hex_color), factor))

