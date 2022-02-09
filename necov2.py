#!/usr/bin/python

from random import randint
import cv2, sys

# TODO!
"""
add all colors mode
"""

print("Necoarc generator v0.0.3")
print()
print(" Mode: ")
print(" 1) Random")
print(" 2) Custom")
modch = input("Mode: ")

if modch=="1":
    number = int(input("Number: "))
elif modch=="2":
    number = 1
    boots = int(input("Boots(0-180): "))
    hair = int(input("Hair(0-180): "))
    hair_sub = int(input("Hair sub(0-180): "))
    left_eye = int(input("Left eye(0-180): "))
    right_eye = int(input("Right eye(0-180): "))
    shirt = int(input("Shirt(0-180): "))
    skirt = int(input("Skirt(0-180): "))
else:
    sys.exit(0)

print("Wait...")

for i in range(number):
    newarc = cv2.imread("input/body.png")
    for part in ["boots", "hair", "hair_sub", "left_eye", "right_eye", "shirt", "skirt"]:
        picture = cv2.imread("input/" + part + ".png")
        hsv = cv2.cvtColor(picture, cv2.COLOR_RGB2HSV)
        h = hsv[:,:,0]
        s = hsv[:,:,1]
        v = hsv[:,:,2]
        if modch=="2":
            if part=="boots":
                huechange = boots
            elif part=="hair":
                huechange = hair
            elif part=="hair_sub":
                huechange = hair_sub
            elif part=="left_eye":
                huechange = left_eye
            elif part=="right_eye":
                huechange = right_eye
            elif part=="shirt":
                huechange = shirt
            elif part=="skirt":
                huechange = skirt
        elif modch=="1":
            huechange = randint(0,180)
        hnew = cv2.add(h, huechange)
        hsvnew = cv2.merge([hnew,s,v])
        result = cv2.cvtColor(hsvnew, cv2.COLOR_HSV2RGB)
        newarc = cv2.add(newarc, result)
    cv2.imwrite('output/' + str(i+1) + '.png', newarc)
    print("Neco arc: " + str(i+1) + "/" + str(number))
