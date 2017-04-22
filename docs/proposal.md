 ---
layout: default
title:  Proposal
---

## Summary of the Project
We are planning to use Computer Vision to construct a plugin that will take in objects from the Minecraft screen, and output accurate captions of what those objects are. The applications of this include autonomous vehicles (cars, drones, planes, boats, etc.), which must know what objects it sees and recognize which of those it must avoid while moving.

## AI/ML Algorithms
Deep learning for images is the main algorithm that will be used.

## Evaluation Plan
### Quantitative Evaluation
Metrics include the ability to recognize the object from multiple angles and with other objects in the view, near it or even partially covering it. For example, could the object be recognized in sunny weather and rainy / snowy weather? Our baseline is being able to recognize the object in straight point-of-view, with nothing else on the screen. We expect our approach to improve the metric by at least 80%. We will evaluate our data based on a collection of Minecraft images and screenshots. This data will be collected by us through various resources including Google Images and our own generated worlds in Minecraft.

### Qualitative Evaluation
