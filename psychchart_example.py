# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 14:38:34 2020

@author: Mark Hoehne
"""

from psychrochart.chart import PsychroChart
import json


if __name__ == "__main__":
    TEST_EXAMPLE_ZONES = [
        {
            "label": "LT",
            "points_x": [-23, -17.78],
            "points_y": [0, 100],
            "style": {
                "edgecolor": [1.0, 0.749, 0.0, 0.8],
                "facecolor": [1.0, 0.749, 0.0, 0.2],
                "linestyle": "--",
                "linewidth": 2,
            },
            "zone_type": "dbt-rh",
        },
        {
            "label": "MT",
            "points_x": [2, 4],
            "points_y": [50, 95],
            "style": {
                "edgecolor": [0.498, 0.624, 0.8],
                "facecolor": [0.498, 0.624, 1.0, 0.2],
                "linestyle": "--",
                "linewidth": 2,
            },
            "zone_type": "dbt-rh",
        },
        {
            "label": "Summer",
            "points_x": [18, 25],
            "points_y": [30, 60],
            "style": {
                "edgecolor": [0.498, 0.624, 0.8],
                "facecolor": [0.498, 0.624, 1.0, 0.2],
                "linestyle": "--",
                "linewidth": 2,
            },
            "zone_type": "dbt-rh",
        },
    ]
    TEST_EXAMPLE_FIG_CONFIG = {
        "figsize": [16, 9],
        "partial_axis": True,
        "position": [0, 0, 1, 1],
        "title": None,
        "x_axis": {
            "color": [0.855, 0.145, 0.114],
            "linestyle": "-",
            "linewidth": 2,
        },
        "x_axis_labels": {"color": [0.855, 0.145, 0.114], "fontsize": 10},
        "x_axis_ticks": {
            "color": [0.855, 0.145, 0.114],
            "direction": "in",
            "pad": -20,
        },
        "x_label": None,
        "y_axis": {
            "color": [0.0, 0.125, 0.376],
            "linestyle": "-",
            "linewidth": 2,
        },
        "y_axis_labels": {"color": [0.0, 0.125, 0.376], "fontsize": 10},
        "y_axis_ticks": {
            "color": [0.0, 0.125, 0.376],
            "direction": "in",
            "pad": -20,
        },
        "y_label": None,
    }    
    custom_style = {
            "chart_params": {
                "constant_h_label": None,
                "constant_h_labels": [-25, -15, 0, 10, 15],
                "constant_h_step": 5,
                "constant_humid_label": None,
                "constant_humid_label_include_limits": False,
                "constant_humid_label_step": 1,
                "constant_humid_step": 0.5,
                "constant_rh_curves": [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "constant_rh_label": True,
                "constant_rh_labels": [20, 40, 60],
                "constant_rh_labels_loc": 0.8,
                "constant_temp_label": None,
                "constant_temp_label_include_limits": False,
                "constant_temp_label_step": 5,
                "constant_temp_step": 1,
                "constant_v_label": None,
                "constant_v_labels": [0.74, 0.76, 0.78, 0.8],
                "constant_v_labels_loc": 0.01,
                "constant_v_step": 0.01,
                "constant_wet_temp_label": None,
                "constant_wet_temp_labels": [-15, -10, -5, 0],
                "constant_wet_temp_step": 5,
                "range_wet_temp": [-25, 5],
                "range_h": [-30, 350],
                "range_vol_m3_kg": [0.7, 1.8],
                "with_constant_dry_temp": True,
                "with_constant_h": True,
                "with_constant_humidity": True,
                "with_constant_rh": True,
                "with_constant_v": False,
                "with_constant_wet_temp": False,
                "with_zones": True,
            },
            "constant_dry_temp": {
                "color": [255,255,255, 0.7],
                "linestyle": "-",
                "linewidth": 0.75,
            },
            "constant_h": {
                "color": [30,144,255, 0.7],
                "linestyle": "-",
                "linewidth": 2,
            },
            "constant_humidity": {
                "color": [255,255,255, 0.7],
                "linestyle": "-",
                "linewidth": 0.75,
            },
            "constant_rh": {
                "color": [169,169,169, 0.7],
                "linestyle": "-",
                "linewidth": 2,
            },
            "constant_v": {
                "color": [127,255,212, 0.7],
                "linestyle": "-",
                "linewidth": 1,
            },
            "constant_wet_temp": {
                "color": [138,43,226, 0.7],
                "linestyle": "-",
                "linewidth": 1,
            },
            "figure": TEST_EXAMPLE_FIG_CONFIG,
            "limits": {
                "range_humidity_g_kg": [0, 10],
                "range_temp_c": [-40, 40],
                "step_temp": 0.5,
                "pressure_kpa": 101.42,
            },
            "saturation": {
                "color": [1,1,1],
                "linestyle": "-",
                "linewidth": 3,
            },
            "zones": TEST_EXAMPLE_ZONES,
        }   
    
    # app_json = json.dumps(custom_style, indent=4)
    # y = json.loads(app_json)
    
    with open('data.json', 'w') as outfile:
        json.dump(custom_style, outfile, indent=4)
        
        
    with open('data.json', 'r') as openfile:
        json_read = json.load(openfile)        
        
    psy = PsychroChart(json_read,TEST_EXAMPLE_ZONES)
    fig = psy.plot()
    fig.show()

    fig.write_html("psychchart.html")
    fig.update_layout(showlegend=False)

    fig.write_image("psychchart.jpg")
    fig.write_image("psychchart.pdf")