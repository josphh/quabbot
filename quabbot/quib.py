import colorsys
import random
from os import path

from cairosvg import svg2png

from quabbot.user_data import get_user_file

svg_path = path.join(path.dirname(__file__), "resources/quib.svg")
with open(svg_path) as svg_file:
    svg_code = svg_file.read()


def generate_quib(user):
    hue = random.random()
    lightness = 0.5 + (random.random() / 2)
    saturation = 0.8
    red, green, blue = colorsys.hls_to_rgb(hue, lightness, saturation)
    hex_colour = "{0:02x}{1:02x}{2:02x}".format(
        round(red * 255), round(green * 255), round(blue * 255)
    )

    svg2png(
        bytestring=svg_code.replace("99ffa1", hex_colour),
        write_to=get_user_file(user, "quib.png"),
    )
