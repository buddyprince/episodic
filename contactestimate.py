"""拟合感染率函数"""
import matplotlib.pyplot as plt
import openpyxl
from scipy.optimize import curve_fit

workbook = openpyxl.load_workbook(r'C:\Users\Buddy\Desktop\感染率.xlsx', data_only=True)
worksheet = workbook['Sheet1']
infectionrate = [j.value for j in worksheet['C']]
while None in infectionrate:
    infectionrate.remove(None)
infectionrate.remove('传染率')


def func(x, a, b, c, d):
    return (a+b*x)/(c+d*x)


argument = curve_fit(func, range(len(infectionrate)), infectionrate)[0]


def contact(time):
    return (argument[0]+argument[1]*time)/(argument[2]+argument[3]*time)
