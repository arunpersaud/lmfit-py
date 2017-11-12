#!/usr/bin/env python
#<examples/doc_load_modelresult.py>
import numpy as np
from lmfit.model import load_modelresult
import matplotlib.pyplot as plt

data = np.loadtxt('model1d_gauss.dat')
x = data[:, 0]
y = data[:, 1]


result = load_modelresult('gauss_modelresult.sav')

print(result.fit_report())

plt.plot(x, y,         'bo')
# plt.plot(x, result.init_fit, 'k--')
plt.plot(x, result.best_fit, 'r-')
plt.show()
#<end examples/doc_load_modelresult.py>
