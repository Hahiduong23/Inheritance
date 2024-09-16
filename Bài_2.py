class DongVat:
    def __init__(self, name):
        self.__name = name  

    def get_name(self):
        return self.__name  

class BoSat(DongVat):
    def __init__(self, name):
        super().__init__(name)

class CoVu(DongVat):
    def __init__(self, name):
        super().__init__(name)

class ThanLan(BoSat):
    def __init__(self, name):
        super().__init__(name)

class Ran(BoSat):
    def __init__(self, name):
        super().__init__(name)

class KhiDot(CoVu):
    def __init__(self, name):
        super().__init__(name)

class Gau(CoVu):
    def __init__(self, name):
        super().__init__(name)

covu = CoVu("Thư")
print(covu.__class__.__bases__[0].__name__)  
print(covu.get_name())  

bosat = BoSat("Chí")
print(bosat.__class__.__bases__[0].__name__) 
print(bosat.get_name()) 



