from tkinter import *
#===========================================================================    
#===========================================================================
def button_press(num) :
    global equation_text 
    
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    
     
#===========================================================================
def equals() :
    
    try : 
        global equation_text 
    
        equal = str(eval(equation_text))
    
        equation_label.set(equal)
    
        equation_text = equal
        
    except ZeroDivisionError :
        equation_label.set("Logic error")
        
        equation_text = ""
    except SyntaxError :
        
        equation_label.set("What was that ? ")
        
        equation_text = ""
    
#===========================================================================
def clear() :
    global equation_text 
    
    equation_label.set("")
    equation_text = ""
  
 
#===========================================================================
window = Tk()

window.title("Calculator")

window.geometry("500x500")

equation_text = ""

equation_label = StringVar() 

label = Label(window , textvariable=equation_label , font=("consolas" , 30)  , fg="black" , height=2 )
label.pack()


frame = Frame(window)
frame.pack()

#===========================================================================
button_1 = Button(frame , text=1 , height=4 , width=9 , font=35,
                  command= lambda : button_press(1))
button_1.grid(row=0 , column=1)

button_2 = Button(frame , text=2 , height=4 , width=9 , font=35,
                  command= lambda : button_press(2))
button_2.grid(row=0 , column=2)

button_3 = Button(frame , text=3 , height=4 , width=9 , font=35,
                  command= lambda : button_press(3))
button_3.grid(row=0 , column=3)

button_4 = Button(frame , text=4 , height=4 , width=9 , font=35,
                  command= lambda : button_press(4))
button_4.grid(row=1 , column=1)

button_5 = Button(frame , text=5 , height=4 , width=9 , font=35,
                  command= lambda : button_press(5))
button_5.grid(row=1 , column=2)

button_6 = Button(frame , text=6 , height=4 , width=9 , font=35,
                  command= lambda : button_press(6))
button_6.grid(row=1 , column=3)

button_7 = Button(frame , text=7 , height=4 , width=9 , font=35,
                  command= lambda : button_press(7))
button_7.grid(row=2 , column=1)

button_8 = Button(frame , text=8 , height=4 , width=9 , font=35,
                  command= lambda : button_press(8))
button_8.grid(row=2 , column=2)

button_9 = Button(frame , text=9 , height=4 , width=9 , font=35,
                  command= lambda : button_press(9))
button_9.grid(row=2 , column=3)

button_0 = Button(frame , text=0 , height=4 , width=9 , font=35,
                  command= lambda : button_press(0))
button_0.grid(row=3 , column=1)

plus = Button(frame , text='+' , height=4 , width=9 , font=35,
                  command= lambda : button_press('+'))
plus.grid(row=0 , column=4)

mines = Button(frame , text='-' , height=4 , width=9 , font=35,
                  command= lambda : button_press('-'))
mines.grid(row=1 , column=4)

result = Button(frame , text='=' , height=4 , width=9 , font=35,
                  command= equals)
result.grid(row=3 , column=3)

dot = Button(frame , text='.' , height=4 , width=9 , font=35,
                  command= lambda : button_press('.'))
dot.grid(row=3 , column=2)

multi = Button(frame , text='x' , height=4 , width=9 , font=35,
                  command= lambda : button_press('*'))
multi.grid(row=2 , column=4)

divide = Button(frame , text='÷' , height=4 , width=9 , font=35,
                  command= lambda : button_press('/'))
divide.grid(row=3 , column=4)

clearr= Button(frame , text='C' , height=4 , width=9 , font=35,
                  command=clear)
clearr.grid(row=4 , column=2)





window.mainloop()