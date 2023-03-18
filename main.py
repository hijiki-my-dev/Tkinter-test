from tkinter import *

def main():
    root = Tk()

    #ラベルウィジェット（クラス）画面にテキストや画像を表示する。
    mylabel = Label(
        root,
        text = "Hello World!",
        foreground="#33589A",
        width=10, #幅と高さは数字の0の幅と高さを基準にしている
        height=10
    )
    
    #ボタン。ラベルとの違いはクリックできるかどうか
    mybutton = Button(
        text="Click me!",
        width=25,
        height=5,
        #bg = "#33589A",
        fg = "#33589A"
    )


    mylabel.pack()
    mybutton.pack()
    
    #root.configure(bg = "black")

    root.mainloop()
    

if __name__ == "__main__":
    main()