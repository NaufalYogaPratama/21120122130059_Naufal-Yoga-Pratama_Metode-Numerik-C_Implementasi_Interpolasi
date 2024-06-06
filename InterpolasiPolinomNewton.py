#Nama: Naufal Yoga Pratama
#NIM: 21120122130059
#Kelas: C

import numpy as np
import matplotlib.pyplot as plt

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])


#Fungsi untuk menghitung tabel selisih terbagi Newton.
#x: array dari titik data x
#y: array dari nilai data y
#return: array dari koefisien polinomial Newton
def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef[0, :]


#Fungsi untuk menghitung nilai interpolasi menggunakan polinomial Newton. 
# coef: koefisien polinomial Newton 
# x_data: array dari titik data x 
# x: titik di mana interpolasi dihitung return: nilai interpolasi di x
def newton_poly(coef, x_data, x):
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Menguji interpolasi Newton
a_s = divided_diff(x, y)
x_new = np.linspace(5, 40, 400)
y_newton = [newton_poly(a_s, x, i) for i in x_new]

plt.plot(x, y, 'o', label='Data Asli')
plt.plot(x_new, y_newton, '--', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Polinom Newton')
plt.show()
