from tkinter import *

class HinhTru:
    def __init__(self, ten, duong_kinh, do_cao):
        self.ten = ten
        self.duong_kinh = duong_kinh
        self.do_cao = do_cao

    def dien_tich_xung_quanh(self):
        chu_vi_day = 3.14 * self.duong_kinh
        return chu_vi_day * self.do_cao

    def tinh_the_tich(self):
        ban_kinh = self.duong_kinh / 2
        return 3.14 * ban_kinh * ban_kinh * self.do_cao

ds_hinh_tru = []
def nhap_danh_sach_hinh_tru():
    n = int(entry1.get())
    var = IntVar()
    def add():
        ds_hinh_tru.append(HinhTru(entry2.get(), float(entry3.get()), float(entry4.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập tên của hình trụ {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập đường kính của hình trụ {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập độ cao của hình trụ {}: ".format(i+1))
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
    return ds_hinh_tru

def in_danh_sach_hinh_tru():
    Label(root,text="Danh sach hinh tru la: ").pack()
    for i, hinh_tru in enumerate(ds_hinh_tru):
        label = Label(root, text="Hình trụ {}: Tên = {}, Đường kính = {}, Độ cao = {}".format(i+1, hinh_tru.ten, hinh_tru.duong_kinh, hinh_tru.do_cao))
        label.pack()

def tim_hinh_tru_co_the_tich_lon_nhat():
    hinh_tru_lon_nhat = max(ds_hinh_tru, key=lambda h: h.tinh_the_tich())
    label = Label(root, text="Hình trụ có thể tích lớn nhất: Tên = {}, Đường kính = {}, Độ cao = {}".format(hinh_tru_lon_nhat.ten, hinh_tru_lon_nhat.duong_kinh, hinh_tru_lon_nhat.do_cao))
    label.pack()

def tim_hinh_tru_co_the_tich_nho_nhat():
    hinh_tru_nho_nhat = min(ds_hinh_tru, key=lambda h: h.tinh_the_tich())
    label = Label(root, text="Hình trụ có thể tích nhỏ nhất: Tên = {}, Đường kính = {}, Độ cao = {}".format(hinh_tru_nho_nhat.ten, hinh_tru_nho_nhat.duong_kinh, hinh_tru_nho_nhat.do_cao))
    label.pack()

def tinh_tong_dien_tich_xung_quanh():
    tong_dien_tich = sum(hinh_tru.dien_tich_xung_quanh() for hinh_tru in ds_hinh_tru)
    label = Label(root, text="Tổng diện tích xung quanh các hình trụ trong danh sách: {}".format(tong_dien_tich))
    label.pack()

root = Tk()
root.title("Quản lý hình trụ")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng hình trụ:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_hinh_tru)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_hinh_tru)
button2.pack()
button3 = Button(root, text="Tìm hình trụ có thể tích lớn nhất", state=DISABLED, command=tim_hinh_tru_co_the_tich_lon_nhat)
button3.pack()
button4 = Button(root, text="Tìm hình trụ có thể tích nhỏ nhất", state=DISABLED, command=tim_hinh_tru_co_the_tich_nho_nhat)
button4.pack()
button5 = Button(root, text="Tính tổng diện tích xung quanh", state=DISABLED, command=tinh_tong_dien_tich_xung_quanh)
button5.pack()
button6 = Button(root,text='Nhap')
button6.pack()
root.mainloop()
