from subprocess import Popen, PIPE
import platform
import os

def run_cmd(cmd):
    p = Popen([cmd], stdout=PIPE, shell=True)
    out, err = p.communicate()
    return out, err

def get_devices():
    adb_path = os.getcwd() + f"platform-tools/adb_{platform.system()}"
    out, err = run_cmd(f"{adb_path} devices -l")
    devices = []
    for line in out.decode().strip().split("\n"):
        if "model" not in line:
            continue
        device_id = line.split()[0]
        model = line.split()[4].replace("model:", "")
        devices.append({device_id:model})
    return devices
