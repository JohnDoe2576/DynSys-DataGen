
import numpy as np

class Params:
    def __init__(self):
        # Basic parameters
        self.signal = None  # Type of Excitation signal
        self.system = None  # Type of system

        # Signal parameters
        self.n = None       # Number of samples
        self.dt = None      # Time-stepping

        self.tau = None     # Delay (min, max) before level-shit (For Skyline)
        self.alpha = None   # Min-Max level (For skyline)

        # System parameters
        self.a = None       # System coefficient `a`
        self.b = None       # System coefficient `b`
        self.c = None       # System coefficient `c`

        self.x0 = None      # Initial conditions/values
    
    @property 
    def time_sequence(self):
        return np.arange(self.dt, self.dt*self.n, self.dt)
    
    def __str__(self):
        return f'\nExcitation Signal: {self.signal}\n' + \
               f'System: {self.system}\n\n' + \
               f'Number of samples, n: {self.n}\n' + \
               f'Time-step, dt: {self.dt}\n\n' + \
               f'System parameters\n' + \
               f'-----------------\n' + \
               f'System coefficients: (a, b, c): {self.a, self.b, self.b}\n' + \
               f'Initial state, x0: {self.x0}\n'

class ParamsBuilder:
    def __init__(self, params=Params()):
        self.params = params
    
    @property
    def basics(self):
        return BasicParamsBuilder(self.params)
    
    @property
    def signal(self):
        return SignalParamsBuilder(self.params)
    
    @property
    def system(self):
        return SystemParamsBuilder(self.params)
    
    def build(self):
        return self.params

class BasicParamsBuilder(ParamsBuilder):
    def __init__(self, params):
        super().__init__(params)
    
    def choice_of_signal(self, signal):
        self.params.signal = signal
        return self
    
    def choice_of_system(self, system):
        self.params.system = system
        return self

class SignalParamsBuilder(ParamsBuilder):
    def __init__(self, params):
        super().__init__(params)
    
    def with_sample_size(self, n):
        self.params.n = n
        return self
    
    def with_time_step(self, dt):
        self.params.dt = dt
        return self
    
    def with_delay_range(self, tau: list):
        self.params.tau = tau
        return self
    
    def within_levels(self, levels: list):
        self.params.alpha = levels
        return self

class SystemParamsBuilder(ParamsBuilder):
    def __init__(self, params):
        super().__init__(params)
    
    def with_coeffs(self, coeffs):
        self.params.a, self.params.b, self.params.c = coeffs
        return self
    
    def with_initial_values(self, x0: list):
        self.params.x0 = x0
        return self