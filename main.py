#!/bin/python3

import numpy as np
import sys
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn import decomposition


n = len(sys.argv)

if n != 3:
    print("Usage: python3 {} [INPUT_VIDEO] [OUTPUT_VIDEO]\nApplies SVD on a input video and extracts the movement\n\nWith no input and output videos the program displays the help menu".format(sys.argv[0]))
    exit(0)

video_in = sys.argv[1]
video_out = sys.argv[2]

cap = cv.VideoCapture(video_in)

scale = 100 # ?/100
width = cap.get(3) * (scale / 100)
height = cap.get(4) * (scale / 100)
fps = cap.get(cv.CAP_PROP_FPS)
dims = (int(width), int(height))

print("fps:", fps)
print(dims)

index = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        print("Error receiving frame or finnished")
        break
    else:
        new_size = cv.resize(frame, dims)
        gray = cv.cvtColor(new_size, cv.COLOR_BGR2GRAY)
        vector = np.array(gray).flatten()
        try:
            M = np.vstack([M, vector])
        except:
            print(frame.shape)
            M = vector

    print(index)
    index += 1
    if cv.waitKey(1) == ord('q'):
        break

cap.release()

print(M, M.shape)
frames = len(M)

u, s, v = decomposition.randomized_svd(M, 2)

print(u.shape, s.shape, v.shape)

low_rank = u @ np.diag(s) @ v

print(low_rank.shape)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(video_out, fourcc, fps, dims, isColor=False)


for i in range(0, frames):
    # background extraction
    #frame = np.reshape(M[i, :] - low_rank[i, :], dims[::-1])
    frame = np.reshape(low_rank[i, :], dims[::-1])
    frame8 = cv.convertScaleAbs(frame)

    cv.imshow('gray', frame8)
    if cv.waitKey(1) == ord('q'):
         break

    out.write(frame8)

out.release()
cv.destroyAllWindows()
