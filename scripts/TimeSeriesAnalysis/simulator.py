
import numpy as np # type: ignore

from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp

from signals import SignalFactory
from systems import SystemsFactory

class Simulator:
    def __init__(self, params):
        self.params = params
        
        self.signal = SignalFactory.make(params.signal)
        self.system = SystemsFactory.make(params.system)
    
    @property 
    def time_sequence(self):
        dt = self.params.dt
        n = self.params.n
        
        return np.arange(dt, dt*(n+1), dt, dtype=np.float32)
    
    @property
    def excitation_sequence(self):
        n = self.params.n
        dt = self.params.dt
        tau = self.params.tau
        alpha = self.params.alpha

        return self.signal(n, dt, tau, alpha).construct()
    
    def _system_response(self, t, u):
        model = self.system(self.params.a, self.params.b, self.params.c)
        t_span = (t[0], t[-1])
        u_interp = interp1d(x=t, y=u, kind='previous')

        sol = solve_ivp(
            fun=model,
            t_span=t_span,
            y0=self.params.x0,
            t_eval=t,
            args = (u_interp,),
            rtol=1e-10
        )

        return np.array(sol.y[0,:], np.float32)
    
    def simulate(self):
        t = self.time_sequence
        u = self.excitation_sequence
        y = self._system_response(t, u)

        return t, u, y