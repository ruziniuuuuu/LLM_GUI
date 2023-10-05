from tkinter import Tk
from chat_app import ChatApp

def main():
    root = Tk()
    app = ChatApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()