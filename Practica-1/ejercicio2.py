import math
class ecuacioncuadratica:
    def _init_(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def discriminante(self):
        return self._b**2 - 4*self.a*self._c

    def raiz1(self):
        d = self.discriminante()
        if d < 0:
            return 0
        return (-self._b + math.sqrt(d)) / (2 * self._a)

    def raiz2(self):
        d = self.discriminante()
        if d < 0:
            return 0
        return (-self._b - math.sqrt(d)) / (2 * self._a)

valores = input("ingrese a, b, c separados: ").split()
a, b, c = map(float, valores)
eq = ecuacioncuadratica(a, b, c)
d = eq.discriminante()
if d > 0:
    print("La ecuación tiene dos raíces:")
    print("Raíz 1=", eq.raiz1())
    print("Raíz 2=", eq.raiz2())
elif d == 0:
    print("La ecuación tiene una raíz:")
    print("Raíz =", eq.raiz1())
else:
    print("La ecuación no tiene raíces reales")
