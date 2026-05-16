import tkinter as tk

#title
root=tk.Tk()
root.title("My First GUI")

#lable1
lable=tk.Label(root,text="My First GUI",fg="cyan").pack()

#photo
pic = tk.PhotoImage(file="Smiley.png")

#lableImage
ilable=tk.Label(root,image=pic).pack()

#button
def happy():
    print("Ok You Clicked Me :D")
button=tk.Button(root,text="Click Me :P",command=happy).pack()

#end
root.mainloop()