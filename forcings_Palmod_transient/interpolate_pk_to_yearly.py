# coding: utf-8
from scipy import interpolate
import numpy as np
PK_GHG = np.genfromtxt("Koehler_GHG_forcing_0.01ka_resolution.dat")
age = PK_GHG[:, 0]
co2 = PK_GHG[:, 1]
ch4 = PK_GHG[:, 2]
n2o = PK_GHG[:, 3]
co2_interpolate_func = interpolate.interp1d(age, co2)
ch4_interpolate_fuc = interpolate.interp1d(age, ch4)
n2o_interpolate_func = interpolate.interp1d(age, n2o)
age_new = np.arange(0, 7, 0.001)
co2_new = co2_interpolate_func(age_new)
ch4_new = ch4_interpolate_fuc(age_new)
n2o_new = n2o_interpolate_func(age_new)

np.savetxt("age_new.txt", age_new, fmt="%.3f")
np.savetxt("co2_new.txt", co2_new, fmt="%.3f")
np.savetxt("ch4_new.txt", ch4_new, fmt="%.3f")
np.savetxt("n2o_new.txt", n2o_new, fmt="%.3f")
