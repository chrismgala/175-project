 ---
layout: default
title:  Proposal
---

## Appointment with Professor Singh
Date: April 27, 2017
Time: 2:00pm

## Summary of the Project
We are planning to use Computer Vision to construct a plugin that will take in objects from the Minecraft screen, and mark out those objects with labels on screen. The applications of this include autonomous vehicles (cars, drones, planes, boats, etc.), which must know what objects it sees and recognize which of those it must avoid while moving.

## AI/ML Algorithms
Deep learning for images is the main algorithm that will be used.

## Evaluation Plan
### Quantitative Evaluation
Metrics includes the confidence rate with which we can say that an image was recognized correctly. For example, if our program is 90% confident in its prediction of 'cat' for a cat object, then our confidence rate is high enough to say our prediction is correct. Another metric that we can calculate is the fraction of angles that our program gets correct. For example, if our program is able to get 18/20 different camera angles correct, then we can factor that in to how well our program is doing. Whether or not it can recognize an object in blurry conditions (rain / snow) is also something we will consider. Our baseline is being able to recognize the object in straight point-of-view, with nothing else on the screen. We expect our approach to improve the metric by at least 80%. We will evaluate our data based on a collection of Minecraft images and screenshots. This data will be collected by us through various resources including Google Images and our own generated worlds in Minecraft.

### Qualitative Evaluation
Metrics include the ability to recognize the object from multiple angles and with other objects in the view, near it or even partially covering it. For example, could the object be recognized in sunny weather and rainy / snowy weather? The sanity test cases for the program would be verifying that when looking at certain simple trained objects directly, the algorithm should at least recognize the object in some angle if not in most of them. We can output the list of predicted items ordered by level of confidence to visualize the internal algorithm performance. Our moonshot case would be having the algorithm recognize a fairly large set of objects from most angles under sub-optimal viewing conditions.
