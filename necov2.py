#!/usr/bin/python

from random import randint
import cv2, sys

# TODO!
"""
add all colors mode
add custom colors mode
"""

I = 0

print("Necoarc generator v0.0.2")
print()
print(" Mode: ")
print(" 1) Random")
print(" 2) Custom")
modch = input("Mode: ")

if modch=="1":
    number = int(input("Number: "))
elif modch=="2":
    number = 1
    boots = input("Boots: ")
    hair = input("Hair: ")
    hair_sub = input("Hair sub: ")
    left_eye = input("Left eye: ")
    right_eye = input("Right eye: ")
    shirt = input("Shirt: ")
    skirt = input("Skirt: ")
else:
    sys.exit(0)

print("Wait...")

for i in range(number):
    newarc = cv2.imread("input/body.png")
    for part in ["boots", "hair", "hair_sub", "left_eye", "right_eye", "shirt", "skirt"]:
        if modch=="1":
            cr, cg, cb = (randint(0,255), randint(0,255), randint(0,255))
        elif modch=="2":
            if part=="boots":
                curcolors = boots.split(" ")
            elif part=="hair":
                curcolors = hair.split(" ")
            elif part=="hair_sub":
                curcolors = hair_sub.split(" ")
            elif part=="left_eye":
                curcolors = left_eye.split(" ")
            elif part=="right_eye":
                curcolors = right_eye.split(" ")
            elif part=="shirt":
                curcolors = shirt.split(" ")
            elif part=="skirt":
                curcolors = skirt.split(" ")
            cr = int(curcolors[0])
            cg = int(curcolors[1])
            cb = int(curcolors[2])
        picture = cv2.imread("input/" + part + ".png")
        if cr+cg+cb!=0:
            height, width = tuple(picture.shape[1::-1])
            for x in range(width):
                for y in range(height):
                    r, g, b = picture[x, y]
                    if r!=0 and g!=0 and b!=0:
                        picture[x, y] = r-cr, g-cg, b-cb
        newarc = cv2.add(newarc, picture)
    cv2.imwrite('output/' + str(I+1) + '.png', newarc)
    I += 1
    print("Neco arc: " + str(I) + "/" + str(number))
