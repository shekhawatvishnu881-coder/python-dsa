class teacher:
    def input(self):
        self.id=int(input(" enter teacher id "))
        self.name=input(" enter teacher name")
        self.subject=input(" enter teacher subject ")
        self.salary=int(input(" enter teacher salary "))

    def output(self):
        print(f" teacher id is {self.id}")
        print(f" teacher name  is {self.name}")
        print(f" teacher subject is {self.subject}")
        print(f" teacher salary is {self.salary}")

t1=teacher()
t1.input()
t2=teacher()
t2.input()

if t1.salary>t2.salary:
  print("max is ",t1)
  t1.output()
else:
  print("max is",t2)
  t2.output()

