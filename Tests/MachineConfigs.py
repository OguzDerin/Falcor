import os

machine_name = os.environ['COMPUTERNAME']
machine_name = machine_name.lower()

machine_build_script = "BuildSolution.bat"
machine_process_default_kill_time = 500.0