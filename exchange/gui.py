#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import rates


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.update_rates()
        self.pack()
        self.create_widgets()

    def update_rates(self):
        """Check change rates online[NBP]"""
        self.r, self.msg = rates.get()
        print(self.msg)
        self.r["PLN"] = {"currency": "złoty polski", "mid": 1.0}
        self.currencies = sorted(list(self.r.keys()))
    
    def create_widgets(self):
        """Create app layout"""
        self.Max_Frame = ttk.LabelFrame(text="Kalkulator walut" , labelanchor="n")
        # Group everything except button
        self.Main_Frame = ttk.Frame(master=self.Max_Frame)
        # Labels on the left
        self.Label_Frame = ttk.Frame(master=self.Main_Frame)
        self.From_Currency_Label = ttk.Label(master=self.Label_Frame, text="Waluta źródłowa:", )
        self.From_Currency_Label.pack(side=tk.TOP, fill=tk.X)
        self.To_Currency_Label = ttk.Label(master=self.Label_Frame, text="Waluta docelowa:")
        self.To_Currency_Label.pack(side=tk.TOP, fill=tk.X)
        self.Label_Frame.pack(side=tk.LEFT, fill=tk.Y)
        # Middle column
        self.Middle_Frame = ttk.Frame(master=self.Main_Frame)
        self.From_Currency_Input = ttk.Entry(master=self.Middle_Frame)
        self.From_Currency_Input.pack(side=tk.TOP, fill=tk.X)
        self.To_Currency_Value = ttk.Label(master=self.Middle_Frame, text="")
        self.To_Currency_Value.pack(side=tk.TOP, fill=tk.X)
        self.Middle_Frame.pack(side=tk.LEFT, fill=tk.Y)
        # Choosing a currency boxes
        self.Choose_Frame = ttk.Frame(master=self.Main_Frame)
        self.From_Currency = ttk.Combobox(master=self.Choose_Frame, values=self.currencies, state="readonly", width=4)
        self.From_Currency.pack(side=tk.TOP)
        self.To_Currency = ttk.Combobox(master=self.Choose_Frame, values=self.currencies, state="readonly", width=4)
        self.To_Currency.pack(side=tk.TOP)
        self.Choose_Frame.pack(side=tk.LEFT, fill=tk.Y)
        self.Main_Frame.pack()
        # Add button
        self.Calculate_Button = ttk.Button(master = self.Max_Frame, text="Oblicz", command=self.calculate)
        self.Calculate_Button.pack(side=tk.BOTTOM, fill=tk.X)
        self.Max_Frame.pack(fill=tk.BOTH, expand=1)

    def calculate(self):
        """Calculate amount in given currency"""
        user_input = float(self.From_Currency_Input.get())
        from_rate = self.From_Currency.get()
        to_rate = self.To_Currency.get()
        result = user_input * float(self.r[from_rate]["mid"]) / float(self.r[to_rate]["mid"])
        self.To_Currency_Value.configure(text=str(round(result, 2)))