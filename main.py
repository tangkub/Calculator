# Calculator projects

# modules
import tkinter as tk
import parser
from math import sqrt, pi
from tkinter import font



class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # constant
        self.WIDTH1 = 8
        self.HEIGHT1 = 3
        self.FONT1 = ("Helvetica", 16)
        self.FONT2 = ("Helvetica", 20)

        # GUI
        # window
        self.title("Calculator")
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)
        self.columnconfigure([0, 1, 2, 3], weight=1)

        # entry
        self.ent_display = tk.Entry(master=self, font=self.FONT2, justify="right")
        self.ent_display.grid(row=0, columnspan=4, sticky="nsew", ipady=20)

        # button
        # number button
        self.btn_num1 = tk.Button(master=self, text="1", command=lambda: self.GetVar(1), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num2 = tk.Button(master=self, text="2", command=lambda: self.GetVar(2), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num3 = tk.Button(master=self, text="3", command=lambda: self.GetVar(3), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num1.grid(row=5, column=0, sticky="nsew")
        self.btn_num2.grid(row=5, column=1, sticky="nsew")
        self.btn_num3.grid(row=5, column=2, sticky="nsew")

        self.btn_num4 = tk.Button(master=self, text="4", command=lambda: self.GetVar(4), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num5 = tk.Button(master=self, text="5", command=lambda: self.GetVar(5), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num6 = tk.Button(master=self, text="6", command=lambda: self.GetVar(6), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num4.grid(row=4, column=0, sticky="nsew")
        self.btn_num5.grid(row=4, column=1, sticky="nsew")
        self.btn_num6.grid(row=4, column=2, sticky="nsew")

        self.btn_num7 = tk.Button(master=self, text="7", command=lambda: self.GetVar(7), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num8 = tk.Button(master=self, text="8", command=lambda: self.GetVar(8), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num9 = tk.Button(master=self, text="9", command=lambda: self.GetVar(9), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num7.grid(row=3, column=0, sticky="nsew")
        self.btn_num8.grid(row=3, column=1, sticky="nsew")
        self.btn_num9.grid(row=3, column=2, sticky="nsew")

        # AC | 0 | . button
        self.btn_ac = tk.Button(master=self, text="AC", command=lambda: self.ClearAll(), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_num0 = tk.Button(master=self, text="0", command=lambda: self.GetVar(0), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_dot = tk.Button(master=self, text=".", command=lambda: self.GetVar("."), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_ac.grid(row=6, column=0, sticky="nsew")
        self.btn_num0.grid(row=6, column=1, sticky="nsew")
        self.btn_dot.grid(row=6, column=2, sticky="nsew")

        # operator button
        self.btn_plus = tk.Button(master=self, text="+", command=lambda: self.GetOpt("+"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_minus = tk.Button(master=self, text="-", command=lambda: self.GetOpt("-"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_multi = tk.Button(master=self, text="*", command=lambda: self.GetOpt("*"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_divide = tk.Button(master=self, text="/", command=lambda: self.GetOpt("/"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_plus.grid(row=2, column=3, sticky="nsew")
        self.btn_minus.grid(row=3, column=3, sticky="nsew")
        self.btn_multi.grid(row=4, column=3, sticky="nsew")
        self.btn_divide.grid(row=5, column=3, sticky="nsew")

        self.btn_exp = tk.Button(master=self, text="X^2", command=lambda: self.GetOpt("**2"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_sqrt = tk.Button(master=self, text="√", command=lambda: self.SquareRoot(), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_flip = tk.Button(master=self, text="1/X", command=lambda: self.Flip(), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_undo = tk.Button(master=self, text="<-", command=lambda: self.Undo(), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_exp.grid(row=1, column=0, sticky="nsew")
        self.btn_sqrt.grid(row=1, column=1, sticky="nsew")
        self.btn_flip.grid(row=1, column=2, sticky="nsew")
        self.btn_undo.grid(row=1, column=3, sticky="nsew")

        self.btn_brkt_left = tk.Button(master=self, text="(", command=lambda: self.GetOpt("("), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_brkt_right = tk.Button(master=self, text=")", command=lambda: self.GetOpt(")"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_pi = tk.Button(master=self, text="π", command=lambda: self.GetOpt("pi"), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_cal = tk.Button(master=self, text="=", command=lambda: self.Calculate(), width=self.WIDTH1, height=self.HEIGHT1, font=self.FONT1)
        self.btn_brkt_left.grid(row=2, column=0, sticky="nsew")
        self.btn_brkt_right.grid(row=2, column=1, sticky="nsew")
        self.btn_pi.grid(row=2, column=2, sticky="nsew")
        self.btn_cal.grid(row=6, column=3, sticky="nsew")

    # function
    # get number and insert to display
    def GetVar(self, num):
        length = len(self.ent_display.get())
        self.ent_display.insert(length, num)

    # get operator and insert to display
    def GetOpt(self, opt):
        opt_len = len(opt)
        length = len(self.ent_display.get())
        self.ent_display.insert(length, opt)

    # remove all characters on display
    def ClearAll(self):
        self.ent_display.delete(0, tk.END)

    # square root of given number
    def SquareRoot(self):
        all_char = self.ent_display.get()
        result = f"sqrt({all_char})"
        length = len(result)
        self.ClearAll()
        self.ent_display.insert(0, result)

    # flip numerator and denominator
    def Flip(self):
        all_char = self.ent_display.get()
        if len(all_char):
            result = f"1/{all_char}"
            length = len(result)
            self.ClearAll()
            self.ent_display.insert(0, result)

    # remove last character
    def Undo(self):
        all_char = self.ent_display.get()
        if len(all_char):
            all_char = all_char[:-1]
            self.ClearAll()
            self.ent_display.insert(0, all_char)

    # fetch input text and evaluate them
    def Calculate(self):
        all_char = self.ent_display.get()
        try:
            result = eval(parser.expr(all_char).compile())
            self.ClearAll()
            self.ent_display.insert(0, result)
        except Exception as e:
            print(f"Error: {e}")
            self.ClearAll()
            self.ent_display.insert(0, "ERROR")

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()