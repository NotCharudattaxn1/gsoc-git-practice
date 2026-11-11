import platform
import socket


def get_os_info():
    """
    Collect basic operating system information.
    """

    information = {
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "Platform": platform.platform(),
        "Python Version": platform.python_version(),
    }

    return information
