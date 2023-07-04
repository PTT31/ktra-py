from tkinter import *
import math
class MachMUX:
    def __init__(self, ten, so_dau_vao, so_dau_ra):
        self.ten = ten
        self.so_dau_vao = so_dau_vao
        self.so_dau_ra = so_dau_ra

    def tinh_so_duong_dieu_khien(self):
        return int(math.log2(self.so_dau_vao / self.so_dau_ra))

def nhap_danh_sach_mux():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_mux.append(MachMUX(entry2.get(), int(entry3.get()), int(entry4.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập tên của mạch MUX {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập số bit đầu vào của mạch MUX {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập số bit đầu ra của mạch MUX {}: ".format(i+1))
        label4.pack()
        entry4 = Entry(nf)
        entry4.pack()
        nf.pack()
        button6.wait_variable(var)
        nf.destroy()
       
    button1.config(state=DISABLED)
    entry1.config(state=DISABLED)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=NORMAL)
    button6.config(state=DISABLED)

def in_danh_sach_mux():
    Label(root, text="Danh sách mạch MUX:").pack()
    for i, mux in enumerate(ds_mux):
        label = Label(root, text="Mạch MUX {}: Tên = {}, Số bit đầu vào = {}, Số bit đầu ra = {}".format(i+1, mux.ten, mux.so_dau_vao, mux.so_dau_ra))
        label.pack()

def sap_xep_danh_sach_giam_so_bit_dau_vao():
    ds_mux.sort(key=lambda x: x.so_dau_vao, reverse=True)
    Label(root, text="Danh sách mạch MUX được sắp xếp theo thứ tự giảm dần của số bit đầu vào:").pack()
    for i, mux in enumerate(ds_mux):
        label = Label(root, text="Mạch MUX {}: Tên = {}, Số bit đầu vào = {}, Số bit đầu ra = {}".format(i+1, mux.ten, mux.so_dau_vao, mux.so_dau_ra))
        label.pack()

def tim_mux_nhieu_duong_dieu_khien_nhat():
    max_duong_dieu_khien = max(mux.tinh_so_duong_dieu_khien() for mux in ds_mux)
    mux_co_nhieu_duong_dieu_khien = [mux for mux in ds_mux if mux.tinh_so_duong_dieu_khien() == max_duong_dieu_khien]
    Label(root, text="Mạch MUX có nhiều đường điều khiển nhất:").pack()
    for i, mux in enumerate(mux_co_nhieu_duong_dieu_khien):
        label = Label(root, text="Mạch MUX {}: Tên = {}, Số bit đầu vào = {}, Số bit đầu ra = {}".format(i+1, mux.ten, mux.so_dau_vao, mux.so_dau_ra))
        label.pack()

ds_mux = []

root = Tk()
root.title("Quản lý mạch MUX")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng mạch MUX:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_mux)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_mux)
button2.pack()
button3 = Button(root, text="Sắp xếp giảm dần theo số bit đầu vào", state=DISABLED, command=sap_xep_danh_sach_giam_so_bit_dau_vao)
button3.pack()
button4 = Button(root, text="Tìm mạch MUX có nhiều đường điều khiển nhất", state=DISABLED, command=tim_mux_nhieu_duong_dieu_khien_nhat)
button4.pack()
button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
