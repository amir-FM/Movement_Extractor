# Movement Extractor

A program that uses the **SVD** algorithm to extract the movement out of a video. The resulting file can be either just the movement or just the background. The output video is in B&W so to make the process faster.

## Description

The program makes a matrix in which every frame is a row. In this configuration **SVD** is applied resulting in a **low_rank** matrix, which is used to create the backgroud or the movement videos.

## Specifications

The input file can be of **any** format, but the output is in **.avi** format.

## Recommandations

The project was built and developed on a machine with *16gb of ram*, it still wasn't enough (using *SWAP memory* aswell). Depending on the video's length and resolution the process can be more or less of a resource hog. The **scale** of the input video can be ajusted directly in in the source file, aswell as a **verbose** mode.

## Instalation

``` sh
git clone [url] [instalation directory]
cd ./[instalation directory]
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 ./main.py
```

To deactivate **venv**
``` sh
deactivate
```
