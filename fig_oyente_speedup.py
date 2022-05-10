import matplotlib.pyplot as plt
import os
from util import *
import json

def get_time_x_y(result_dir1, result_dir2, global_timeout):
    time_x = []
    time_y = []

    files = os.listdir(result_dir1)
    print(files)

    for file_name in files:
        try:
            res = json.loads(open(result_dir1+file_name).read())
            type1_time = res["time"]
            res = json.loads(open(result_dir2+file_name).read())
            type2_time = res["time"]
            time_x.append(type1_time)
            time_y.append(type2_time)
        except:
            continue
    
    return time_x, time_y


origin_res = get_oyente_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=10000, global_timeout=3600, cpu_count=4)
pork_res = get_oyente_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=10000, global_timeout=3600, cpu_count=16)

origin_time, pork_time = get_time_x_y(origin_res, pork_res, 3600)
speedup = []
for i in range(len(pork_time)):
    speedup.append(origin_time[i]/pork_time[i])

msize=20
plt.scatter(origin_time, speedup, label='L=$1\\times10^7$')

#设置坐标轴范围
#设置坐标轴名称
plt.xlabel('Dealed Blocks', fontsize=20)
# plt.xticks([0, 10, 20,100])
plt.ylabel('# UTXO Cache Missed', fontsize=20)
# plt.ylim((18,30))

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.legend(loc=2, ncol=1, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列
plt.tight_layout()
plt.show()
# plt.savefig("blocks_cachemiss.pdf")
