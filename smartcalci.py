#importing data
from tkinter import*
import math
from PIL import ImageTk,Image
import parser
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt
#giving geometry to main page or page which will see in begining
root = Tk()
root.title("Supersmart Calculator")
root.configure(background="black")
root.resizable(width=False, height=False)
root.geometry("498x660+0+0")
op=""

calc= Frame(root)
calc.grid()
#functioning to buttons
def click(num):
    global op
    op = op+str(num)
    txtvs.set(op)
class Calc():
    def __init__(self):
        self.total=0
        self.current=""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
    def evaluate(self):
        global op
        output=str(eval(op))
        txtvs.set(output) 
    def display(self,value):
        txtDisplay.delete(0,END)
        txtDisplay.insert(0, value)        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)
    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtvs.get()))
        self.display(self.current)
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtvs.get())))
        self.display(self.current)
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtvs.get())))
        self.display(self.current)
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtvs.get())))
        self.display(self.current)  
    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtvs.get())))
        self.display(self.current)
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtvs.get())))
        self.display(self.current)
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtvs.get())))
        self.display(self.current)  
    def log10(self):
        self.result = False
        self.current = math.log10(float(txtvs.get()))
        self.display(self.current)
    def log2(self):
        self.result = False
        self.current = math.log2(float(txtvs.get()))
        self.display(self.current)  
    def log(self):
        self.result = False
        self.current = math.log(float(txtvs.get()))
        self.display(self.current)
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtvs.get()))
        self.display(self.current)
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtvs.get()))
        self.display(self.current)
    def sqrt(self):
        self.result = False
        self.current = math.sqrt(float(txtvs.get()))
        self.display(self.current)
    def clearDisplay(self):
        global op
        op =""
        txtvs.set(op)    
    def mathsPM(self):
        self.result=False
        self.current= -(float(txtDisplay.get()))
        self.display(self.current)
    def reci(self):
        self.result=False
        self.current= 1/(float(txtDisplay.get()))
        self.display(self.current)
    def fact(self):
        self.result=False
        self.current= math.factorial(float(txtvs.get()))
        self.display(self.current)
    def sqr(self):
        self.result=False
        self.current= (float(txtDisplay.get()))*(float(txtDisplay.get()))
        self.display(self.current)
    def sqq(self):
        self.result=False
        self.current= (float(txtDisplay.get()))*(float(txtDisplay.get()))*(float(txtDisplay.get()))
        self.display(self.current)   
    def sqt(self):
        self.result=False
        self.current= (float(txtDisplay.get()))**(1/3)
        self.display(self.current) 
    def rnd(self):
        self.result=False
        self.current= round(float(txtDisplay.get()))
        self.display(self.current)
    def isin(self):
        self.result = False
        self.current = math.asin((float(txtvs.get())))
        self.display(self.current) 
    def icos(self):
        self.result = False
        self.current = math.acos((float(txtvs.get())))
        self.display(self.current)  
    def itan(self):
        self.result = False
        self.current = math.atan((float(txtvs.get())))
        self.display(self.current)  
    def icosh(self):
        self.result = False
        self.current = math.acosh((float(txtvs.get())))
        self.display(self.current)  
    def itanh(self):
        self.result = False
        self.current = math.atanh((float(txtvs.get())))
        self.display(self.current)  
    def isinh(self):
        self.result = False
        self.current = math.asinh((float(txtvs.get())))
        self.display(self.current)  
    def lgamma(self):
        self.result = False
        self.current = math.lgamma((float(txtvs.get())))
        self.display(self.current)  
    def expm1(self):
        self.result = False
        self.current = math.expm1((float(txtvs.get())))
        self.display(self.current)  
    def log1p(self):
        self.result = False
        self.current = math.log1p((float(txtvs.get())))
        self.display(self.current) 
    def backspace(self):
        numLen = len(txtvs.get())
        length = numLen-1
        es = txtDisplay.delete(length,END)
        txtDisplay.update(es)
    def graphs(self):
        self.x = np.linspace(-10, 10, 1000)
        self.y = np.sin(self.x)
        plt.plot(self.x,self.y)
        plt.show()
    def graphc(self):
        self.x = np.linspace(-10, 10, 1000)
        self.y = np.cos(self.x)
        plt.plot(self.x,self.y)
        plt.show()
    def graphtan(self):
        self.x = np.linspace(-2*np.pi, 2*np.pi, 10000)
        self.y = np.tan(self.x)
        plt.ylim(-5,5)
        plt.plot(self.x,self.y)
        plt.show()
    def graphsec(self):
        self.x = np.linspace(-10, 10, 1000)
        self.y = 1 /(np.cos(self.x))
        plt.plot(self.x,self.y)
        plt.ylim(-5,5)
        plt.show()
    def graphcsc(self):
        self.x = np.linspace(-10, 10, 1000)
        self.y = 1 /(np.sin(self.x))
        plt.plot(self.x,self.y)
        plt.ylim(-5,5)
        plt.show()
    def graphcot(self):
        self.x = np.linspace(-10, 10, 1000)
        self.y = 1 /(np.tan(self.x))
        plt.plot(self.x,self.y)
        plt.ylim(-5,5)
        plt.show()
    def graphis(self):
        self.x = np.linspace(-5, 5, 1000)
        self.y = np.sin(self.x)
        plt.plot(self.y,self.x)
        plt.show()
    def graphic(self):
        self.x = np.linspace(-5, 5, 1000)
        self.y = np.cos(self.x)
        plt.plot(self.y,self.x)
        plt.show()
    def graphit(self):
        self.x = np.linspace(-5, 5, 1000)
        self.y = np.tan(self.x)
        plt.xlim(-5,5)
        plt.plot(self.y,self.x)
        plt.show()
    def graphsinh(self):
        self.x = np.linspace(-5, 5, 1000)
        self.y = np.sinh(self.x)
        plt.xlim(-25,25)
        plt.plot(self.x,self.y)
        plt.show()
    def graphcosh(self):
        self.x = np.linspace(-5, 5, 1000)
        self.y = np.cosh(self.x)
        plt.xlim(-15,15)
        plt.plot(self.x,self.y)
        plt.show()
    def graphtanh(self):
        self.x = np.linspace(-100, 100, 1000)
        self.y = np.tanh(self.x)
        plt.xlim(-5,5)
        plt.plot(self.x,self.y)
        plt.show()     

