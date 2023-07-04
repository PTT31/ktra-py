from tkinter import *
import  math
class BoDem:
    def __init__(self, ten, Kd, loai):
        self.ten = ten
        self.Kd = Kd
        self.loai = loai

    def tinh_so_FF(self):
        return math.ceil(math.log(self.Kd))
def nhap_danh_sach_bo_dem():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_bo_dem.append(BoDem(entry2.get(), int(entry3.get()), entry4.get()))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập tên của bộ đếm {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập Kđ của bộ đếm {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập loại của bộ đếm {}: ".format(i+1))
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

def in_danh_sach_JKFF():
    Label(root, text="Danh sách bộ đếm từ JKFF:").pack()
    for i, bd in enumerate(ds_bo_dem):
        if bd.loai == "JKFF":
            label = Label(root, text="Bộ đếm {}: Tên = {}, Kđ = {}, Loại = {}, Số FF: {}".format(i+1, bd.ten, bd.Kd, bd.loai,bd.tinh_so_FF()))
            label.pack()

def sap_xep_danh_sach_giam_Kd():
    ds_bo_dem.sort(key=lambda x: x.Kd, reverse=True)
    Label(root, text="Danh sách bộ đếm được sắp xếp theo thứ tự giảm dần của Kđ:").pack()
    for i, bd in enumerate(ds_bo_dem):
        label = Label(root, text="Bộ đếm {}: Tên = {}, Kđ = {}, Loại = {}".format(i+1, bd.ten, bd.Kd, bd.loai))
        label.pack()

def xoa_bo_dem_Kd_10():
    ds_bo_dem[:] = [bd for bd in ds_bo_dem if bd.Kd != 10]
    Label(root, text="Danh sách bộ đếm sau khi xóa các bộ đếm có Kđ = 10:").pack()
    for i, bd in enumerate(ds_bo_dem):
        label = Label(root, text="Bộ đếm {}: Tên = {}, Kđ = {}, Loại = {}".format(i+1, bd.ten, bd.Kd, bd.loai))
        label.pack()

ds_bo_dem = []

root = Tk()
root.title("Quản lý bộ đếm")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng bộ đếm:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_bo_dem)
button1.pack()
button2 = Button(root, text="In danh sách từ JKFF", state=DISABLED, command=in_danh_sach_JKFF)
button2.pack()
button3 = Button(root, text="Sắp xếp danh sách giảm dần theo Kđ", state=DISABLED, command=sap_xep_danh_sach_giam_Kd)
button3.pack()
button4 = Button(root, text="Xóa các bộ đếm có Kđ = 10", state=DISABLED, command=xoa_bo_dem_Kd_10)
button4.pack()
button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
