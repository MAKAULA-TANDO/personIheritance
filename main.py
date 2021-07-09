from tkinter import *


class Person:
    def __init__(self):
        self.__name = ''
        self.__sname = ''
        self.__id = ''
        self.__dob = ''

    def setname(self, name):
        self.__sname = name

    def getname(self):
        return self.__name

    def setsname(self, name):
        self.__sname = name

    def getsname(self):
        return self.__sname

    def setid(self, id):
        self.__id = id

    def getid(self):
        return self.__id

    def setdob(self, dob):
        self.__dob = dob

    def getdob(self):
        return self.__dob

    name = property(getname, setname)
    sname = property(getsname, setsname)
    id = property(getid, setid)
    dob = property(getdob, setdob)

    def display(self):
        text = "First name : " + self.name
        text = text + "\n" + "Surname : " + self.sname
        text = text + "\n" + "ID Number : " + self.id
        text = text + "\n" + "Date Of Birth : " + self.dob
        return text


class PhDStudent(Person):
    def __init__(self):
        super().__init__()
        self.__stdnum = ''
        self.__intmark = 0
        self.__extmark = 0

    def setstdnum(self, stdnum):
        self.__stdnum = stdnum

    def getstdnum(self):
        return self.__stdnum

    def setintmark(self, intmark):
        self.__intmark = intmark

    def getintmark(self):
        return self.__intmark

    def setextmark(self, extmark):
        self.__extmark = extmark

    def getextmark(self):
        return self.__extmark

    stdnum = property(getstdnum, setstdnum)
    intmark = property(getintmark, setintmark)
    extmark = property(getextmark, setextmark)

    def average(self):
        return (self.intmark + self.extmark) / 2

    def display(self):
        text = "PhD Student Report" + "\n"
        text = text + "\n" + super().display()
        text = text + "\n" + "Student Number: " + self.stdnum
        text = text + "\n" + "Internal Mark: " + str(self.intmark) + "%"
        text = text + "\n" + "External Mark: " + str(self.extmark) + "%"
        text = text + "\n" + "The final mark:  " + str(self.average()) + "%"
        return text


class PhDExaminer(Person):
    def __init__(self):
        super().__init__()
        self.__stfn = ''
        self.__hrate = 0
        self.__nhours = 0

    def setstfn(self, stfn):
        self.__stfn = stfn

    def getstfn(self):
        return self.__stfn

    def sethrate(self, hrate):
        self.__hrate = hrate

    def gethrate(self):
        return self.__hrate

    def setnhours(self, hours):
        self.__nhours = hours

    def getnhours(self):
        return self.__nhours

    stfn = property(getstfn, setstfn)
    hrate = property(gethrate, sethrate)
    nhours = property(getnhours, setnhours)

    def salary(self):
        return self.hrate * self.nhours

    def display(self):
        text = "PhD Examiner Report" + "\n"
        text = text + "\n" + super().display()
        text = text + "\n" + "Staff Number: " + self.stfn
        text = text + "\n" + "Hourly Rate: R" + str(self.hrate)
        text = text + "\n" + "Total hours: " + str(self.nhours) + " Hrs"
        text = text + "\n" + "Total salary: R" + str(self.salary())
        return text


class ScreenCreate:
    def __init__(self, win):
        self.lblname = Label(win, text='First name')
        self.lblsname = Label(win, text='Surname')
        self.lblid = Label(win, text='ID Number')
        self.lbldob = Label(win, text='Date of Birth')
        self.dis = Label(win, text='Report')
        self.txtname = Entry(bd=3)
        self.txtsname = Entry()
        self.txtid = Entry()
        self.txtdob = Entry()
        self.dis = Text(height=10, width=40)
        self.lblname.place(x=100, y=50)
        self.lblsname.place(x=100, y=100)
        self.lblid.place(x=100, y=150)
        self.lbldob.place(x=100, y=200)
        self.txtname.place(x=200, y=50)
        self.txtsname.place(x=200, y=100)
        self.txtid.place(x=200, y=150)
        self.txtdob.place(x=200, y=200)
        self.val = IntVar()
        self.val.set(1)
        self.rads = Radiobutton(text="PhDStudent", variable=self.val, value=1)
        self.rade = Radiobutton(text="PhDExaminer", variable=self.val, value=2)
        self.rads.place(x=100, y=245)
        self.rade.place(x=400, y=245)
        self.lblstdn = Label(win, text='Student Number')
        self.lblintm = Label(win, text='Internal Mark')
        self.lblextm = Label(win, text='External Mark')
        self.lblstfn = Label(win, text='Staff Number')
        self.lblhrate = Label(win, text='Hourly Rate')
        self.lblnhours = Label(win, text='Number Of Hours')
        self.txtstdn = Entry()
        self.txtintm = Entry()
        self.txtextm = Entry()
        self.txtstfn = Entry()
        self.txthrate = Entry()
        self.txtnhours = Entry()
        self.lblstdn.place(x=100, y=330)
        self.lblintm.place(x=100, y=360)
        self.lblextm.place(x=100, y=390)
        self.lblstfn.place(x=350, y=330)
        self.lblhrate.place(x=350, y=360)
        self.lblnhours.place(x=350, y=390)
        self.txtstdn.place(x=200, y=330)
        self.txtintm.place(x=200, y=360)
        self.txtextm.place(x=200, y=390)
        self.txtstfn.place(x=450, y=330)
        self.txthrate.place(x=450, y=360)
        self.txtnhours.place(x=450, y=390)
        self.b1 = Button(win, text='OK', command=self.show)
        self.b1.place(x=100, y=450)
        self.dis.place(x=100, y=500)
        self.dis.place(x=150, y=500)

    def show(self):
        fn = self.txtname.get()
        sn = self.txtsname.get()
        id = self.txtid.get()
        dob = self.txtdob.get()
        if self.val.get() == 1:
            intm = int(self.txtintm.get())
            extm = int(self.txtextm.get())
            stdn = self.txtstdn.get()
            phde = PhDStudent()
            phde.firstname = fn
            phde.lastname = sn
            phde.idno = id
            phde.dob = dob
            phde.stdnum = stdn
            phde.intmark = intm
            phde.extmark = extm
            m = phde.display()
            self.dis.delete('1.0', END)
            self.dis.insert(INSERT, m)
        if self.val.get() == 2:
            hrate = int(self.txthrate.get())
            nhours = int(self.txtnhours.get())
            stfn = self.txtstfn.get()
            phde = PhDExaminer()
            phde.firstname = fn
            phde.lastname = sn
            phde.idno = id
            phde.dob = dob
            phde.stfn = stfn
            phde.hrate = hrate
            phde.nhours = nhours
            m = phde.display()
            self.dis.delete('1.0', END)
            self.dis.insert(INSERT, m)


def screen():
    screen = Tk()
    ScreenCreate(screen)
    screen.geometry("750x750")
    screen.mainloop()


if __name__ == '__main__':
    screen()