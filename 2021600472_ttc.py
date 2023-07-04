from tkinter import *

class ttc:
    def __init__ (self,ten,sl,gia):
        self.ten = ten
        self.sl = sl
        self.gia = gia
    def tinh_cong(self):
        return int(self.sl * self.gia)
lttc = []
def nhap():
    var = IntVar()
    try:
        n = int(entry1.get())
    except:
        print("Nhap lai!")
    def add():
        try:
            lttc.append(ttc(entry2.get(),int(entry3.get()),int(entry4.get())))
            var.set(1)
        except:
            print("Nhap Lai!")
    button5.config(command=add)
    for i in range(0,n):
        nf = Frame(root)
        
        Label(nf,text="Nhap ten tho {}".format(i+1)).pack()
        entry2 = Entry(nf)
        entry2.pack()
        Label(nf,text="Nhap So tham det duoc tho thu {}".format(i+1)).pack()
        entry3 = Entry(nf)
        entry3.pack()
        Label(nf,text="Nhap gia tham tho thu {}".format(i+1)).pack()
        entry4 = Entry(nf)
        entry4.pack()
        nf.pack()
        button5.wait_variable(var)
        nf.destroy()
    button1.config(state=DISABLED)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)
    button4.config(state=NORMAL)
    button5.config(state=DISABLED)
def in_danh_sach():
    for i,x in enumerate(lttc):
        Label(root,text="Tho {}, ten : {}, ns : {}, don gia : {}".format(i+1,x.ten,x.sl,x.gia)).pack()
def dem():
    Label(root,text="Tho co thu nhap cao nhat la: ").pack()
    maxt = max(lttc,key=lambda t:t.tinh_cong())
    i = 0
    for x in lttc:
        if x.tinh_cong() == maxt.tinh_cong():
            i += 1
            Label(root,text="Tho {}, ten : {}, ns : {}, don gia : {}".format(i,x.ten,x.sl,x.gia)).pack()
    Label(root,text="co {} tho cao nhat".format(i)).pack()
def tupple_ds():
    t = []
    Label(root,text="Tho co thu nhap thap nhat la: ").pack()
    maxt = min(lttc,key=lambda t:t.tinh_cong())
    for x in lttc:
        if x.tinh_cong() == maxt.tinh_cong():
            t.append(x)
    a = tuple(t)
    print(type(a))            
    print(a[0].ten)
    for x in a:
        Label(root,text=x.ten).pack()
root = Tk()
Label(root,text="Nhap so luong tho thu cong: ").pack()
entry1 = Entry(root)
entry1.pack()
button1 = Button(root,text='Xac Nhan',command=nhap)
button1.pack()
button2 = Button(root,text="In danh sach",state=DISABLED,command=in_danh_sach)
button2.pack()
button3 = Button(root,text="Dem va hien thi: ",state=DISABLED,command=dem)
button3.pack()
button4 = Button(root,text="Tao tuple",state=DISABLED,command=tupple_ds)
button4.pack()
button5 = Button(root,text='Nhap')
button5.pack()

root.mainloop()