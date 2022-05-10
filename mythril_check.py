import json
import os
from util import *

def compare_dir_1by1(result_dir1, result_dir2, global_timeout, verbose=False):
    print(result_dir1, result_dir2)
    
    speedups = []

    files = os.listdir(result_dir1)

    for file_name in files:
        try:
            res = json.loads(open(result_dir1+file_name).read())
            type1_time = res["time"]
            type1_states = res["total_states"]
            res = json.loads(open(result_dir2+file_name).read())
            type2_time = res["time"]
            type2_states = res["total_states"]
        except:
            continue


        if type1_time < global_timeout:
            speedups.append(type1_time/type2_time)
            print(type1_time, type2_time, type1_time/type2_time)

    return speedups


def compare_dir(result_dir1, result_dir2, global_timeout, verbose=False):
    print(result_dir1, result_dir2)
    all_cnt = 0
    all_time_1 = 0
    all_time_2 = 0
    all_states_1 = 0
    all_states_2 = 0

    intime_cnt = 0
    intime_time_1 = 0
    intime_time_2 = 0

    timeout_cnt = 0
    timeout_states_1 = 0
    timeout_states_2 = 0

    files = os.listdir(result_dir1)

    for file_name in files:
        try:
            res = json.loads(open(result_dir1+file_name).read())
            type1_time = res["time"]
            type1_states = res["total_states"]
            res = json.loads(open(result_dir2+file_name).read())
            type2_time = res["time"]
            type2_states = res["total_states"]
        except:
            continue

        all_cnt += 1
        all_time_1 += type1_time
        all_time_2 += type2_time
        all_states_1 += type1_states
        all_states_2 += type2_states

        if type1_time < global_timeout:
            intime_cnt += 1
            intime_time_1 += type1_time
            intime_time_2 += type2_time
        else:
            timeout_cnt += 1
            timeout_states_1 += type1_states
            timeout_states_2 += type2_states
        
        if verbose:
            print(file_name, type1_time, type2_time)

    print("-----------------------", all_cnt)
    print(result_dir1, result_dir2)
    print("all", all_cnt, all_time_1/all_cnt, all_time_2/all_cnt, all_states_1/all_cnt, all_states_2/all_cnt)
    print("intime", intime_cnt, intime_time_1/intime_cnt, intime_time_2/intime_cnt, "speedup", intime_time_1/intime_time_2)
    print("timeout", timeout_cnt, timeout_states_1/timeout_cnt, timeout_states_2/timeout_cnt, "statesup", timeout_states_2/timeout_states_1)

    return {
        "all_avg_time_1": all_time_1/all_cnt,
        "all_avg_time_2": all_time_2/all_cnt,
        
        "full_cnt": intime_cnt,
        "full_avg_time_1": intime_time_1/intime_cnt,
        "full_avg_time_2": intime_time_2/intime_cnt,
        "speedup": intime_time_1/intime_time_2,

        "timeout_cnt": timeout_cnt,
        "timeout_avg_cover_1": timeout_states_1/timeout_cnt,
        "timeout_avg_cover_2": timeout_states_2/timeout_cnt,
        "coverup": timeout_states_2/timeout_states_1,
    }

def get_p_tp(result_dir):
    all_cnt = 0
    tp = 0
    p = 0
    files = os.listdir(result_dir)

    for file_name in files:
        try:
            res = json.loads(open(result_dir+file_name).read())
        except:
            continue

        tp += get_mythril_tp(res)
        p += len(res["issues"])
    
    return p, tp

def get_p(result_dir):
    all_cnt = 0
    p = 0
    files = os.listdir(result_dir)

    for file_name in files:
        try:
            res = json.loads(open(result_dir+file_name).read())
        except:
            continue

        p += len(res["issues"])
    
    return p


def compare_label(result_dir1, result_dir2, type="all", timeout=0):
    all_cnt = 0
    tp_1 = 0
    tp_2 = 0
    p_1 = 0
    p_2 = 0

    files = os.listdir(result_dir1)

    for file_name in files:
        try:
            res1 = json.loads(open(result_dir1+file_name).read())
            res2 = json.loads(open(result_dir2+file_name).read())
        except:
            continue

        if type=="all":
            tp_1 += get_mythril_tp(res1)
            p_1 += len(res1["issues"])
            tp_2 += get_mythril_tp(res2)
            p_2 += len(res2["issues"])
            all_cnt += 1
        elif type=="full":
            if res1["time"] <= timeout:
                tp_1 += get_mythril_tp(res1)
                p_1 += len(res1["issues"])
                tp_2 += get_mythril_tp(res2)
                p_2 += len(res2["issues"])
                all_cnt += 1
        elif type=="timeout":
            if res1["time"] > timeout:
                tp_1 += get_mythril_tp(res1)
                p_1 += len(res1["issues"])
                tp_2 += get_mythril_tp(res2)
                p_2 += len(res2["issues"])
                all_cnt += 1

    return {
        "all_cnt": all_cnt,
        "p_1": p_1,
        "p_2": p_2,
        "tp_1": tp_1,
        "tp_2": tp_2,
    }



def compare_detected(result_dir1, result_dir2, type="all", timeout=0):
    all_cnt = 0
    p_1 = 0
    p_2 = 0

    files = os.listdir(result_dir1)

    for file_name in files:
        try:
            res1 = json.loads(open(result_dir1+file_name).read())
            res2 = json.loads(open(result_dir2+file_name).read())
        except:
            continue

        if type=="all":
            p_1 += len(res1["issues"])
            p_2 += len(res2["issues"])
            all_cnt += 1
        elif type=="full":
            if res1["time"] <= timeout:
                p_1 += len(res1["issues"])
                p_2 += len(res2["issues"])
                all_cnt += 1
        elif type=="timeout":
            if res1["time"] > timeout:
                p_1 += len(res1["issues"])
                p_2 += len(res2["issues"])
                all_cnt += 1

    return {
        "all_cnt": all_cnt,
        "p_1": p_1,
        "p_2": p_2
    }


def compare_each(run_type1, run_type2, dataset, solver_timeout_ms, global_timeout, cpu_count):
    base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
    result_dir1 = base_dir+run_type1+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"
    result_dir2 = base_dir+run_type2+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"
    compare_dir(result_dir1, result_dir2)

"""
result_dir1 = get_mythril_dir(dataset="top1k", run_type="origin", solver_timeout_ms=1000, global_timeout=1200, cpu_count=16, tx_count=2)
result_dir2 = get_mythril_dir(dataset="top1k", run_type="pork", solver_timeout_ms=1000, global_timeout=1200, cpu_count=16, tx_count=2)
compare_dir(result_dir1, result_dir2, global_timeout=1200)



result_dir1 = get_mythril_dir(dataset="top1k", run_type="origin", solver_timeout_ms=1000, global_timeout=3600, cpu_count=16, tx_count=2)
result_dir2 = get_mythril_dir(dataset="top1k", run_type="pork", solver_timeout_ms=1000, global_timeout=3600, cpu_count=16, tx_count=2)
compare_dir(result_dir1, result_dir2, global_timeout=3600)
# compare_label(result_dir1, result_dir2)
"""