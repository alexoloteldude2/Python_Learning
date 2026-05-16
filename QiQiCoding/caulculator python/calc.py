import tkinter as tk
root=tk.Tk()
root.geometry("325x257")
root.title("Calculator")

firstDigit = 0
lastDigit = 0
oper = ""
needClear = False

def cal(value):
    global firstDigit, lastDigit, oper, needClear
    current = entry_calc1.get()
    # entry_calc1.delete(0,tk.END)
    if(value.isdigit()):
        if(oper != "" and needClear == True):
            entry_calc1.delete(0,tk.END)
            entry_calc1.insert(tk.END,value)
            needClear = False
        else:
            entry_calc1.insert(tk.END,value)
    elif(value=="+"):
        firstDigit = float(current)
        oper = value
        needClear = True
    elif(value=="-"):
        firstDigit = float(current)
        oper = value
        needClear = True
    elif(value=="x"):
        firstDigit = float(current)
        oper = value
        needClear = True
    
    elif(value=="÷"):
        firstDigit = float(current)
        oper = value
        needClear = True
        

    elif(value=="="):
        currentDigit = float(current)
        result=0
        if (oper=="+"):
            result=firstDigit+currentDigit
            result=int(result)
            entry_calc1.delete(0,tk.END)
            entry_calc1.insert(tk.END,result)

        elif(oper=="-"):
            result=firstDigit-currentDigit
            result=int(result)
            entry_calc1.delete(0,tk.END)
            entry_calc1.insert(tk.END,result)

        elif(oper=="x"):
            result=firstDigit*currentDigit
            result=int(result)
            entry_calc1.delete(0,tk.END)
            entry_calc1.insert(tk.END,result)

        elif(oper=="÷"):
            if (currentDigit==0):
                entry_calc1.delete(0,tk.END)
                entry_calc1.insert(tk.END,"Error")
                needClear = False
                firstDigit = 0
                lastDigit = 0
                oper = ""
            else:
                result=firstDigit/currentDigit
                result=int(result)
                entry_calc1.delete(0,tk.END)
                entry_calc1.insert(tk.END,result)
            
            

        

lbl_calc1=tk.Label(root,text="View (V)")
lbl_calc1.grid(row=0,column=0,padx=1,sticky="e,w")
lbl_calc2=tk.Label(root,text="Edit (E)")
lbl_calc2.grid(row=0,column=1,padx=1,sticky="e,w")
lbl_calc3=tk.Label(root,text="Help (H)")
lbl_calc3.grid(row=0,column=2,padx=1,sticky="e,w")
lbl_calc4=tk.Label(root,text="About (A)")
lbl_calc4.grid(row=0,column=3,padx=1,sticky="e,w")
lbl_calc5=tk.Label(root,text="Others (O)")
lbl_calc5.grid(row=0,column=4,padx=1,sticky="e,w")

entry_calc1=tk.Entry(root,font=("Calibri",24), justify="right")
entry_calc1.grid(row=1,column=0,columnspan=5,rowspan=1,sticky="e,w")

btn_calc1=tk.Button(root,text="MC",command=lambda : cal(btn_calc1.cget("text")))
btn_calc1.grid(row=2,column=0,sticky="e,w")
btn_calc2=tk.Button(root,text="MR",command=lambda : cal(btn_calc2.cget("text")))
btn_calc2.grid(row=2,column=1,sticky="e,w")
btn_calc3=tk.Button(root,text="MS",command=lambda : cal(btn_calc3.cget("text")))
btn_calc3.grid(row=2,column=2,sticky="e,w")
btn_calc4=tk.Button(root,text="M+",command=lambda : cal(btn_calc4.cget("text")))
btn_calc4.grid(row=2,column=3,sticky="e,w")
btn_calc5=tk.Button(root,text="M-",command=lambda : cal(btn_calc5.cget("text")))
btn_calc5.grid(row=2,column=4,sticky="e,w")

