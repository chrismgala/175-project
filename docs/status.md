---
layout: default
title:  Status
---
# Status

## Project Summary

While the original vision for the project revolves around object detection with precise bounding boxes indicating results, the actual execution was more challenging than we imagined. We experimented with various commonly used object recognition techniques, including HOG feature descriptors and Haar Cascade using OpenCV, but the results were far from satisfactory. We believed that the primary cause of inaccurate results were the insufficient amount of training data. A typical classifier requires thousands of positive and negative images in order to achieve acceptable results. We decided that manually collecting this amount of data and having each image properly annotated for training was not a feasable approach. After more research, we turned our attention to the Inception v3 network built for image classification based on Tensorflow. While this not allow us to accurately show the location of a detected object on screen, we will instead output names of objects recognized by our A.I in the Minecraft chatbox.

## Approach

