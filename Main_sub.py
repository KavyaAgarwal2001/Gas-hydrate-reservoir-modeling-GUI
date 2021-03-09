# import all components 
# from the tkinter library
from tkinter import *
#import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
#import matplotlib as plt
# import filedialog module 
from tkinter import filedialog 
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import numpy as np
import time

import subprocess 
import os 

# Function for opening the  
# file explorer window 
def browseFiles(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    b_1.configure(text="File Path: "+filename)
    #L_1 = Label(root, text= filename.name,padx=5, bg="orange")
    #L_1.grid(row=0, column=1)

#def myClick():
def browseFiles2(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    b_12.configure(text="File Path: "+filename)

def browseFiles3(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    b_13.configure(text="File Path: "+filename)


# Create the root window
root = Tk()
# Set root window title
root.title("GUI for: Full Wave Form Inversion")
# Set root window size 
root.geometry("800x5000")
#Set root window background color 
root.config(background = "black")
root.resizable(width=False, height=False)

#myLabel1 = Label(root, text="This is the GUI Application for the project")
#myLabel1.grid(row=0, column=0)
b_1 = Label(root, text="Filename Textbox", padx=5, bg="white")
b_1.grid(row=0 ,column=1,columnspan=2,padx=3, pady=3,sticky=EW)

b_12 = Label(root, text="Filename Textbox", padx=5, bg="white")
b_12.grid(row=1 ,column=1,columnspan=2,padx=3, pady=3,sticky=EW)

b_13 = Label(root, text="Filename Textbox", padx=5, bg="white")
b_13.grid(row=2 ,column=1,columnspan=2,padx=3, pady=3,sticky=EW)

def open():
    top = Toplevel()
    top.title("Second window")

    def sel1():
        selection1 = "Value = " + str(var1.get())
        label1.config(text = selection1)

    def sel2():
        selection2 = "Value = " + str(var2.get())
        label2.config(text = selection2)

    def sel3():
        selection3 = "Value = " + str(var3.get())
        label3.config(text = selection3)

    var1 = DoubleVar()
    scale = Scale( top, variable = var1 )
    scale.pack(anchor = CENTER)

    button = Button(top, text = "Parameter 1", command = sel1)
    button.pack(anchor = CENTER)

    label1 = Label(top)
    label1.pack()

    var2 = DoubleVar()
    scale = Scale( top, variable = var2 )
    scale.pack(anchor = CENTER)

    button = Button(top, text = "Parameter 2", command = sel2)
    button.pack(anchor = CENTER)

    label2 = Label(top)
    label2.pack()

    var3 = DoubleVar()
    scale = Scale( top, variable = var3 )
    scale.pack(anchor = CENTER)

    button = Button(top, text = "Parameter 3", command = sel3)
    button.pack(anchor = CENTER)

    label3 = Label(top)
    label3.pack()

    btn = Button(top, text="Close window", command=top.destroy).pack()

def executeCpp(): 
  
    # create a pipe to a child process 
    data, temp = os.pipe() 
  
    # write to STDIN as a byte object(convert string 
    # to bytes with encoding utf8) 
    os.write(temp, bytes("5 10\n", "utf-8")); 
    os.close(temp) 
  
    # store output of the program as a byte string in s 
    s = subprocess.check_output("g++ test.cpp -o out2;./out2", stdin = data, shell = True) 
  
    # decode s to a normal string 
    print(s.decode("utf-8")) 


def plot(): 
    start = time.time()
    executeCpp()

    with open('data.txt') as f:
        lines = f.readlines()
        x = [line.split()[0] for line in lines]
        y = [line.split()[1] for line in lines]

    fig = plt.figure()

    ax1 = fig.add_subplot(111)

    ax1.set_title("Plot title")    
    ax1.set_xlabel('x label')
    ax1.set_ylabel('y label')

    ax1.plot(x,y, c='r', label='the data')

    leg = ax1.legend()

    plt.show()

    # the figure that will contain the plot 

     
       
    # list of squares 
    #y = [f.readline() for i in range(25)]
    # adding the subplot 
    #plot1 = fig.add_subplot(111) 
  
    # plotting the graph
    #plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                               master = root)   
    
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().grid(row=5, column=0) 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   root) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().grid(row=0 , column=1)

b_select = Button(root, text="Load initial model", command=browseFiles, bg="white")
#b_1 = Button(root, text="Select File", padx=5 , command=browseFiles, bg="white")
b_select2 = Button(root, text="Observed data", command=browseFiles2, bg="white")
b_select3 = Button(root, text="Source Signature", command=browseFiles3, bg="white")
button_exit = Button(root, text = "Exit", command = exit) 
def button_click():
    return;

def button_click_stop():
    end = time.time()
    return;

b_2 = Button(root, text="Start", padx=5 , command=plot,height = 1, width = 70, bg="white")
b_3 = Button(root, text="Pause/Resume", padx=5 , command=button_click, bg="white")
b_4 = Button(root, text="Stop", padx=5 , command=button_click, bg="white")
L_2 = Label(root, text="Running time:",padx=5, bg="white")
#b_5 = Button(root, text="Configure Settings", padx=5, command=open)
#b_6 = Button(root, text="Parameter Settings", padx=5 , command=open)
btn = Button(root, text="Parameter Settings", command=open).grid(row=4 ,column=1,padx=5,sticky=EW)

# Grid method is chosen for placing 
# the widgets at respective positions  
# in a table like structure by 
# specifying rows and columns
b_select.grid(row=0, column=0,sticky=EW)
b_select2.grid(row=1, column=0,sticky=EW)
b_select3.grid(row=2, column=0,sticky=EW)
#b_1.grid(row=0 ,column=1)
button_exit.grid(column = 2,row = 4, sticky=EW)

b_2.grid(row=3 ,column=0,padx=2, pady=10, sticky=EW)
b_3.grid(row=3 ,column=1,padx=3,sticky=EW)
b_4.grid(row=3 ,column=2,sticky=EW)
L_2.grid(row=4, column=0,sticky=EW)
#b_5.grid(row=4 ,column=1,sticky=EW)
#b_6.grid(row=4 ,column=2,sticky=EW)
 
# button that displays the plot 
plot_button = Button(master = root,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 




root.mainloop()