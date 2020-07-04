### face-eye detection/Haar-Cascades
OpenCV already contains many pre-trained classifiers for face, eyes, smile etc.

>you can find those XML files [here](https://github.com/opencv/opencv/tree/master/data/haarcascades)

__________________________________________________________________________________________________________________________________________________________
Basics:

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. For this, haar features shown in below image are used. They are just like our convolutional kernel. Each feature is a single value obtained by subtracting sum of pixels under white rectangle from sum of pixels under black rectangle.
![](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/h1.jpg)



>more [details](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

>results:

![face](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/result.png)
___________________________________________________________________________________________________________________________________________________________
![faces](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/result2.png)
