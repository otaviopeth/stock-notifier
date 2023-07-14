from stock import *
from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import simpledialog
import time

wnd = Tk()
wnd.title("Notifier")
wnd.geometry("300x400")
wnd.resizable(False, False)
background_image = PhotoImage(file="bg.png")
lb_bg = Label(wnd, image=background_image)
lb_bg.place(x=0, y=0, relwidth=1, relheight=1)


# Update the Entry widget with the selected item in list


def check(e):
    v = entry.get()
    if v == '':
        data = values
    else:
        data = []
        for item in values:
            if v.lower() in item.lower():
                data.append(item)
    update(data)


def update(data):
    # Clear the Combobox
    menu.delete(0, END)
    # Add values to the combobox
    for value in data:
        menu.insert(END, value)


def selected_item():
    menu_stock = menu.get(ACTIVE)
    desired_price = txt_price.get('1.0', END)
    try:
        # Convert it into float
        float(desired_price)
    except ValueError:
        messagebox.showerror('Erro', 'Insira um valor válido!')
        return
    new_stock = Stock(menu_stock, txt_price.get('1.0', END))
    stock_mon_list.append(new_stock)
    txt_price.delete('1.0', END)


def start_monitor():
    if stock_mon_list:
        global monitor_flag
        monitor_flag += 1
        if monitor_flag == 1:
            btn_add.pack_forget()
            btn_mon.pack_forget()
            btn_stop.pack()
        for index, item in enumerate(stock_mon_list):
            print(monitor_flag)
            response = item.monitor(msg_to)
            if response:
                del stock_mon_list[index]
    else:
        messagebox.showerror('Erro', 'Adicione uma ação!')
    wnd.after(5000000, start_monitor())


def stop_monitor():
    wnd.after_cancel(after_id)
    global monitor_flag
    monitor_flag = 0
    stock_mon_list.clear()
    btn_stop.pack_forget()
    btn_add.pack(side=TOP, pady=20)
    btn_mon.pack(side=TOP, pady=5)


# Add a Bottom Label
lb_1 = Label(wnd, text="Selecione uma ação:", font=font.Font(family='Helvetica'))
lb_1.pack(padx=15, pady=20)

# Create an Entry widget
entry = Entry(wnd, width=35)
entry.pack()
entry.bind('<KeyRelease>', check)

# Create a Listbox widget to display the list of items
menu = Listbox(wnd)
menu.pack()
# Add values to our combobox
values = Stock.import_stocks()
values.sort()
update(values)

txt_price = Text(wnd, height=1, width=5)
txt_price.pack(side=TOP, pady=2)

btn_add = Button(wnd, text="Adicionar", command=selected_item)
btn_add.pack(side=TOP, pady=20)

btn_mon = Button(wnd, text="Monitorar", bg='#2596be', width=15, command=start_monitor)
btn_mon.pack(side=TOP, pady=5)

btn_stop = Button(wnd, text="Parar", bg='red', width=15, command=stop_monitor)

msg_to = simpledialog.askstring(title="E-mail", prompt="Cadastre o e-mail de destino.")

stock_mon_list = []
monitor_flag = 0
after_id = 0
wnd.mainloop()
