class MyClass:
    def myPublicMethod(self):
        print('public method')
    def __myPrivateMethod(self):
        print('this is private!!')

obj = MyClass()
obj.myPublicMethod()

#obj.__myPrivateMethod()
obj._MyClass__myPrivateMethod()
