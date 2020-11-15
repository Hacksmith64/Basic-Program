class Computer:
    def Config(self):
        print("i5,16GB,1TB")

Com_1 = Computer()
Com_2 = Computer()


Computer.Config(Com_1)
Computer.Config(Com_2)

Com_1.Config()
Com_2.Config()