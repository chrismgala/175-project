# TODO build malmo obstacle
# TODO have multiple items, agent walk through, capture screenshot at right times
# TODO create variety of environments for template matching

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import numpy as np
import cv2

max_accuracy = 0
max_accuracy_idx = 0
templates = []
results = {}

image = cv2.imread('./data/train/apple.png')
image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

templates.append(('apple', cv2.imread('./data/templates/apple.png')))
templates.append(('arrow', cv2.imread('./data/templates/arrow.png')))
templates.append(('bed', cv2.imread('./data/templates/bed.png')))
templates.append(('beef', cv2.imread('./data/templates/beef.png')))
templates.append(('bowl', cv2.imread('./data/templates/bowl.png')))
templates.append(('bread', cv2.imread('./data/templates/bread.png')))
templates.append(('book', cv2.imread('./data/templates/book.png')))
templates.append(('bone', cv2.imread('./data/templates/bone.png')))
templates.append(('fish', cv2.imread('./data/templates/fish.png')))
templates.append(('melon', cv2.imread('./data/templates/melon.png')))
templates.append(('potion', cv2.imread('./data/templates/potion.png')))
templates.append(('wooden_sword', cv2.imread('./data/templates/wooden_sword.png')))

for t in range(len(templates)):
    template = templates[t][1]

    # Resize template
    template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)

    # Convert to grayscale
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Find template
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    results[t] = {}
    results[t]['name'] = templates[t][0]
    results[t]['min_val'] = min_val
    results[t]['max_val'] = max_val
    results[t]['min_loc'] = min_loc
    results[t]['max_loc'] = max_loc
    results[t]['templateGray'] = templateGray

for k, v in results.items():
    if results[k]['max_val'] > max_accuracy:
        max_accuracy = results[k]['max_val']
        max_accuracy_idx = k

print max_accuracy, results[max_accuracy_idx]['name']

top_left = results[max_accuracy_idx]['max_loc']
h, w = results[max_accuracy_idx]['templateGray'].shape
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(image, top_left, bottom_right,(0,0,255),4)

# Show result
cv2.imshow("Result", image)

cv2.moveWindow("Result", 150, 50);

cv2.waitKey(3000)
