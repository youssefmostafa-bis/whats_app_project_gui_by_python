from tkinter import *
top = Tk()
top.title(string='Press A Button')
top.geometry('400x300')
def java():
 output_label.config(text='You Pressed Java Button')

def python():
 output_label.config(text='You Pressed Python Button')

B1=Button(top,text="Java", command=java)
B1.pack()
B2=Button(top,text="Python",command=python)
B2.pack()

output_label = Label(top)
output_label.pack()
top.mainloop()