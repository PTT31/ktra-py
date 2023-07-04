from tkinter import *

class PhuongTrinhBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_nghiem(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta > 0:
            x1 = (-self.b + delta ** 0.5) / (2 * self.a)
            x2 = (-self.b - delta ** 0.5) / (2 * self.a)
            return (x1, x2)
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return (x,)
        else:
            return ()

def nhap_danh_sach_phuong_trinh():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_phuong_trinh.append(PhuongTrinhBac2(float(entry2.get()), float(entry3.get()), float(entry4.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập hệ số a của phương trình {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập hệ số b của phương trình {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập hệ số c của phương trình {}: ".format(i+1))
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

def in_danh_sach_phuong_trinh():
    Label(root, text="Danh sách phương trình:").pack()
    for i, pt in enumerate(ds_phuong_trinh):
        nghiem = pt.tinh_nghiem()
        label = Label(root, text="Phương trình {}: a = {}, b = {}, c = {}, Nghiệm = {}".format(i+1, pt.a, pt.b, pt.c, nghiem))
        label.pack()

def dem_phuong_trinh_vo_nghiem():
    count = sum(1 for pt in ds_phuong_trinh if not pt.tinh_nghiem())
    label = Label(root, text="Số phương trình vô nghiệm: {}".format(count))
    label.pack()

def dem_nghiem_duong():
    count = sum(1 for pt in ds_phuong_trinh if any(x > 0 for x in pt.tinh_nghiem()))
    label = Label(root, text="Số phương trình có nghiệm dương: {}".format(count))
    label.pack()

ds_phuong_trinh = []

root = Tk()
root.title("Quản lý phương trình bậc 2")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng phương trình:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_phuong_trinh)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_phuong_trinh)
button2.pack()
button3 = Button(root, text="Đếm phương trình vô nghiệm", state=DISABLED, command=dem_phuong_trinh_vo_nghiem)
button3.pack()
button4 = Button(root, text="Đếm nghiệm dương", state=DISABLED, command=dem_nghiem_duong)
button4.pack()
button5 = Button(root, text="Đếm nghiệm dương", state=DISABLED, command=dem_nghiem_duong)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
