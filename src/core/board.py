import sys
import ujson

class Board:

    @staticmethod
    def _getClass(dev_ref):
        dev_c, dev = dev_ref.rsplit('.', 1)

        m = __import__(dev_c)
        cls = getattr(m, dev)

        return cls

    @staticmethod
    def load_config():
        sys_name = sys.platform
        devices = []

        try:
            with open(f"config_{sys_name}.json", "r") as f:
                pin_map = ujson.load(f)

            for dev_ref, arg in pin_map.items():
                if isinstance(arg, list):
                    dev_obj = Board._getClass(dev_ref)(*arg)
                elif isinstance(arg, dict):
                    dev_obj = Board._getClass(dev_ref)(**arg)
                else:
                    dev_obj = Board._getClass(dev_ref)(arg)

                devices.append(dev_obj)

            print(f"Config file loaded for {sys_name} platform")
        except OSError:
            print("Config file not found")

        return devices
