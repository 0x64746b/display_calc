USAGE
=====

```
$ python display_size.py --help
usage: display_size.py [-h] [-r WIDTH HEIGHT] [-d DIAMETER]

Calculate the size of a display from its resolution and diameter.

optional arguments:
  -h, --help            show this help message and exit
  -r WIDTH HEIGHT, --resolution WIDTH HEIGHT
  -d DIAMETER, --diameter DIAMETER
```

EXAMPLE
=======

```
$ # nexus 10
$ python display_size.py -r 2560 1600 -d 10.1
Display size: 21.75 x 13.60 cm
```
