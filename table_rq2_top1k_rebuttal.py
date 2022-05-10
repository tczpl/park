import matplotlib.pyplot as plt
import os
from util import *
import json
import oyente_check
import mythril_check


config = {
    "st": 1,
    "gt": 3600
}
st = int(config["st"] * 1000)
gt = config["gt"]
cpu = 16
origin_dir = get_mythril_dir(dataset="top1k", run_type="origin", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=2)
pork_dir = get_mythril_dir(dataset="top1k", run_type="pork", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=2)
speedups = mythril_check.compare_dir_1by1(origin_dir, pork_dir, gt)


target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10000]
num = [0,0,0,0,0,0,0,0,0,0,0,0,0]

for speedup in speedups:
    for i in range(len(target)):
        if speedup<target[i]:
            num[i] += 1
            

#print(target)
#print(num)
