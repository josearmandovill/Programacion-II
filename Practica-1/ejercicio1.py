class ecuacionlineal:
    def _init_(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def solucion(self):
        return (self._a * self.d - self.b * self._c) != 0

    def X(self):
        return (self._e * self.d - self.b * self.f) / (self.a * self.d - self.b * self._c)

    def Y(self):
        return (self._a * self.f - self.e * self.c) / (self.a * self.d - self.b * self._c)

valores = input("ingrese a, b, c, d, e, f separados: ").split()
a, b, c, d, e, f = map(float, valores)

eq = ecuacionlineal(a, b, c, d, e, f)

if eq.solucion():
    print("La solución del sistema es:")
    print("x =", eq.X())
    print("y =", eq.Y())
else:
    print("La ecuación no tiene solución")
