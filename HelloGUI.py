import tkinter
import Tkinter


class App:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        self.hi_there = Button (frame, text='hola',command =self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print('Hola mundo')

root = Tk()
app = App(root)
root.mainloop()


