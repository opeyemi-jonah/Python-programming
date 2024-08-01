import tkinter as tk

count = 0
top = tk.Tk()
btn = tk.Button(text='Click me please')
resetBtn = tk.Button(text='Reset')
def Clicked():
    global count
    count = count + 1
    print('I was clicked!')
    btn.config(text=f'I was clicked {count} times')
    return count

def Reset():
    global count
    count = 0
    btn.config(text=f'I was clicked {count} times')
    return count


btn.config(command=Clicked,width=20,height=5)
resetBtn.config(command=Clicked,width=20,height=5)

btn.pack()
resetBtn.pack()

resetBtn.config(text='Reset', command=Reset,width=20, height=5)
tk.mainloop()

