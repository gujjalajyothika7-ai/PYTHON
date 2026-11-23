class teacher:
    pass
r=teacher()
print(id(r))
print(type(r))
print(type(teacher))
print(isinstance(r,teacher))


class teacher:
    pass
class  student(teacher):
    pass
s=student()
print(issubclass(student,teacher))
print(issubclass(teacher,student))


class thatha:
    pass
class nanna(thatha):
    pass
class nenu(nanna):
    pass
n=nenu()
print(issubclass(nenu,thatha))
print(issubclass(nanna,thatha))


class teacher:
    name="shadow"
t=teacher()
print(setattr(t,"name","shiva"))
print(getattr(t,"name"))
print(delattr(t,"name"))
print(hasattr(t,"name"))
#get attribute
#set attribute
#delete attribute
#has attribute

class teacher:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
t=teacher("shiva")
print(t)