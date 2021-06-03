# import all components 
# from the tkinter library
from tkinter import *
from tkinter import ttk
#from tkinter.ttk import*
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
from matplotlib import style
import numpy as np


#paraindex = [5.0,0.001,1,60,10,10,10]
paraindex = [5.0,0.001,1,10]
f = open("parameter.txt")
#paraindex = f.read().splitlines()

#print(paraindex[0])
#print(" "+ paraindex[1])

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
    btn_loadinitialmode.configure(text="File Path: "+filename)
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
    btn_observeddata.configure(text="File Path: "+filename)

def browseFiles3(): 
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*"))) 
       
    # Change label contents 
    btn_sourcesignature.configure(text="File Path: "+filename)


def executeC(): 
  
    # create a pipe to a child process 
    data, temp = os.pipe() 
  
    # write to STDIN as a byte object(convert string 
    # to bytes with encoding utf8) 
    os.write(temp, bytes("5 10\n", "utf-8")); 
    os.close(temp) 
  
    # store output of the program as a byte string in s 
    #s = subprocess.check_output("g++ main.c -o out2;./out2", stdin = data, shell = True) 
    ##os.system("g++ main.c -o out2;./out2 &")
    s = subprocess.check_call("./out2", stdin = data, shell = True) 

    # decode s to a normal string 
    #print(s.decode("utf-8")) 

def plot(): 
    executeC()
    style.use("ggplot")
    fig = Figure(figsize=(5,5), dpi=100)
    ax1 = fig.add_subplot(111)

    def animate(i):
    
        pullData = open("fobj.txt","r").read()
        #yar = pullData.split('\n')
        yar = np.loadtxt("fobj.txt")
        #xar = [1,2,3,4,5,6,7,8,9,10]
        #yar = []
        """for eachLine in dataArray:
            if len(eachLine)>1:
                #x,y = eachLine.split(' ')
                y=eachLine
                #xar.append(int(x))
                yar.append(y)
                #ax1.plot(xar,yar, 'r', marker='o')"""
                
        #ax1.clear()
        ax1.plot(yar)
    plotcanvas = FigureCanvasTkAgg(fig, TAB2_1)
    plotcanvas.get_tk_widget().place(relx=0.05, rely=0.24, relwidth=0.9, relheight=0.67)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plotcanvas.show()
    
def plot2(): 
    executeC()
    style.use("ggplot")
    fig = Figure(figsize=(5,5), dpi=100)
    ax1 = fig.add_subplot(111)
    
    def animate(i):
    
        #pullData = open("fobj.txt","r").read()
        #dataArray = pullData.split('\n')
        #xar = [1,2,3,4,5,6,7,8,9,10]
        #yar = np.loadtxt("result_model.txt")
        yar = np.loadtxt("result_model.txt")
        """for eachLine in dataArray:
            if len(eachLine)>1:
                #x,y = eachLine.split(' ')
                y=eachLine
                #xar.append(int(x))
                yar.append(y)
                #ax1.plot(xar,yar, 'r', marker='o')"""
        
        #ax1.clear()
        ax1.plot(yar)
    plotcanvas = FigureCanvasTkAgg(fig, frame2)
    plotcanvas.get_tk_widget().place(relx=0.05, rely=0.24, relwidth=0.9, relheight=0.67)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plotcanvas.show()

def plot3(): 
    executeC()
    style.use("ggplot")
    fig = Figure(figsize=(5,5), dpi=100)
    ax1 = fig.add_subplot(111)
    
    def animate(i):
    
        #pullData = open("fobj.txt","r").read()
        #dataArray = pullData.split('\n')
        #xar = [1,2,3,4,5,6,7,8,9,10]
        #yar = np.loadtxt("residual_field.dat")
        yar = np.loadtxt("synthetic_model.txt")
        """for eachLine in dataArray:
            if len(eachLine)>1:
                #x,y = eachLine.split(' ')
                y=eachLine
                #xar.append(int(x))
                yar.append(y)
                #ax1.plot(xar,yar, 'r', marker='o')"""
        
        #ax1.clear()
        ax1.plot(yar)
    plotcanvas = FigureCanvasTkAgg(fig, frame2)
    plotcanvas.get_tk_widget().place(relx=0.05, rely=0.24, relwidth=0.9, relheight=0.67)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plotcanvas.show()

