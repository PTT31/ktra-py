from tkinter import *

class SinhVien:
    def __init__(self, ten, diem_bao_cao, diem_thiet_ke_pc, diem_thiet_ke_pm, diem_thuyet_trinh):
        self.ten = ten
        self.diem_bao_cao = diem_bao_cao
        self.diem_thiet_ke_pc = diem_thiet_ke_pc
        self.diem_thiet_ke_pm = diem_thiet_ke_pm
        self.diem_thuyet_trinh = diem_thuyet_trinh

    def tinh_tong_diem(self):
        return self.diem_bao_cao + self.diem_thiet_ke_pc + self.diem_thiet_ke_pm + self.diem_thuyet_trinh

ds_sinh_vien = []

def nhap_danh_sach_sinh_vien():
    n = int(entry1.get())
    var = IntVar()
    
    def add():
        ds_sinh_vien.append(SinhVien(entry2.get(), float(entry3.get()), float(entry4.get()), float(entry5.get()), float(entry6.get())))
        var.set(1)

    button6.configure(command=add)
    
    for i in range(n):
        nf = Frame(root)
        
        label2 = Label(nf, text="Nhập tên sinh viên {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()

        label3 = Label(nf, text="Nhập điểm báo cáo của sinh viên {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()

        label4 = Label(nf, text="Nhập điểm thiết kế phần cứng của sinh viên {}: ".format(i+1))
        label4.pack()
        entry4 = Entry(nf)
        entry4.pack()

        label5 = Label(nf, text="Nhập điểm thiết kế phần mềm của sinh viên {}: ".format(i+1))
        label5.pack()
        entry5 = Entry(nf)
        entry5.pack()

        label6 = Label(nf, text="Nhập điểm thuyết trình của sinh viên {}: ".format(i+1))
        label6.pack()
        entry6 = Entry(nf)
        entry6.pack()

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

def in_danh_sach_sinh_vien():
    Label(root, text="Danh sách sinh viên:").pack()
    for i, sv in enumerate(ds_sinh_vien):
        label = Label(root, text="Sinh viên {}: Tên = {}, Điểm báo cáo = {}, Điểm thiết kế phần cứng = {}, Điểm thiết kế phần mềm = {}, Điểm thuyết trình = {}".format(i+1, sv.ten, sv.diem_bao_cao, sv.diem_thiet_ke_pc, sv.diem_thiet_ke_pm, sv.diem_thuyet_trinh))
        label.pack()

def sap_xep_danh_sach():
    ds_sinh_vien.sort(key=lambda sv: sv.tinh_tong_diem(), reverse=True)
    Label(root, text="Danh sách sinh viên sau khi được sắp xếp:").pack()
    for i, sv in enumerate(ds_sinh_vien):
        label = Label(root, text="Sinh viên {}: Tên = {}, Tổng điểm = {}".format(i+1, sv.ten, sv.tinh_tong_diem()))
        label.pack()

def tach_danh_sach():
    ds_pm = []
    ds_pc = []

    for sv in ds_sinh_vien:
        if sv.diem_thiet_ke_pm > sv.diem_thiet_ke_pc:
            ds_pm.append(sv)
        else:
            ds_pc.append(sv)

    Label(root, text="Danh sách sinh viên có khả năng thiết kế phần mềm tốt hơn phần cứng:").pack()
    for i, sv in enumerate(ds_pm):
        label = Label(root, text="Sinh viên {}: Tên = {}, Điểm thiết kế phần mềm = {}, Điểm thiết kế phần cứng = {}".format(i+1, sv.ten, sv.diem_thiet_ke_pm, sv.diem_thiet_ke_pc))
        label.pack()

    Label(root, text="Danh sách sinh viên có khả năng thiết kế phần cứng tốt hơn phần mềm:").pack()
    for i, sv in enumerate(ds_pc):
        label = Label(root, text="Sinh viên {}: Tên = {}, Điểm thiết kế phần cứng = {}, Điểm thiết kế phần mềm = {}".format(i+1, sv.ten, sv.diem_thiet_ke_pc, sv.diem_thiet_ke_pm))
        label.pack()

root = Tk()
root.title("Quản lý điểm đồ án tốt nghiệp")
root.geometry("400x600")

label1 = Label(root, text="Nhập số lượng sinh viên:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

button1 = Button(root, text="Nhập danh sách", command=nhap_danh_sach_sinh_vien)
button1.pack()

button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_sinh_vien)
button2.pack()

button3 = Button(root, text="Sắp xếp danh sách", state=DISABLED, command=sap_xep_danh_sach)
button3.pack()

button4 = Button(root, text="Tách danh sách", state=DISABLED, command=tach_danh_sach)
button4.pack()

button5 = Button(root, text="Thoát", command=root.quit)
button5.pack()

button6 = Button(root, text="Nhập")
button6.pack()

root.mainloop()
