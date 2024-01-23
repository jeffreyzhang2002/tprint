#!/usr/bin/env python3

import cv2
import sys

if len(sys.argv) <= 2:
    print(f"Command {sys.argv[0]} <Image> <Width> <Optional Vscale>")
    exit()

scale = float(sys.argv[3]) if len(sys.argv) >= 4 else 0.75

img = cv2.imread(sys.argv[1])

ratio = int(sys.argv[2]) / img.shape[0]

half = cv2.resize(img, (int(img.shape[0] * ratio), int(img.shape[1] * ratio * scale)), interpolation=cv2.INTER_AREA)

for i in range(half.shape[0]):
    for j in range(half.shape[1]):
        b, g, r = half[i,j]
        print(f"\033[48;2;{r};{g};{b}m \033[0m", end="")
    print()
