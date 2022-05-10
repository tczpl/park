import json
import os



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

    print("-----------------------")
    print(result_dir1, result_dir2)
    print("all", all_cnt, all_time_1/all_cnt, all_time_2/all_cnt)
    print("intime", intime_cnt, intime_time_1/intime_cnt, intime_time_2/intime_cnt, "speedup", intime_time_1/intime_time_2)
    print("timeout", timeout_cnt, timeout_cover_1/timeout_cnt, timeout_cover_2/timeout_cnt, "coverup", (timeout_cover_2-timeout_cover_1)/timeout_cnt)

def compare_each(run_type1, run_type2, dataset, solver_timeout_ms, global_timeout, cpu_count):
    base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
    result_dir1 = base_dir+run_type1+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"
    result_dir2 = base_dir+run_type2+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"
    compare_dir(result_dir1, result_dir2)

solver_timeout_ms = 10000
global_timeout = 3600
dataset = "smartbugs"

run_type = "origin"
cpu_count = 4
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir1 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"


run_type = "pork"
cpu_count = 16
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir2 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"

compare_dir(result_dir1, result_dir2, global_timeout)




solver_timeout_ms = 1000
global_timeout = 300
dataset = "top1k"

run_type = "origin"
cpu_count = 4
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir1 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"


run_type = "pork"
cpu_count = 16
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir2 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"

compare_dir(result_dir1, result_dir2, global_timeout)




"""
solver_timeout_ms = 10000
global_timeout = 600
dataset = "top1k"

run_type = "origin"
cpu_count = 16
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir1 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"


run_type = "pork"
cpu_count = 16
base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
result_dir2 = base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"

compare_dir(result_dir1, result_dir2, global_timeout)


"""
