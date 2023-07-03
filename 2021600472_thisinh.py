from tkinter import *
class thisinh:
    def __init__(self,ten,sbd,toan,ly,hoa) -> None:
        self.ten = ten
        self.sbd = sbd
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    def diem_t(self):
        return self.toan+self.ly+self.hoa
def nhap_ts():
    var =IntVar()
    def Append():
        try:
            l.append(thisinh(ten.get(),sbd.get(),float(toan.get()),float(ly.get()),float(hoa.get())))
            tb.configure(text='Thanh Cong!')
            tb.grid(column=0,row=4)
            var.set(1)
        except ValueError:
            tb.configure(text='Nhap Lai!')
            tb.grid(column=0,row=4)
            print('Nhap Lai')

    Label(win,text='Nhap Ten').grid(column=1,row=0)
    Entry(win,textvariable=ten).grid(column=2,row=0)
    Label(win,text='Nhap sbd').grid(column=1,row=1)
    Entry(win,textvariable=sbd).grid(column=2,row=1)
    Label(win,text='Nhap Toan').grid(column=1,row=2)
    Entry(win,textvariable=toan).grid(column=2,row=2)
    Label(win,text='Nhap Ly').grid(column=1,row=3)
    Entry(win,textvariable=ly).grid(column=2,row=3)
    Label(win,text='Nhap Hoa').grid(column=1,row=4)
    Entry(win,textvariable=hoa).grid(column=2,row=4)
    button.configure(command=Append,state='active')
    button.grid(column=2,row=5)
    button.wait_variable(var)
def nhap():
    try:
        n = int(soluong.get())
        tb.configure(text='')
    except:
        tb.configure(text='Nhap Lai!')
        tb.grid(column=0,row=6)
    for x in range(0,n):
        nhap_ts()
    button.configure(state='disabled')
    sap_x.grid(column=0,row=3)
    mtoan()
    hienthi(0,6,l)
def hienthi(c,r,li):
    for n in range(0,len(li)):
        Label(win,text=str(n+1)).grid(column=c,row=r+n)
        Label(win,text=str(li[n].ten)).grid(column=c+1,row=r+n)
        Label(win,text=str(li[n].sbd)).grid(column=c+2,row=r+n)
        Label(win,text=str(li[n].toan)).grid(column=c+3,row=r+n)
        Label(win,text=str(li[n].ly)).grid(column=c+4,row=r+n)
        Label(win,text=str(li[n].hoa)).grid(column=c+5,row=r+n)
def sapxep():   
    l.sort(key = lambda x:x.diem_t())
    hienthi(0,9+int(soluong.get()),l)
def mtoan():
    a = max(l,key=lambda x:x.toan)
    print(a.ten)
    win1 = Tk()
    win1.geometry('400x200')
    win1.title('SapXep')
    Label(win1,text=str(a.ten)).grid(column=0,row=0)
    Label(win1,text=str(a.sbd)).grid(column=1,row=0)
    Label(win1,text=str(a.toan)).grid(column=2,row=0)
    Label(win1,text=str(a.ly)).grid(column=3,row=0)
    Label(win1,text=str(a.hoa)).grid(column=4,row=0)
l = []
win = Tk()
soluong = StringVar()
ten = StringVar()
sbd = StringVar()
toan  = StringVar()
ly = StringVar()
hoa = StringVar()
Label(win,text='Nhap so sinh vien: ').grid(column=0,row=0)
Entry(win,textvariable=soluong).grid(column=0,row=1)
tb = Label(win)
Button(win,text='Xac Nhan',command=nhap).grid(column=0,row=2)
button = Button(win,text='Nhap')
sap_x = Button(win,command=sapxep,text='sapxep')
win.mainloop()
