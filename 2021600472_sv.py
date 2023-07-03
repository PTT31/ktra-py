from tkinter import *
class sv:
    def __init__(self,ten,msv,toan,ly,hoa) -> None:
        self.ten = ten
        self.msv = msv
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def diemtb(self):
        P = self.hoa + self.toan + self.ly
        return P/3
def nhap_sv():
    def add():
        try:
            l.append(sv(ten.get(),msv.get(),float(toan.get()),float(ly.get()),float(hoa.get())))
        except ValueError:
            print("nhap lai!")
        else:
            var.set(1)
    ten = StringVar()
    msv = StringVar()
    toan = StringVar()
    ly = StringVar()
    hoa = StringVar()
    var = IntVar(value=0)
    Label(window,text='Nhap ten sv: ').grid(column=2,row=0)
    Entry(window,textvariable=ten).grid(column=2,row=1)
    Label(window,text='Nhap msv: ').grid(column=3,row=0)
    Entry(window,textvariable=msv).grid(column=3,row=1)
    Label(window,text='Nhap toan: ').grid(column=4,row=0)
    Entry(window,textvariable=toan).grid(column=4,row=1)
    Label(window,text='Nhap ly: ').grid(column=5,row=0)
    Entry(window,textvariable=ly).grid(column=5,row=1)
    Label(window,text='Nhap hoa: ').grid(column=6,row=0)
    Entry(window,textvariable=hoa).grid(column=6,row=1)
    nhapsv.grid(column=0,row=7)
    nhapsv.configure(command=add)
    nhapsv.wait_variable(var)

def nhap():
    try:
        n = int(soluong.get())
    except ValueError:
        print('Nhap lai!')
    else:
        for x in range(0,n):
            nhap_sv()
    tbm.grid(column= 7,row= 2)
    nhapsv.destroy()
    print(n)
    hienthi(l,n,2)
    tb()

def tb():
    for x in l:
        if (x.diemtb() < 5):
            l1.append(x)
        else:
            l2.append(x)
    if(l1 != None):
        hienthi(l1,len(l1),int(soluong.get())*2)
    if(l2 != None):
        hienthi(l2,len(l2),int(soluong.get())*3)            
def hienthi(li,n,r):
    for x in range(0,n):
        Label(window,text=str(x+1)).grid(column=0,row=r)
        Label(window,text=str(li[x].ten)).grid(column=1,row=r)
        Label(window,text=str(li[x].msv)).grid(column=2,row=r)
        Label(window,text=str(li[x].toan)).grid(column=3,row=r)
        Label(window,text=str(li[x].ly)).grid(column=4,row=r)
        Label(window,text=str(li[x].hoa)).grid(column=5,row=r)
        r += 1
def diem_tb_mon():
    toan_t = 0
    ly_t = 0
    hoa_t = 0
    for x in range(0,len(l)):
        toan_t += l[x].toan
        ly_t += l[x].ly
        hoa_t += l[x].hoa
    toan_tb = toan_t/len(l)
    ly_tb = ly_t/len(l)
    hoa_tb = hoa_t/len(l)
    ltb = [toan_tb,ly_tb,hoa_tb]
    print(ltb)

     
l = []
l1 = []
l2 = []
window = Tk()
soluong = StringVar()
Label(window, text='Nhap so luong sinh vien: ').grid(column=0,row = 0)
Entry(window,textvariable=soluong).grid(column=0,row=1)
Button(window,text='Xac Nhan',command=nhap).grid(column=1,row=1)
nhapsv = Button(window,text='Nhap')
tbm = Button(window,text='tinh tb mon',command=diem_tb_mon)
window.mainloop()