def plot4(): 
    executeC()
    style.use("ggplot")
    fig = Figure(figsize=(5,5), dpi=100)
    ax1 = fig.add_subplot(111)
    
    def animate(i):
    
        #pullData = open("fobj.txt","r").read()
        #dataArray = pullData.split('\n')
        #xar = [1,2,3,4,5,6,7,8,9,10]
        #yar = np.loadtxt("residual_field.dat")
        yar = np.loadtxt("real_model.txt")
        """for eachLine in dataArray:
            if len(eachLine)>1:
                #x,y = eachLine.split(' ')
                y=eachLine
                #xar.append(int(x))
                yar.append(y)
                #ax1.plot(xar,yar, 'r', marker='o')"""
        
        #ax1.clear()
        ax1.plot(yar)
    plotcanvas = FigureCanvasTkAgg(fig, frame2)
    plotcanvas.get_tk_widget().place(relx=0.05, rely=0.24, relwidth=0.9, relheight=0.67)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plotcanvas.show()

def stopfoo():
    os.system("pkill out2")

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

#Create Tab Control
TAB_CONTROL = ttk.Notebook(root)

#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='GUI   ')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Team  ')
TAB_CONTROL.pack(expand=1, fill="both")


#INSERT FIRST FRAME
frame1 = Frame(TAB1, bg='#FFA384', bd=5)
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

btn_pause = Button(frame1, text="Pause/Resume")
btn_pause.place(relx=0.32, rely= 0.75,relwidth=0.23, relheight=0.25)

btn_resume = Button(frame1, text="Stop", command=stopfoo)
btn_resume.place(relx=0.55, rely= 0.75,relwidth=0.23, relheight=0.25)

btn_runningtime = Button(frame1, text="Time", bitmap = "hourglass")
btn_runningtime.place(relx=0.78, rely= 0.75,relwidth=0.22, relheight=0.25)

#INSERT SECOND FRAME
frame2 = Frame(TAB1, bg='#FFA384', bd=5)
frame2.place(relx=0.05, rely=0.38, relwidth=0.53, relheight=0.59, anchor='nw')

lbl_graph = Label(frame2, text="Graph", bg='#EFE7BC')
lbl_graph.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.1)

#Create Tab Control2 for all the graphs
TAB_CONTROL2 = ttk.Notebook(frame2)

#Tab1
TAB2_1 = ttk.Frame(TAB_CONTROL2)
TAB_CONTROL2.add(TAB2_1, text='Misfit vs Iterations  ')
TAB_CONTROL2.pack(expand=1, fill="both")

#Tab3
TAB2_3 = ttk.Frame(TAB_CONTROL2)
TAB_CONTROL2.add(TAB2_3, text='Synthetic Model ')
TAB_CONTROL2.pack(expand=1, fill="both")

#Tab4
TAB2_4 = ttk.Frame(TAB_CONTROL2)
TAB_CONTROL2.add(TAB2_4, text='Real Model ')
TAB_CONTROL2.pack(expand=1, fill="both")

#Tab2
TAB2_2 = ttk.Frame(TAB_CONTROL2)
TAB_CONTROL2.add(TAB2_2, text='Output ')
TAB_CONTROL2.pack(expand=1, fill="both")


#RADIO BUTTONS FOR GRAPH SELECTION
def sel_radio():
    selection = "Plot for Graph " + str(var.get())
    label.config(text = selection)
    plot()

def sel_radio_2():
    selection = "Plot for Graph " + str(var.get())
    label.config(text = selection)
    plot2()

def sel_radio_3():
    selection = "Plot for Graph " + str(var.get())
    label.config(text = selection)
    plot3()

def sel_radio_4():
    selection = "Plot for Graph " + str(var.get())
    label.config(text = selection)
    plot4()


var = IntVar()

