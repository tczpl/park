import matplotlib.pyplot as plt
import os
from util import *
import json

from matplotlib.ticker import FuncFormatter
msize = 20

processes = range(1,33)
spspp_d1581 = []
spspp_8255c = []
spspp_epycrome = []

with open("smt_loss/curve_d1581.txt") as f:
    lines = f.readlines()
    for line in lines:
        arr = line.strip().split(" ")
        spspp_d1581.append(float(arr[2]))

with open("smt_loss/curve_8255c.txt") as f:
    lines = f.readlines()
    for line in lines:
        arr = line.strip().split(" ")
        spspp_8255c.append(float(arr[2]))

with open("smt_loss/curve_epycrome.txt") as f:
    lines = f.readlines()
    for line in lines:
        arr = line.strip().split(" ")
        spspp_epycrome.append(float(arr[2]))


ast_d1581 = []
ast_8255c = []
ast_epycrome = []
for i in range(32):
    ast_d1581.append(1000/spspp_d1581[i])
    ast_8255c.append(1000/spspp_8255c[i])
    ast_epycrome.append(1000/spspp_epycrome[i])



"""
plt.plot(processes, ast_d1581, "g-", label='Intel Xeon D1581', marker='^', markersize=msize/2)#label为标签
plt.plot(processes, ast_8255c, "b-", label='Intel Xeon 8255C', marker='.', markersize=msize/2)#label为标签
plt.plot(processes, ast_epycrome, "r-", label='AMD EPYC Rome', marker='*', markersize=msize/2)#label为标签

plt.xlabel('Number of Processes', fontsize=20)    #设置x轴标题
plt.ylabel('Average Solving Time (ms)', fontsize=20)   #设置Y1轴标题

location = 2
plt.legend(loc=location, ncol=1, fontsize=17)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(1,32)

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/smt_time.pdf")
"""

slpp_d1581 = [0]
slpp_8255c = [0]
slpp_epycrome = [0]
for i in range(1,32):
    slpp_d1581.append(spspp_d1581[i]/spspp_d1581[0] - 1)
    slpp_8255c.append(spspp_8255c[i]/spspp_8255c[0] - 1)
    slpp_epycrome.append(spspp_epycrome[i]/spspp_epycrome[0] - 1)



plt.plot(processes, slpp_d1581, "g-", label='Intel Xeon D1581', marker='^', markersize=msize/2)#label为标签
plt.plot(processes, slpp_8255c, "b-", label='Intel Xeon 8255C', marker='.', markersize=msize/2)#label为标签
plt.plot(processes, slpp_epycrome, "r-", label='AMD EPYC Rome', marker='*', markersize=msize/2)#label为标签

plt.xlabel('Number of Processes', fontsize=20)    #设置x轴标题
plt.ylabel('SMT Loss Per Process', fontsize=20)   #设置Y1轴标题

def to_percent(temp, position):
    return '%1.0f'%(100*temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))

location = 3
plt.legend(loc=location, ncol=1, fontsize=17)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.xlim(1,32)

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/smt_loss.pdf")

