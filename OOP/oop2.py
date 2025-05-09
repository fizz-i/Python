class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(thing):
    thing.quack()  # Doesn't care if it's a Duck or not

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack!
make_it_quack(p)  # Output: I'm pretending to be a duck!
