# Classyfy
This is our implementation of minecraft item image classification. We believe that our implementation can become an intelligent agent that assists players in their decisions to create specific recipes based on the items they have available. 
In real life this could be expanded to helping people understand what recipes they can make with the items they have. 

# Installation Steps
1. From your home directory, clone the repository and enter it.

2. Download Malmo
    Go to your cloned directory in terminal and get the latest version of malmo for your system from - 
    https://github.com/Microsoft/malmo/releases
      
      e.g. for mac malmo 0.21 --> wget https://github.com/Microsoft/malmo/releases/download/0.21.0/Malmo-0.21.0-Mac-64bit.zip
      
    unzip Malmo-*
    
    rm Malmo-*.zip
    
    mv Malmo-* MalmoTF
    
    cd ./MalmoTF
    
3. Create a virtual env.
    virtualenv -p /usr/bin/python2.7 malmo
    
3. Activate your virtual env.  
    source malmo/bin/activate
    
4. Get tensorflow inside your env.
    pip install --upgrade tensorflow   --> More info and error resolution can be found here https://www.tensorflow.org/install/
      *NOTE pip doesn't have tensorflow package at time of write so do 
      pip install --upgrade  https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.1.0-py2-none-any.whl 
      with the respective .whl file

5. Get other dependencies
    pip install Pillow

6. Move git files to the right place in your environment.
    Go up to the top level of your git directory. Your path should end in Classyfy/
    mv status_tutorial.py MalmoTF/Python_Examples/
    mv tf_files/ MalmoTF/Python_Examples/
 
6. Train the classifier
    Switch into ~/Classyfy/MalmoTF/Python_Examples/tf_files/

    python retrain.py \\
  --bottleneck_dir=bottlenecks \\
  --how_many_training_steps=500 \\
  --model_dir=inception \\
  --summaries_dir=training_summaries/basic \\
  --output_graph=retrained_graph.pb \\
  --output_labels=retrained_labels.txt \\
  --image_dir=minecraft_photos
    

# Running our mission
1. cd ~/Classyfy/MalmoTF/Minecraft
2. ./launchClient.sh
3. Open a new terminal tab.
4. cd ~/Classyfy/MalmoTF/Python_Examples/
5. python status_tutorial.py

# Video Summary 
Embedding wasn't possible so click on the image below to see the gameplay of our agent. 

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
