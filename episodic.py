"""传染病预测模型"""
import matplotlib.pyplot as plt
import numpy as np
from myepisodic import contactestimate
from myepisodic import setting

deathrate = setting.deathrate  # 死亡率
cure = setting.cure  # 治愈率
i0 = setting.i0  # 初始感染人数
t = setting.t  # 时间差分步长
time = setting.time  # 结束时刻（天）;
e = setting.e  # 疑似病例传染调整参数
a = setting.a  # 疑似转为确诊比例
b = setting.b  # 疑似转为隔离比例
c = setting.c  # 隔离转入治疗比例
d = setting.d  # 确诊转入治疗比例

suspected = [setting.s0]  # 疑似人数
quarantine = [setting.q0]  # 已隔离但尚未治疗人数
treatment = [setting.t0]  # 已隔离且已经开始治疗人数
infection = [setting.i0]  # 感染人数
removal = [setting.r0]  # 治愈人数
death = [setting.d0]  # 死亡人数

for k in range(time):
    '''疑似人数变化'''
    suspected.append(-1)
    suspected[k+1] = (t * (contactestimate.contact(k) * e - a - b) + 1) * suspected[k] + t * contactestimate.contact(k) * t * infection[k]

    '''感染人数变化'''
    infection.append(-1)
    infection[k+1] = (1-t*(deathrate+d))*infection[k]+t*a*suspected[k]

    '''隔离人数变化'''
    quarantine.append(-1)
    quarantine[k+1] = (1-c*t)*quarantine[k]+t*b*suspected[k]

    '''治疗人数变化'''
    treatment.append(-1)
    treatment[k+1] = (1-t*(deathrate+cure))*treatment[k]+t*d*infection[k]+t*c*quarantine[k]

    '''治愈人数变化'''
    removal.append(-1)
    removal[k+1] = removal[k]+t*cure*treatment[k]

    '''死亡人数变化'''
    death.append(-1)
    death[k+1] = death[k]+t*deathrate*(infection[k]+treatment[k])

plt.xticks(np.arange(0, time, 1))
plt.yticks(np.arange(0, 10000, 10))

plt.plot(list(range(time+1)), infection, '*-')
# plt.plot(list(range(time+1)), quarantine, '*-')
plt.show()
