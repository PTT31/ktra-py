from tkinter import *

class Ga:
    def __init__(self, loai, tuoi, gioi_tinh):
        self.loai = loai
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh

    def tinh_so_trung(self):
        if self.loai == "Gà ri" and self.tuoi > 45:
            return self.tuoi - 45
        elif self.loai == "Gà lai" and self.tuoi > 30:
            return 2 * (self.tuoi - 30)
        elif self.tuoi > 35:
            return self.tuoi - 35
        else:
            return 0

ds_ga = []

def nhap_danh_sach_ga():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_ga.append(Ga(entry2.get(), int(entry3.get()), entry4.get()))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập loại gà {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập tuổi gà {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập giới tính gà {}: ".format(i+1))
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

def in_danh_sach_ga():
    Label(root, text="Danh sách gà: ").pack()
    for i, ga in enumerate(ds_ga):
        label = Label(root, text="Gà {}: Loại = {}, Tuổi = {}, Giới tính = {}".format(i+1, ga.loai, ga.tuoi, ga.gioi_tinh))
        label.pack()

def tinh_tong_so_trung():
    tong_so_trung = sum(ga.tinh_so_trung() for ga in ds_ga)
    label = Label(root, text="Tổng số trứng đàn gà đã đẻ: {}".format(tong_so_trung))
    label.pack()

def dem_ga_trong_ri_va_so_trung_ga_ri():
    dem_ga_trong_ri = 0
    so_trung_ga_ri = 0
    for ga in ds_ga:
        if ga.loai == "gà ri":
            dem_ga_trong_ri += 1
            so_trung_ga_ri += ga.tinh_so_trung()
    label1 = Label(root, text="Số con gà trống ri: {}".format(dem_ga_trong_ri))
    label1.pack()
    label2 = Label(root, text="Số trứng gà ri: {}".format(so_trung_ga_ri))
    label2.pack()

root = Tk()
root.title("Quản lý gà")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng gà:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_ga)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_ga)
button2.pack()
button3 = Button(root, text="Tính tổng số trứng", state=DISABLED, command=tinh_tong_so_trung)
button3.pack()
button4 = Button(root, text="Đếm gà trống ri và số trứng gà ri", state=DISABLED, command=dem_ga_trong_ri_va_so_trung_ga_ri)
button4.pack()
button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
