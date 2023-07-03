from tkinter import *
class ong:
    def __init__(self,l,v,t):
        self.loai = l
        self.vantoc = v
        self.thoigian = t
    def s(self):
        return self.vantoc*self.thoigian
def nhap_ong():
    var = IntVar()
    def add():
        try:
            print(loai.get())
            l.append(ong(loai.get(), int(vantoc.get()), int(thoigian.get())))
            var.set(1)
        except ValueError:
            print('nhap lai!')
            # print(loai.get())
    c.configure(command=add)
   
    c.grid(column=2,row=7)
    lo = Label(window,text='nhap loai ong').grid(column=0, row=3)
    Entry(window,textvariable=loai).grid(column=2, row=3)
    v = Label(window,text='nhap van toc: ').grid(column=0, row=4)
    Entry(window, textvariable=vantoc).grid(column=2, row=4)
    t = Label(window,text='Nhap thoi gian: ').grid(column=0, row=5)
    Entry(window, textvariable=thoigian).grid(column=2, row=5)
    c.wait_variable(var)

def nhap():
    for i in range(0, int(soluong.get())):
        print(i)
        nhap_ong()
    hien_thi()
    c.destroy()
def Max_s():
    a = max(l,key=lambda x:x.s())
    count =  0
    for x in l:
        # print(x.s())
        # print(type(x.s()))
        if (x.s() == a.s()):
            count = count+1
    Label(window,text=str(count)).grid(column=1,row=7)
    Label(window,text=str(a.loai)).grid(column=2,row=7)
    Label(window,text=str(a.s())).grid(column=3,row=7)
def hien_thi():
    n = int(soluong.get())
    for n in range(0,n):
        a = Label(window,width=10,text=str(n+1)).grid(column=0,row=8+n)
        x=0
        Label(window,text=str(l[n].loai)).grid(column=x+1,row=8+n)
        Label(window,text=str(l[n].vantoc)).grid(column=x+2,row=8+n)
        Label(window,text=str(l[n].thoigian)).grid(column=x+3,row=8+n)
        
l =  []
window = Tk()
window.title('Ong')
window.geometry('600x300')
soluong = StringVar()
loai = StringVar()
vantoc = StringVar()
thoigian = StringVar()
l1 = Label(window,text='Nhap so ong').grid(column=0,row=1)
a = Entry(window,textvariable=soluong).grid(column=2,row=1)
c = Button(window, text='ok')
b = Button(window,text='Xac Nhan',command=nhap).grid(column=1,row=2)
d = Button(window,text='Max',command=Max_s).grid(column=0,row=7)
window.mainloop()


