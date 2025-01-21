
import numpy as np # type: ignore

from abc import ABC, abstractmethod # type: ignore

class Systems(ABC):
    def __init__(self, *args):
        # Extract model coefficients
        pass

    def __call__(self, t, u, x):
        return self.response(t, u, x)

    @abstractmethod
    def response(self, t, x, u):
        # t: time
        # x: System states
        # u: Input sequence
        pass

class RoboticArm(Systems):
    def __init__(self, coeffs):
        self.a, self.b, self.c = coeffs
    
    def response(self, t, x, u):
        x1, x2 = x
        return np.array([x2, self.c*u(t) + self.b*np.sin(x1) - self.a*x2])

class MagLev(Systems):
    def __init__(self, coeffs):
        self.a, self.b, self.c = coeffs
    
    def response(self, t, x, u):
        x1, x2 = x
        return np.array([x2, -9.81 + ((self.a/self.c) * (u(t)**2 * np.sign(u(t))/x1)) - ((self.b/self.c)*x2)])

class VanDerPol(Systems):
    def __init__(self, *coeffs):
        self.a, self.b, self.c = coeffs
    
    def response(self, t, x, u):
        x1, x2 = x
        return np.array([x2, self.c*u(t) - (self.a*(x1**2 - 1)*x2 ) - (self.b*x1)])

class SystemsFactory:
    MODELS = {
        'robotic_arm': RoboticArm,
        'magnetic_levitation': MagLev,
        'van_der_pol': VanDerPol
    }

    @staticmethod
    def make(model):
        if model in SystemsFactory.MODELS:
            return SystemsFactory.MODELS[model]
        else:
            raise ValueError('Unknown ModelType')