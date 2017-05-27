import label_image as lI

top_k, label_lines, predictions = lI.classify()
for node_id in top_k:
    human_string = label_lines[node_id]
    score = predictions[0][node_id]
    print('%s (score = %.5f)' % (human_string, score))