#making labels and buttons    
added_value = Calc()    
txtvs=StringVar()
txtDisplay = Entry(calc, font=('arial',20,'bold'),bg="black",fg="white",bd=30, width=29 ,justify=RIGHT,textvariable=txtvs)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")


bt7=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(7),bg="grey",text="7",bd=5,
           padx=15,pady=10).grid(row=3,column=0,pady=1)
bt8=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(8),bg="grey",text="8",bd=5,
           padx=15,pady=10).grid(row=3,column=1,pady=1)
bt9=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(9),bg="grey",text="9",bd=5,
           padx=15,pady=10).grid(row=3,column=2,pady=1)
btadd=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click('+'),bg="black",fg="gold",text="+",bd=5,
           padx=15,pady=10).grid(row=2,column=3,pady=1)
bt4=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(4),bg="grey",text="4",bd=5,
           padx=15,pady=10).grid(row=4,column=0,pady=1)
bt5=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(5),bg="grey",text="5",bd=5,
           padx=15,pady=10).grid(row=4,column=1,pady=1)
bt6=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(6),bg="grey",text="6",bd=5,
           padx=15,pady=10).grid(row=4,column=2,pady=1)
btsub=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click('-'),bg="black",fg="gold",text="-",bd=5,
           padx=15,pady=10).grid(row=3,column=3,pady=1)
bt1=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(1),bg="grey",text="1",bd=5,
           padx=15,pady=10).grid(row=5,column=0,pady=1)
bt2=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(2),bg="grey",text="2",bd=5,
           padx=15,pady=10).grid(row=5,column=1,pady=1)
bt3=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(3),bg="grey",text="3",bd=5,
           padx=15,pady=10).grid(row=5,column=2,pady=1)
btmul=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click('*'),bg="black",fg="gold",text="*",bd=5,
           padx=15,pady=10).grid(row=4,column=3,pady=1)
bt0=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click(0),bg="grey",fg="black",text="0",bd=5,
           padx=15,pady=10).grid(row=6,column=0,pady=1)
