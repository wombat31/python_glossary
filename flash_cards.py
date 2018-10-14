from tkinter import *
import random

def fetchQuestion():
    global question
    #clear the question and answer output box
    questionOutput.delete(0.0,END)
    answerOutput.delete(0.0,END)

    #pick a random key from the dictionary
    question = random.choice(list(questionBank))
    #output the question to the questionOutput box
    questionOutput.insert(END,question)

def fetchAnswer():
    global question
    #Output the answer dependent on the key from the question bank
    answerOutput.insert(END,questionBank[question])


window=Tk()
window.title("Test Myself Flash Cards")
#set up the question button
Button(window,text="GET QUESTION", width=15,command=fetchQuestion).grid(row=0,column=0,sticky=W)
#set up the answer button
Button(window,text="GET ANSWER", width=15,command=fetchAnswer).grid(row=0,column=0,sticky=E)
#Set up the question output widget
questionOutput = Text(window,width=75,height=2,background="light green")
questionOutput.grid(row=2,column=0,sticky=E)

Label(window, text="\nAnswer:").grid(row=3,column=0,sticky=W)
#Set up the answer output widget
answerOutput=Text(window, width=75,height=6,wrap=WORD, background="light green")
answerOutput.grid(row=4,column=0,columnspan=2,sticky=W)

#The dictionary
questionBank = {
    'What is the definition of algorithm?':'Step by step instructions to perform a task that a computer could understand.',
    'What is a bug?':'A piece of code that is causing a program to fail to run properly or at all.',
    'What is a binary number':'A number represented in base 2.'
}

window.mainloop()