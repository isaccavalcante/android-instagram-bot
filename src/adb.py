from subprocess import call, Popen, PIPE
import platform
import os

system = platform.system()
adb_path = os.getcwd()
if system == "Linux":
    adb_path += "/platform-tools/adb_Linux"
elif system == "Windows":
    adb_path += "\\platform-tools\\adb.exe"

def run_cmd(cmd):
    p = Popen([cmd], stdout=PIPE)
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


def get_device_model(output):
    try:
        model = output.split()[7].replace("model:", "")
        device = output.split()[8].replace("device:", "")
        return f"{device} {model} ✅"
    except Exception as e:
        return "Dispositivo não conectado ❌"

def get_devices_v2():
    p =  Popen([adb_path, "devices", "-l"], stdout=PIPE)
    out, err = p.communicate()
    output =  out.decode().strip()
    return get_device_model(output)

def restart_adb():
    p =  Popen([adb_path, "kill-server"], stdout=PIPE)
    p.communicate()
    p =  Popen([adb_path, "start-server"], stdout=PIPE)
    p.communicate()

restart_adb()