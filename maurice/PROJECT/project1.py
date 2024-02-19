import tkinter
root=tkinter.Tk()
root.title("Registration Form")

name_label=tkinter.Label(root,text="Enter Name")
name_label.pack()
name_textbox=tkinter.Entry(root)
name_textbox.pack()

email_label=tkinter.Label(root,text="Enter Email")
email_label.pack()
email_textbox=tkinter.Entry(root)
email_textbox.pack()

age_label=tkinter.Label(root,text="Enter age")
age_label.pack()
age_textbox=tkinter.Entry(root)
age_textbox.pack()

submit_button=tkinter.Button(root,text='Submit')
submit_button.pack()
root.mainloop()