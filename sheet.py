#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gimpfu import *

def to_sheet(image, drawable):
    dx = 0
    dy = 0

    frame_width, frame_height = image.width, image.height
    number_of_layers = len(image.layers)
    mul = 0
    i=0
    while mul<=number_of_layers:
        mul = i*i
        i += 1
    i -= 1;
    image.undo_group_start()
    col = 1;
    # Move layers in sheet
    for layer in image.layers:
        layer.resize(frame_width, frame_height, 0, 0)
        layer.set_offsets(dx, dy)
        #columns
        if col < i:
            dx += frame_width
        else:
            col = 0
            dx = 0
            dy += frame_height
        col+=1


    image.resize(frame_width * i, frame_height * i, 0, 0)
    image.undo_group_end()

if __name__ == '__main__':
    register(
            "redimensionar_imagen",
            "Redimensionar imagen",
            "Redimensionar imagen",
            "Hugo Ruscitti",
            "Hugo Ruscitti",
            "2010",
            "<Image>/Python-Fu/SpriteTool/Create sheet",
            "RGB*, GRAY*",
            [],
            [],
            to_sheet)
    main()
