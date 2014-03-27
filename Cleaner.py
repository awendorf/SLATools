#There should be a subfolder called "Captions" in the same folder with this script
#Each of the files in Captions should be an SRT file saved as a plain text file.
#This script will go through each of the srt files and combine them into a single
#large text file in normal prose format called CleanCaptions.txt.
#CleanCaptions.txt is used several of my other scripts.
#Created by Arthur Wendorf on 3/26/2014
#Last updated by Arthur on 3/27/2014
#This script was created in Windows 7 using Python 3.3.3
#To run, make sure Captions folder is prepared, open command prompt,
#navigate to folder that contains this script and the Captions folder
#and use: python Cleaner.py
#This output file will most likely need to be run through TreeTagger.
#To do this use the command: tag-spanish CleanCaptions.txt > TaggedCaptions.txt
#(if you have not added treetagger to your path then you should first copy
#CleanCaptions.txt to the bin folder in TreeTagger, and then use the command
#in that folder.

import re, os.path

nFile = open("CleanCaptions.txt", 'w')

for filename in os.listdir("Captions"):
    with open("Captions/"+filename) as current_file:
        for line in current_file:
            if not (re.search("\d", line)):
                line = line.strip()
                nFile.write(line+" ")
