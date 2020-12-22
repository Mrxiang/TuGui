import tkinter as tk
from tkinter import  *
import time

class Watch(Frame):
    msec = 1000

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        lable = Label(self, textvariable=self.timestr)
        lable.pack(side=LEFT)

    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)

    def _settime(self):
        today_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.timestr.set(today_time)

    def start(self):
        self._update()
        self.pack()

if __name__ == '__main__':
        root = Tk()
        root.geometry('250x150')
        frame = Frame(root)
        frame.pack(side=TOP)
        mw = Watch(frame)
        # mywatch = Button(frame1, text='时钟', command=mw.start)
        # mywatch.pack(side=LEFT)
        mw.start()
        root.mainloop()