btC=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=added_value.clearDisplay,fg="black",bg="yellow",text="C",bd=5,
           padx=15,pady=10).grid(row=1,column=0,pady=1)
bteql=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=added_value.evaluate,bg="Red",text="=",bd=5,
           padx=15,pady=10).grid(row=6,column=3,pady=1)
btdiv=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=lambda:click('/'),bg="black",fg="gold",text=chr(247),bd=5,
           padx=15,pady=10).grid(row=5,column=3,pady=1)
btbcksp=Button(calc,width=6,height=2,font=('arial',15,'bold'),command=added_value.backspace,fg="black",bg="yellow",text="<<",bd=5,
           padx=15,pady=10).grid(row=1,column=1,pady=1)
btnreci = Button(calc,width=6,height=2, text="1/x", font=('arial',20,'bold'), bd=4, 
                bg="black",fg="silver",command=added_value.reci).grid(row=2,column=1,pady=1)
btsqrt=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=added_value.sqrt,bg="black",fg="silver",text="√",bd=5,
           padx=15,pady=10).grid(row=2,column=0,pady=1)
btdot=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=lambda:click('.'),bg="black",fg="white",text=".",bd=5,
           padx=15,pady=10).grid(row=6,column=2,pady=1)
btPM=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=added_value.mathsPM,bg="black",fg="coral1",text="+/-",bd=5,
           padx=15,pady=10).grid(row=6,column=1,pady=1)
btbl=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=lambda:click('('),bg="black",fg="cyan",text="(",bd=5,
           padx=15,pady=10).grid(row=1,column=2,pady=1)
btbr=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=lambda:click(')'),bg="black",fg="cyan",text=")",bd=5,
           padx=15,pady=10).grid(row=1,column=3,pady=1)
btsqr=Button(calc,width=6,height=2,font=('arial',15,'bold',),command=added_value.sqr,bg="black",fg="silver",text=" x^2",bd=5,
           padx=15,pady=10).grid(row=2,column=2,pady=1)

lblDisplay = Label(calc,text="Scientific Calculator Mode",font=('arial',30,'bold'),justify=CENTER)
lblDisplay.grid(row=0, column=4,columnspan=5)  
lblDisplay = Label(calc,text="Graphs",font=('arial',20,'bold'),justify=CENTER,fg = "Blue")
lblDisplay.grid(row=0, column=9,columnspan=2)  
#Scientific Calculator
btnPi = Button(calc, text="π", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.pi).grid(row=1,column=4,pady=1)

btnCos = Button(calc, text="cos", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="royal blue1",command=added_value.cos).grid(row=1,column=5,pady=1)

btnSin = Button(calc, text="sin", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="royal blue1",command=added_value.sin).grid(row=1,column=6,pady=1)

btntan = Button(calc, text="tan", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="royal blue1",command=added_value.tan).grid(row=1,column=7,pady=1)


btn2pi = Button(calc, text="2π", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.tau).grid(row=2,column=4,pady=1)

