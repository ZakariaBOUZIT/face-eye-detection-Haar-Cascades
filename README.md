### face-eye detection/Haar-Cascades
OpenCV already contains many pre-trained classifiers for face, eyes, smile etc.

>you can find those XML files [here](https://github.com/opencv/opencv/tree/master/data/haarcascades)

__________________________________________________________________________________________________________________________________________________________
Basics:

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, “Rapid Object Detection using a Boosted Cascade of Simple Features” in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. For this, haar features shown in below image are used. They are just like our convolutional kernel. Each feature is a single value obtained by subtracting sum of pixels under white rectangle from sum of pixels under black rectangle.

![](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/h1.jpg)

Now all possible sizes and locations of each kernel is used to calculate plenty of features. (Just imagine how much computation it needs? Even a 24x24 window results over 160000 features). For each feature calculation, we need to find sum of pixels under white and black rectangles. To solve this, they introduced the integral images. It simplifies calculation of sum of pixels, how large may be the number of pixels, to an operation involving just four pixels. Nice, isn’t it? It makes things super-fast.

But among all these features we calculated, most of them are irrelevant. For example, consider the image below. Top row shows two good features. The first feature selected seems to focus on the property that the region of the eyes is often darker than the region of the nose and cheeks. The second feature selected relies on the property that the eyes are darker than the bridge of the nose. But the same windows applying on cheeks or any other place is irrelevant. So how do we select the best features out of 160000+ features? It is achieved by Adaboost.

![](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/h2.png)


>more [details](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection)

>results:

![face](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/result.png)
___________________________________________________________________________________________________________________________________________________________
![faces](https://github.com/zackq88/face-eye-detection-Haar-Cascades/blob/master/result2.png)
