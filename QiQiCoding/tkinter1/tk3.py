import tkinter as tk
root=tk.Tk()
root.title("DRAWING")
root.geometry('1000x1000')
canvas=tk.Canvas(root,width=200,height=200, bg='black')
canvas.create_line(0,0,100,100)
canvas.pack()
root.mainloop()
