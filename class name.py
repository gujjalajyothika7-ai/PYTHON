class students:
    studentid=212
    studentname="jyothika"
s=students()
print(s.studentid)
print(s.studentname)


class students:
    studentid=212
    studentname="jyothika"
    def display(self):
        print(self.studentid)
        print(self.studentname)
s1=students()
s1.display()

class students:
    studentid=212
    studentname="jyothika"
    def studentdetails(self):
        print(self.studentid)
        print(self.studentname)
        print("------------------------------")
s1=students()
s1.studentdetails()


class students:
      college="MRDUT"
      def display(self,sid,sname):
          print(sid)
          print(sname)
          print(self.college)
          print("------------")
s=students()
s.display(210,"chaitu")
s.display(121,"jyothika")

class student:
    def display (self):
        print("Hello")
s=student()
s.display

class student:
    def __init__(self):
        print("Hello")
s=student()
