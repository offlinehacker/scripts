#!/bin/bash
ffmpeg -f x11grab -r 20 -s 1366x768 -i :0.0 -threads 0 -sameq -f mpeg2video video.mp2
