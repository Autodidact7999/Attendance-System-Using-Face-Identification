# attendancesystem
# Attendance-System-using-Face-recognition
Library:
cmake
imutils
qrcode
pyzbar
pyqrcode
pyzmq
pandas
opencv-python
opencv-contrib-python
numpy
dlib
pillow
matplotlib
scipy
geopy
geocoder
pypng

This repository contains code for facial recognition using openCV and python with a tkinter gui interface. If you want to test the code then run train.py file

Technology used : -openCV (Opensource Computer Vision) -Python -tkinter GUI interface

Here I am working on Face recognition based Attendance Management System by using OpenCV(Python). One can mark thier attendance by simply facing the camera.


Abstract:
The face is the identity of the person. Every person has different types of faces and this is why now days Face recognition application is a very useful and trending security control framework. Here we have proposed Student attendance System with help of face recognition in this project we have first created the Application based on python using Tkinter for the GUI purpose in that application student has to enter his data. The  face Detection is carried by Viola Jones using Haar Cascade classifier. The median filter applied to remove the noise of color image to a grayscale image. As a training when the faculty click on the take attendance button all the faces detect Using a (LBP) Local Binary Pattern. In order to find the image that matches the input image we have compared two histograms and return the image with the closest histogram via Euclidean distance. Finally, attendance of Student is marked and saved in excel file.




How it works :

When we run train.py a window is opened and ask for Enter Id and Enter Name. After enter name and id then we have to click Take Images button. By clicking Take Images camera of running computer is opened and it start taking image sample of person.This Id and Name is stored in folder StudentDetails and file name is StudentDetails.csv. It takes 60 images as sample and store them in folder TrainingImage.After completion it notify that iamges saved. After taking image sample we have to click Train Image button.Now it take few seconds to train machine for the images that are taken by clicking Take Image button and creates a Trainner.yml file and store in TrainingImageLabel folder. Now all initial setups are done. By clicking Track Image button camera of running machine is opened again. If face is recognised by system then Id and Name of person is shown on Image. Press Q(or q) for quit this window.After quitting it attendance of person will be stored in Attendance folder as csv file with name, id, date and time and it is also available in window.

PROJECT BY
HARSH NAIK
