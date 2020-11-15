from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(Computer):
    def process(self):
        print("It is running")

class Whiteboard(Computer):
    def write(self):
        print("It's Writing")

class Programmer:
    def Work(self,com):
        print("Solving Bugs")
        com.process()

#com =Computer()
com1 = laptop()
#com2 = Whiteboard()
prog1 = Programmer()
prog1.Work(com1)
#com.process()
#com1.process()