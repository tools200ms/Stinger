from time import sleep

from sensors import H2, TempHumi

h2_sensor = H2(28)
# temp_humi_sensor = TempHumi()

try:
    while True:
        print(h2_sensor.read())
        sleep(1)
except KeyboardInterrupt:
    print("\nMonitoring stopped")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    h2_sensor.close()

