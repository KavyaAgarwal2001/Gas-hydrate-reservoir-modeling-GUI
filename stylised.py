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
import matplotlib.animation as animation
import os
import subprocess
import time

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
    #executeCpp()

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def animate(i):
    
        pullData = open("data.txt","r").read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        for eachLine in dataArray:
            if len(eachLine)>1:
                x,y = eachLine.split(' ')
                xar.append(int(x))
                yar.append(int(y))
                
                
        #ax1.clear()
        ax1.plot(xar,yar)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
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

def button_click():
    return;

def button_click_stop():
    end = time.time()
    return;

# Create the root window
root = Tk()
# Set root window title
root.title("GUI for: Full Wave Form Inversion")
# Set root window size 
root.geometry("1200x800")
#Set root window background color 
##root.config(background = "black")
#root.resizable(width=False, height=False)

frame1 = Frame(root, bg='#FFA384', bd=5)
frame1.place(relx=0.5, rely=0.05, relwidth=0.9, relheight=0.3, anchor='n')

btn_loadinitialmode = Button(frame1, text = "Load Initial Mode", command=browseFiles)
btn_loadinitialmode.place(relwidth=0.3, relheight=0.25)
lbl_filename1 = Label(frame1, text="Filename Textbox", padx=5, bg='#74BDCB')
lbl_filename1.place(relx=0.32, relheight=0.24, relwidth=0.68)

btn_observeddata = Button(frame1, text="Observed Data", command=browseFiles2)
btn_observeddata.place(rely= 0.25,relwidth=0.3, relheight=0.25)
lbl_filename2 = Label(frame1, text="Filename Textbox", padx=5, bg='#74BDCB')
lbl_filename2.place(relx=0.32, rely=0.25, relheight=0.24, relwidth=0.68)

btn_sourcesignature = Button(frame1, text="Source Signature", command=browseFiles2)
btn_sourcesignature.place(rely= 0.50,relwidth=0.3, relheight=0.25)
lbl_filename2 = Label(frame1, text="Filename Textbox", padx=5, bg='#74BDCB')
lbl_filename2.place(relx=0.32, rely=0.50, relheight=0.24, relwidth=0.68)

btn_start = Button(frame1, text="Start", command=plot)
btn_start.place(rely= 0.75,relwidth=0.3, relheight=0.25)

btn_pause = Button(frame1, text="Pause")
btn_pause.place(relx=0.32, rely= 0.75,relwidth=0.23, relheight=0.25)

btn_resume = Button(frame1, text="Pause")
btn_resume.place(relx=0.55, rely= 0.75,relwidth=0.23, relheight=0.25)

btn_runningtime = Button(frame1, text="Time", bitmap = "hourglass")
btn_runningtime.place(relx=0.78, rely= 0.75,relwidth=0.22, relheight=0.25)

frame2 = Frame(root, bg='#FFA384', bd=5)
frame2.place(relx=0.05, rely=0.4, relwidth=0.6, relheight=0.55, anchor='nw')

lbl_graph = Label(frame2, text="Graph", bg='#EFE7BC')
lbl_graph.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.1)

frame3 = Frame(root, bg='#FFA384', bd=5)
frame3.place(relx=0.67, rely=0.4, relwidth=0.28, relheight=0.55, anchor='nw')

btn_para = Label(frame3, text="Parameter Settings", bg='#EFE7BC')
btn_para.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.1)

#insert slider
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
scale = Scale( frame3, variable = var1 )
scale.place(relx=0.05,rely=0.14, anchor = 'nw')

button = Button(frame3, text = "Parameter 1", command = sel1)
button.place(relx=0.95, rely=0.14, relwidth=0.7, relheight=0.1, anchor = 'ne')


label1 = Label(frame3, bg='#74BDCB')
label1.place(relx=0.95, rely=0.38, relwidth=0.7,relheight=0.1, anchor='se')

var2 = DoubleVar()
scale = Scale(frame3, variable = var2 )
scale.place(relx=0.05,rely=0.41, anchor = 'nw')

button = Button(frame3, text = "Parameter 2", command = sel2)
button.place(relx=0.95, rely=0.41, relwidth=0.7, relheight=0.1, anchor = 'ne')

label2 = Label(frame3, bg='#74BDCB')
label2.place(relx=0.95, rely=0.65, relwidth=0.7,relheight=0.1, anchor='se')

#lbl_parameter3 = Label(frame3, text = "Parameter 3")
#lbl_parameter3.place(relx=0.95, rely=0.82, relwidth=0.7, relheight=0.1, anchor = 'ne')

#spinbox1 = Spinbox(frame3, from_ = 0, to = 10, bg='#74BDCB')
#spinbox1.place(relx=0.95, rely=0.93, relwidth=0.7,anchor='ne')

var3 = DoubleVar()
scale = Scale(frame3, variable = var3 )
scale.place(relx=0.05,rely=0.68, anchor = 'nw')

button = Button(frame3, text = "Parameter 3", command = sel3)
button.place(relx=0.95, rely=0.68, relwidth=0.7, relheight=0.1, anchor = 'ne')

label2 = Label(frame3, bg='#74BDCB')
label2.place(relx=0.95, rely=0.92, relwidth=0.7,relheight=0.1, anchor='se')

#insert radiobuttons
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

var = IntVar()
R1 = Radiobutton(frame3, text = "Option 1", variable = var, value = 1,
                  command = sel)
R1.place(anchor = 'nw',relx=0.05, rely=0.94)

R2 = Radiobutton(frame3, text = "Option 2", variable = var, value = 2,
                  command = sel)
R2.place(anchor = 'nw', relx=0.37, rely=0.94)

R3 = Radiobutton(frame3, text = "Option 3", variable = var, value = 3,
                  command = sel)
R3.place( anchor = 'nw', relx=0.69, rely=0.94)

label = Label(root)
label.pack()

root.mainloop()