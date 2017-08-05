#! python3

# Creator  ANikesh PAtel
# Date :  4/08/2017

import os

def audioScan(folderPath):
    audioFiles = []
    audioExtensions = ['mp3','m4a','ac3','aac']
    allFiles = os.listdir(folderPath)
    for audioExtension in audioExtensions:
        for fileName in allFiles:
            if audioExtension in fileName:
                audioFiles.append(fileName)
    return audioFiles


def videoScan(folderPath):
    videoFiles = []
    videoExtensions = ['mp4','mkv','flv','3gp']
    allFiles = os.listdir(folderPath)
    for videoExtension in videoExtensions:
        for fileName in allFiles:
            if videoExtension in fileName:
                videoFiles.append(fileName)
    return videoFiles


def imageScan(folderPath):
    imageFiles = []
    imageExtensions = ['jpg','png','gif']
    allFiles = os.listdir(folderPath)
    for imageExtension in imageExtensions:
        for fileName in allFiles:
            if imageExtension in fileName:
                imageFiles.append(fileName)
    return imageFiles


def docScan(folderPath):
    docFiles = []
    docExtensions = ['pdf','doc','ppt','exel']
    allFiles = os.listdir(folderPath)
    for docExtension in docExtensions:
        for fileName in allFiles:
            if docExtension in fileName:
                docFiles.append(fileName)
    return docFiles

