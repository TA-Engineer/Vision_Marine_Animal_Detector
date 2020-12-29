function img = load_image(num)
% num is the num of image with 

%prefix = 'C:\Users\tua_f\Documents\2020_Fall_Term1\AER1515 - Perception in Robotics\Project\Images\';
%suffix = '.png';
%path = [prefix,num2str(num),suffix];
path = num
img = imread(path);