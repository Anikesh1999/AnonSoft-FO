#! python3

import os , Shultil
import shutil

#  \................... Intro  ...................../ 

print ("\n\n")
print (r" /\/\//\/\/\//\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")
print (r" \/                                                                                 /\ ")
print (r" \/                                                                                 /\ ")
print (r" \/                             Design By   : Anikesh Patel                         /\ ")
print (r" \/                             Complete in : 15/08/2017                            /\ ")
print (r" \/                                                                                 /\ ")
print (r" \/                                    Created By - AnonSoft                        /\ ")
print (r" \/                                                       The Mind In Your Hand     /\ ")
print (r" \/                                                                                 /\ ")
print (r" /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ ")



#\.................  Design Start Here ................./



print ("\n Type or Paste Folder Path For Manage :  ")
folderPath = input("\n \t > ")
data= {}
data['Audio Files'] = Shultil.audioScan(folderPath)
data['Video Files'] = Shultil.videoScan(folderPath)
data['Image Files'] = Shultil.imageScan(folderPath)
data['Doc Files'] = Shultil.docScan(folderPath)

for fileType in data.keys():
    if data[fileType]:
        print ("\n We Found "+ str(len(data[fileType])) + " " + str(fileType))
        print ("\n Do You Want To Move Your " + str(fileType) + " : Y/N  \n")
        ans = input ("\n \t > ")
        if ans == 'Y' or ans == 'y' :
            print ("\n Type Which Folder You Want TO Move Your "+str(fileType)+" :  \n")
            while True:
                folderName = input("\n \t > ")
                newFolderPath = os.path.join(folderPath,folderName)
                if os.path.isdir(newFolderPath):
                    print ("\n  This Folder Already Exist Type Other Different Name : ")
                    continue
                else:
                    os.makedirs(newFolderPath)
                    break
            for file in data[fileType]: 
                currentPath = os.path.join(folderPath,file)
                lastPath = os.path.join(newFolderPath,file)
                shutil.move(currentPath,lastPath)
        else:
                print("\n  Okey We Wont Move Your Files :")
    else:
        print("\n\n  Sorry There Is No  >>>  " + str (fileType))


print ("\n\n \t >>>  ThankYou Very Much <<<")
