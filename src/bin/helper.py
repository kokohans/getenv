import platform
import socket
import os


def get_info():
    info = {}
    suptime = os.popen('uptime').read()[:-1].split(" ")[1].split(":")

    info['hostname'] = socket.getfqdn()
    info['addr'] = socket.gethostbyname(socket.gethostname())

    try:
        info['uptime'] = f"up {suptime[0]} hours, {suptime[1]} minutes"
    except IndexError:
        info['uptime'] = f"up {suptime[0]} hours, 0 minutes"


    info['cpu'] = os.popen('cat /proc/cpuinfo  | grep -m1 "model name"').read()[:-1].split(":")[1].lstrip()
    info['platform'] = platform.uname()
    info['python-version'] = platform.python_version()

    return info