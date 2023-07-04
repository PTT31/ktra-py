from tkinter import *
import math

class MachLocThongThapRC:
    def __init__(self, ten, gia_tri_R, gia_tri_C):
        self.ten = ten
        self.gia_tri_R = gia_tri_R
        self.gia_tri_C = gia_tri_C

    def tinh_tan_so_cat(self):
        return 1 / (2 * math.pi * self.gia_tri_R * self.gia_tri_C)

def nhap_danh_sach_loc_thong_thap():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_loc_thong_thap.append(MachLocThongThapRC(entry2.get(), float(entry3.get()), float(entry4.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập tên của mạch lọc thông thấp RC {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập giá trị của R (Ω) của mạch lọc thông thấp RC {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập giá trị của C (F) của mạch lọc thông thấp RC {}: ".format(i+1))
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
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)

def in_danh_sach_loc_thong_thap():
    Label(root, text="Danh sách mạch lọc thông thấp RC:").pack()
    for i, loc_thong_thap in enumerate(ds_loc_thong_thap):
        label = Label(root, text="Mạch lọc thông thấp RC {}: Tên = {}, Giá trị của R = {}, Giá trị của C = {}, Tần số cắt = {}".format(i+1, loc_thong_thap.ten, loc_thong_thap.gia_tri_R, loc_thong_thap.gia_tri_C, loc_thong_thap.tinh_tan_so_cat()))
        label.pack()

def sap_xep_danh_sach_giam_tan_so_cat():
    ds_loc_thong_thap.sort(key=lambda x: x.gia_tri_R, reverse=True)
    Label(root, text="Danh sách mạch lọc thông thấp RC được sắp xếp theo thứ tự giảm dần của trở kháng:").pack()
    for i, loc_thong_thap in enumerate(ds_loc_thong_thap):
        label = Label(root, text="Mạch lọc thông thấp RC {}: Tên = {}, Giá trị của R = {}, Giá trị của C = {}, Tần số cắt = {}".format(i+1, loc_thong_thap.ten, loc_thong_thap.gia_tri_R, loc_thong_thap.gia_tri_C, loc_thong_thap.tinh_tan_so_cat()))
        label.pack()

def tim_mach_dai_thong_nhat():
    mach_max = max(ds_loc_thong_thap, key=lambda x: x.tinh_tan_so_cat())
    label = Label(root, text="Mạch lọc thông thấp RC có dải thông lớn nhất: Tên = {}, Giá trị của R = {}, Giá trị của C = {}, Tần số cắt = {}".format(mach_max.ten, mach_max.gia_tri_R, mach_max.gia_tri_C, mach_max.tinh_tan_so_cat()))
    label.pack()

ds_loc_thong_thap = []

root = Tk()
root.title("Quản lý mạch lọc thông thấp RC")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng mạch lọc thông thấp RC:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_loc_thong_thap)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_loc_thong_thap)
button2.pack()
button3 = Button(root, text="Sắp xếp theo trở kháng giảm dần", state=DISABLED, command=sap_xep_danh_sach_giam_tan_so_cat)
button3.pack()
button4 = Button(root, text="Tìm mạch có dải thông lớn nhất", state=DISABLED, command=tim_mach_dai_thong_nhat)
button4.pack()
button6 = Button(root, text="Thêm mạch")
button6.pack()
button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()

root.mainloop()
