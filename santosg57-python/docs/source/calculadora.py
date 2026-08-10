#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def button_click(button_name):
    if button_name in '0123456789':
        x = float(button_name)
        print(x)
    else:
        print(button_name)
        
root = tk.Tk()
root.title("Calculadora")

b1 = tk.Button(root, text="1", command=lambda: button_click("1"))
b2 = tk.Button(root, text="2", command=lambda: button_click("2"))
b3 = tk.Button(root, text="3", command=lambda: button_click("3"))
b4 = tk.Button(root, text="4", command=lambda: button_click("4"))
b5 = tk.Button(root, text="5", command=lambda: button_click("5"))
b6 = tk.Button(root, text="6", command=lambda: button_click("6"))
b7 = tk.Button(root, text="7", command=lambda: button_click("7"))
b8 = tk.Button(root, text="8", command=lambda: button_click("8"))
b9 = tk.Button(root, text="9", command=lambda: button_click("9"))
b0 = tk.Button(root, text="0", command=lambda: button_click("0"))
mas = tk.Button(root, text="+", command=lambda: button_click("+"))
menos = tk.Button(root, text="-", command=lambda: button_click("-"))
igual = tk.Button(root, text="=", command=lambda: button_click("="))


b1.grid(row=0, column=0, padx=5, pady=5) 
b2.grid(row=0, column=1, padx=5, pady=5)
b3.grid(row=0, column=2, padx=5, pady=5)
b4.grid(row=1, column=0, padx=5, pady=5)
b5.grid(row=1, column=1, padx=5, pady=5)
b6.grid(row=1, column=2, padx=5, pady=5)
b7.grid(row=2, column=0, padx=5, pady=5)
b8.grid(row=2, column=1, padx=5, pady=5)
b9.grid(row=2, column=2, padx=5, pady=5)
b0.grid(row=3, column=0, padx=5, pady=5)
mas.grid(row=3, column=1, padx=5, pady=5)
menos.grid(row=3, column=2, padx=5, pady=5)
igual.grid(row=4, column=0, padx=5, pady=5)
# Start the Tkinter event loop
root.mainloop()

# In[ ]:




# In[ ]:




# In[ ]:



