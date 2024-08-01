import tkinter as tk

top = tk.Tk()

for row in range(3):
    for col in range(3):
        tk.Button(text=f"row{row}/col{col}").grid(row=row, column=col)
tk.mainloop()