btnCosh = Button(calc, text="cosh", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="cyan",command=added_value.cosh).grid(row=2,column=5,pady=1)
btnSinh = Button(calc, text="sinh", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="cyan",command=added_value.sinh).grid(row=2,column=6,pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="cyan",command=added_value.tanh).grid(row=2,column=7,pady=1)
btnlog = Button(calc, text="ln", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.log).grid(row=3,column=4,pady=1)
btnExp = Button(calc, text="exp", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.exp).grid(row=3,column=5,pady=1)
btnMod = Button(calc, text="Mod", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command = lambda:click('%') ).grid(row=3,column=6,pady=1)
btnE = Button(calc, text="e", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.e).grid(row=3,column=7,pady=1)      
btnlog2 = Button(calc, text="log2", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.log2).grid(row=4,column=4,pady=1)
btnround = Button(calc, text="Round", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.rnd).grid(row=6,column=4,pady=1)
btndeg = Button(calc, text="deg", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.degrees).grid(row=4,column=5,pady=1)
btngsqr = Button(calc, text="x^y", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=lambda:click('**')).grid(row=4,column=6,pady=1)
btnsqt3 = Button(calc, text="3√x", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.sqt).grid(row=4,column=7,pady=1)
btnlog10 = Button(calc, text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="pink",command=added_value.log10).grid(row=5,column=4,pady=1)
btnsq3 = Button(calc, text="x^3", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.sqq).grid(row=5,column=5,pady=1)
btnfact = Button(calc, text="x!", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=added_value.fact).grid(row=5,column=6,pady=1)
btnpowt = Button(calc, text="10^x", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="violet",command=lambda:click('10**')).grid(row=5,column=7,pady=1)
btnisin = Button(calc, text="sin-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="purple1",command=added_value.isin).grid(row=6,column=5,pady=1)
btnicos = Button(calc, text="cos-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="purple1",command=added_value.icos).grid(row=6,column=6,pady=1)
btnitan = Button(calc, text="tan-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="purple1",command=added_value.itan).grid(row=6,column=7,pady=1)  
btnisinh = Button(calc, text="sinh-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="light green",command=added_value.isinh).grid(row=1,column=8,pady=1)  
btnicosh = Button(calc, text="cosh-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="light green",command=added_value.icosh).grid(row=2,column=8,pady=1)  
btnitanh = Button(calc, text="tanh-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="light green",command=added_value.itanh).grid(row=3,column=8,pady=1)  
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="orange",command=added_value.lgamma).grid(row=4,column=8,pady=1)  
btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="orange",command=added_value.expm1).grid(row=5,column=8,pady=1)  
btnlog1p = Button(calc, text="log1p", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="orange",command=added_value.log1p).grid(row=6,column=8,pady=1) 
btnggsin = Button(calc, text="sin(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphs).grid(row=1,column=9,pady=1)  
btnggcos = Button(calc, text="cos(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphc).grid(row=2,column=9,pady=1)  
btnggtan = Button(calc, text="tan(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphtan).grid(row=3,column=9,pady=1)  
btnggsec = Button(calc, text="sec(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphsec).grid(row=4,column=9,pady=1)  
btnggcsc = Button(calc, text="csc(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphcsc).grid(row=5,column=9,pady=1)  
btnggcot = Button(calc, text="cot(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="OrangeRed2",command=added_value.graphcot).grid(row=6,column=9,pady=1) 
btnggis = Button(calc, text="sin-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="plum1",command=added_value.graphis).grid(row=1,column=10,pady=1) 
btnggic = Button(calc, text="cos-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="plum1",command=added_value.graphic).grid(row=2,column=10,pady=1) 
btnggit = Button(calc, text="tan-1(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="plum1",command=added_value.graphit).grid(row=3,column=10,pady=1)
btnggsinah = Button(calc, text="sinh(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="SeaGreen1",command=added_value.graphsinh).grid(row=4,column=10,pady=1)
btnggcosah = Button(calc, text="cosh(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="SeaGreen1",command=added_value.graphcosh).grid(row=5,column=10,pady=1)
btnggtanah = Button(calc, text="tanh(x)", width=6, height=2, font=('arial',20,'bold'), bd=4, 
                bg="black",fg="SeaGreen1",command=added_value.graphtanh).grid(row=6,column=10,pady=1)
#functioning and making message boxes       
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Do you want to exit?")
    if iExit>0:
        root.destroy()
        return
def Scientific():
    root.resizable(width =False, height=False)
    root.geometry("1080x660+0+0")
def Standard():
    root.resizable(width =False, height=False)
    root.geometry("498x660+0+0")
def Graph():
    root.resizable(width =False, height=False)
    root.geometry("1310x660+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="File", menu=filemenu)
filemenu.add_command(label = "Standard", command= Standard)
filemenu.add_command(label = "Scientific", command= Scientific)
filemenu.add_command(label = "Standard Trigo, Inverse Trigo & Trigo Hyperbolic Graphs", command= Graph)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="Edit", menu=editmenu)
editmenu.add_command(label = "Cut",command=lambda:w.event_generate("<<Cut>>"))
editmenu.add_command(label = "Copy",command=lambda:w.event_generate("<<Copy>>"))
editmenu.add_separator()
editmenu.add_command(label = "Paste",command=lambda:w.event_generate("<<Paste>>"))

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

#endiing it.
root.configure(menu=menubar)
root.mainloop()



        
