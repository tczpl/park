import json
import os
from util import *

def compare_dir(result_dir1, result_dir2, global_timeout, verbose=False):
    all_cnt = 0
    all_time_1 = 0
    all_time_2 = 0
    all_cover_1 = 0
    all_cover_2 = 0

    intime_cnt = 0
    intime_time_1 = 0
    intime_time_2 = 0

    timeout_cnt = 0
    timeout_cover_1 = 0
    timeout_cover_2 = 0

    files = os.listdir(result_dir1)

    for file_name in files:
        try:
            res = json.loads(open(result_dir1+file_name).read())
            type1_time = res["time"]
            type1_cover = res["evm_code_coverage"]
            res = json.loads(open(result_dir2+file_name).read())
            type2_time = res["time"]
            type2_cover = res["evm_code_coverage"]
        except:
            continue

        all_cnt += 1
        all_time_1 += type1_time
        all_time_2 += type2_time
        all_cover_1 += type1_cover
        all_cover_2 += type2_cover

        if type1_time < global_timeout:
            intime_cnt += 1
            intime_time_1 += type1_time
            intime_time_2 += type2_time
        else:
            timeout_cnt += 1
            timeout_cover_1 += type1_cover
            timeout_cover_2 += type2_cover
        
        if verbose:
            print(file_name, type1_time, type2_time)

    """
    print("-----------------------")
    print(result_dir1, result_dir2)
    print("all", all_cnt, all_time_1/all_cnt, all_time_2/all_cnt, all_cover_1/all_cnt, all_cover_2/all_cnt)
    print("intime", intime_cnt, intime_time_1/intime_cnt, intime_time_2/intime_cnt, "speedup", intime_time_1/intime_time_2)
    print("timeout", timeout_cnt, timeout_cover_1/timeout_cnt, timeout_cover_2/timeout_cnt, "coverup", timeout_cover_2/timeout_cover_1)
    """

    return {
        "all_avg_time_1": all_time_1/all_cnt,
        "all_avg_time_2": all_time_2/all_cnt,
        
        "full_cnt": intime_cnt,
        "full_avg_time_1": intime_time_1/intime_cnt,
        "full_avg_time_2": intime_time_2/intime_cnt,
        "speedup": intime_time_1/intime_time_2,

        "timeout_cnt": timeout_cnt,
        "timeout_avg_cover_1": timeout_cover_1/timeout_cnt,
        "timeout_avg_cover_2": timeout_cover_2/timeout_cnt,
        "coverup": timeout_cover_2/timeout_cover_1,
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

        tp += get_oyente_tp(res)
        p += get_oyente_p(res)
    
    return p, tp


def get_p(result_dir):
    all_cnt = 0
    p = 0
    files = os.listdir(result_dir)

    for file_name in files:
        try:
            # print(result_dir+file_name)
            res = json.loads(open(result_dir+file_name).read())
        except:
            continue

        p += get_oyente_p(res)
    
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
            all_cnt += 1
            tp_1 += get_oyente_tp(res1)
            p_1 += get_oyente_p(res1)
            tp_2 += get_oyente_tp(res2)
            p_2 += get_oyente_p(res2)
        elif type=="full":
            if res1["time"] <= timeout:
                all_cnt += 1
                tp_1 += get_oyente_tp(res1)
                p_1 += get_oyente_p(res1)
                tp_2 += get_oyente_tp(res2)
                p_2 += get_oyente_p(res2)
        elif type=="timeout":
            if res1["time"] > timeout:
                all_cnt += 1
                tp_1 += get_oyente_tp(res1)
                p_1 += get_oyente_p(res1)
                tp_2 += get_oyente_tp(res2)
                p_2 += get_oyente_p(res2)

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
            all_cnt += 1
            p_1 += get_oyente_p(res1)
            p_2 += get_oyente_p(res2)
        elif type=="full":
            if res1["time"] <= timeout:
                all_cnt += 1
                p_1 += get_oyente_p(res1)
                p_2 += get_oyente_p(res2)
        elif type=="timeout":
            if res1["time"] > timeout:
                all_cnt += 1
                p_1 += get_oyente_p(res1)
                p_2 += get_oyente_p(res2)

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
result_dir1 = get_oyente_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=10000, global_timeout=3600, cpu_count=4)
result_dir2 = get_oyente_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=10000, global_timeout=3600, cpu_count=16)
compare_dir(result_dir1, result_dir2, global_timeout=3600)
compare_label(result_dir1, result_dir2)

result_dir1 = get_oyente_dir(dataset="top1k", run_type="origin", solver_timeout_ms=1000, global_timeout=300, cpu_count=4)
result_dir2 = get_oyente_dir(dataset="top1k", run_type="pork", solver_timeout_ms=1000, global_timeout=300, cpu_count=16)
compare_dir(result_dir1, result_dir2, global_timeout=300)



result_dir1 = get_oyente_dir(dataset="smartbugs", run_type="origin", solver_timeout_ms=1000, global_timeout=100, cpu_count=4)
result_dir2 = get_oyente_dir(dataset="smartbugs", run_type="originpl", solver_timeout_ms=1000, global_timeout=100, cpu_count=4)
compare_dir(result_dir1, result_dir2, global_timeout=100)


result_dir1 = get_oyente_dir(dataset="top1k", run_type="origin", solver_timeout_ms=1000, global_timeout=100, cpu_count=4)
result_dir2 = get_oyente_dir(dataset="top1k", run_type="originpl", solver_timeout_ms=1000, global_timeout=100, cpu_count=4)
compare_dir(result_dir1, result_dir2, global_timeout=100)

result_dir1 = get_oyente_dir(dataset="smartbugs", run_type="originpl", solver_timeout_ms=1000, global_timeout=100, cpu_count=4)
result_dir2 = get_oyente_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=1000, global_timeout=100, cpu_count=16)
compare_dir(result_dir1, result_dir2, global_timeout=100)
compare_label(result_dir1, result_dir2)

"""