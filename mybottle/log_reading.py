from sensors import temperature_pressure_humidity
import subprocess

data =  temperature_pressure_humidity.read()
print(data)
subprocess.call('./mvlog_to_copy_of_log.sh')
with open("current_reading", "w") as outfile:
    outfile.write(str(data) + "\n")
subprocess.call('./log.sh')    

