# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 16:58:43 2020

@author: Mark Hoehne
"""

from psychrochart import PsychroChart, load_config

# Load default style:
# chart_default = PsychroChart()
# ax = chart_default.plot()
# ax.get_figure()
# ax.show


# Load preconfigured styles:
print("** Preconfigured chart style: `ashrae`:")
chart_ashrae_style = PsychroChart('ashrae')
ax = chart_ashrae_style.plot()
ax.get_figure()