
from tkinter import * 

# next함수 정의하기 
def next():
    print("나 눌렀어?")

win=Tk() #윈도우 생성함수 
canvas=Canvas(win, width=800, height=800, bg="yellow")

#버튼을 누를때 next라는 코드를 호출한다!!(즉 함수를 호출한다..)
bt=Button(win, text="다음사진", command=next)

canvas.pack()
bt.pack()

win.mainloop() #윈도우창이 계속 떠있게, 즉 유지되게..