 ---
layout: default
title:  Final Report
---

## Video
[![placeholder](https://img.youtube.com/vi/oYg_o5zpFXQ&feature=youtu.be/0.jpg)]
(https://youtu.be/oYg_o5zpFXQ)


## Project Summary
We started out with the goal of being able to implement Object Detection. This resulted in us being able to detect images close to the Agent but did not work out very well for different variations. This includes the object being a different size / distance from the Agent. As a result, we pivoted to Classification to better predict what an object is.

After changing to Classification, we focused on being able to build classifiers using a small amount of data. We wanted to get things up and running with a stripped down version of our main goal which is to classify multiple objects on the screen at once as the Agent moves through a World. This was successful in that we were able to get our classifier to recognize a couple of built-in items in Minecraft. The classifier runs in the background of Project Malmo and outputs the names of objects detected on screen in the chatbox.

Since then we have expanded to support classification of multiple objects on the screen with similar / slightly better accuracy. We increased our number of classes to more than five and can classify two to three items on the screen at the same time. We need ML / AI for
this project because in order to recognize / classify these objects instantaneously, we need a classifier that is trained to continuously recognize them. It is non-trivial especially becausee of the variety of conditions and environments (e.g. clear vs. rain / snow) with differing layouts, backgrounds, and angles that the object could reside in.

## Approaches
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

```
python retrain.py \
  --bottleneck_dir=bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=inception \
  --summaries_dir=training_summaries/basic \
  --output_graph=retrained_graph.pb \
  --output_labels=retrained_labels.txt \
  --image_dir=minecraft_photos
```

The script will proceed to generate bottleneck files, as mentioned above, and begin the training of the final layer. To do so, the trainer runs repeated steps, each randomly chooses 10 images from the training set and retrieve the respective bottlenecks to form a prediction on the final layer. The results will be compared against the true labels of the images. The differences used to update the weight values of the final layer using stochastic gradient descent. Note that we limited the amount of training steps to 500 while a general image classification training on this model will usually run 4000 steps. This is due to the limited size of our training set compared to the amount of images used during normal practices. The recommended number of images for a relatively accurate classifier is 200 or more. Our collection of 40 images barely meets the minimum requirement for training a passable A.I. Since increasing training steps will only be beneficial given sufficient amount of training data, we needn't perform the default of 4000 training steps.

## Evaluation

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/test/wheat_eval.png" width="1000" height="700"/>

#### Results
iron shovel (score = 0.9021)
wheat (score = 0.885)

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/test/bow_eval.png" width="1000" height="700"/>

#### Results
bow (score = 0.8214)
wooden axe (score = 0.683)

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/test/iron_shovel_eval.png" width="1000" height="700"/>

#### Results
iron shovel (score = 0.842)
wheat (score = 0.634)

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/test/wooden_axe_eval.png" width="1000" height="700"/>

#### Results
iron shovel (score = 0.7784)
wooden axe (score = 0.7762)


### Quantitative Evaluation
For our quantitative evaluation, we used TensorFlow's built in mathematical calculations to produce a confidence indicating whether or not the classification was successful for each image. For example, in the 7 images above, we have output below each image for the two different classes we trained our classifier on, 'apples' and 'coal'. For those two classes, we have results from TensorFlow's calculations which uses functions like the softmax function used in neural networks. This function is used in the final layer of a neural net classifier and computes probabilities which allow a confidence to be returned, leading to the classification of the object in the images above as 'apples' since the confidence returned in each run is above 0.80. All seven of the images above passed as each run resulted in the 'apples' classification which is 100% accuracy.  However, this was on images very similar to our training data. In some other scenarios, our classifier doesn't give a clear confidence reading on which item was in the image. As a result, we look forward to increasing our training data set from a mere 20 per item to 100 per item and increase the number of items.  We hope to achieve better accuracy this way. Over several different runs of real time gameplay our agent had an accuracy of approximately 70% - 75%.

This is only using one Minecraft item. So for our final iteration, we would like to test it on many more of Minecraft's 188 built-in items. We would also add more classes so it wouldn't be a simple either-or prediction.

Further information and visualization of the softmax equation used in TensorFlow
(taken from [TensorFlow Documentation](https://www.tensorflow.org/get_started/mnist/beginners#softmax_regressions)):

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/evaluation/equation1.png" width="600" height="400"/>

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/evaluation/equation2.png" width="600" height="300"/>

<img src="https://raw.githubusercontent.com/chrismgala/Classyfy/master/data/evaluation/equation3.png" width="600" height="300"/>

### Qualitative Evaluation
For our qualitative evaluation, we wanted to make sure that we had generated a diverse set of environments for the objects we wanted to recognize. For example, in the 7 images above, we have an Apple shown in rainy, snowy, and clear weather. We also have multiple different backgrounds, including grass, trees, flowers, mushrooms, forests, and boxes. In the clear weather environments, the screen is much brighter as opposed to the screen in rainy or snowy weather. These variations helped us qualitatively evaluate our project. For each of the variations above, our classifier was able to confidently predict the correct class, 'apples'. For future iterations, we would like to add more angles, as we only tested on straight point-of-view angles in the above images.

## References
[Project Malmo](https://github.com/Microsoft/malmo) as our playground

[TensorFlow](https://www.tensorflow.org) as our Computer Vision API for training a classifier
