
import numpy as np

class Signals:
    def __init__(self, n_samples, delta_t):
        self.n = n_samples
        self.dt = delta_t

class Skyline(Signals):
    def __init__(self, n_samples, delta_t, tau_range: list, alpha_range: list):
        super().__init__(n_samples, delta_t)

        self.tau = np.array(tau_range, dtype=np.float32)
        self.alpha = np.array(alpha_range, dtype=np.float32)
    
    @property
    def min_width(self):
        return int(self.tau.min()/self.dt)
    
    @property
    def max_width(self):
        return int(self.tau.max()/self.dt)
    
    def construct(self):
        rng = np.random.default_rng()

        indices = np.insert(np.cumsum(rng.integers(self.min_width, self.max_width, size=self.n)), 0, 0)
        indices = indices[:np.argmax(indices >= self.n)+1]
        indices[-1] = self.n

        amplitude = rng.normal(self.alpha.min(), self.alpha.max(), size=indices.size-1)

        signal = np.empty((self.n,), dtype=np.float32)

        positions = np.arange(self.n)
        segment_indices = np.searchsorted(indices, positions, side='right') - 1
        signal[:] = amplitude[segment_indices]
        
        return signal.astype(np.float32)

class SignalFactory:
    EXCITER_TYPE = {
        'skyline': Skyline
    }

    @staticmethod
    def make(exciter_type: str) -> Signals:
        if exciter_type in SignalFactory.EXCITER_TYPE.keys():
            return SignalFactory.EXCITER_TYPE[exciter_type]
        else:
            raise ValueError('Unknown ExciterType')