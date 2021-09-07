# Vision_Marine_animal_detector

This is a repository for my Underwater Animal Detection research project.

This is a novel implementation from my research on underwater marine animal detector project that utilizes YOLOV4 implementation in Python along with MATLAB for ditial image processing using Fusion Algorithm.




From several underwater Brackish water dataset individual frames (approc 14,000) were extracted using OPENCV library. These frames were then processed using MATLAB for colour correction and image enhancement as underwater image have green tint due to refraction of light.

The processed images were then sorted to create a balanced dataset eith equal images in each class. These images were then split into 90-10 split which were then used to train a YOLOV4 model.


**FINDINGS: MAP AVERAGE PRECISION of 92%
