# model.py
from helipad import Helipad

__all__ = ["new_model", "show_cpanel", "run_model"]

def new_model(model_params:dict):

    assert model_params["num_agents"] is not None, "missing: num_agents"
    assert model_params["max_vision"] is not None, "missing: max_vision"
    assert model_params["min_harvest_level"] is not None, "missing: min_harvest_level"
    assert model_params["discount"] is not None, "missing: discount"

    assert model_params["percent_best_land"] is not None, "missing: percent_best_land"
    assert model_params["regrowth_rate"] is not None, "missing: regrowth_rate"
    assert model_params["is_imitate_on"] is not None, "missing: is_imitate_on"

    assert model_params["stdev_error"] is not None, "missing: stdev_error"
    assert model_params["cost_punish"] is not None, "missing: cost_punish"
    assert model_params["cost_punished"] is not None, "missing: cost_punished"
    assert model_params["radius"] is not None, "missing: radius"
    assert model_params["is_punish_on"] is not None, "missing: is_punish_on"

    model = Helipad()
    model.name = "Governing the Commons Model One - Apple Eaters"
    
    model.agents.order = 'linear'   # Can be changed to 'random' or 'match'
    model.stages = 2                # Change to create a multi-stage model
    model.timer = True

    model.agents.addBreed('apple-eating-bear', 'red')
    model.goods.add('apples', 'black', 0)
    model.goods.add('min_harvest_level', 'black', model_params["min_harvest_level"])

    model.params['num_agent'].opts = {'low': 1, 'high': model_params["num_agents"], 'step': 500}
    model.param('num_agent', model_params["num_agents"])
    model.param('refresh', 1)
    model.param("stopafter", "stop_after")

    # model.params.add('max_vision', 'Max Agent Vision', 'slider', dflt=15, opts={'low': 1, 'high': 15, 'step': 1})
    model.params.add('min_harvest_level', 'Minimum Harvest Level', 'slider', dflt=model_params["min_harvest_level"], opts={'low': 0, 'high': 10, 'step': 1})
    # model.params.add('discount', 'Discount', 'slider', dflt=model_params["discount"], opts={'low': 0, 'high': 1, 'step': 1})
    # model.params.add('percent_best_land', 'Percent Best Land', 'slider', dflt=model_params["percent_best_land"], opts={'low': 5, 'high': 25, 'step': 1})
    model.params.add('regrowth_rate', 'Apples Regrowth Rate', 'slider', dflt=model_params["regrowth_rate"], opts={'low': 0, 'high': 1, 'step': 0.1})

    # model.params.add('is_imitate_on', 'Imitate?', 'check', dflt=model_params["is_imitate_on"])
    # model.params.add('stdev_error', 'Stdev Error', 'slider', dflt=model_params["stdev_error"], opts={'low': 0, 'high': 0.1, 'step': 0.01})
    # model.params.add('cost_punish', 'Cost Punish', 'slider', dflt=model_params["cost_punish"], opts={'low': 0, 'high': 1, 'step': 0.1})
    # model.params.add('cost_punished', 'Cost Punished', 'slider', dflt=model_params["cost_punished"], opts={'low': 0, 'high': 1, 'step':0.1})
    # model.params.add('radius', 'Radius', 'slider', dflt=model_params["radius"], opts={'low': 0, 'high': 10, 'step':1})
    # model.params.add('is_punish_on', 'Punish?', 'check', dflt=model_params["is_punish_on"])

    return model

def show_cpanel(model: Helipad):        
    model.launchCpanel()

def run_model(model: Helipad):
    model.launchVisual()
