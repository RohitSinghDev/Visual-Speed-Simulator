
# Visual Speed Simulator

A Model which continuously captures images/frames from camera, recognises the traffic signs and changes the speed of the vehicle accordingly.

## Working of model:

1. The speed simulator uses the available camera and takes frames after every 5 seconds.
2. The model tries to recognise if there is any traffic sign present in the image.
3. If the model detects a traffic/road sign, it accordingly suggests the changes to be made to the speed of the vehicle.



## Components
1. The external camera is used with the help of python library Opencv
2. Machine learning model which predicts the traffic/road sign present in the image.

### Dataset for the ML model:
- The machine learning model was trained with images of 4 different traffic/road signs
        
        1. red traffic sign
        2. green traffic sign
        3. "slow" road sign
        4. "stop" road sign
![dataset](https://github.com/RohitSinghDev/Visual-Speed-Simulator/blob/main/datasets1.png)
- For each of these classes, 200 images were used of which 80% were traing Dataset and 20% testing Dataset.

## Libraries used: 
1. opencv-python == 4.5.4.58
2. PyAutoGUI == 0.9.53
3. scikit-learn == 0.22.2.post1
4. scikit-image == 0.16.2
5. pickle == 4.0
6. matplotlib == 3.2.2
7. numpy
