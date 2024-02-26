class R_H:
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def sphereVolume(self):
        return (4/3) * 3.14 * (self.r**3)

    def sphereSurface(self):
        return 4 * 3.14 * (self.r**2)

    def cylinderVolume(self):
        return 3.14 * self.r**2 * self.h

    def cylinderSurface(self):
        return 2 * 3.14 * self.r * (self.r + self.h)

    def coneVolume(self):
        return (1/3) * 3.14 * self.r**2 * self.h

    def coneSurface(self):
        return 3.14 * self.r * (self.r + ((self.r**2 + self.h**2)**0.5))


r = float(input("Enter radius: "))
h = float(input("Enter height: "))
values = R_H(r, h)

print("Sphere Volume =", values.sphereVolume())
print("Sphere Surface =", values.sphereSurface())
print("Cylinder Volume =", values.cylinderVolume())
print("Cylinder Surface =", values.cylinderSurface())
print("Cone Volume =", values.coneVolume())
print("Cone Surface =", values.coneSurface())
