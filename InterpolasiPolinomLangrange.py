#Nama: Naufal Yoga Pratama
#NIM: 21120122130059
#Kelas: C

import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan/disoal
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

#def fungsi untuk interpolasi polinom lagrange
def lagrange_interpolation(x, y, xp):
    yp = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xp - x[j]) / (x[i] - x[j])
        yp += y[i] * p
    return yp

# Menguji interpolasi Lagrange
x_new = np.linspace(5, 40, 400)
y_new = [lagrange_interpolation(x, y, i) for i in x_new]

plt.plot(x, y, 'o', label='Data Asli')
plt.plot(x_new, y_new, '-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.show()
