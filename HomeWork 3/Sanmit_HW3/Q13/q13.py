# -*- coding: utf-8 -*-
"""Q13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tHQKJcV0QpDTQ0nCd2KilEGM4SzX_EcY

# Question 13

![image.png](data:image/png;base64,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)

For point 1 we have:

$$\frac{V_+ - V_1}{R_1} + \frac{V_1}{R_4} + C_1\frac{d}{dt}(V_1-V_2)=0  \\ \implies \frac{(x_1 -x_+)e^{i\omega t}}{R_1} + \frac{x_1e^{i\omega t}}{R_4}+ iC_1\omega (x_1 -x_2)e^{i\omega t} =0\\ \implies \frac{x_1}{R_1} - \frac{x_+}{R_4} + iC_1\omega x_1 - iC_1\omega x_2=0 \\ \implies (\frac{1}{R_1} + \frac{1}{R_4} +iC_1\omega)x_1 - iC_1\omega x_2 = \frac{x_+}{R_1}$$  


Similarly, for point 2 we have:

$$\frac{V_+ - V_2}{R_2}+\frac{V_2}{R_5} + C_1 \frac{d}{dt}(V_2-V_1) + C_2\frac{d}{dt}(V_3-V_2)=0 \\ \implies \frac{(x_2 -x_+)e^{i\omega t}}{R_2} + \frac{x_2e^{i\omega t}}{R_5}+ iC_1\omega (x_2 -x_1)e^{i\omega t}  + iC_2\omega (x_2 -x_3)e^{i\omega t}=0 \\ \implies -i\omega C_1 x_1 +(\frac{1}{R_2} + \frac{1}{R_5} + i\omega C_1 + i\omega C_2)x_2 -i\omega C_2 x_3=\frac{x_+}{R_2}$$

point 3 we have:

$$\frac{V_+ - V_3}{R_3} + \frac{V_3}{R_6} + C_2\frac{d}{dt}(V_3-V_2)=0  \\ \implies \frac{(x_3 -x_+)e^{i\omega t}}{R_3} + \frac{x_3e^{i\omega t}}{R_6}+ iC_1\omega (x_3 -x_2)e^{i\omega t} =0\\ \implies \frac{x_3}{R_1} - \frac{x_+}{R_6} + iC_2\omega x_2 - iC_2\omega x_2=0 \\ \implies (\frac{1}{R_3} + \frac{1}{R_6} +iC_2\omega)x_3 - iC_2\omega x_2 = \frac{x_+}{R_3}  $$
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.linalg as lg
import cmath
from numpy import array



R1=1
R2=2
R3=1
R4=2
R5=1
R6=2
C1=1e-6
C2=0.5e-6
xp=3
omega=1e12



V=array([[1/R1 + 1/R4 + (C1*omega)*1j, -(C1*omega)*1j, 0],
         [-(C1*omega)*1j, (1/R2 +1/R5 +omega*C1*1j +omega*C2*1j), -(C2*omega)*1j],
         [0, -C2*omega*1j, 1/R3 + 1/R6 + C2*omega*1j]])

A=array([xp/R1, xp/R2, xp/R3])

sol=lg.solve(V,A)
amplitude=[]
phase=[]
for i in range(len(sol)):
  amplitude.append(cmath.polar(sol[i])[0])
  phase.append(cmath.polar(sol[i])[1])

print('voltages are respectively:', sol)
print('amplitudes are respectively:', amplitude)
print('phases are respectively:', phase)