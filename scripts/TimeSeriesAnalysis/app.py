
import plotly.graph_objects as go

from params import ParamsBuilder
from simulator import Simulator

class Application:
    def __init__(self):
        self.params = ParamsBuilder()

    def run(self):
        params = self.params \
            .basics\
                .choice_of_signal('skyline')\
                .choice_of_system('van_der_pol')\
            .signal\
                .with_sample_size(200000)\
                .with_time_step(0.01)\
                .with_delay_range([0.01, 15.0])\
                .within_levels([-2.5, 2.5])\
            .system\
                .with_coeffs([1.0, 1.0, 1.0])\
                .with_initial_values([0.1, 0.1])\
            .build()

        t, u, y = Simulator(params).simulate()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t, y=u, name='u', line={'color': 'crimson'}))
        fig.add_trace(go.Scatter(x=t, y=y, name='y', line={'color': 'dodgerblue'}))
        fig.show()