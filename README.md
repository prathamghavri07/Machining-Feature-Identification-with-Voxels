## Machinabe Feature Recognizer
Developed a 3 D convolutional neural network (CNN)  model to identify 24 unique machinable features ,it learns the distribution of complex machining feature shapes across a large 3D model data set and discovers distinguishing features that help in recognition process automatically.The dataset is a parametrically created dataset of 3 D CAD models with labelled machining features

## Dataset
Credits
Zhang, Z., Jaiswal, P., & Rai, R. (2018). FeatureNet: Machining feature recognition based on 3D Convolution Neural Network. Computer-Aided Design, 101, 12-22.

The Dataset has 24000 models belonging to 24 classes ,you can access the https://github.com/madlabub/Machining-feature-dataset
![image](https://github.com/prathamghavri07/Machining-Feature-Identification-with-Voxels/assets/166663640/3ba29a2e-d395-4939-ab54-fd6d0a3aadb6)

## Data Pre-processing
The file format of the dataset is in the form of STL , so we had to convert the goven files into a Voxel format(Scripts to convert file in folder name :Binvox)

A Binvox file in raw format looks like this 
 #binvox 1
    dim 256 256 256
   translate 0 0 0
   scale 10
   data
   b'\x01\xff\x01\xff\x01\xff\x01\xff\x01\xff\x01\xff\x01\xff\x01\xff\x01\xff\x01
![image](https://github.com/user-attachments/assets/43468c90-4907-4bb1-9ba7-1c5a3124f08b)

We have 24,000 models so we have created a 

## Recognizer

A Deep 3D convolutional neural network to be our recognizer. The input of recognizer is the model with only single feature. And the output is the class input feature belonging to.

## Axis of attack
We Determined the axis of attack by figuring out the 0s in the matrix and using the same axis x/y/z axis as axis of attack
We used the COM of the 0s coordinates to find the point of attack and the depth off the attack correspondingly.  
![image](https://github.com/user-attachments/assets/83c02d94-6806-494b-b107-266387096431)

## Result
1. Confusion Matrix
   ![image](https://github.com/user-attachments/assets/b8964dd5-424a-4180-9fb3-7552223ed5a5)

2. Grad Cam
  ![image](https://github.com/user-attachments/assets/43173b1a-c726-4b9c-b7ba-d5aecba492ca)
  ![image](https://github.com/user-attachments/assets/a4192776-59fd-4f1e-9233-b919f0fa72e5)

## Credits
Zhang, Z., Jaiswal, P., & Rai, R. (2018). FeatureNet: Machining feature recognition based on 3D Convolution Neural Network. Computer-Aided Design, 101, 12-22.