radio_1 = Radiobutton(TAB2_1, text="Graph 1", variable=var, value=1, command=sel_radio)
radio_1.place(relx=0.36,rely=0.1, relwidth=0.29, relheight=0.09, anchor = 'nw')

radio_2 = Radiobutton(TAB2_2, text="Graph 2", variable=var, value=2, command=sel_radio_2)
radio_2.place(relx=0.36, rely=0.1, relwidth=0.29, relheight=0.09, anchor = 'nw')

radio_3 = Radiobutton(TAB2_3, text="Graph 3",variable=var, value=3, command=sel_radio_3)
radio_3.place(relx=0.36, rely=0.1, relwidth=0.29,relheight=0.09, anchor='nw')

radio_4 = Radiobutton(TAB2_4, text="Graph 4",variable=var, value=3, command=sel_radio_4)
radio_4.place(relx=0.36, rely=0.1, relwidth=0.29,relheight=0.09, anchor='nw')

label = Label(frame2)
label.place(relx=0.05, rely=0.93, relwidth=0.9, relheight=0.075, anchor='nw')


#INSERT THIRD FRAME
frame3 = Frame(TAB1, bg='#FFA384', bd=5)
frame3.place(relx=0.60, rely=0.38, relwidth=0.35, relheight=0.59, anchor='nw')

btn_para = Label(frame3, text="Parameter Settings", bg='#EFE7BC')
btn_para.place(relx=0.05, rely=0.01, relwidth=0.9, relheight=0.1)

#INSERT SLIDER
def sel1():
    selection1 = str(inputtxt1.get(1.0, "end-1c"))
    label1.config(text = selection1)
    paraindex[0] = inputtxt1.get(1.0, "end-1c")
    #print(paraindex[0])
    
    
def sel2():
    selection2 = str(inputtxt2.get(1.0, "end-1c"))
    label2.config(text = selection2)
    paraindex[1] = inputtxt2.get(1.0, "end-1c")

def sel3():
    selection3 = str(inputtxt3.get(1.0, "end-1c"))
    label3.config(text = selection3)
    paraindex[2] = inputtxt3.get(1.0, "end-1c")


def sel4():
    selection4 = str(inputtxt4.get(1.0, "end-1c"))
    label3.config(text = selection4)
    paraindex[3] = inputtxt4.get(1.0, "end-1c")

def sel5():
    selection5 = str(inputtxt5.get(1.0, "end-1c"))
    label5.config(text = selection5)
    paraindex[3] = inputtxt5.get(1.0, "end-1c")

def sel6():
    selection6 = str(inputtxt6.get(1.0, "end-1c"))
    label6.config(text = selection6)
    paraindex[5] = inputtxt6.get(1.0, "end-1c")

def sel7():
    #selection7 = "Value = " + str(inputtxt7.get(1.0, "end-1c"))
    selection7 = str(inputtxt7.get(1.0, "end-1c"))
    label7.config(text = selection7)
    paraindex[6] = inputtxt7.get(1.0, "end-1c")    

def sel8():

    a_file = open("parameter.txt", "w")

    #for row in paraindex:
    #    np.savetxt(a_file, row)

    np.savetxt("parameter.txt", np.array([paraindex[0], paraindex[1]], paraindex[2], paraindex[3]), fmt="%s")
    a_file.close()

    #n=2
    #for i in range(n):
    #    np.savetxt("parameter.txt", np.array(paraindex[i], fmt="%s"))
    #a_file.close()

var1 = DoubleVar()
inputtxt1 = Text(frame3,height = 2,width = 15)
inputtxt1.place(relx=0.05,rely=0.14, relwidth=0.3, relheight=0.1, anchor = 'nw')


button = Button(frame3, text = "Spacial resolution", command = sel1)
button.place(relx=0.37, rely=0.14, relwidth=0.34, relheight=0.1, anchor = 'nw')


label1 = Label(frame3, bg='#74BDCB')
label1.place(relx=0.95, rely=0.14, relwidth=0.23,relheight=0.1, anchor='ne')
label1.config(text = paraindex[0])

