import tkinter as tk

from MainAppController import MainAppController

def main():

    controller = MainAppController()
    root = tk.Tk()
    root.title('Tomograf')

    controller.init_view(root)


    print('end of program')



if __name__ == "__main__":
    main()