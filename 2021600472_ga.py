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

danh_sach_ga = []

def nhap_danh_sach_ga():
    n = int(entry1.get())
    var = IntVar()
    def add():
        try:
            ga = Ga(entry2.get(), int(entry3.get()), entry4.get())
            danh_sach_ga.append(ga)
            print(entry3.get())
            var.set(1)
        except:
            print('Nhap lai!')
    button5.config(command=add,state=NORMAL)
    button5.pack()
    for i in range(n):
        nf = Frame(root)
        
        

        label2 = Label(nf, text="Loại gà:")
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()

        label3 = Label(nf, text="Tuổi gà:")
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()

        label4 = Label(nf, text="Giới tính:")
        label4.pack()
        entry4 = Entry(nf)
        entry4.pack()
        nf.pack()
        loai = entry2.get()
        tuoi = entry3.get()

        gioi_tinh = entry4.get()
        button5.wait_variable(var)
        nf.destroy()
        
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)

def in_danh_sach_ga():
    text_box.delete("1.0", END)
    text_box.insert(END, "Danh sách gà:\n")
    for i, ga in enumerate(danh_sach_ga):
        text_box.insert(END, "Gà {}: Loại = {}, Tuổi = {}, Giới tính = {}\n".format(i+1, ga.loai, ga.tuoi, ga.gioi_tinh))

def tinh_tong_so_trung():
    tong_so_trung = sum(ga.tinh_so_trung() for ga in danh_sach_ga)
    text_box.insert(END, "Tổng số trứng đàn gà đã đẻ là: {}\n".format(tong_so_trung))

def dem_ga_trong_ri():
    dem_ga_trong_ri = sum(1 for ga in danh_sach_ga if ga.loai == "Gà ri" and ga.gioi_tinh == "Gà trống")
    dem_trung_ga_ri = sum(ga.tinh_so_trung() for ga in danh_sach_ga if ga.loai == "Gà ri" and ga.gioi_tinh == "Gà trống")
    text_box.insert(END, "Số lượng gà trống ri là: {}\n".format(dem_ga_trong_ri))
    text_box.insert(END, "Số quả trứng gà ri là: {}\n".format(dem_trung_ga_ri))

root = Tk()
root.title("Quản lý con gà")
root.geometry("400x400")
label1 = Label(root, text="Nhập số lượng con gà:")
label1.pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Nhập danh sách", command=nhap_danh_sach_ga)
button1.pack()

button2 = Button(root, text="In danh sách", state=DISABLED, command=in_danh_sach_ga)
button2.pack()

button3 = Button(root, text="Tính tổng số trứng", state=DISABLED, command=tinh_tong_so_trung)
button3.pack()

button4 = Button(root, text="Đếm gà trống ri", state=DISABLED, command=dem_ga_trong_ri)
button4.pack()

button5 = Button(root,text='Nhap',state=DISABLED)
button5.pack()


text_box = Text(root, height=10, width=40)
text_box.pack()

root.mainloop()
