from tkinter import *

# create a main parent window, tkinter offers a method Tk.
window=Tk()

window.title('Interest Calculator')
window.geometry("400x400")
window.configure(bg='lightcyan')

def calculate_interest():
    #storing what they wrote for their height and their weight in variables then use the interest formula
    p=float(principle.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)
    
    showLabel.destroy()
    msg=""
    
  
      
    output_message= Label(result_frame,text=name+", your Interest is "+str(interest)+" and "+msg, bg = "lightcyan", font=("Calibri", 12), width=42)
    output_message.place(x=20,y=40)
    output_message.pack()



#fg is foreground: font color(in this case)
heading_label=Label(window, text = "Interst CALCULATOR",fg = "black",bg = "lightcyan",font = ("Calibri" , 20), bd = 5)
heading_label.place(x = 50, y = 20)


#making a block to let the person write their input
username=Entry(window, text = "" , bd = 2, width = 22)
username.place(x = 150 , y = 92)



result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

showLabel=Label(result_frame,text="Your text will be displayed here ", bg = "lightcyan", font=("Calibri", 12), width=33)
showLabel.place(x=20,y=20)
showLabel.pack()

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)



window.mainloop()