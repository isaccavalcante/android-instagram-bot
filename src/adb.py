from subprocess import Popen, PIPE


def run_cmd(cmd):
	p = Popen([cmd], stdout=PIPE, shell=True)
	out, err = p.communicate()
	return out, err

def get_devices():
    out, err = run_cmd("adb devices -l")
    devices = []
    for line in out.decode().strip().split("\n")[1:]:
        device_id = line.split()[0]
        model = line.split()[4].replace("model:", "")
        devices.append({device_id:model})
    return devices
