# CPU = 8
# python run_dataset_type_solver_global_tx_cpu.py smartbugs origin 1000 100
# python run_dataset_type_solver_global_tx_cpu.py smartbugs originpl 1000 100
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 100 50
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 50
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 100
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 200
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 300
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 400
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 500
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 1000 600
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 10000 600
# python run_dataset_type_solver_global_tx_cpu.py smartbugs pork 10000 3600
# python run_dataset_type_solver_global_tx_cpu.py top1k origin 1000 100
# python run_dataset_type_solver_global_tx_cpu.py top1k originpl 1000 100
# python run_dataset_type_solver_global_tx_cpu.py top1k pork 100 50
# python run_dataset_type_solver_global_tx_cpu.py top1k pork 1000 50

#python cp_dataset_type_solver_fromglobal_toglobal_tx_cpu.py top1k pork 1000 50 100

python run_dataset_type_solver_global_tx_cpu.py             top1k pork 1000 100
python cp_dataset_type_solver_fromglobal_toglobal_tx_cpu.py top1k pork 1000 100 200
python run_dataset_type_solver_global_tx_cpu.py             top1k pork 1000 200
python cp_dataset_type_solver_fromglobal_toglobal_tx_cpu.py top1k pork 1000 200 300
python run_dataset_type_solver_global_tx_cpu.py             top1k pork 1000 300
