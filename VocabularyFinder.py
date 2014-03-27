#There should be a text file called TaggedCaptions.txt in the same folder with this script
#See the comments in "Cleaner.py" with instructions on how to prepare this file.
#There should also be a plain text file that has each vocabulary word that you are
#interested in on a separate line. This file should be called TargetVocab.txt.
#This script will go through the compilation of the srt files and locate each occurance
#of each vocabulary item and then create two new files.
#The first is called VocabularyWorksheet.txt and contains extracts from the original texts
#Each extract is a blank space (where a vocabulary item should go), surrounded
#by some context. At the bottom of the sheet is a list of all of the vocabulary
#that is needed to fill out the worksheet. The second file is the answer key.
#Created by Arthur Wendorf on 3/26/2014
#Last updated by Arthur on 3/27/2014
#This script was created in Windows 7 using Python 3.3.3
#To run, make sure TaggedCaptions.txt and TargetVocabulary are prepared and in the same folder
#with this script open command prompt, navigate to folder that contains this script
#and use: python VocabularyFinder.py

words = {}
real = {}
pos = {}
options = {}
tracker = 0
oTracker = 0

nFile = open("VocabWorksheet.txt", 'w')
aFile = open("VocabWorksheetAnswers.txt", 'w')

with open("TaggedCaptions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        content = line.split("\t")
        if len(content) > 2:
            words[tracker] = content[2]
            pos[tracker] = content[1]
            real[tracker] = content[0]
            tracker += 1

with open("TargetVocab.txt", 'r') as g:
    for stuff in g:
        stuff = stuff.strip()
        key = 0
        for item in words:
            if stuff == words[item]:
                do = -15
                while do < 0:
                    nFile.write(real[key+do]+" ")
                    aFile.write(real[key+do]+" ")
                    do += 1
                nFile.write("__________ " )
                aFile.write(real[key+do]+" ")
                options[oTracker] = words[key+do]
                oTracker+=1
                do += 1
                while do < 15:
                    nFile.write(real[key+do]+" ")
                    aFile.write(real[key+do]+" ")
                    do += 1
                nFile.write("\n")
                aFile.write("\n")
            key+=1
for bling in options:
    nFile.write(options[bling]+"\n")
