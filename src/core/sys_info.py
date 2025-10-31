import os
import time

from machine import unique_id


class SysInfo:
    @staticmethod
    def machine():
        board = os.uname()
        sys_platform = board.sysname
        return {"name": board.machine,
                "platform": sys_platform,
                "release": board.release,
                "version": board.version,
                "id": unique_id()}


    @staticmethod
    def fs(path="/"):
        s = os.statvfs(path)
        size = s[0] * s[2]
        free = s[0] * s[3]
        return {"total": size,
                "used": size - free,
                "free": free}

    @staticmethod
    def mem():
        import gc
        gc.collect()
        return lambda: {"free": gc.mem_free(), "alloc": gc.mem_alloc()}

    @staticmethod
    def uptime_ms():
        return time.ticks_ms()
