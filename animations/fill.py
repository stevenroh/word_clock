from .colors import *


def gen_fill_animation(color):
    "Generate the fill animation with specific color"
    fill_animation = []

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )


    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF, OFF],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )

    fill_animation.append(
        [
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
            [color, color, color, color, color, color, color, color, color, color, color],
        ]
    )
    return fill_animation
