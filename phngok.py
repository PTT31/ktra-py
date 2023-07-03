from tkinter import *

class Bee:
    def __init__(self, type, velocity, timeFly):
        self.type = type
        self.velocity = velocity
        self.timeFly = timeFly
    def distance(self):
        return self.velocity * self.timeFly
    def __repr__(self):
        return f"Loại: {self.type} - Vận tốc: {self.velocity} - Thời gian bay: {self.timeFly}"

class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Con ong")
        self.root.geometry("500x500")

        self.bees = []
        self.index = 1

        self.mainFrame = Frame(self.root, pady=10)
        self.mainFrame.pack(anchor=CENTER)
        self.content = Label(self.mainFrame, font=80)

        self.btnFrame = Frame(self.root, pady=10)
        self.btnFrame.pack(anchor=CENTER)

        self.labelLengthArr = Label(self.mainFrame, text="N:", font=80)
        self.labelLengthArr.pack(side=LEFT)

        self.entryLengthArr = Entry(self.mainFrame, font=80)
        self.entryLengthArr.pack(side=LEFT)
        self.entryLengthArr.focus()

        self.btnSubmit = Button(self.btnFrame, text="Nhập", font=80, command=self.inputLength)
        self.btnSubmit.pack()
        self.root.bind('<Return>', self.inputLength)

        self.root.mainloop()

    def inputLength(self, *arg):
        self.length = int(self.entryLengthArr.get())
        self.labelLengthArr.destroy()
        self.entryLengthArr.destroy()
        self.initInputBees()
        self.btnSubmit.destroy()
        self.btnSubmit = Button(self.btnFrame, text="Nhập", font=80, command=self.pushBee)
        self.root.unbind('<Return>')
        self.root.bind('<Return>', self.pushBee)
        self.btnSubmit.pack()

    def initInputBees(self):
        text = "Nhập con ong thứ " + str(self.index)
        self.noti = Label(self.mainFrame, text=text, font=80)
        self.noti.pack(anchor=CENTER)
        #type
        self.typeFrame = Frame(self.mainFrame, pady=10)
        self.typeFrame.pack(anchor=E)
        self.labelType = Label(self.typeFrame, text="Loại:", font=80)
        self.labelType.pack(side=LEFT)
        self.entryType = Entry(self.typeFrame, font=80)
        self.entryType.pack(side=LEFT)
        self.entryType.focus()

        #velocity
        self.velocityFrame = Frame(self.mainFrame)
        self.velocityFrame.pack(anchor=E)
        self.labelvelocity = Label(self.velocityFrame, text="Vận tốc:", font=80)
        self.labelvelocity.pack(side=LEFT)
        self.entryVelocity = Entry(self.velocityFrame, font=80)
        self.entryVelocity.pack(side=LEFT)

        #time fly
        self.timeFlyFrame = Frame(self.mainFrame, pady=10)
        self.timeFlyFrame.pack(anchor=E)
        self.labelTimeFly = Label(self.timeFlyFrame, text="Thời gian bay:", font=80)
        self.labelTimeFly.pack(side=LEFT)
        self.entryTimeFly = Entry(self.timeFlyFrame, font=80)
        self.entryTimeFly.pack(side=LEFT)

    def updateInputBees(self):
        self.index += 1
        type = self.entryType.get()
        velocity = float(self.entryVelocity.get())
        timeFly = float(self.entryTimeFly.get())
        self.bees.append(Bee(type, velocity, timeFly))
        if self.index > self.length:
            self.index = 1
            self.typeFrame.destroy()
            self.timeFlyFrame.destroy()
            self.velocityFrame.destroy()
            self.noti.destroy()
            self.btnSubmit.destroy()
            self.root.unbind('<Return>')
            self.btnDisplay = Button(self.btnFrame, text="Hiển thị danh sách", font=80, command=self.display)
            self.btnDisplay.pack(anchor=CENTER)
            self.btnBeeFastest = Button(self.btnFrame, text="Con ong vận tốc nhanh nhất", font=80, command=self.fastestBee)
            self.btnBeeFastest.pack(anchor=CENTER, padx=5)
            self.btnCountBees = Button(self.btnFrame, text="Số con ong bay dài nhất", font=80, command=self.countBees)
            self.btnCountBees.pack(anchor=CENTER, padx=5)
            self.btnMaxDistance = Button(self.btnFrame, text="Quãng đường dài nhất", font=80, command=self.showMaxDistance)
            self.btnMaxDistance.pack(anchor=CENTER, padx=5)
        else:
            textUpdate = "Nhập con ong thứ " + str(self.index)
            self.noti["text"] = textUpdate
            self.entryTimeFly.delete(0, END)
            self.entryType.delete(0, END)
            self.entryType.focus()
            self.entryVelocity.delete(0, END)

    def maxDistance(self):
        res = 0
        for bee in self.bees:
            if bee.distance() > res:
                res = bee.distance()
        return res

    def showMaxDistance(self):
        self.content["text"] = f"Quãng đường dài nhất: {self.maxDistance()}"

    def countBees(self):
        cnt = 0
        textDisplay = ""
        for bee in self.bees:
            if bee.distance() == self.maxDistance():
                cnt += 1
        textDisplay = f"Có {cnt} con ong bay được quãng đường dài nhất"
        self.content["text"] = textDisplay

    def fastestBee(self):
        textDisplay = ""
        maxVelocity = 0
        for bee in self.bees:
            if bee.velocity > maxVelocity:
                maxVelocity = bee.velocity
        textDisplay += "Con ong vận tốc nhanh nhất:\n"
        for bee in self.bees:
            if bee.velocity == maxVelocity:
                textDisplay += f"{bee}\n"
            self.index += 1
        textDisplay += "\n"
        self.content["text"] = textDisplay
        self.index = 1

    def display(self):
        textDisplay = ""
        for bee in self.bees:
            textDisplay += f"{self.index}: {bee}\n"
            self.index += 1
        self.content["text"] = textDisplay
        self.content.pack(anchor=CENTER)
        self.index = 1

    def pushBee(self, *arg):
        self.updateInputBees()


if __name__ == "__main__":
    GUI()