var2 = DoubleVar()
inputtxt2 = Text(frame3,height = 2,width = 15)
inputtxt2.place(relx=0.05,rely=0.25, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Temporal resolution", command = sel2)
button.place(relx=0.37, rely=0.25, relwidth=0.34, relheight=0.1, anchor = 'nw')

label2 = Label(frame3, bg='#74BDCB')
label2.place(relx=0.95, rely=0.25, relwidth=0.23,relheight=0.1, anchor='ne')
label2.config(text = paraindex[1])

#lbl_parameter3 = Label(frame3, text = "Parameter 3")
#lbl_parameter3.place(relx=0.95, rely=0.82, relwidth=0.7, relheight=0.1, anchor = 'ne')

#spinbox1 = Spinbox(frame3, from_ = 0, to = 10, bg='#74BDCB')
#spinbox1.place(relx=0.95, rely=0.93, relwidth=0.7,anchor='ne')

var3 = DoubleVar()
inputtxt3 = Text(frame3,height = 2,width = 15)
inputtxt3.place(relx=0.05,rely=0.36, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Reciever position", command = sel3)
button.place(relx=0.37, rely=0.36, relwidth=0.34, relheight=0.1, anchor = 'nw')

label3 = Label(frame3, bg='#74BDCB')
label3.place(relx=0.95, rely=0.36, relwidth=0.23,relheight=0.1, anchor='ne')
label3.config(text = paraindex[2])

var4 = DoubleVar()
inputtxt4 = Text(frame3,height = 2,width = 15)
inputtxt4.place(relx=0.05,rely=0.47, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Recording time", command = sel4)
button.place(relx=0.37, rely=0.47, relwidth=0.34, relheight=0.1, anchor = 'nw')

label4 = Label(frame3, bg='#74BDCB')
label4.place(relx=0.95, rely=0.47, relwidth=0.23,relheight=0.1, anchor='ne')
#label4.config(text = paraindex[3])

var5 = DoubleVar()
inputtxt5 = Text(frame3,height = 2,width = 15)
inputtxt5.place(relx=0.05,rely=0.58, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Frequency", command = sel3)
button.place(relx=0.37, rely=0.58, relwidth=0.34, relheight=0.1, anchor = 'nw')

label5 = Label(frame3, bg='#74BDCB')
label5.place(relx=0.95, rely=0.58, relwidth=0.23,relheight=0.1, anchor='ne')
#label5.config(text = paraindex[4])
label5.config(text = paraindex[3])

#Depth button
#iterations 
var6 = DoubleVar()
inputtxt6 = Text(frame3,height = 2,width = 15)
inputtxt6.place(relx=0.05,rely=0.69, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Depth button", command = sel6)
button.place(relx=0.37, rely=0.69, relwidth=0.34, relheight=0.1, anchor = 'nw')

label6 = Label(frame3, bg='#74BDCB')
label6.place(relx=0.95, rely=0.69, relwidth=0.23,relheight=0.1, anchor='ne')
#label6.config(text = paraindex[5])

var7 = DoubleVar()
inputtxt7 = Text(frame3,height = 2,width = 15)
inputtxt7.place(relx=0.05,rely=0.80, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Iterations", command = sel7)
button.place(relx=0.37, rely=0.80, relwidth=0.34, relheight=0.1, anchor = 'nw')

label7 = Label(frame3, bg='#74BDCB')
label7.place(relx=0.95, rely=0.80, relwidth=0.23,relheight=0.1, anchor='ne')
#label7.config(text = paraindex[6])


var8 = DoubleVar()
#inputtxt8 = Text(frame3,height = 2,width = 15)
#inputtxt8.place(relx=0.05,rely=0.91, relwidth=0.3, relheight=0.1, anchor = 'nw')

button = Button(frame3, text = "Save all parameters", command = sel8)
button.place(relx=0.05, rely=0.91, relwidth=0.90, relheight=0.1, anchor = 'nw')

#label8 = Label(frame3, bg='#74BDCB')
#label8.place(relx=0.95, rely=0.91, relwidth=0.27,relheight=0.1, anchor='ne')

#print(paraindex[0])
#f.write()


root.mainloop()