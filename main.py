from tkinter import *

def main():
    root = Tk()

    myLabel = Label(root,
                    text = "Hello World!",
                    foreground="#33589A",
                    width=10,
                    height=10)

    myLabel.pack()

    root.mainloop()
    

if __name__ == "__main__":
    main()