import matplotlib.pyplot as plt
import os
from util import *
import json
import oyente_check
import mythril_check



output = open("table_rq2_smartbugs.csv", "w")

def write_row(row):
    global output
    to_write = []
    for index in range(len(row)):
        i = row[index]
        if type(i)==float:
            if index == 7 or index==9:
                to_write.append(format(i, ".2f")+"x")
            else:
                to_write.append(format(i, ".2f"))
        else:
            to_write.append(str(i))
    output.write(",".join(to_write)+"\n")

configs = [{
    "st": 0.1,
    "gt": 50
},{
    "st": 1,
    "gt": 300
},{
    "st": 10,
    "gt": 3600
}]
for config in configs:
    st = int(config["st"] * 1000)
    gt = config["gt"]
    origin_dir = get_oyente_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=st, global_timeout=gt, cpu_count=4)
    
    cmp_res = oyente_check.compare_dir(origin_dir, origin_dir, gt)
    all_label = oyente_check.compare_label(origin_dir, origin_dir)
    full_label = oyente_check.compare_label(origin_dir, origin_dir, "full", gt)
    timeout_label = oyente_check.compare_label(origin_dir, origin_dir, "timeout", gt)

    write_row([
        "oyente", str(config["st"])+":"+str(config["gt"]), "origin",
        full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],"-",

        timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], "-", 
        
        all_label["p_2"],  all_label["tp_2"] 
    ])

    for cpu in [2,4,8,16]:
        pork_dir = get_oyente_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu)
        cmp_res = oyente_check.compare_dir(origin_dir, pork_dir, gt)
        all_label = oyente_check.compare_label(origin_dir, pork_dir)
        full_label = oyente_check.compare_label(origin_dir, pork_dir, "full", gt)
        timeout_label = oyente_check.compare_label(origin_dir, pork_dir, "timeout", gt)
        
        write_row([
            "oyente", str(config["st"])+":"+str(config["gt"]), "park",
            full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],cmp_res["speedup"],

            timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], cmp_res["coverup"], 
            
            all_label["p_2"],  all_label["tp_2"] 
        ])
        """
        {
            "all_avg_time_1": all_time_1/all_cnt,
            "all_avg_time_2": all_time_2/all_cnt,
            "full_avg_time_1": intime_time_1/intime_cnt,
            "full_avg_time_2": intime_time_2/intime_cnt,
            "speedup": intime_time_1/intime_time_2,
            "timeout_avg_cover_1": timeout_cover_1/timeout_cnt,
            "timeout_avg_cover_2": timeout_cover_2/timeout_cnt,
            "coverup": timeout_cover_2/timeout_cover_1
        }
        """

config = {
    "st": 10,
    "gt": 4000
}
st = int(config["st"] * 1000)
gt = config["gt"]
cpu = 16


origin_dir = get_mythril_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=1)
cmp_res = mythril_check.compare_dir(origin_dir, origin_dir, gt)
all_label = mythril_check.compare_label(origin_dir, origin_dir)
full_label = mythril_check.compare_label(origin_dir, origin_dir, "full", gt)
timeout_label = mythril_check.compare_label(origin_dir, origin_dir, "timeout", gt)

write_row([
    "mythril", str(config["st"])+":"+str(config["gt"]), "origin",
    full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],"-",

    timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], "-", 
    
    all_label["p_2"],  all_label["tp_2"] 
])



pork_dir = get_mythril_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=1)
cmp_res = mythril_check.compare_dir(origin_dir, pork_dir, gt)

all_label = mythril_check.compare_label(origin_dir, pork_dir)
full_label = mythril_check.compare_label(origin_dir, pork_dir, "full", gt)
timeout_label = mythril_check.compare_label(origin_dir, pork_dir, "timeout", gt)

write_row([
    "mythril", str(config["st"])+":"+str(config["gt"]), "park",
    full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],cmp_res["speedup"],

    timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], cmp_res["coverup"], 
    
    all_label["p_2"],  all_label["tp_2"] 
])




origin_dir = get_mythril_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=2)
cmp_res = mythril_check.compare_dir(origin_dir, origin_dir, gt)
all_label = mythril_check.compare_label(origin_dir, origin_dir)
full_label = mythril_check.compare_label(origin_dir, origin_dir, "full", gt)
timeout_label = mythril_check.compare_label(origin_dir, origin_dir, "timeout", gt)

write_row([
    "mythril", str(config["st"])+":"+str(config["gt"]), "origin",
    full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],"-",

    timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], "-", 
    
    all_label["p_2"],  all_label["tp_2"] 
])



pork_dir = get_mythril_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=st, global_timeout=gt, cpu_count=cpu, tx_count=2)
cmp_res = mythril_check.compare_dir(origin_dir, pork_dir, gt)

all_label = mythril_check.compare_label(origin_dir, pork_dir)
full_label = mythril_check.compare_label(origin_dir, pork_dir, "full", gt)
timeout_label = mythril_check.compare_label(origin_dir, pork_dir, "timeout", gt)

write_row([
    "mythril", str(config["st"])+":"+str(config["gt"]), "park",
    full_label["all_cnt"], full_label["p_2"],  full_label["tp_2"], cmp_res["full_avg_time_2"],cmp_res["speedup"],

    timeout_label["all_cnt"], timeout_label["p_2"],  timeout_label["tp_2"], cmp_res["timeout_avg_cover_2"], cmp_res["coverup"], 
    
    all_label["p_2"],  all_label["tp_2"] 
])


output.close()