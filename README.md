# Home-Surveillance-Using-Realtime-Attendance
The project is aimed at solving that problem making use of latest tech for machine learning, face recognition, notification alert system and database management.
Parameters Involved -Any house will have the following aspects defined:
i) State of House – Secure or Unsecured
ii) Owners of House – Maximum 5 (can be increased or decreased)
iii) Guests

Scope -
At the time of system setup, we shall register the owners of the house.Their faces will be recorded to enable face recognition.This data of the house owners along with their face data is added into a database.Two cameras would be fixed on either side of the house’s entrance to
capture the faces of people entering or leaving the perimeter. When a house owner is recognized entering or leaving the house, the database is updated and the state of house varies.So,every time a particular owner enters the house, he/she is marked as ‘present’ in the database and when he/she leaves, is marked ‘absent’. The state of house is said to be secure if at least one of the registered house owners is inside the house.It is unsecure if all of the owners step out of the house. 

Primary Research on Tech Stack To Be Used -
We have started with face detection. Preliminary research on the internet led us to two OpenCV modules, namely Haar Cascacades and YOLO for face recognition. We also had two programming language options, namely Python and C++.As the first steps we have developed using Haar Cascades module in C++ and Python. Upon comparison between the two projects, it has been observed that using OpenCV with Python is more efficient and powerful. Then we have developed using different modules in Python and upon another iteration of comparison, we noticed Haar Cascades module was more performant. Hence, after multiple iterations,comparisons and tests we have decided to build our final project in Python using OpenCV module.

Tech Stack -
The developmental tools used in this project are OpenCV, NumPy,Notify-Run, SQ Lite, Pillow, Haar Cascades for face detection and Local
Binary Pattern Histogram (LBPH) algorithm for face recognition.

Details of Algorithms and Designs:
After experimenting with several algorithms, we found two algorithms best suited for our use case, namely Haar Cascades for face detection
and LBPH for face recognition.

Haar Cascades -Haar Cascades algorithm is a machine learning based approach in which we use a classifier function which is trained by a large number of photos. Based on this training, the function is used to detect particular objects (faces in our case) in other images. This algorithm has four stages1. Haar Feature Selection
2. Creating Integral Images
3. Adaboost Training
4. Cascading Classifiers
The first stage, Haar Feature Selection, considers adjacent rectangular regions at a specific location, sums up the pixel intensities in each region and calculates the difference between these sums. This helps us to detect features like edge features, line features and four-rectangle features. The purpose of stage 2, creation of integral images, is to enhance the speed of this process.But most of the features we calculate are irrelevant. So, selection or pooling of these features is done by the concept of Adaboost which selects the best features and trains the classifiers that use them. The Cascading classifier consists of a collection of stages where each stage is an ensemble of weak learners, which in turn are simple.

LBPH Algorithm -
For face recognition, we are using the most popular algorithm, LBPH, due to its computational simplicity and discriminative power. It works on LBP operator. The LBP operator is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the
neighborhood of each pixel and considers the result as a binary number.The LBP operator when combined with histogram of oriented gradients
(HOG) descriptor improves the performance considerably on some datasets. They work together and represent the face images with a
simple data vector.The most important property of LBP operator in real-world
applications can be its robustness to monotonic gray-scale changes caused, for example, due to illumination variations. Its computational
simplicity makes it possible to analyze images in real-time setting.

In a nutshell, these are the important results/outcomes of our project -
1. Faces recognized in real-time
2. Database updated when face recognized
3. Mobile notification
4. Python is better for our specific use case
5. Haar Cascades is better than YOLO for our specific use case
