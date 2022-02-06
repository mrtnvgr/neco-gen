from random import randint
import cv2

# TODO!
"""
add all colors mode
add custom colors mode
"""

I = 0

print("Necoarc generator v0.0.1")
print()
number = int(input("Number: "))
print("Wait...")
for i in range(number):
    newarc = cv2.imread("input/body.png")
    for part in ["boots", "hair", "hair_sub", "left_eye", "right_eye", "shirt", "skirt"]:
        cr, cg, cb = (randint(0,255), randint(0,255), randint(0,255))
        picture = cv2.imread("input/" + part + ".png")
        if cr+cg+cb!=0:
            height, width = tuple(picture.shape[1::-1])
            for x in range(width):
                for y in range(height):
                    r, g, b = picture[x, y]
                    if r!=0 and g!=0 and b!=0:
                        picture[x, y] = cr-r, cg-g, cb-b
        newarc = cv2.add(newarc, picture)
    cv2.imwrite('output/' + str(I+1) + '.png', newarc)
    I += 1
    print("Neco arc: " + str(I) + "/" + str(number))
