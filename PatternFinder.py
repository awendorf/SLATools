#There should be a text file called TaggedCaptions.txt in the same folder with this script
#See the comments in "Cleaner.py" with instructions on how to prepare this file.
#You should adjust the content of this script as indicated below
#This script will go through the compilation of the srt files and locate each occurance
#of each pattern and then create two new files.
#The first is called GrammarWorksheet.txt and contains extracts from the original texts
#Each extract is a blank space (where a conjugated verb should go), followed by a verb
#in the infinitive form, surrounded by some context. The second file is the answer key.
#Created by Arthur Wendorf on 3/26/2014
#Last updated by Arthur on 3/27/2014
#This script was created in Windows 7 using Python 3.3.3
#To run, make sure TaggedCaptions.txt is prepared and in the same folder
#with this script, update the content of the script as desired
#open command prompt, navigate to folder that contains this script
#and use: python PatternFinder.py
#Currently this script only searches for patterns that trigger specific verb conjugations

words = {}
real = {}
pos = {}
tracker = 0

nFile = open("SubWorksheet.txt", 'w')
aFile = open("SubWorksheetAnswers.txt", 'w')

stopwords = ["cuando"] #enter all single-word patterns that you are looking for
#The script will extract the very next verb, for example, right now this script
#will search for each occurence of cuando, then it will remove the very next verb
#and put its infinitive form in parentheses for the student to conjugate

stopwords2 = ["sin", "para", "menos", "de", "tal", "caso", "hasta"]
#enter the first word for all two consecutive word patterns.

stop2 = "que"
#enter the second word for all two consecutive word patterns.
#The script will extract the very next verb, for example, right now this script
#will search for each occurence of sin, para, menos, de, tal, caso, and hasta
#that is followed by que, then it will remove the very next verb
#and put its infinitive form in parentheses for the student to conjugate

stopwords3 = ["un", "una", "unos", "unas", "ningún", "ningunos", "ninguna", "ningunas"]
#enter the first word for all two non-consecutive word patterns.

stop3 = "que"
#enter the second word for all two non-consecutive word patterns.
#The script will extract the very next verb, for example, right now this script
#will search for each occurence of un, una, unos, unas, ningún, ningunos, ninguna, and ningunas
#that is followed by another word, which is followed by que
#then it will remove the very next verb
#and put its infinitive form in parentheses for the student to conjugate

key = 0
found = 0

with open("TaggedCaptions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        content = line.split("\t")
        if len(content) > 2:
            words[tracker] = content[2]
            pos[tracker] = content[1]
            real[tracker] = content[0]
            tracker += 1

while key < tracker:
    if key > 15 and key < tracker - 15:
        if (real[key] in stopwords) or (real[key] in stopwords2 and real[key+1] == stop2) or (real[key] in stopwords3 and real[key+2] == stop3):
            found = 1
        elif(found == 1) and pos[key][0] == "V":
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
            found = 0
    key += 1
