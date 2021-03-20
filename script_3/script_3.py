





#program to exploit the system resources
import tkinter
import random
import time

root= tkinter.Tk()
root.title("Hacked")
root.geometry("300x100")
root.config(bg="black")


#change for loop with a while true statement in real scenerio
#sometimes while may not work. therefore increase the range
def hack():
    for i in range(1000):
        rand_x = random.randint(0,2000)
        rand_y = random.randint(0,1500)
        topj=tkinter.Toplevel(root,bg="green")
        topj.geometry("300x100+{}+{}".format(rand_x,rand_y))
        

start_btn = tkinter.Button(root,bg="green",fg="black",text="Start",command=hack)
start_btn.pack(ipadx=30,ipady=10,padx=100,pady=20)

root.mainloop()