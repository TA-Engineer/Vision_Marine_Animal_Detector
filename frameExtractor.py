import os
import subprocess
import argparse
import pathlib
import ipdb
import cv2

image_types = ['.png', '.jpg', '.jpeg']
video_types = ['.avi', '.mp4']

def extractFrames():
    main_dir = r"C:\\Users\\tua_f\\Desktop\\New folder\\dataset"
    output_dir =  ""
    
    sub_main_dirs = []
    for dirs,sub_dir,files in os.walk(main_dir):
        sub_main_dirs.append(dirs)
    #print(sub_main_dir)

    #print(list(os.walk(main_dir)))

    for sub_main_dir in sub_main_dirs[1:]:
        for dirs,sub_dir,files in os.walk(sub_main_dir):
            #print(dirs)
            #print(sub_dir)
            #print(files)
            
            #for dirs,sub_dir,files in os.walk(main_dir)
            for filename in files:
                
                # print(filename)
                if os.path.splitext(filename)[1].lower() in video_types:
                    videoFile = os.path.join(os.path.abspath(dirs), filename)
                # print(videoFile)
                    cam = cv2.VideoCapture(videoFile) 


                    if output_dir != '':
                        fileFolder = output_dir
                    else:
                        fileFolder = os.path.splitext(videoFile)[0]
                    pathlib.Path(os.path.abspath(fileFolder)).mkdir(exist_ok=True, parents=True)
                    #print(fileFolder)
                    fileprefix = os.path.join(fileFolder, os.path.splitext(filename)[0])
                    #print(os.path.splitext(filename))
                    #print(fileprefix)
                    
                    
                    
                    currentframe = 1
                    while(True): 
                        # reading from frame 
                        ret,frame = cam.read() 
                        if ret: 
                            # if video is still left continue creating images 
                            name = fileprefix +'-' +str(currentframe).zfill(4) + '.png'
                            #print (name) 
                            

                            # writing the extracted images 
                            cv2.imwrite(name, frame) 
                            
                            # increasing counter so that it will 
                            # show how many frames are created 
                            currentframe += 1
                        else: 
                            break

                    cam.release() 
                    cv2.destroyAllWindows()
                    print('Complete: ',dirs)
                    #cmd_command = ["ffmpeg", "-i", videoFile, "-vf", "scale=960:540", "-sws_flags", "bicubic", "{}-%04d.png".format(fileprefix), "-hide_banner"]
                    #print(cmd_command)
                    
                    #subprocess.call(cmd_command)

                    # Create a .txt file with the names of all the image files in the respective folder
                    dirContent = os.listdir(fileFolder)
                    for fi in dirContent:
                        if os.path.splitext(fi)[1] in image_types:
                            with open("{}".format(os.path.join(fileFolder, "inputList.txt")), "a") as f:
                                f.write("{}\n".format(fi))


    #if __name__ == "__main__":
        #ap = argparse.ArgumentParser(description = "Takes a set of videos and extracts the frames into separate folders")
        #ap.add_argument("-in", type=str, required = True, help="Path to the main folder containing all the videos")
        #ap.add_argument("-out",  type=str, required = False, help="Path the image output folder. NOTE: if no outputfolder argument is provided, the images will be placed in folders corresponding to their respective video-names; if an argument IS given, all images will be placed in a folder with the provided argument name.", default='')

        #args = vars(ap.parse_args())
        #args ={"--inputFolder":r"C:\\Users\\tua_f\Desktop\\New folder\dataset\\crab" ,
        #       "--outputFolder": r"C:\\Users\\tua_f\Desktop\\New folder\Images\\crab"
        #}
extractFrames()
