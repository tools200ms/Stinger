
from core import board

#board.Board().run()
dev = board.Board().load_config()


# h2_sensor = H2(28)
# temp_humi_sensor = TempHumi(4)
#
# try:
#     while True:
#         print(h2_sensor.read())
#         sleep(1)
# except KeyboardInterrupt:
#     print("\nMonitoring stopped")
# except Exception as e:
#     print(f"Error: {str(e)}")
# finally:
#     h2_sensor.close()

