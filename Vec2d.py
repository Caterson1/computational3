import math


class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vec2d):
            return (
                Vec2d(
                    self.x + other.x,
                    self.y + other.y,
                )
            )

        raise TypeError(f"cannot compute sum of vector and {type(other)}")

    def __neg__(self):
        return Vec2d(-self.x, -self.y)

    def __mul__(self, other):
        return Vec2d(self.x * other, self.y * other)

    def __rmul__(self, other):

        return Vec2d(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return Vec2d(self.x / other, self.y / other)

        raise ZeroDivisionError("no.")

    def __sub__(self, other):
        if isinstance(other, Vec2d):
            return self + (-other)

        raise TypeError(f"{type(other)}is not allowed: you tried {self} - {other}")

    def __pow__(self, power):
        return self*(self.mag()**(power-1))

    def __repr__(self):
        return f"< {self.x}, {self.y} >"

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def cross(self, b):
        if isinstance(b, Vec2d):
            return Vec2d(
                (self.y * b.z) - (self.z * b.y),
                (self.z * b.x) - (self.x * b.z),
            )

    def tuple(self, number:int = 3):
        if number == 2:
            return tuple((self.x, self.y))
        return tuple((self.x, self.y))


def dot2d(a, b):
    if isinstance(a, Vec2d) and isinstance(b, Vec2d):
        return a.x * b.x + a.y * b.y + a.z * b.z
    raise TypeError(f"honestly what are you even doing why are you giving me a {type(a)} and a {type(b)}")


def norm2d(vec2d):
    if vec2d.mag() != 0:
        return Vec2d(vec2d.x / vec2d.mag(), vec2d.y / vec2d.mag())
    return Vec2d()


def mag2d(a):
    return math.sqrt(a.x ** 2 + a.y ** 2)

def minus_one_D(vec):
    return Vec2d(vec.x, vec.y)


# # theta_xz = angle on the x-z plane; theta_xy = angle on the x-y plane
# def vectorize(mag_vec, theta_xy, theta_xz=0):
#     # these three are separated out so it looks nicer
#     xy_rad = math.radians(theta_xy)
#     xz_rad = math.radians(theta_xz)
#     # the hypotenuse between the x and z components
#     mini_hypotenuse = mag_vec * math.cos(xy_rad)
#
#     return(Vec(
#         mini_hypotenuse * math.cos(xz_rad),
#         mag_vec * math.sin(xy_rad),
#         mini_hypotenuse * math.sin(xz_rad)
#     ))
#
# def vector(i):
#     if isinstance(i, list):
#         return Vec(float(i[0]), float(i[1]), float(i[2]))
#     else:
#         raise TypeError(f"vector isn't prepared for {i}")
#
# def vec_reverse_repr(imput):
#     imput = imput.strip().strip("<").strip(">").replace(",", "").split()
#     return Vec(float(imput[0]), float(imput[1]), float(imput[2]))
