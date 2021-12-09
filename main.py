# Calculator projects

# modules
import tkinter as tk
import parser
from math import sqrt, pi
from tkinter import font

# constant
WIDTH1 = 8
HEIGHT1 = 3
FONT1 = ("Helvetica", 16)
FONT2 = ("Helvetica", 20)

# function
# i for tracking position of input text
i = 0

# get number and insert to display
def GetVar(num):
    global i
    ent_display.insert(i, num)
    i+=1

# get operator and insert to display
def GetOpt(opt):
    global i
    opt_len = len(opt)
    ent_display.insert(i, opt)
    i+=opt_len

# remove all characters in display
def ClearAll():
    ent_display.delete(0, tk.END)

# square root of given number
def SquareRoot():
    global i
    all_char = ent_display.get()
    result = f"sqrt({all_char})"
    length = len(result)
    ClearAll()
    ent_display.insert(0, result)
    i+=length

# flip numerator and denominator
def Flip():
    global i
    all_char = ent_display.get()
    if len(all_char):
        result = f"1/{all_char}"
        length = len(result)
        ClearAll()
        ent_display.insert(0, result)
        i+=length

# remove last character
def Undo():
    all_char = ent_display.get()
    if len(all_char):
        all_char = all_char[:-1]
        ClearAll()
        ent_display.insert(0, all_char)

# fetch input text and evaluate them
def Calculate():
    all_char = ent_display.get()
    try:
        result = eval(parser.expr(all_char).compile())
        ClearAll()
        ent_display.insert(0, result)
    except Exception:
        ClearAll()
        ent_display.insert(0, result)

# GUI
# window
window = tk.Tk()
window.title("Calculator")
window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
window.columnconfigure([0, 1, 2, 3], weight=1)

# entry
ent_display = tk.Entry(master=window, font=FONT2, justify="right")
ent_display.grid(row=0, columnspan=4, sticky="nsew", ipady=20)

# button
# number button
btn_num1 = tk.Button(master=window, text="1", command=lambda: GetVar(1), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num2 = tk.Button(master=window, text="2", command=lambda: GetVar(2), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num3 = tk.Button(master=window, text="3", command=lambda: GetVar(3), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num1.grid(row=5, column=0, sticky="nsew")
btn_num2.grid(row=5, column=1, sticky="nsew")
btn_num3.grid(row=5, column=2, sticky="nsew")

btn_num4 = tk.Button(master=window, text="4", command=lambda: GetVar(4), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num5 = tk.Button(master=window, text="5", command=lambda: GetVar(5), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num6 = tk.Button(master=window, text="6", command=lambda: GetVar(6), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num4.grid(row=4, column=0, sticky="nsew")
btn_num5.grid(row=4, column=1, sticky="nsew")
btn_num6.grid(row=4, column=2, sticky="nsew")

btn_num7 = tk.Button(master=window, text="7", command=lambda: GetVar(7), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num8 = tk.Button(master=window, text="8", command=lambda: GetVar(8), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num9 = tk.Button(master=window, text="9", command=lambda: GetVar(9), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num7.grid(row=3, column=0, sticky="nsew")
btn_num8.grid(row=3, column=1, sticky="nsew")
btn_num9.grid(row=3, column=2, sticky="nsew")

# AC | 0 | . button
btn_ac = tk.Button(master=window, text="AC", command=lambda: ClearAll(), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_num0 = tk.Button(master=window, text="0", command=lambda: GetVar(0), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_dot = tk.Button(master=window, text=".", command=lambda: GetVar("."), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_ac.grid(row=6, column=0, sticky="nsew")
btn_num0.grid(row=6, column=1, sticky="nsew")
btn_dot.grid(row=6, column=2, sticky="nsew")

# operator button
btn_plus = tk.Button(master=window, text="+", command=lambda: GetOpt("+"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_minus = tk.Button(master=window, text="-", command=lambda: GetOpt("-"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_multi = tk.Button(master=window, text="*", command=lambda: GetOpt("*"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_divide = tk.Button(master=window, text="/", command=lambda: GetOpt("/"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_plus.grid(row=2, column=3, sticky="nsew")
btn_minus.grid(row=3, column=3, sticky="nsew")
btn_multi.grid(row=4, column=3, sticky="nsew")
btn_divide.grid(row=5, column=3, sticky="nsew")

btn_exp = tk.Button(master=window, text="X^2", command=lambda: GetOpt("**2"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_sqrt = tk.Button(master=window, text="√", command=lambda: SquareRoot(), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_flip = tk.Button(master=window, text="1/X", command=lambda: Flip(), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_undo = tk.Button(master=window, text="<-", command=lambda: Undo(), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_exp.grid(row=1, column=0, sticky="nsew")
btn_sqrt.grid(row=1, column=1, sticky="nsew")
btn_flip.grid(row=1, column=2, sticky="nsew")
btn_undo.grid(row=1, column=3, sticky="nsew")

btn_brkt_left = tk.Button(master=window, text="(", command=lambda: GetOpt("("), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_brkt_right = tk.Button(master=window, text=")", command=lambda: GetOpt(")"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_pi = tk.Button(master=window, text="π", command=lambda: GetOpt("pi"), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_cal = tk.Button(master=window, text="=", command=lambda: Calculate(), width=WIDTH1, height=HEIGHT1, font=FONT1)
btn_brkt_left.grid(row=2, column=0, sticky="nsew")
btn_brkt_right.grid(row=2, column=1, sticky="nsew")
btn_pi.grid(row=2, column=2, sticky="nsew")
btn_cal.grid(row=6, column=3, sticky="nsew")

window.mainloop()