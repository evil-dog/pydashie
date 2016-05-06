from dashie_sampler import DashieSampler

import collections
import random

class PoolTempSampler(DashieSampler):
    def __init__(self, *args, **kwargs):
        DashieSampler.__init__(self, *args, **kwargs)

    def name(self):
        return 'Pool_Temp'

    def sample(self):
        s = {'value': random.randint(0, 100)}
        return s

class SolarTempSampler(DashieSampler):
  def __init__(self, *args, **kwargs):
    DashieSampler.__init__(self, *args, **kwargs)

  def name(self):
    return 'Solar_Temp'

  def sample(self):
    s = {'value': random.randint(0, 100)}
    return s

class WeatherSampler(DashieSampler):
  def __init__(self, *args, **kwargs):
    DashieSampler.__init__(self, *args, **kwargs)

  def name(self):
    return 'weather'

  def sample(self):
    s = {
      'now_temp': 80,
      'humidity': 40,
      'temp_low': 20,
      'temp_high': 90,
      'precip': 30,
      'icon': 'cloudy',
      'tomorrow_temp_low': 25,
      'tomorrow_temp_high': 85,
      'tomorrow_icon': 'clear',
      'tomorrow_precip': 24,
      'wind_speed': 50,
      'wind_speed_gust': 100,
      'wind_dir': 'NE',
    }

    return s
