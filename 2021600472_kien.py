from tkinter import *
class kien:
    def __init__(self,loai,ns,t) -> None:
        self.loai = loai
        self.ns = ns
        self.t = t
    def tinh(self):
        return self.ns*self.t
class GUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('Con Kien')
        self.root.geometry('600x800')

        self.sl = StringVar()

        self.lkien = []

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack(anchor=CENTER)
        
        self.notificationFrame = Frame(self.root)
        self.notificationFrame.pack(anchor=CENTER)
        self.notificationLabel = Label(self.notificationFrame)

        self.label1 = Label(self.mainFrame,text='Nhap so luong kien')
        self.label1.pack(side=LEFT)
        self.entry_sl = Entry(self.mainFrame,textvariable=self.sl)
        self.entry_sl.pack(side=LEFT)
        self.button_sl = Button(self.mainFrame,text='Xac Nhan',command=self.nhap)
        self.button_sl.pack(side=RIGHT)


        self.root.mainloop()
    def nhap(self):
        try:
            n = int(self.entry_sl.get())
            self.thongbao("Nhap thanh cong")
        except:
            self.thongbao('Nhap Lai!')
        self.nhap_kien(n)
        self.nhap_kien_Frame.destroy()
        self.hienthi(self.lkien)
        self.mkien()
        self.tong()
    def nhap_kien(self,n):
        self.nhap_kien_Frame = Frame(self.root)
        self.nhap_kien_Frame.pack(fill=X)

        l1 = Label(self.nhap_kien_Frame)
        l1.pack()

        llFrame = Frame(self.nhap_kien_Frame)
        llFrame.pack(anchor=CENTER)
        ll = Label(llFrame,text='Nhap loai kien',width=20)
        ll.pack(side=LEFT)
        loai = Entry(llFrame)
        loai.pack(side=RIGHT)

        lnsFrame = Frame(self.nhap_kien_Frame)
        lnsFrame.pack(anchor=CENTER)
        lns = Label(lnsFrame,text='Nhap nang suat kien',width=20,)
        lns.pack(side=LEFT)
        ns = Entry(lnsFrame)
        ns.pack(side=RIGHT)

        ltFrame = Frame(self.nhap_kien_Frame)
        ltFrame.pack(anchor=CENTER)
        lt = Label(ltFrame,text="nhap thoi gian kien lam",width=20)
        lt.pack(side=LEFT)
        t = Entry(ltFrame)
        t.pack(side=RIGHT)

        b1 = Button(self.nhap_kien_Frame,text='Xac Nhan',command=lambda:b1_var.set(1))
        b1.pack()
        for x in range(0,n):
            while(1):
                b1_var = IntVar()
                l1.configure(text = f"nhap con kien thu {x+1}")
                print(x)
                b1.wait_variable(b1_var)
            
                try:
                    self.lkien.append(kien(loai.get(),int(ns.get()),int(t.get())))
                except:
                    self.thongbao(f'Nhap lai kien thu {x+1}')
                else:
                    self.thongbao('Nhap Thanh Cong')
                    break
    def hienthi(self,l,messge=''):
        self.hienthiFrame = Frame(self.root)
        # self.hienthiFrame.grid()
        a = self.hienthiFrame
        Label(a,text=str(messge)).grid(column=0,row=0)
        for n in range(0,len(l)):
            
            Label(a,text=str(n+1)).grid(column=1,row=n)
            Label(a,text=str(l[n].loai)).grid(column=2,row=n)
            Label(a,text=str(l[n].ns)).grid(column=3,row=n)
            Label(a,text=str(l[n].t)).grid(column=4,row=n)
            a.pack()
        a.after(10000,lambda:a.destroy())
    def mkien(self):
        a=min(self.lkien,key=lambda x:x.tinh())
        self.hienthi([a],'Con kien tha moi kem nhat la') 
    def tong(self):
        t = 0
        for x in self.lkien:
            t = t + x.tinh()
        tinhf = Frame(self.root)
        Label(tinhf,text=f"Danh kien tha duoc tong {t}").pack()
        tinhf.pack(anchor=CENTER)
    def thongbao(self,text):
        # t = StringVar()
        # t.set(text)
        self.notificationLabel.configure(text=text)
        self.notificationLabel.pack()
if __name__ == "__main__":
    GUI()
