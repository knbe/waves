from numpy import array

def Vec3(x, y, z):
    return array([x, y, z])

def v3_mag_sq(v):
    return v[0] ** 2 + v[1] ** 2 + v[2] ** 2

def v3_mag(v):
    return sqrt(v3_mag_sq(v))

def v3_unit(v):
    v_mag = v3_mag(v)
    return Vec3(
            v[0] / v_mag, 
            v[1] / v_mag, 
            v[2] / v_mag
            )

def v3_mult(self, k):
    return [self[0] * k, 
            self[1] * k, 
            self[2] * k]
