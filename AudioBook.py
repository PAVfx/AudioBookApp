from re import M
import pyttsx3 # pyttsx3 free python library for text to speach version 3
import PyPDF2 # pypdf2 free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files

with open('books/TheMindfulAthlete.pdf', 'rb') as book: # booksname.pdf and 'rb' = reading bytes

    full_text = ""

    reader = PyPDF2.PdfReader(book) # lets extract th strings using a reader (PyPDF2) by passing in the book as the content
    audioReader = pyttsx3.init() # initialize object
    audioReader.setProperty("rate", 115) # how fast we want to reader to read (words/min)
    audioReader.setProperty("volume", 0.8) # (name, value): volume from 0 to 1.0
    voices = audioReader.getProperty('voices')
    gender = input(" Type 'M' for Male Narrator or 'F' for Female Narrator: ")
    if gender == 'M':
        gender = 0
        audioReader.setProperty("voice", voices[gender].id) # active voice
        #audioReader.say('Sally sells seashells by the seashore.')

    elif gender == 'F':
        gender = 1
        audioReader.setProperty("voice", voices[gender].id) # active voice
        #audioReader.say('Sally sells seashells by the seashore.')

    for page in range(len(reader.pages)): # for each page of range of 0 to num pages (entire pdf amount)
        nextPage = reader.pages[page] # page number
        content = nextPage.extract_text() # extract content from this page
        full_text += content

    audioReader.save_to_file(full_text, "myAudioBook.mp3") #  save the extracted text into an audio file
    audioReader.runAndWait() #  implement everything
    audioReader.stop()