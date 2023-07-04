import math
from tkinter import *

class TamGiacVuong:
    def __init__(self, canh_1, canh_2):
        self.canh_1 = canh_1
        self.canh_2 = canh_2

    def tinh_goc(self):
        goc_vuong = 90
        # goc_con_lai = 180 - goc_vuong
        canh_huyen = math.sqrt(self.canh_1**2 + self.canh_2**2)
        goc_a = math.degrees(math.atan(self.canh_1/self.canh_2))
        goc_b = 90 - goc_a
        return goc_vuong, goc_a, goc_b, canh_huyen
danh_sach_tam_giac = []
def nhap_danh_sach_tam_giac():
    n = int(entry1.get())
    var = IntVar()
    def add():
        danh_sach_tam_giac.append(TamGiacVuong(float(entry2.get()), float(entry3.get())))
        var.set(1)
    button6.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập cạnh thứ nhất của tam giác {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập cạnh thứ hai của tam giác {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
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

def in_danh_sach_tam_giac():
    Label(root, text="Danh sách tam giác:").pack()
    for i, tam_giac in enumerate(danh_sach_tam_giac):
        goc_vuong, goc_a , goc_b, canh_huyen = tam_giac.tinh_goc()
        label = Label(root, text="Tam giác {}: Cạnh thứ nhất = {}, Cạnh thứ hai = {}, Góc vuông = {}, Góc a = {:3f} Góc b = {}, Cạnh huyền = {}".format(i+1, tam_giac.canh_1, tam_giac.canh_2, goc_vuong, goc_a,goc_b, canh_huyen))
        label.pack()

def sap_xep_danh_sach_giam_dien_tich():
    danh_sach_tam_giac.sort(key=lambda x: x.canh_1 * x.canh_2 / 2, reverse=True)
    Label(root, text="Danh sách tam giác sau khi được sắp xếp theo diện tích giảm dần:").pack()
    for i, tam_giac in enumerate(danh_sach_tam_giac):
        goc_vuong, goc_a , goc_b, canh_huyen  = tam_giac.tinh_goc()
        label = Label(root, text="Tam giác {}: Cạnh thứ nhất = {}, Cạnh thứ hai = {}, Góc vuông = {}, Góc a = {}, Góc b = {}, Cạnh huyền = {}".format(i+1, tam_giac.canh_1, tam_giac.canh_2, goc_vuong, goc_a,goc_b, canh_huyen))
        label.pack()

def tim_tam_giac_lon_nhat():
    tam_giac_lon_nhat = max(danh_sach_tam_giac, key=lambda x: x.canh_1 * x.canh_2 / 2)
    goc_vuong, goc_a , goc_b, canh_huyen= tam_giac_lon_nhat.tinh_goc()
    label = Label(root, text="Tam giác : Cạnh thứ nhất = {}, Cạnh thứ hai = {}, Góc vuông = {}, Góc a = {}, Góc b = {}, Cạnh huyền = {}".format( tam_giac_lon_nhat.canh_1, tam_giac_lon_nhat.canh_2, goc_vuong, goc_a,goc_b, canh_huyen))
    label.pack()

danh_sach_tam_giac = []

root = Tk()
root.title("Quản lý tam giác vuông")
root.geometry("400x400")

label1 = Label(root, text="Nhập số lượng tam giác:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Tạo danh sách", command=nhap_danh_sach_tam_giac)
button1.pack()
button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_tam_giac)
button2.pack()
button3 = Button(root, text="Sắp xếp theo diện tích", state=DISABLED, command=sap_xep_danh_sach_giam_dien_tich)
button3.pack()
button4 = Button(root, text="Tìm tam giác lớn nhất", state=DISABLED, command=tim_tam_giac_lon_nhat)
button4.pack()
button5 = Button(root, text="Sắp xếp theo diện tích", state=DISABLED, command=sap_xep_danh_sach_giam_dien_tich)
button5.pack()
button6 = Button(root, text="Nhập")
button6.pack()
button6.place(x=300, y=30)

root.mainloop()
