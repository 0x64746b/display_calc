#!/usr/bin/env python
# coding: utf-8


"""Calculate the size of a display from its resolution and diameter."""


from __future__ import (
    division,
    print_function,
)


import argparse
import math


def calculate_size(resolution, diameter):
    aspect_ratio = resolution[0] / resolution[1]

    b = math.sqrt(diameter ** 2/(aspect_ratio ** 2 + 1))
    a = aspect_ratio * b

    return a, b


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '-r',
        '--resolution',
        metavar=('WIDTH', 'HEIGHT'),
        type=int,
        nargs=2,
    )
    parser.add_argument('-d', '--diameter', type=float)
    args = parser.parse_args()

    display_size = calculate_size(args.resolution, args.diameter)

    print(
        'Display size: {:.2f}" x {:.2f}"'.format(
            display_size[0],
            display_size[1]
        )
    )
