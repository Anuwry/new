class P:
    def query(self): print("P")

class X(P):
    def query(self): super().query()

class Y(P):
    pass

class Z(X, Y):
    pass

Z().query()