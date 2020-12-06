# 컴퓨터에게 3을 기억하라고 명령 
# 변수란?  컴퓨터가 데이터를 기억할 기억 장소를 의미 
 
 #x=0 #0을 기억해두었다가, 그 공간의 이름을 x라고 부르자!!
 #x=x+3 #기존의 x라는 공간의 값에 3을 더하여 다시 x에 대입해
from tkinter import *  #tkinter라는 모듈(GUI)중의 모든 함수를 다 참고하기!!
from PIL import Image # PIL 모듈의 Image 라는 클래스를 가져오자
from PIL import ImageTk

# 생성하기
win=Tk() #윈도우 화면 호출 
# 켄버스를 만들고, 만들어진 켄버스를 canvas변수로 부르자!!
canvas=Canvas(win, width=1460, height=800, bg="yellow")

img=Image.open("./images/sky.png")
# 이미지 사이즈 원하는 크기로 재조정 
img=img.resize( (1460,800), Image.ANTIALIAS)
img=ImageTk.PhotoImage(img)

#윈도우창의 크기를 원하는크기로 지정 
win.geometry("1460x800") #가로(너비)x세로 (높이)

# 켄버스를 윈도우창에 부착!!
canvas.pack() 
win.mainloop() #윈도우창을 닫지않고, 계속 유지하자
