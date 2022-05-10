import matplotlib.pyplot as plt
import os
from util import *
import json
import oyente_check
import mythril_check


gt = 600

origin_dir = "temp_evaluate_smartbugs/originsr-t1000-gt600/"
pork_dir = "temp_evaluate_smartbugs/pork-t1500-gt600/"

cmp_res = mythril_check.compare_dir(origin_dir, pork_dir, gt)
all_label = mythril_check.compare_label(origin_dir, pork_dir)
full_label = mythril_check.compare_label(origin_dir, pork_dir, "full", gt)
timeout_label = mythril_check.compare_label(origin_dir, pork_dir, "timeout", gt)

print(cmp_res)
print(all_label)
print(full_label)
print(timeout_label)
#print(cmp_res, all_label, full_label, timeout_label)