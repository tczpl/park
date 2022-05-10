import matplotlib.pyplot as plt
import os
from util import *
import json

msize = 20


fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

gts = [50, 100, 200,300,400,500,600]
ps = []
states = []
for gt in gts:
    res_dir = get_mythril_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=1000, global_timeout=gt, cpu_count=8, tx_count=1)
    files = os.listdir(res_dir)
    p = 0
    state = 0
    for file in files:
        res = json.loads(open(res_dir+file).read())
        p += len(res["issues"])
        state += res["total_states"]
    ps.append(p)
    states.append(state)


ax1.plot(gts,ps, "g-", label='Detected', marker='^', markersize=msize/1.5)#label为标签
ax1.plot([],[], "b--", label='# States', marker='.', markersize=msize)#label为标签
ax2.plot(gts,states, "b--", label='# States', marker='.', markersize=msize)#label为标签

ax1.set_xlabel('Global Timeout (Second)', fontsize=20)    #设置x轴标题
ax1.set_ylabel('Detected Vulnerabilites', color='g', fontsize=20)   #设置Y1轴标题
ax2.set_ylabel('Total States', color='b', fontsize=20)  #设置Y2轴标题
ax1.set_ylim([300,450])
ax2.set_ylim([95000,110000])

location = 4
ax1.legend(loc=location, ncol=1, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列

for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
plt.yticks(fontsize=20)
#plt.xlim((0, 695000))
#plt.xticks([0, 230000, 460000, 695000])

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/rq3_impact_gt_mythril_smartbugs.pdf")

fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

gts = [50, 100, 200,300]
ps = []
states = []
for gt in gts:
    res_dir = get_mythril_dir(dataset="top1k", run_type="pork", solver_timeout_ms=1000, global_timeout=gt, cpu_count=8, tx_count=1)
    files = os.listdir(res_dir)
    p = 0
    state = 0
    for file in files:
        res = json.loads(open(res_dir+file).read())
        p += len(res["issues"])
        state += res["total_states"]
    ps.append(p)
    states.append(state)


ax1.plot(gts,ps, "g-", label='Detected', marker='^', markersize=msize/1.5)#label为标签
ax1.plot([],[], "b--", label='# States', marker='.', markersize=msize)#label为标签
ax2.plot(gts,states, "b--", label='# States', marker='.', markersize=msize)#label为标签

ax1.set_xlabel('Global Timeout (Second)', fontsize=20)    #设置x轴标题
ax1.set_ylabel('Detected Vulnerabilites', color='g', fontsize=20)   #设置Y1轴标题
# ax1.set_ylim([600,800])
ax2.set_ylabel('Total States', color='b', fontsize=20)  #设置Y2轴标题

location = 4
ax1.legend(loc=location, ncol=1, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列

for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
plt.yticks(fontsize=20)
#plt.xlim((0, 695000))
#plt.xticks([0, 230000, 460000, 695000])

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/rq3_impact_gt_mythril_top1k.pdf")



fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

gts = [50, 100, 200,300,400,500,600]
ps = []
coverages = []
for gt in gts:
    res_dir = get_oyente_dir(dataset="smartbugs", run_type="pork", solver_timeout_ms=1000, global_timeout=gt, cpu_count=8)
    files = os.listdir(res_dir)
    p = 0
    coverage = 0
    for file in files:
        res = json.loads(open(res_dir+file).read())
        p += get_oyente_p(res)
        coverage += res["evm_code_coverage"]
    ps.append(p)
    coverages.append(coverage/len(files))


ax1.plot(gts,ps, "g-", label='Detected', marker='^', markersize=msize/1.5)#label为标签
ax1.plot([0],[0], "b--", label='Coverage', marker='.', markersize=msize)#label为标签
ax2.plot(gts,coverages, "b--", label='Coverage', marker='.', markersize=msize)#label为标签

ax1.set_xlabel('Global Timeout (Second)', fontsize=20)    #设置x轴标题
ax1.set_ylabel('Detected Vulnerabilites', color='g', fontsize=20)   #设置Y1轴标题
ax1.set_ylim([600,800])
ax2.set_ylim([0.932,0.94])
ax2.set_ylabel('Average Coverage', color='b', fontsize=20)  #设置Y2轴标题

location = 4
ax1.legend(loc=location, ncol=1, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列

for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
plt.yticks(fontsize=20)
#plt.xlim((0, 695000))
#plt.xticks([0, 230000, 460000, 695000])

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/rq3_impact_gt_oyente_smartbugs.pdf")



fig,ax1 = plt.subplots()
ax2 = ax1.twinx()

gts = [50, 100, 200,300]
ps = []
coverages = []
for gt in gts:
    res_dir = get_oyente_dir(dataset="top1k", run_type="pork", solver_timeout_ms=1000, global_timeout=gt, cpu_count=8)
    files = os.listdir(res_dir)
    p = 0
    coverage = 0
    for file in files:
        res = json.loads(open(res_dir+file).read())
        p += get_oyente_p(res)
        coverage += res["evm_code_coverage"]
    ps.append(p)
    coverages.append(coverage/len(files))


ax1.plot(gts,ps, "g-", label='Detected', marker='^', markersize=msize/1.5)#label为标签
ax1.plot([0],[0], "b--", label='Coverage', marker='.', markersize=msize)#label为标签
ax2.plot(gts,coverages, "b--", label='Coverage', marker='.', markersize=msize)#label为标签


ax1.set_xlabel('Global Timeout (Second)', fontsize=20)    #设置x轴标题
ax1.set_ylabel('Detected Vulnerabilites', color='g', fontsize=20)   #设置Y1轴标题
ax1.set_ylim([150,200])
ax2.set_ylabel('Average Coverage', color='b', fontsize=20)  #设置Y2轴标题

location = 4
ax1.legend(loc=location, ncol=1, fontsize=20)#图例及位置： 1右上角，2 左上角 loc函数可不写 0为最优 ncol为标签有几列

for tick in ax1.xaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
for tick in ax1.yaxis.get_major_ticks():
    tick.label.set_fontsize(20) 
plt.yticks(fontsize=20)

#plt.xlim((0, 695000))
#plt.xticks([0, 230000, 460000, 695000])

plt.grid(True, color='#666666', linestyle = ":", linewidth = "2")

plt.tight_layout()
plt.savefig("fig/rq3_impact_gt_oyente_top1k.pdf")
