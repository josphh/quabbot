import colorsys
import random

from cairosvg import svg2png

from quabbot.user_data import get_user_file


def random_hex_colour():
    hue = random.random()
    lightness = 0.5 + (random.random() / 2)
    saturation = 0.8

    red, green, blue = colorsys.hls_to_rgb(hue, lightness, saturation)

    return "{0:02x}{1:02x}{2:02x}".format(
        round(red * 255), round(green * 255), round(blue * 255)
    )


def generate_quib(user):
    stroke_dash_1 = random.randint(30, 80)
    stroke_dash_2 = random.randint(1, 10)

    svg_code = f"""
    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <svg
       width="204.98608mm"
       height="204.98637mm"
       viewBox="0 0 204.98609 204.98637"
       version="1.1"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:svg="http://www.w3.org/2000/svg">
      <g transform="translate(7.6344409,-30.602059)">
        <path
           style="fill:#{random_hex_colour()};fill-opacity:1;stroke:#000000;stroke-width:9.44882;stroke-miterlimit:4;stroke-dasharray:{stroke_dash_1}, {stroke_dash_2};stroke-dashoffset:0;stroke-opacity:1"
           d="m 456.91366,246.66771 c 47.3241,79.01118 -116.00252,107.93406 -104.28006,206.12674 11.72246,98.19267 133.81873,215.9895 60.7291,260.63028 C 340.27307,758.06551 260.99789,653.89465 170.87495,627.10676 80.752014,600.31887 46.480258,797.90937 -22.651456,732.11982 -91.78317,666.33028 -43.031992,547.80428 -28.403677,463.37178 -13.775361,378.93927 -154.98001,254.11809 -89.134648,189.86397 c 65.84536,-64.25411 171.256084,62.20697 266.113478,57.39945 94.85739,-4.80752 232.61073,-79.60689 279.93483,-0.59571 z"
           transform="matrix(0.26458333,0,0,0.26458333,48.703566,13.61495)" />
        <path
           style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:5.49592;stroke-miterlimit:4;stroke-dasharray:{stroke_dash_1}, {stroke_dash_2};stroke-dashoffset:0"
           d="m 246.86787,451.4826 c -2.83676,-6.1976 2.17884,-12.80925 8.14889,-14.43068 8.89292,-2.41526 17.45123,4.38497 19.19437,12.98387 2.2826,11.26014 -6.2971,21.74787 -17.25984,23.57683 -13.4526,2.24435 -25.78797,-8.03676 -27.69401,-21.1982 -2.24815,-15.52382 9.65924,-29.63002 24.89976,-31.61031 17.50221,-2.27416 33.31303,11.19483 35.36646,28.42145 2.31317,19.40568 -12.66227,36.86434 -31.7995,38.99034 -21.2466,2.36033 -40.30399,-14.07417 -42.50215,-35.05882 -2.41285,-23.03406 15.43946,-43.64718 38.21747,-45.91715 24.77498,-2.46899 46.90581,16.76486 49.24722,41.28914 1.97036,20.63771 -10.2254,40.50474 -29.17739,48.6637"
           transform="matrix(0.45241435,0,0,0.45736417,-44.710639,-94.342072)" />
        <path
           style="fill:none;fill-rule:evenodd;stroke:#000000;stroke-width:5.49592;stroke-miterlimit:4;stroke-dasharray:{stroke_dash_1}, {stroke_dash_2};stroke-dashoffset:0"
           d="m 328.97732,423.89457 c -3.34894,-4.084 -0.89574,-10.0282 3.25764,-12.42157 6.18684,-3.56512 13.94196,-0.15892 16.94542,5.94027 3.93298,7.9868 -0.42576,17.53891 -8.27926,21.07326 -9.63719,4.33708 -20.90959,-0.93184 -24.9357,-10.41764 -4.74876,-11.18843 1.38922,-24.10874 12.41825,-28.60087 12.66573,-5.15876 27.17156,1.81288 32.11053,14.31568 5.5637,14.08432 -2.21147,30.12226 -16.13159,35.49273 -15.45444,5.96241 -32.97832,-2.59048 -38.76752,-17.88065 -6.35458,-16.78344 2.95362,-35.75291 19.5734,-41.9499 18.07685,-6.74029 38.45624,3.30354 45.05146,21.21772 5.55001,15.07517 0.33307,32.36906 -12.25742,42.22353"
           transform="matrix(0.45241435,0,0,0.45736417,-38.075525,-73.091662)" />
        <path
           style="fill:none;stroke:#000000;stroke-width:2.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-dasharray:{stroke_dash_1}, {stroke_dash_2};stroke-dashoffset:0;stroke-opacity:1"
           d="m 61.849359,151.47986 c 47.169381,-2.04948 58.310201,6.79938 58.310201,6.79938" />
      </g>
    </svg>
    """

    svg2png(
        bytestring=svg_code.strip(),
        write_to=get_user_file(user, "quib.png"),
    )
