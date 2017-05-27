---
layout: default
title:  Status
---
# Status


## Project Summary
While the original vision for the project revolved around object detection with precise bounding boxes indicating results, the actual execution was more challenging than we imagined. We experimented with various commonly used object recognition techniques, including HOG feature descriptors and Haar Cascade using OpenCV, but the results were far from satisfactory. We believed that the primary cause of inaccurate results were the insufficient amount of training data. A typical classifier requires thousands of positive and negative images in order to achieve acceptable results. We decided that manually collecting this amount of data and having each image properly annotated for training was not a feasable approach. After more research, we turned our attention to the Inception v3 network built for Image Classification based on TensorFlow. While this not allow us to accurately show the location of a detected object on screen, we will instead output names of objects recognized by our A.I in the Minecraft chatbox.

## Approach
Inception v3, as a neural network model, is made up of layers of nodes stacked on top of each other. However, only the last layer before the final output layer, also called the bottleneck layer, will change for the specific object that we want to classify. Every other layer will contain information that are generally good for classifying most images. Therefore, we left all previous layers in already-trained state to speed up our training process. Since the inception model is already included in the TensorFlow library, we only needed the script to retrain the model for our purposes. The TensorFlow For Poets tutorial (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#4) provides the completed version of this script, obtainable here:

```
https://raw.githubusercontent.com/tensorflow/tensorflow/r1.1/tensorflow/examples/image_retraining/retrain.py
```

With the trainer in hand, we began our data collection process. For each object we wanted to train, we generate the same object in different worlds that guarantee overall different lighting and visibility on the object to diversify training data. We use a simple command

```Python
call(["screencapture", "./images/" + "apple" + str(i) + ".png"])
```

to capture a screenshot every second. With this method, we generated roughly 40 images for each object. 
We started the actual training process by running the retrain.py script as follows

```Python
python retrain.py \
  --bottleneck_dir=bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=inception \
  --summaries_dir=training_summaries/basic \
  --output_graph=retrained_graph.pb \
  --output_labels=retrained_labels.txt \
  --image_dir=minecraft_photos
```
