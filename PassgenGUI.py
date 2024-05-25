from tkinter import *
from tkinter import ttk
import random, string, pyperclip

class PassgenGUI:
    def __init__(self,app):
        self.root = app
        self.app_layout()

    def app_layout(self): 
        self.LetterCount = ttk.Label(app, text="Number of letters: ")
        self.LetterCount.grid(column = 0, row = 0, ipadx=5, pady=5, sticky=W)
        self.NumberCount = ttk.Label(app, text="Number of digits: ")
        self.NumberCount.grid(column = 0, row = 1, ipadx=5, pady=5, sticky=W)
        self.SymbolCount = ttk.Label(app, text="Number of symbols: ")
        self.SymbolCount.grid(column = 0, row = 2, ipadx=5, pady=5, sticky=W)
        self.PassResult = ttk.Label(app, text="The password: ")
        self.PassResult.grid(column = 0, row = 3, ipadx=5, pady=5, sticky=W)

        self.LetterBox = ttk.Entry(app, width=35)
        self.LetterBox.grid(column=1,row=0,padx=10,pady=5, sticky=N)
        self.NumberBox = ttk.Entry(app, width=35)
        self.NumberBox.grid(column=1,row=1,padx=10,pady=5, sticky=N)
        self.SymbolBox = ttk.Entry(app, width=35)
        self.SymbolBox.grid(column=1,row=2,padx=10,pady=5, sticky=N)
        self.PassBox = ttk.Entry(app, width=35)
        self.PassBox.grid(column=1,row=3,padx=10,pady=5, sticky=N)

        resultButton = ttk.Button(app, text='Generate Password',command=self.PassGen)
        resultButton.grid(column=0, row=4, pady=10, sticky=W)
        resultCopy = ttk.Button(app, text='Copy', command=self.CopyPass)
        resultCopy.grid(column=1, row=4, pady=10, sticky=W)
    
    def CopyPass(self):
        pyperclip.copy(self.PassBox.get())

    def PassGen(self):
        letter_length = int(self.LetterBox.get())
        number_length = int(self.NumberBox.get())
        symbols_length = int(self.SymbolBox.get())

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
            self.PassBox.delete(0, "end")
        self.PassBox.insert(0, password)

if __name__ == "__main__":
    app = Tk()
    app.title("Password Generator")
    app.geometry("400x200")
    app.resizable(width=False, height=False)
    app2 = PassgenGUI(app)
    app.mainloop()
