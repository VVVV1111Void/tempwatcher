import subprocess

def get_cpu_temp(core):
    output = subprocess.check_output(['sensors', 'coretemp-isa-0000']).decode('utf-8')
    lines = output.split('\n')
    for line in lines:
        if f'Core {core}' in line:
            temp_str = line.split()[2]
            temp_value = float(temp_str[:-2])  # Remove the last two characters ('°C')
            return temp_value
        
def get_all_core_temps(count):
    """Start from 1 to n (n = core count)"""
    temps = []
    for core in range(0, count):
        temps.append(get_cpu_temp(core))
    return temps

def get_temps():
    return get_all_core_temps(4)