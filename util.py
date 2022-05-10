import json
import os

def get_oyente_dir(dataset, run_type, solver_timeout_ms, global_timeout, cpu_count):
    server_dir = "oyente-cpu"+str(cpu_count)+"/"
    base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+'/'
    return server_dir + base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"

def get_mythril_dir(dataset, run_type, solver_timeout_ms, global_timeout, cpu_count, tx_count):
    server_dir = "mythril-cpu"+str(cpu_count)+"/"
    base_dir = 'result_'+dataset+'-cpu'+str(cpu_count)+"-tx"+str(tx_count)+'/'
    return server_dir + base_dir+run_type+'-t'+str(solver_timeout_ms)+'-gt'+str(global_timeout)+"/"

def get_avg_time(result_dir):
    all_time = 0
    files = os.listdir(result_dir)
    for file_name in files:
        res = json.loads(open(result_dir+file_name).read())
        all_time += res["time"]
    return all_time / len(files)

oyente_vul2cate = {
    "callstack": "denial_of_service",
    "reentrancy": "reentrancy",
    "time_dependency": "time_manipulation", 
    "integer_overflow": "arithmetic",
    "integer_underflow": "arithmetic",
    "parity_multisig_bug_2": "access_control",
    "money_concurrency": "front_running",
    "assertion_failure": "arithmetic"
}
"""
mythril,AccessControl_11,Call data forwarded with delegatecall(),AccessControl
mythril,Other_8,Dependence on predictable variable,Other
mythril,FrontRunning_1,Transaction order dependence,FrontRunning
"""
mythril_vul2cate = {
    "Jump to an arbitrary instruction":             "access_control",
    "Write to an arbitrary storage location":       "access_control",
    "Delegatecall to user-supplied address":        "access_control",
    "Dependence on tx.origin":                      "access_control",
    "Dependence on predictable environment variable":"other",
    "Unprotected Ether Withdrawal":                 "access_control",
    "Exception State":                              "other",
    "External Call To User-Supplied Address":       "reentrancy",
    "Integer Arithmetic Bugs":                      "arithmetic",
    "Multiple Calls in a Single Transaction":       None,
    "State access after external call":             "reentrancy",
    "Unprotected Selfdestruct":                     "access_control",
    "Unchecked return value from external call.":   "unchecked_low_level_calls",
}

"""
    {
        "path": "dataset/access_control/wallet_04_confused_sign.sol",
        "vulnerabilities": [
            {
                "lines": [
                    30
                ],
                "category": "access_control"
            }
        ]
    },
"""

res = json.loads(open("smartbugs_label.json").read())
path2line2cate = {}
for i in res:
    path = i["path"]
    if path not in path2line2cate:
        path2line2cate[path] = {}
    vulnerabilities = i["vulnerabilities"]
    for vul in vulnerabilities:
        cate = vul["category"]
        for line in vul["lines"]:
            if line not in path2line2cate[path]:
                path2line2cate[path][line] = {}
            if cate not in path2line2cate[path][line]:
                path2line2cate[path][line][cate] = True


"""
Oyente
{
    "vulnerabilities": {
        "callstack": [],
        "reentrancy": [],
        "assertion_failure": [],
        "time_dependency": [],
        "integer_overflow": [
            "temp/tmp22:9:2: Warning: Integer Overflow.\n contract Wallet {\n ^\nSpanning multiple lines.\nInteger Overflow occurs if:\n    bonusCodes.length = 115792089237316195423570985008687907853269984665640564039457584007878769901566"
        ],
        "parity_multisig_bug_2": [],
        "integer_underflow": [
            "temp/tmp22:28:10: Warning: Integer Underflow.\n         bonusCodes.length--\nInteger Underflow occurs if:\n    bonusCodes.length = 0"
        ],
        "money_concurrency": []
    },
    "file_path": "dataset/access_control/arbitrary_location_write_simple.sol",
    "evm_code_coverage": 0.7700831024930748,
    "time": 1.2224929332733154
}
"""

def get_oyente_detected_line2vul(res):
    line2vul = {}

    vuls = res["vulnerabilities"]
    for vul in vuls:
        if vul != "money_concurrency":
            for warning in vuls[vul]:
                line = int(warning.split(":")[1])
                if line not in line2vul:
                    line2vul[line] = {}
                line2vul[line][vul] = True
        else:
            for warnings in vuls[vul]:
                for warning in warnings:
                    line = int(warning.split(":")[1])
                    if line not in line2vul:
                        line2vul[line] = {}
                    line2vul[line][vul] = True
    
    return line2vul
        

def get_mythril_detected_line2vul(res):
    line2vul = {}

    vuls = res["issues"]
    for issue in vuls:
        vul = issue["title"]

        # TODO check lineno
        if "lineno" not in issue:
            print(vul)
            continue

        line = issue["lineno"]
        if line not in line2vul:
            line2vul[line] = {}
        line2vul[line][vul] = True
    
    return line2vul
    
def get_mythril_tp(res):
    path = res["file_path"]
    line2vul = get_mythril_detected_line2vul(res)
    line2cate = path2line2cate[path]
    tp = 0
    for line in line2vul:
        if line in line2cate:
            for detected_vul in line2vul[line]:
                detected_cate = mythril_vul2cate[detected_vul]
                if detected_cate in line2cate[line]:
                    tp+=1
    return tp

def get_oyente_tp(res):
    path = res["file_path"]
    line2vul = get_oyente_detected_line2vul(res)
    line2cate = path2line2cate[path]
    tp = 0
    for line in line2vul:
        if line in line2cate:
            for detected_vul in line2vul[line]:
                detected_cate = oyente_vul2cate[detected_vul]
                if detected_cate in line2cate[line]:
                    tp+=1
    return tp


def get_oyente_p(res):
    path = res["file_path"]
    if type(res["vulnerabilities"]["callstack"]) == list:
        line2vul = get_oyente_detected_line2vul(res)
        p = 0
        for line in line2vul:
            p += len(line2vul[line])
        return p
    else:
        p = 0
        for vul in res["vulnerabilities"]:
            if res["vulnerabilities"][vul]:
                p += 1
        return p
