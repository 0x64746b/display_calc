#!/usr/bin/env python
# coding: utf-8


from __future__ import (
    division,
    print_function,
)


import math


def calculate_size(resolution, diameter):
    aspect_ratio = resolution[0] / resolution[1]

    b = math.sqrt(diameter ** 2/(aspect_ratio ** 2 + 1))
    a = aspect_ratio * b

    return a, b


if __name__ == '__main__':
    resolution = (2560, 1600)
    diameter = 10.055

    display_size = calculate_size(resolution, diameter)

    print('Display size: {} x {}'.format(display_size[0], display_size[1]))
