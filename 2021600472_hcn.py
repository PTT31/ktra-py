from tkinter import *

class HinhHopChuNhat:
    def __init__(self, chieu_dai, chieu_rong, do_cao):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        self.do_cao = do_cao

    def dien_tich_toan_phan(self):
        return 2 * (self.chieu_dai * self.chieu_rong + self.chieu_dai * self.do_cao + self.chieu_rong * self.do_cao)

    def tinh_the_tich(self):
        return self.chieu_dai * self.chieu_rong * self.do_cao
ds_hinh_hop_chu_nhat = []
# def nhap_hinh_hop_chu_nhat():
#     n = int(input("Nhập số lượng hình hộp chữ nhật: "))
#     for i in range(n):
#         chieu_dai = float(input("Nhập chiều dài của hình {}: ".format(i+1)))
#         chieu_rong = float(input("Nhập chiều rộng của hình {}: ".format(i+1)))
#         do_cao = float(input("Nhập độ cao của hình {}: ".format(i+1)))
#         hinh_hop_chu_nhat = HinhHopChuNhat(chieu_dai, chieu_rong, do_cao)
#         ds_hinh_hop_chu_nhat.append(hinh_hop_chu_nhat)
#     return ds_hinh_hop_chu_nhat

def in_danh_sach_hinh_hop_chu_nhat(ds_hinh_hop_chu_nhat):
    Label(root,text="Danh sach hinmh chu nhat: ").pack()
    for i, hinh_hop_chu_nhat in enumerate(ds_hinh_hop_chu_nhat):
        print("Hình {}: Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(i+1, hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao))
        Label(root,text="Hình {}: Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(i+1, hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao)).pack()

def tim_hinh_hop_chu_nhat_theo_the_tich(ds_hinh_hop_chu_nhat):
    ds_hinh_hop_chu_nhat_theo_the_tich = tuple(filter(lambda h: h.tinh_the_tich() > 50, ds_hinh_hop_chu_nhat))
    return ds_hinh_hop_chu_nhat_theo_the_tich

def sap_xep_theo_the_tich(ds_hinh_hop_chu_nhat):
    ds_hinh_hop_chu_nhat.sort(key=lambda h: h.tinh_the_tich(), reverse=True)
    return ds_hinh_hop_chu_nhat

# Giao diện sử dụng Tkinter
root = Tk()

# Tạo các đối tượng giao diện
label1 = Label(root, text="Nhập số lượng hình hộp chữ nhật:")
label1.pack()
entry1 = Entry(root)
entry1.pack()

def create_rectangle_objects():
    n = int(entry1.get())
    var = IntVar()
    # ds_hinh_hop_chu_nhat = []
    def add():
            ds_hinh_hop_chu_nhat.append(HinhHopChuNhat(float(entry2.get()), float(entry3.get()), float(entry4.get())))
            var.set(1)
    button5.configure(command=add)
    for i in range(n):
        nf = Frame(root)
        label2 = Label(nf, text="Nhập chiều dài của hình {}: ".format(i+1))
        label2.pack()
        entry2 = Entry(nf)
        entry2.pack()
        label3 = Label(nf, text="Nhập chiều rộng của hình {}: ".format(i+1))
        label3.pack()
        entry3 = Entry(nf)
        entry3.pack()
        label4 = Label(nf, text="Nhập độ cao của hình {}: ".format(i+1))
        label4.pack()
        entry4 = Entry(nf)
        entry4.pack()
        nf.pack()
        button5.wait_variable(var)
        nf.destroy()
    button1.config(state=DISABLED)
    entry1.config(state=DISABLED)
    button5.config(state=DISABLED)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    return ds_hinh_hop_chu_nhat

button1 = Button(root, text="Tạo danh sách", command=create_rectangle_objects)
button1.pack()

def print_rectangle_list():
    # ds_hinh_hop_chu_nhat = create_rectangle_objects()
    in_danh_sach_hinh_hop_chu_nhat(ds_hinh_hop_chu_nhat)

button2 = Button(root, text="In danh sách", state=DISABLED, command=print_rectangle_list)
button2.pack()

def filter_rectangles():
    # ds_hinh_hop_chu_nhat = create_rectangle_objects()
    ds_hinh_hop_chu_nhat_theo_the_tich = tim_hinh_hop_chu_nhat_theo_the_tich(ds_hinh_hop_chu_nhat)
    Label(root,text="Hình có thể tích > 50").pack()
    for hinh_hop_chu_nhat in ds_hinh_hop_chu_nhat_theo_the_tich:
        print("Hình có thể tích > 50: Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao))
        Label(root,text="Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao)).pack()
button3 = Button(root, text="Lọc hình có thể tích > 50", state=DISABLED, command=filter_rectangles)
button3.pack()

def sort_rectangles():
    # ds_hinh_hop_chu_nhat = create_rectangle_objects()
    ds_hinh_hop_chu_nhat_sap_xep = sap_xep_theo_the_tich(ds_hinh_hop_chu_nhat)
    Label(root,text="Hình được sắp xếp theo thứ tự giảm dần của thể tích:").pack()
    for i,hinh_hop_chu_nhat in enumerate(ds_hinh_hop_chu_nhat_sap_xep):
        print("Hình được sắp xếp theo thứ tự giảm dần của thể tích: Hình {}  Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(i,hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao))
        Label(root,text=" Hình {} Chiều dài = {}, Chiều rộng = {}, Độ cao = {}".format(i,hinh_hop_chu_nhat.chieu_dai, hinh_hop_chu_nhat.chieu_rong, hinh_hop_chu_nhat.do_cao)).pack()
button4 = Button(root, text="Sắp xếp theo thể tích",state=DISABLED, command=sort_rectangles)
button4.pack()
button5 = Button(root,text='Nhap')
button5.pack()
root.mainloop()
