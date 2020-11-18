#! /usr/bin/python3

import subprocess

print(subprocess.check_output('date').decode('ascii').strip())


print(subprocess.check_output('vcgencmd','measure_temp').decode('ascii').strip())
