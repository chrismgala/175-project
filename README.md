# Classyfy
This is our implementation of minecraft item image classification. We believe that our implementation can become an intelligent agent that assists players in their decisions to create specific recipes based on the items they have available. 
In real life this could be expanded to helping people understand what recipes they can make with the items they have. 

# Installation Steps
1. Download Malmo
    Go to your home directory in terminal (cd)
    Get the latest version of malmo for your system from - https://github.com/Microsoft/malmo/releases
      e.g. for mac malmo 0.21 --> wget https://github.com/Microsoft/malmo/releases/download/0.21.0/Malmo-0.21.0-Mac-64bit.zip
    unzip Malmo-*
    cd ~/Malmo
2. Create a virtual env.
    virtualenv -p /usr/bin/python2.7 malmo
3. Activate your virtual env.  
    source malmo/bin/activate
4. Get tensorflow inside your env.
    pip install --upgrade tensorflow   --> More info and error resolution can be found here https://www.tensorflow.org/install/
5. Train the classifier
    Switch into ~/malmo/Python_Examples/tf_files/

    python retrain.py \
  --bottleneck_dir=bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=inception \
  --summaries_dir=training_summaries/basic \
  --output_graph=retrained_graph.pb \
  --output_labels=retrained_labels.txt \
  --image_dir=minecraft_photos
    

# Running our mission
1. cd ~/malmo/Python_Examples/
2. python status_tutorial.py

# Video Summary 
<a href="http://www.youtube.com/watch?feature=player_embedded&v=d5n6dN1qB6s
" target="_blank"><img src="http://img.youtube.com/vi/d5n6dN1qB6s/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


# Future Improvements
1. Better data collection with more items and enlarged training data set for each item.
2. Adding object detection to the intelligent agent.
3. Hooking it up to recipe creation and inventory in minecraft. 


# Links Used
1. Tensorflow for Poets - https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#4
2. How does Tensorflow work? - https://www.youtube.com/watch?v=bYeBL92v99Y
3. Object Detection (For Future Enhancement) - https://pjreddie.com/darknet/yolo/
