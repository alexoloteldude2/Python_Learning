import tkinter as tk
root=tk.Tk()
root.title("Log In")
lable_account=tk.Label(root,text="username").pack(side="left")
entry_account=tk.Entry(root).pack(side="left")
lable_pwd=tk.Label(root,text="password").pack(side="left")
entry_pwd=tk.Entry(root).pack(side="left")
def happy():
    print("You Have Created An Account")
loginbtn=tk.Button(root,text="Log In",command=happy).pack(side="left")

root.mainloop()