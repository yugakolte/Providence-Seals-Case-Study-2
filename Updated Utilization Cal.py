# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:43:58 2021

@author: sbgadhwa
"""

import csv, math
import pandas as pd

fileP = r"ProvidenceSealsData.csv"

machines = ["100", "101", "103", "104", "105", "200", "201", "202", "203", "300", "302"]
mNumbers = {"100":2, "101":2, "103":1, "104":2, "105":2, "200":1, "201":1, "202":1, "203":1, "300":1, "302":1}


totalOrders = [{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}]


probabilityMatrix = [{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}]


probForEachMachine = [{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}]


timeMatrix = [{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0},
{"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}]

#totalorders = [o1, o2, o3, o4, o5, o6 o7, o8, o9, o10, o11, o12, o13, o14, o15, o16, o17, o18, o19, o20, o21, o22, o23, o24, o25, o26, o27, o28, o29, o30]

def cycleTime(u, m, t, c):
    c1 = 2*(m+1)
    c2 = math.sqrt(c1)-1
    u1 = u**(c2)
    u2 = m*(1-u)
    uterm = u1/u2
   
    returnTerm = ((c+1)/2)*uterm*t + t
    return returnTerm



def effProcTime(k, t, s):
    return (t + s/k)


print("\n----------------------------------------------- 1) ---------------------------------------------\n")

mUtilization = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
mDirectUtil = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}

mHours = {"100" : 8000, "101" : 8000, "103" : 4000, "104" : 8000, "105" : 8000, "200" : 4000, "201" : 4000, "202" : 4000, "203" : 4000, "300" : 4000, "302" : 4000}


sumArrival = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
sumTotalIncidentForProb = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}


#print("------------------------------1a) Probability of each order arriving on a particular machine is as represented in a dictionary------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            sumArrival[str(int(float(i[5])))] =  sumArrival[str(int(float(i[5])))] + float(i[2])
       
       
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            j = str(int(float(i[5])))
            probabilityMatrix[int(i[0])-1][j] = probabilityMatrix[int(i[0])-1][j] + float(i[2])/sumArrival[j]

#for i in range(0, len(probabilityMatrix)):
#   print(f"Order {i+1} : {probabilityMatrix[i]} \n")

print("\n------------------------------1a) Probability of each order arriving on a particular machine is as represented in table below------------------------------\n")
trialDfa = pd.DataFrame(probabilityMatrix)
ordersA = list(range(1, 31))
trialDfa['Order'] = ordersA
trialDfa.insert(0, 'Order', trialDfa.pop('Order'))
trialDfa.set_index(['Order'])
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(trialDfa)

print("\n")





#print("------------------------------1a) Probability of each order arriving on each machine is as represented in a dictionary------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            sumTotalIncidentForProb[str(int(float(i[5])))] =  sumTotalIncidentForProb[str(int(float(i[5])))] + float(i[2])
            
        if i[10]!='' and str(int(float(i[5]))) in machines:
            sumTotalIncidentForProb[str(int(float(i[10])))] =  sumTotalIncidentForProb[str(int(float(i[10])))] + float(i[2])
            
        if i[15]!='' and str(int(float(i[15]))) in machines:
            sumTotalIncidentForProb[str(int(float(i[15])))] =  sumTotalIncidentForProb[str(int(float(i[15])))] + float(i[2])
            
        if i[20]!='' and str(int(float(i[20]))) in machines:
            sumTotalIncidentForProb[str(int(float(i[20])))] =  sumTotalIncidentForProb[str(int(float(i[20])))] + float(i[2])
       

with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            j = str(int(float(i[5])))
            probForEachMachine[int(i[0])-1][j] = probForEachMachine[int(i[0])-1][j] + float(i[2])/sumTotalIncidentForProb[j]
            
        if i[10]!='' and str(int(float(i[10]))) in machines:
            j = str(int(float(i[10])))
            probForEachMachine[int(i[0])-1][j] = probForEachMachine[int(i[0])-1][j] + float(i[2])/sumTotalIncidentForProb[j]
            
        if i[15]!='' and str(int(float(i[15]))) in machines:
            j = str(int(float(i[15])))
            probForEachMachine[int(i[0])-1][j] = probForEachMachine[int(i[0])-1][j] + float(i[2])/sumTotalIncidentForProb[j]
            
        if i[20]!='' and str(int(float(i[20]))) in machines:
            j = str(int(float(i[20])))
            probForEachMachine[int(i[0])-1][j] = probForEachMachine[int(i[0])-1][j] + float(i[2])/sumTotalIncidentForProb[j]


print("\n------------------------------1a)...Cont.... Probability of each order arriving on a any machine is as represented in table below------------------------------\n")
trialDfaa = pd.DataFrame(probForEachMachine)
ordersA = list(range(1, 31))
trialDfaa['Order'] = ordersA
trialDfaa.insert(0, 'Order', trialDfaa.pop('Order'))
trialDfaa.set_index(['Order'])
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(trialDfaa)
print("\n")

for i in machines:
    for j in probForEachMachine:
        j[i] = j[i]/mNumbers[i]




print("\n------------------------------1a)...Cont.... Probability of each order arriving on one of each machine is as represented in table below (This value to be used to multiply te with)------------------------------\n")
trialDfaa2 = pd.DataFrame(probForEachMachine)
ordersA = list(range(1, 31))
trialDfaa2['Order'] = ordersA
trialDfaa2.insert(0, 'Order', trialDfaa2.pop('Order'))
trialDfaa2.set_index(['Order'])
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(trialDfaa2)
print("\n")


with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            j = str(int(float(i[5])))
            timeMatrix[int(i[0])-1][j] = timeMatrix[int(i[0])-1][j] + effProcTime(float(i[3]), float(i[7]), float(i[6]))*probForEachMachine[int(i[0])-1][j]
           
           
        if i[10]!='' and str(int(float(i[10]))) in machines:
            j = str(int(float(i[10])))
            timeMatrix[int(i[0])-1][j] = timeMatrix[int(i[0])-1][j] + effProcTime(float(i[3]), float(i[12]), float(i[11]))*probForEachMachine[int(i[0])-1][j]
           
        if i[15]!='' and str(int(float(i[15]))) in machines:
            j = str(int(float(i[15])))
            timeMatrix[int(i[0])-1][j] = timeMatrix[int(i[0])-1][j] + effProcTime(float(i[3]), float(i[17]), float(i[16]))*probForEachMachine[int(i[0])-1][j]
           
        if i[20]!='' and str(int(float(i[20]))) in machines:
            j = str(int(float(i[20])))
            timeMatrix[int(i[0])-1][j] = timeMatrix[int(i[0])-1][j] + effProcTime(float(i[3]), float(i[22]), float(i[21]))*probForEachMachine[int(i[0])-1][j]
         
   
   
print("\n------------------------------1b) Each Order's effective processing time at each machine represented in table below------------------------------\n")
trialDfb = pd.DataFrame(timeMatrix)
ordersB = list(range(1, 31))
trialDfb['Order'] = ordersB
trialDfb.insert(0, 'Order', trialDfb.pop('Order'))
trialDfb.set_index(['Order'])
print(trialDfb)

totalTeForMachines = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
meanTeForMachines = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
varTeForMachines = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}


print("\n-----------------------------1b) Total processing time for each machine---------------------------\n")


for i in trialDfb:
    totalTeForMachines[i] = trialDfb[trialDfb[i]>0][i].sum()

totalTeForMachines.pop('Order')
print("\nTo make 1 unit of each of the orders : ")
for i in totalTeForMachines:
    print(f"Total processing time for machine {i} is : {totalTeForMachines[i]} hours")


print("\n-----------------------------1b) Mean effective processing time for each machine---------------------------\n")


for i in trialDfb:
    meanTeForMachines[i] = trialDfb[trialDfb[i]>0][i].mean()

meanTeForMachines.pop('Order')
for i in meanTeForMachines:
    print(f"Te for {i} : {meanTeForMachines[i]}")
print("\n\n")

print("\n-----------------------------1b) Variance of effective processing time for each machine---------------------------\n")

for i in trialDfb:
    varTeForMachines[i] = trialDfb[trialDfb[i]>0][i].var()

varTeForMachines.pop('Order')
for i in varTeForMachines:
    if str(varTeForMachines[i]) == "nan":
        varTeForMachines[i] = 0
    print(f"Sigma2E for {i} : {varTeForMachines[i]}")
print("\n\n")



print("\n------------------------------1c) Ce squared Values for each machine------------------------------\n")

ce2Vals = dict((k, varTeForMachines[k] / meanTeForMachines[k]**2) for k in meanTeForMachines)

for i in ce2Vals:
    print(f"Ce2 for machine {i} : {ce2Vals[i]}")
print("\n\n")


print("\n------------------------------1c) Utilization------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!="":
            if str(int(float(i[5]))) in mUtilization:
                j = str(int(float(i[5])))
                mUtilization[j] = mUtilization[j] + float(i[8])
       
        if i[10]!="":
            if str(int(float(i[10]))) in mUtilization:
                j = str(int(float(i[10])))
                mUtilization[j] = mUtilization[j] + float(i[13])
               
        if i[15]!="":
            if str(int(float(i[15]))) in mUtilization:
                j = str(int(float(i[15])))
                mUtilization[j] = mUtilization[j] + float(i[18])
               
        if i[20]!="":
            if str(int(float(i[20]))) in mUtilization:
                j = str(int(float(i[20])))
                mUtilization[j] = mUtilization[j] + float(i[23])

utilValues = dict((k, (mUtilization[k]) / mHours[k]) for k in mHours)

for i in mUtilization:
    print(f"Load on machine {i} : {mUtilization[i]} ")
print("\n\n")    

for i in utilValues:
    print(f"{i} : {utilValues[i]}")
print("\n\n")


print("\n------------------------------1c) Direct Utilization------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!="":
            if str(int(float(i[5]))) in mDirectUtil:
                j = str(int(float(i[5])))
                mDirectUtil[j] = mDirectUtil[j] + (float(i[4])*(float(i[3])*float(i[7]) + float(i[6]))/float(i[3]))
       
        if i[10]!="":
            if str(int(float(i[10]))) in mDirectUtil:
                j = str(int(float(i[10])))
                mDirectUtil[j] = mDirectUtil[j] + (float(i[4])*(float(i[3])*float(i[12]) + float(i[11]))/float(i[3]))
               
        if i[15]!="":
            if str(int(float(i[15]))) in mDirectUtil:
                j = str(int(float(i[15])))
                mDirectUtil[j] = mDirectUtil[j] + (float(i[4])*(float(i[3])*float(i[17]) + float(i[16]))/float(i[3]))
               
        if i[20]!="":
            if str(int(float(i[20]))) in mDirectUtil:
                j = str(int(float(i[20])))
                mDirectUtil[j] = mDirectUtil[j] + (float(i[4])*(float(i[3])*float(i[22]) + float(i[21]))/float(i[3]))


directFinalUtil = dict((k, (mDirectUtil[k]) / mNumbers[k]) for k in mHours)
for i in directFinalUtil:
    print(f"{i} : {directFinalUtil[i]}")
print("\n\n")




#print("------------------------------1c) Each Order's cycle time at each machine represented in a dictionary------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[5]!='' and str(int(float(i[5]))) in machines:
            j = str(int(float(i[5])))
            #print("order : ", int(i[0]))
            #print("On machine : ", j)
            totalOrders[int(i[0])-1][j] = totalOrders[int(i[0])-1][j] + cycleTime(utilValues[j], mNumbers[j], meanTeForMachines[j], ce2Vals[j])
           
           
        if i[10]!='' and str(int(float(i[10]))) in machines:
            j = str(int(float(i[10])))
            totalOrders[int(i[0])-1][j] = totalOrders[int(i[0])-1][j] + cycleTime(utilValues[j], mNumbers[j], meanTeForMachines[j], ce2Vals[j])
           
        if i[15]!='' and str(int(float(i[15]))) in machines:
            j = str(int(float(i[15])))
            totalOrders[int(i[0])-1][j] = totalOrders[int(i[0])-1][j] + cycleTime(utilValues[j], mNumbers[j], meanTeForMachines[j], ce2Vals[j])
           
        if i[20]!='' and str(int(float(i[20]))) in machines:
            j = str(int(float(i[20])))
            totalOrders[int(i[0])-1][j] = totalOrders[int(i[0])-1][j] + cycleTime(utilValues[j], mNumbers[j], meanTeForMachines[j], ce2Vals[j])
         
   
#for i in range(0, len(totalOrders)):
#   print(f"Order {i+1} : {totalOrders[i]} \n")
   
print("\n------------------------------1c) Each Order's cycle time at each machine represented in table below------------------------------\n")
trialDf = pd.DataFrame(totalOrders)
ordersC = list(range(1, 31))
trialDf['Order'] = ordersC
trialDf.insert(0, 'Order', trialDf.pop('Order'))
trialDf.set_index(['Order'])
print(trialDf)






print("\n----------------------------------------------- 3) ---------------------------------------------\n")


cluster1Orders = [7,2,5,6,9,12,13,15,16,24,25,30,14,23,1,11,21]
cluster1Machines = ["100", "101"]
cluster1MachineHours = {"100" : 8000, "101" : 8000}
cluster1Load = {"100" : 0, "101" : 0}
cluster1SetupTimes = {"100" : 0, "101" : 0}
cluster1SetupTime = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
maxSetupTimeC1 = 0

print(f"\n------------------------------Cluster 1 Analysis ({cluster1Machines})------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[0]!='' and int(i[0])>0:
            j = int(i[0])
            if j in cluster1Orders:
               
                if i[5]!='' and float(i[6]) > maxSetupTimeC1:
                    maxSetupTimeC1 = float(i[2])*float(i[6])
                   
                if i[10]!='' and float(i[11]) > maxSetupTimeC1:
                    maxSetupTimeC1 = float(i[2])*float(i[11])
                   
                if i[15]!='' and float(i[16]) > maxSetupTimeC1:
                    maxSetupTimeC1 = float(i[2])*float(i[16])
                   
                if i[20]!='' and float(i[21]) > maxSetupTimeC1:
                    maxSetupTimeC1 = float(i[2])*float(i[21])
                   
perMachineLoadCluster1 = [cluster1Load]*len(cluster1Orders)

with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        f = int(float(i[0]))
        if i[0]!='' and f in cluster1Orders and str(int(float(i[5]))) in perMachineLoadCluster1[cluster1Orders.index(f)]:
            k = str(int(float(i[5])))
            perMachineLoadCluster1[cluster1Orders.index(f)][k] = perMachineLoadCluster1[cluster1Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[7])
           
        if i[0]!='' and f in cluster1Orders and str(int(float(i[10]))) in perMachineLoadCluster1[cluster1Orders.index(f)]:
            k = str(int(float(i[10])))
            perMachineLoadCluster1[cluster1Orders.index(f)][k] = perMachineLoadCluster1[cluster1Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[12])
           
        if i[0]!='' and f in cluster1Orders and i[15]!='' and str(int(float(i[15]))) in perMachineLoadCluster1[cluster1Orders.index(f)]:
            k = str(int(float(i[15])))
            perMachineLoadCluster1[cluster1Orders.index(f)][k] = perMachineLoadCluster1[cluster1Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[17])
           
        if i[0]!='' and f in cluster1Orders and i[20]!='' and str(int(float(i[20]))) in perMachineLoadCluster1[cluster1Orders.index(f)]:
            k = str(int(float(i[20])))
            perMachineLoadCluster1[cluster1Orders.index(f)][k] = perMachineLoadCluster1[cluster1Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[22])
           
cluster1Load = perMachineLoadCluster1[0]
for i in cluster1Load:
    cluster1Load[i] = cluster1Load[i] + maxSetupTimeC1
   
print(cluster1Load)
cluster1Util = dict((k, float(cluster1Load[k]) / cluster1MachineHours[k]) for k in cluster1MachineHours)
print(cluster1Util)

print("\n\n")    
print(f"The max setup time for cluster 1 is : {maxSetupTimeC1} hours \n")
for i in cluster1Util:
    print(f"Utilization for {i} : {cluster1Util[i]}")
    print(f"Utilization % at machine {i} due to setup time is : {100*maxSetupTimeC1/cluster1Load[i]} %\n")

avCl1 = sum(list(cluster1Util.values()))/len(list(cluster1Util.values()))
print("Average utilization for cluster 1 is : ", avCl1)
print(f"Part of utilization due to setup time is :  {100*maxSetupTimeC1/(sum(list(cluster1Load.values()))/len(list(cluster1Load.values())))} %\n")
print("\n\n")    









cluster2Orders = [26, 18, 29, 19, 3, 10, 17, 8, 28, 4]
cluster2Machines = ["202", "300", "105", "104", "200", "302"]
cluster2MachineHours = {"202" : 4000, "300" : 4000, "105" : 8000, "104" : 8000, "200" : 4000, "302" : 4000}
cluster2Load = {"202" : 0, "300" : 0, "105" : 0, "104" : 0, "200" : 0, "302" : 0}
cluster2SetupTime = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
maxSetupTimeC2 = 0




print(f"\n------------------------------Cluster 2 Analysis ({cluster2Machines})------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[0]!='' and int(i[0])>0:
            j = int(i[0])
            if j in cluster2Orders:
               
                if i[5]!='' and float(i[6]) > maxSetupTimeC2:
                    maxSetupTimeC2 = float(i[2])*float(i[6])
                   
                if i[10]!='' and float(i[11]) > maxSetupTimeC2:
                    maxSetupTimeC2 = float(i[2])*float(i[11])
                   
                if i[15]!='' and float(i[16]) > maxSetupTimeC2:
                    maxSetupTimeC2 = float(i[2])*float(i[16])
                   
                if i[20]!='' and float(i[21]) > maxSetupTimeC2:
                    maxSetupTimeC2 = float(i[2])*float(i[21])
                   
perMachineLoadCluster2 = [cluster2Load]*len(cluster2Orders)

with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        f = int(float(i[0]))
        if i[0]!='' and f in cluster2Orders and str(int(float(i[5]))) in perMachineLoadCluster2[cluster2Orders.index(f)]:
            k = str(int(float(i[5])))
            perMachineLoadCluster2[cluster2Orders.index(f)][k] = perMachineLoadCluster2[cluster2Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[7])
           
        if i[0]!='' and f in cluster2Orders and str(int(float(i[10]))) in perMachineLoadCluster2[cluster2Orders.index(f)]:
            k = str(int(float(i[10])))
            perMachineLoadCluster2[cluster2Orders.index(f)][k] = perMachineLoadCluster2[cluster2Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[12])
           
        if i[0]!='' and f in cluster2Orders and i[15]!='' and str(int(float(i[15]))) in perMachineLoadCluster2[cluster2Orders.index(f)]:
            k = str(int(float(i[15])))
            perMachineLoadCluster2[cluster2Orders.index(f)][k] = perMachineLoadCluster2[cluster2Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[17])
           
        if i[0]!='' and f in cluster2Orders and i[20]!='' and str(int(float(i[20]))) in perMachineLoadCluster2[cluster2Orders.index(f)]:
            k = str(int(float(i[20])))
            perMachineLoadCluster2[cluster2Orders.index(f)][k] = perMachineLoadCluster2[cluster2Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[22])
           
cluster2Load = perMachineLoadCluster2[0]
for i in cluster2Load:
    cluster2Load[i] = cluster2Load[i] + maxSetupTimeC2
   
print(cluster2Load)
cluster2Util = dict((k, float(cluster2Load[k]) / cluster2MachineHours[k]) for k in cluster2MachineHours)

print("\n\n")   
print(f"The max setup time for cluster 2 is : {maxSetupTimeC2} hours \n")
 
for i in cluster2Util:
    print(f"Utilization for {i} : {cluster2Util[i]}")
    print(f"Utilization % at machine {i} due to setup time is : {100*maxSetupTimeC2/cluster2Load[i]} %\n")

avCl2 = sum(list(cluster2Util.values()))/len(list(cluster2Util.values()))
print("Average utilization for cluster 2 is : ", avCl2)
print(f"Part of utilization due to setup time is :  {100*maxSetupTimeC2/(sum(list(cluster2Load.values()))/len(list(cluster2Load.values())))} %\n")
print("\n\n") 




cluster3Orders = [22, 27, 20]
cluster3Machines = ["103", "203"]
cluster3MachineHours = {"103" : 4000, "203" : 4000}
cluster3Load =  {"103" : 0, "203" : 0}
cluster3SetupTime = {"100" : 0, "101" : 0, "103" : 0, "104" : 0, "105" : 0, "200" : 0, "201" : 0, "202" : 0, "203" : 0, "300" : 0, "302" : 0}
maxSetupTimeC3 = 0





print(f"\n------------------------------Cluster 3 Analysis ({cluster3Machines})------------------------------\n")
with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[0]!='' and int(i[0])>0:
            j = int(i[0])
            if j in cluster3Orders:
               
                if i[5]!='' and float(i[6]) > maxSetupTimeC3:
                    maxSetupTimeC3 = float(i[2])*float(i[6])
                   
                if i[10]!='' and float(i[11]) > maxSetupTimeC3:
                    maxSetupTimeC3 = float(i[2])*float(i[11])
                   
                if i[15]!='' and float(i[16]) > maxSetupTimeC3:
                    maxSetupTimeC3 = float(i[2])*float(i[16])
                   
                if i[20]!='' and float(i[21]) > maxSetupTimeC3:
                    maxSetupTimeC3 = float(i[2])*float(i[21])
                   
perMachineLoadCluster3 = [cluster3Load]*len(cluster3Orders)

with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        f = int(float(i[0]))
        if i[0]!='' and f in cluster3Orders and str(int(float(i[5]))) in perMachineLoadCluster3[cluster3Orders.index(f)]:
            k = str(int(float(i[5])))
            perMachineLoadCluster3[cluster3Orders.index(f)][k] = perMachineLoadCluster3[cluster3Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[7])
           
        if i[0]!='' and f in cluster3Orders and str(int(float(i[10]))) in perMachineLoadCluster3[cluster3Orders.index(f)]:
            k = str(int(float(i[10])))
            perMachineLoadCluster3[cluster3Orders.index(f)][k] = perMachineLoadCluster3[cluster3Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[12])
           
        if i[0]!='' and f in cluster3Orders and i[15]!='' and str(int(float(i[15]))) in perMachineLoadCluster3[cluster3Orders.index(f)]:
            k = str(int(float(i[15])))
            perMachineLoadCluster3[cluster3Orders.index(f)][k] = perMachineLoadCluster3[cluster3Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[17])
           
        if i[0]!='' and f in cluster3Orders and i[20]!='' and str(int(float(i[20]))) in perMachineLoadCluster3[cluster3Orders.index(f)]:
            k = str(int(float(i[20])))
            perMachineLoadCluster3[cluster3Orders.index(f)][k] = perMachineLoadCluster3[cluster3Orders.index(f)][k] + float(i[1].replace(",",""))*float(i[22])
           
cluster3Load = perMachineLoadCluster3[0]
for i in cluster3Load:
    cluster3Load[i] = cluster3Load[i] + maxSetupTimeC3
   
print(cluster3Load)
cluster3Util = dict((k, float(cluster3Load[k]) / cluster3MachineHours[k]) for k in cluster3MachineHours)

print("\n\n")
print(f"The max setup time for cluster 3 is : {maxSetupTimeC3} hours \n")
   
for i in cluster3Util:
    print(f"Utilization for {i} : {cluster3Util[i]}")
    print(f"Utilization % at machine {i} due to setup time is : {100*maxSetupTimeC3/cluster3Load[i]} %\n")

avCl3 = sum(list(cluster3Util.values()))/len(list(cluster3Util.values()))
print("Average utilization for cluster 3 is : ", avCl3)
print(f"Part of utilization due to setup time is :  {100*maxSetupTimeC3/(sum(list(cluster3Load.values()))/len(list(cluster3Load.values())))} %\n")
print("\n\n") 



print("\n----------------------------------------------- 4) ---------------------------------------------\n")


cluster1EffTimeMatrix = [{"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0},
                         {"100" : 0, "101" : 0}]


with open(fileP, "r") as csvFile:
    content = csv.reader(csvFile)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    next(content)
    for i in content:
        if i[0]!='' and int(i[0]) in cluster1Orders:
            print(f"int(i[0]), str(int(float(i[5]))), str(int(float(i[5])))")




