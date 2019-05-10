#Simple program take a user input in a form of a txt file and check which word in the file has been used the most
#use intro.txt file as a sample text file. Make sure to keep it in a same folder as the python file....

fupload = input("Enter your file name: ") #enter the file name
fhandle = open(fupload) #open the contents of the file

count = dict() #initializing an empty dictionary
for lines in fhandle :
    words = lines.split() #splitting the contents of the file in a key value pair
    for word in words :
        count[word] = count.get(word, 0) + 1
        
mostUsedWord = None
wordCount = None
for key, value in count.items() : #key and value are used as a double interation variables for count.items()
    if mostUsedWord is None or value > wordCount :
        mostUsedWord = key
        wordCount = value
print("The most used word is", mostUsedWord, "and it appeared", wordCount, "times in the text file"  )




