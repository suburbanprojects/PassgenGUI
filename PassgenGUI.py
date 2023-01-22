import tkinter as tk
import random, string
import pyperclip

app = tk.Tk()
app.title("Password Generator")

def PassGen():
    global LetterBox, NumberBox, SymbolBox
    letter_length = int(LetterBox.get())
    number_length = int(NumberBox.get())
    symbols_length = int(SymbolBox.get())
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    combined_pass = []
    
    for char in range (1, letter_length + 1) :
        combined_pass.append(random.choice(letters))
        
    for char in range(1, number_length + 1):
        combined_pass.append(random.choice(digits))
        
    for char in range(1, symbols_length + 1):
        combined_pass.append(random.choice(symbols))
        
    random.shuffle(combined_pass)
    
    password = ""
    for char in combined_pass:
        password += char
        PassBox.delete(0, "end")
    PassBox.insert(tk.INSERT, password)

def CopyPass():
    pyperclip.copy(PassBox.get())

LetterCount = tk.Label(app, text="Number of letters: ")
LetterCount.grid(column = 0, row = 0, ipadx=5, pady=5, sticky=tk.W+tk.N)
NumberCount = tk.Label(app, text="Number of digits: ")
NumberCount.grid(column = 0, row = 1, ipadx=5, pady=5, sticky=tk.W+tk.N)
SymbolCount = tk.Label(app, text="Number of symbols: ")
SymbolCount.grid(column = 0, row = 2, ipadx=5, pady=5, sticky=tk.W+tk.N)
PassResult = tk.Label(app, text="The password: ")
PassResult.grid(column = 0, row = 3, ipadx=5, pady=5, sticky=tk.W+tk.N)

LetterBox = tk.Entry(app, width=35)
LetterBox.grid(column=1,row=0,padx=10,pady=5, sticky=tk.N)
NumberBox = tk.Entry(app, width=35)
NumberBox.grid(column=1,row=1,padx=10,pady=5, sticky=tk.N)
SymbolBox = tk.Entry(app, width=35)
SymbolBox.grid(column=1,row=2,padx=10,pady=5, sticky=tk.N)
PassBox = tk.Entry(app, width=35)
PassBox.grid(column=1,row=3,padx=10,pady=5, sticky=tk.N)

resultButton = tk.Button(app, text='Generate Password', command=PassGen)
resultButton.grid(column=0, row=4, pady=10, sticky=tk.W)
resultCopy = tk.Button(app, text='Copy', command=CopyPass)
resultCopy.grid(column=1, row=4, pady=10, sticky=tk.W)
resultQuit = tk.Button(app, text='Quit', command=app.quit)
resultQuit.grid(column=2, row=4, pady=10, sticky=tk.W)

app.mainloop()
