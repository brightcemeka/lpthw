class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# 3 ways to do this object creation and instantiation


#dict style
MyStuff['apples']

# module style
MyStuff.apples()
print(MyStuff.tangerine)

#class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)