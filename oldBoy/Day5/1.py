#coding: utf-8
class people:
    def __init__(self,name):
        self.Name = name
    def talk(self,msg):
        print "%s : %s" %(self.Name,msg)
    def  walk(self):
        print "%s is walk" %(self.Name)
p1 = people("tony")
p1.talk("hello")
p2 = people("mark")
p2.walk()