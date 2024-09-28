#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:18:22 2021

@author: santosg
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 03:19:29 2021

@author: santosg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("EXA_C01_S04_01.csv")

x = datos['AGE']

plt.plot(x)

plt.show()


