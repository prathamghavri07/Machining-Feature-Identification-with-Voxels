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
line 1 dims, 2 is this and 3 rd is that 
img
.img of 3d reprentation of a rectangular through pocket

files and how create batches for that

## Recognizer

A Deep 3D convolutional neural network to be our recognizer. The input of recognizer is the model with only single feature. And the output is the class input feature belonging to.

## Axis of attack
1.

## Result
1.Accuracy , f1 score
2. Confusion Matrix
3.Grad Cam

## Credits
Zhang, Z., Jaiswal, P., & Rai, R. (2018). FeatureNet: Machining feature recognition based on 3D Convolution Neural Network. Computer-Aided Design, 101, 12-22.


