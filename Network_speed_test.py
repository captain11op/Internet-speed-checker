from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down_00.config(text=down)
    lab_up_00.config(text=up)




sp = Tk()
sp.title("HowFast")
sp.geometry("300x500")
sp.config(bg="Blue")

lab = Label(sp,text="Internet Speed Test", font=("Verdana",12,"bold"),fg="Black")
lab.place(x=50,y=30,height=30,width=200)  

lab = Label(sp,text="Download Speed", font=("Verdana",15,"bold"),fg="Black")
lab.place(x=50,y=125,height=30,width=200)

lab_down_00 = Label(sp,text="00 ", font=("Verdana",8,"bold"),fg="Red")
lab_down_00.place(x=50,y=160,height=30,width=100)

lab = Label(sp,text="Upload Speed", font=("Verdana",15,"bold"),fg="Black")
lab.place(x=50,y=250,height=30,width=200)

lab_up_00 = Label(sp,text="00", font=("Verdana",8,"bold"),fg="Red")
lab_up_00.place(x=50,y=290,height=30,width=100)

button = Button(sp,text="Check Speed",font=("Verdana",15,"bold"),relief=RAISED,bg="Red", command=speedcheck)
button.place(x=50,y=375,height="30",width="150")


sp.mainloop()



