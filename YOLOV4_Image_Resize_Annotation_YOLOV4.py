import os
import fileinput
import cv2
import shutil
from shutil import copyfile

# Get the current working directory
dire = os.path.abspath(os.getcwd())

try:
    os.mkdir(dire+'\\New_Annotations_Images_Dataset')
except:
    pass
try:
    os.mkdir(dire+'\\Old_Annotations_Images_Dataset')
except:
    pass

all_files = os.listdir()

# Image Size

width = 960
height = 540
with open('large_annotations.txt','w') as prob:
    
    for filename in all_files[:-1]:

        if filename.endswith(".txt"):

            with open(filename, 'r+') as fd:
                
                lines = fd.readlines()
                contents = [x.strip().split(" ") for x in lines] 
            
                #tmp = (label, x, y, width, height)
            
                #print(contents)
                with open(dire+'\\New_Annotations_Images_Dataset\\'+filename,'w') as lb:
                    for content in contents:
                        # print(filename," ",content)
                        w1=960
                        h1=540
                        size=(w1,h1)

                        classes = int(content[0])-1
                        dw = 1./size[0]
                        dh = 1./size[1]
                        '''
                        x = (box[0] + box[1])/2.0
                        y = (box[2] + box[3])/2.0
                        w = box[1] - box[0]
                        h = box[3] - box[2]'''
                        x = int(content[1])*dw
                        y = int(content[2])*dh
                        w = int(content[3])*dw
                        h = int(content[4])*dh
                        # print(classes," ",x," ",y," ",w," ",h)
                    
                        lb.write(str(classes))
                        lb.write(" ")
                        lb.write(str(x))
                        lb.write(" ")
                        lb.write(str(y))
                        lb.write(" ")
                        lb.write(str(w))
                        lb.write(" ")
                        lb.write(str(h))
                        lb.write("\n")
            shutil.move(dire+'\\'+ filename,dire+'\\Old_Annotations_Images_Dataset\\'+filename)
                
            if ((x>=1) or (y>=1) or (w>=1) or (h>=1)):
                prob.write(filename)



        elif filename.endswith(".png"):
            img = cv2.imread(dire + '\\' + filename, cv2.IMREAD_UNCHANGED)
    
            print('Original Dimensions : ',img.shape)
        
            dim = (width, height)
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            print('Resized Dimensions : ',resized.shape)
            cv2.imwrite(dire+'\\New_Annotations_Images_Dataset\\'+filename,resized)
            shutil.move(dire + '\\' + filename, dire + '\\Old_Annotations_Images_Dataset\\' + filename)


    



        
        
        
