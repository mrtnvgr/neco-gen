#!/usr/bin/python

from random import randint
import cv2, sys

# TODO!
"""
add all colors mode
"""

parts_list = ["boots", "hair", "hair_sub", "left_eye", "right_eye", "shirt", "skirt"]

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
    parts_custom_values = []
    for i in parts_list:
        part_value = int(input(i + "(0-180): "))
        parts_custom_values.append(part_value)
else:
    sys.exit(0)

print("Wait...")

for i in range(number):
    newarc = cv2.imread("input/body.png")
    for part in range(len(parts_list)):
        picture = cv2.imread("input/" + parts_list[part] + ".png")
        hsv = cv2.cvtColor(picture, cv2.COLOR_RGB2HSV)
        h = hsv[:,:,0]
        s = hsv[:,:,1]
        v = hsv[:,:,2]
        if modch=="2":
            huechange = parts_custom_values[part]
        elif modch=="1":
            huechange = randint(0,180)
        hnew = cv2.add(h, huechange)
        hsvnew = cv2.merge([hnew,s,v])
        result = cv2.cvtColor(hsvnew, cv2.COLOR_HSV2RGB)
        newarc = cv2.add(newarc, result)
    cv2.imwrite('output/' + str(i+1) + '.png', newarc)
    print("Neco arc: " + str(i+1) + "/" + str(number))
