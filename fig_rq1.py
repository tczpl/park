import json
import os
from util import *
import oyente_check
import matplotlib.pyplot as plt

ylim_of = {
    "oyente":{
        "smartbugs":18,
        "top1k":70
    },
    "mythril":{
        "smartbugs":30,
        "top1k":100
    }
}

def get_dataset(dataset, tool):
    plt.cla()

    x_origin = [1,4,7]
    y_origin = []
    x_originpl = [2,5,8]
    y_originpl = []

    cpus = [2, 4, 8]
    for cpu in cpus:
        if tool == "oyente":
            result_dir = get_oyente_dir(dataset=dataset, run_type="origin", solver_timeout_ms=1000, global_timeout=100, cpu_count=cpu)
        if tool == "mythril":
            result_dir = get_mythril_dir(dataset=dataset, run_type="origin", solver_timeout_ms=1000, global_timeout=100, cpu_count=cpu, tx_count=1)
        y_origin.append(get_avg_time(result_dir))

    cpus = [2, 4, 8]
    for cpu in cpus:
        if tool == "oyente":
            result_dir = get_oyente_dir(dataset=dataset, run_type="originpl", solver_timeout_ms=1000, global_timeout=100, cpu_count=cpu)
        if tool == "mythril":
            result_dir = get_mythril_dir(dataset=dataset, run_type="originpl", solver_timeout_ms=1000, global_timeout=100, cpu_count=cpu, tx_count=1)
        y_originpl.append(get_avg_time(result_dir))


    labels = ["2 Cores", "4 Cores", "8 Cores"]

    plt.bar(x_origin, y_origin, 1, hatch='--', color='white', edgecolor='blue', label='Origin')
    plt.bar(x_originpl, y_originpl, 1, hatch='//', color='white', edgecolor='green', label='OriginPL')

    trans_index = [x_origin, x_originpl]
    trans_value = [y_origin, y_originpl]

    xindex = []
    yindex = []
    for i in trans_index:
        xindex += i
    for i in trans_value:
        yindex += i
    for i in range(len(xindex)):
        theX = xindex[i]
        theY = yindex[i]
        plt.text(theX, theY*1.02 , '%.2f'%theY, ha='center', va='bottom', fontsize=15)

    plt.ylabel("Average Time (Second)", fontsize=20)
    plt.yticks(fontsize=20)
    
    plt.ylim(0, ylim_of[tool][dataset])
    plt.xticks([1.5, 4.5, 7.5], labels=labels, rotation=0, fontsize=20)
    plt.legend(loc=2, ncol=3, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列

    plt.tight_layout()
    plt.savefig("fig/rq1_"+tool+"_"+dataset+".pdf")

#get_dataset("smartbugs", "oyente")
#get_dataset("top1k", "oyente")
#get_dataset("smartbugs", "mythril")
get_dataset("top1k", "mythril")