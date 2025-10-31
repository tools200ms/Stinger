
from .sys_info import SysInfo


class About:
    @staticmethod
    def machine():
        s_info = SysInfo.machine()

        print(
         f"""Running on: {s_info['name']} ({s_info['platform']})
    {s_info['release']} {s_info['version']}
    Board ID: {s_info['id']}
""")

    @staticmethod
    def uptime():
        s = SysInfo.uptime_ms() // 1000
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)

        print("Uptime: {:d}d {:02d}h {:02d}m {:02d}s".format(d, h, m, s))

