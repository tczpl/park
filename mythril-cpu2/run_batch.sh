# CPU = 2
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs origin 1000 100 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs originpl 1000 100 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs pork 100 50 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 100 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 300 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs pork 10000 600 
# python3 run_dataset_type_solver_global_tx_cpu.py smartbugs pork 10000 3600 
# python3 run_dataset_type_solver_global_tx_cpu.py top1k origin 1000 100 
# python3 run_dataset_type_solver_global_tx_cpu.py top1k originpl 1000 100 
# python3 run_dataset_type_solver_global_tx_cpu.py top1k pork 100 50 
python3 run_dataset_type_solver_global_tx_cpu.py             top1k pork 1000 100 
python3 cp_dataset_type_solver_fromglobal_toglobal_tx_cpu.py top1k pork 1000 100 300
python3 run_dataset_type_solver_global_tx_cpu.py             top1k pork 1000 300 