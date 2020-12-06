
from tkinter import * 
win=Tk() #윈도우 생성함수 

canvas=Canvas(win, width=800, height=800, bg="yellow")
bt=Button(win, text="다음사진")

canvas.pack()
bt.pack()

win.mainloop() #윈도우창이 계속 떠있게, 즉 유지되게..