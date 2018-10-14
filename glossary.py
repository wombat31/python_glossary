from tkinter import *
def click():
    entered_text = entry.get()
    output.delete(0.0,END)
    
    try:
        definition = my_glossary[entered_text]
    except:
        definition = "There is no entry for this word."
    output.insert(END, definition)



window=Tk()
window.title("Code Club Glossary")

Label(window, text="Enter the word that you want to define:").grid(row=0,column=0,sticky=W)

entry = Entry(window,width=20,bg="light green")
entry.grid(row=1,column=0,sticky=W)

Button(window,text="SUBMIT",width=5,command=click).grid(row=2,column=0,sticky=W)

Label(window, text="\nDefinition:").grid(row=3,column=0,sticky=W)

output=Text(window, width=75,height=6,wrap=WORD, background="light green")
output.grid(row=4,column=0,columnspan=2,sticky=W)

#The dictionary
my_glossary = {
    'algorithm':'Step by step instructions to perform a task that a computer could understand.',
    'bug':'A piece of code that is causing a program to fail to run properly or at all.',
    'binary number':'A number represented in base 2.'
}

window.mainloop()