btn_calc6=tk.Button(root,text="<-",command=lambda : cal(btn_calc6.cget("text")))
btn_calc6.grid(row=3,column=0,sticky="e,w")
btn_calc7=tk.Button(root,text="CE",command=lambda : cal(btn_calc7.cget("text")))
btn_calc7.grid(row=3,column=1,sticky="e,w")
btn_calc8=tk.Button(root,text="C",command=lambda : cal(btn_calc8.cget("text")))
btn_calc8.grid(row=3,column=2,sticky="e,w")
btn_calc9=tk.Button(root,text="±",command=lambda : cal(btn_calc9.cget("text")))
btn_calc9.grid(row=3,column=3,sticky="e,w")
btn_calc10=tk.Button(root,text="√",command=lambda : cal(btn_calc10.cget("text")))
btn_calc10.grid(row=3,column=4,sticky="e,w")

btn_calc11=tk.Button(root,text="7",command=lambda : cal(btn_calc11.cget("text")))
btn_calc11.grid(row=4,column=0,sticky="e,w")
btn_calc12=tk.Button(root,text="8",command=lambda : cal(btn_calc12.cget("text")))
btn_calc12.grid(row=4,column=1,sticky="e,w")
btn_calc13=tk.Button(root,text="9",command=lambda : cal(btn_calc13.cget("text")))
btn_calc13.grid(row=4,column=2,sticky="e,w")
btn_calc14=tk.Button(root,text="÷",command=lambda : cal(btn_calc14.cget("text")))
btn_calc14.grid(row=4,column=3,sticky="e,w")
btn_calc15=tk.Button(root,text="%",command=lambda : cal(btn_calc15.cget("text")))
btn_calc15.grid(row=4,column=4,sticky="e,w")

btn_calc16=tk.Button(root,text="4",command=lambda : cal(btn_calc16.cget("text")))
btn_calc16.grid(row=5,column=0,sticky="e,w")
btn_calc17=tk.Button(root,text="5",command=lambda : cal(btn_calc17.cget("text")))
btn_calc17.grid(row=5,column=1,sticky="e,w")
btn_calc18=tk.Button(root,text="6",command=lambda : cal(btn_calc18.cget("text")))
btn_calc18.grid(row=5,column=2,sticky="e,w")
btn_calc19=tk.Button(root,text="x",command=lambda : cal(btn_calc19.cget("text")))
btn_calc19.grid(row=5,column=3,sticky="e,w")
btn_calc20=tk.Button(root,text="1/x",command=lambda : cal(btn_calc20.cget("text")))
btn_calc20.grid(row=5,column=4,sticky="e,w")

btn_calc21=tk.Button(root,text="1",command=lambda : cal(btn_calc21.cget("text")))
btn_calc21.grid(row=6,column=0,sticky="e,w")
btn_calc22=tk.Button(root,text="2",command=lambda : cal(btn_calc22.cget("text")))
btn_calc22.grid(row=6,column=1,sticky="e,w")
btn_calc23=tk.Button(root,text="3",command=lambda : cal(btn_calc23.cget("text")))
btn_calc23.grid(row=6,column=2,sticky="e,w")
btn_calc24=tk.Button(root,text="-",command=lambda : cal(btn_calc24.cget("text")))
btn_calc24.grid(row=6,column=3,padx=1,pady=1,sticky="e,w")
btn_calc25=tk.Button(root,text="=",command=lambda : cal(btn_calc25.cget("text")))
btn_calc25.grid(row=6,column=4,rowspan=2,padx=1,pady=1,sticky="e,w,n,s")

btn_calc26=tk.Button(root,text="0",command=lambda : cal(btn_calc26.cget("text")))
btn_calc26.grid(row=7,column=0,columnspan=2,sticky="e,w")
btn_calc27=tk.Button(root,text=".",command=lambda : cal(btn_calc27.cget("text")))
btn_calc27.grid(row=7,column=2,sticky="e,w")
btn_calc28=tk.Button(root,text="+",command=lambda : cal(btn_calc28.cget("text")))
btn_calc28.grid(row=7,column=3,sticky="e,w")





root.mainloop()

















































































































































































