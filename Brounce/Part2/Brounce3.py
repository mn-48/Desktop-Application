from tkinter import  *
import random
import time

tk = Tk()
tk.title("Brounce!")

# windows screen not changeable/ resizeable
tk.resizable(0,0)

# Never hide the brounce window
tk.wm_attributes("-topmost",1)

canvas = Canvas(tk,width = 500,height = 500,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        #print(ht)


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id) # pos =[x1,y1,x2,y2]
        print(pos)

        if pos[1]<=0:
            self.y = 1
        if pos[3]>=self.canvas_height:
            self.y = -1

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)




tk.mainloop()