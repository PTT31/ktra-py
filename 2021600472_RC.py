from tkinter import *
import math

class MachDaoDongLC:
    def __init__(self, ten, gia_tri_L, gia_tri_C):
        self.ten = ten
        self.gia_tri_L = gia_tri_L
        self.gia_tri_C = gia_tri_C

    def tinh_tan_so_dao_dong(self):
        return 1 / (2 * math.pi * math.sqrt(self.gia_tri_L * self.gia_tri_C))

def nhap_danh_sach_dao_dong_lc():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_dao_dong_lc.append(MachDaoDongLC(entry2.get(), float(entry3.get()), float(entry4.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập tên của mạch đạo động LC {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập giá trị của L (H) của mạch đạo động LC {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập giá trị của C (F) của mạch đạo động LC {}: ".format(i+1))
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

def in_danh_sach_dao_dong_lc():
    Label(root, text="Danh sách mạch đạo động LC:").pack()
    for i, dao_dong_lc in enumerate(ds_dao_dong_lc):
        label = Label(root, text="Mạch đạo động LC {}: Tên = {}, Giá trị của L = {}, Giá trị của C = {}, Tần số dao động = {}".format(i+1, dao_dong_lc.ten, dao_dong_lc.gia_tri_L, dao_dong_lc.gia_tri_C, dao_dong_lc.tinh_tan_so_dao_dong()))
        label.pack()

def sap_xep_danh_sach_giam_tan_so_dao_dong():
    ds_dao_dong_lc.sort(key=lambda x: x.tinh_tan_so_dao_dong(), reverse=True)
    Label(root, text="Danh sách mạch đạo động LC được sắp xếp theo thứ tự giảm dần của tần số dao động:").pack()
    for i, dao_dong_lc in enumerate(ds_dao_dong_lc):
        label = Label(root, text="Mạch đạo động LC {}: Tên = {}, Giá trị của L = {}, Giá trị của C = {}, Tần số dao động = {}".format(i+1, dao_dong_lc.ten, dao_dong_lc.gia_tri_L, dao_dong_lc.gia_tri_C, dao_dong_lc.tinh_tan_so_dao_dong()))
        label.pack()

def tim_mach_co_tan_so_lon_nhat():
    max_tan_so = max(dao_dong_lc.tinh_tan_so_dao_dong() for dao_dong_lc in ds_dao_dong_lc)
    mach_co_tan_so_lon_nhat = [dao_dong_lc for dao_dong_lc in ds_dao_dong_lc if dao_dong_lc.tinh_tan_so_dao_dong() == max_tan_so]
    Label(root, text="Mạch đạo động LC có tần số lớn nhất:").pack()
    for i, dao_dong_lc in enumerate(mach_co_tan_so_lon_nhat):
        label = Label(root, text="Mạch đạo động LC {}: Tên = {}, Giá trị của L = {}, Giá trị của C = {}, Tần số dao động = {}".format(i+1, dao_dong_lc.ten, dao_dong_lc.gia_tri_L, dao_dong_lc.gia_tri_C, dao_dong_lc.tinh_tan_so_dao_dong()))
        label.pack()

ds_dao_dong_lc = []

root = Tk()
root.title("Quản lý mạch đạo động LC")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng mạch đạo động LC:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_dao_dong_lc)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_dao_dong_lc)
button2.pack()
button3 = Button(root, text="Sắp xếp giảm dần theo tần số dao động", state=DISABLED, command=sap_xep_danh_sach_giam_tan_so_dao_dong)
button3.pack()
button4 = Button(root, text="Tìm mạch có tần số lớn nhất", state=DISABLED, command=tim_mach_co_tan_so_lon_nhat)
button4.pack()
button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
