#There should be a text file called TaggedCaptions.txt in the same folder with this script
#See the comments in "Cleaner.py" with instructions on how to prepare this file.
#You should adjust the content of this script as indicated below
#This script will go through the compilation of the srt files and locate each occurance
#of each grammar item and then create two new files.
#The first is called GrammarWorksheet.txt and contains extracts from the original texts
#Each extract is a blank space (where a vocabulary item should go), followed by a verb
#in the infinitive form, surrounded by some context. The second file is the answer key.
#Created by Arthur Wendorf on 3/26/2014
#Last updated by Arthur on 3/27/2014
#This script was created in Windows 7 using Python 3.3.3
#To run, make sure TaggedCaptions.txt is prepared and in the same folder
#with this script, update the content of the script as desired
#open command prompt, navigate to folder that contains this script
#and use: python VerbFinder.py
#Currently this script only searches for verbs in particular conjugations

words = {}
real = {}
pos = {}
tracker = 0

nFile = open("GrammarWorksheet.txt", 'w')
aFile = open("GrammarWorksheetAnswers.txt", 'w')

stopwords = ["ré", "rás", "rá", "remos", "rán"] #update this with the verb endings that you are looking for
#currently it is set up to look for all occurences of the spanish synthetic future

surplus = 1 #update this to show how many letters should be taken off of the end
#of the infinitive form before the ending is added

key = 0

with open("TaggedCaptions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        content = line.split("\t")
        if len(content) > 2:
            words[tracker] = content[2]
            pos[tracker] = content[1]
            real[tracker] = content[0]
            tracker += 1

with open("TaggedCaptions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        content = line.split("\t")
        if len(content) > 2:
            if content[1][0] == "V":
                if ((content[0][(len(content[2])-surplus):]) in stopwords) and key > 15 and key < tracker - 15:
                    do = -15
                    while do < 0:
                        nFile.write(real[key+do]+" ")
                        aFile.write(real[key+do]+" ")
                        do += 1
                    nFile.write("__________ ("+words[key]+") ")
                    aFile.write("("+real[key]+") ")
                    do += 1
                    while do < 15:
                        nFile.write(real[key+do]+" ")
                        aFile.write(real[key+do]+" ")
                        do += 1
                    nFile.write("\n")
                    aFile.write("\n")
            key+=1
            
