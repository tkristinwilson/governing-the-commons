# data.py
from .model import *

__all__ = ["add_data"]


def add_data(model, model_params: dict):

    assert model_params["field_width"] is not None, "missing: fiel_width"
    assert model_params["field_height"] is not None, "missing: field_height"

    grid = model.spatial(dim=(model_params["field_width"],model_params["field_height"]), wrap=True)
    grid.config({
        'patchProperty': 'good:apples',
        'patchColormap': 'Greens',
        'agentLabel' : False,
        'agentSize' : 1,
        'agentMarker': 'X'
    })

    model.data.addReporter('patch-apples', model.data.agentReporter('stocks', 'patch', good='apples', stat='mean'))
    model.data.addReporter('agent-apples', model.data.agentReporter('stocks', 'agent', good='apples', stat='mean'))
    
    applesPlot = model.visual.addPlot('applesPlot', 'Apples', 'timeseries', selected=True)
    applesPlot.addSeries('patch-apples', 'Patch Apples (Avg.)', 'green')
    applesPlot.addSeries('agent-apples', 'Agent Apples (Avg.)', 'red')

    model.data.addReporter('agent-harvest', model.data.agentReporter('stocks', 'agent', good='min_harvest_level', stat='mean'))
    harvestPlot = model.visual.addPlot('harvestPlot', 'Harvest Level', 'timeseries', selected=True)
    harvestPlot.addSeries('agent-harvest', 'Agent Minimum Harvest Level (Avg.)', 'blue')

    return model
