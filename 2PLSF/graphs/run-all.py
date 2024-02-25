#!/usr/bin/env python2
import os

bin_folder = "bin/"
time_duration = "20"                                # 每次运行的持续时间（秒）
num_runs = "1"                                      # 运行次数。最终结果将是所有运行的中位数
thread_list = "1,4,8,12,16,24,32,40,48,56,64"    # 用于 cervino-2 的线程列表
#thread_list = "1,4,8,12,16,24,32,40,48,55"       # 使用 2plundo 的 cervino-2 的线程列表
#thread_list = "1,4,8,12,16,20,24,32,40"          # 要执行的线程列表。该列表用于 castor-1/pollux
#thread_list = "1,4,8,16,32,48,64"                # 要执行的线程列表。用于 moleson-1
#thread_list = "1,4,8,16,32,48,64,80,96"          # 要执行的线程列表。该列表适用于 AWS c5.24xlarge 或 c5d.24xlarge
ratio_list = "1000,200,0"                        # 以 permils 为单位的写入比率（100 表示 10%写入和 90%读取）
#ratio_list = "100"                            # 对于原版 TL2，使用 0% 的写入率
cmd_line_options = " --duration="+time_duration+"  --runs="+num_runs+" --threads="+thread_list+" --ratios="+ratio_list

# 我们希望在基准中包含的 STM
stm_name_list = [
    "2plsf",          # 采用分布式 RW 锁和无饥饿功能的两阶段锁
    "tiny",           # 微型 STM
    "tl2orig",        # 原版 TL2
    "tlrweager",      # TLRW 
    "oreceager",      # 带有急迫锁定功能的 Orec
    "ofwf",           # OneFile Wait-Free
    "tl2",            # TL2 
    "oreclazy",
    "2plundo",        # 使用 RW-Lock 进行两阶段锁定。仅支持 56 个线程
    "2plundodist",    # 带有分布式 RW 锁的两阶段锁
]



print "\n\n+++ Running concurrent microbenchmarks +++\n"

for stm in stm_name_list:
    os.system(bin_folder+"set-ravl-1m-"+ stm + cmd_line_options + " --keys=1000000")

for stm in stm_name_list:
    os.system(bin_folder+"set-skiplist-1m-"+ stm + cmd_line_options + " --keys=1000000")

for stm in stm_name_list:
    os.system(bin_folder+"set-ziptree-1m-"+ stm + cmd_line_options + " --keys=1000000")

#for stm in stm_name_list:
#    os.system(bin_folder+"set-tree-1m-"+ stm + cmd_line_options + " --keys=1000000")

#for stm in stm_name_list:
#    os.system(bin_folder+"set-btree-1m-"+ stm + cmd_line_options + " --keys=1000000")

for stm in stm_name_list:
    os.system(bin_folder+"set-hash-10k-"+ stm + cmd_line_options + " --keys=10000")

# 以延迟测量为基准
#os.system("rm latency.log")
#for stm in stm_name_list:
#    os.system(bin_folder+"part-disjoint-"+ stm + " --duration=20 --threads=1,4,8,16,24,32 >> latency.log")

# 以图为基准并对记录（值）进行更新的基准测试
for stm in stm_name_list:
    os.system(bin_folder+"map-ravl-"+ stm +     " --keys=100000 --duration="+time_duration+" --ratios=1000 --threads="+thread_list)
for stm in stm_name_list:
    os.system(bin_folder+"map-skiplist-"+ stm + " --keys=100000 --duration="+time_duration+" --ratios=1000 --threads="+thread_list)
for stm in stm_name_list:
    os.system(bin_folder+"map-ziptree-"+ stm +  " --keys=100000 --duration="+time_duration+" --ratios=1000 --threads="+thread_list)