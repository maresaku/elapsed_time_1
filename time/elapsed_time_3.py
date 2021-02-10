#1分ごとの時間の差分その2
#今回はほぼ自作

from datetime import datetime
import pytz
import time

Tokyo=pytz.timezone("Asia/Tokyo")
start_time = datetime.now(Tokyo)

try:
	while True:
		time.sleep(60)
		end_time = datetime.now(Tokyo)
		elapsed_time = int(end_time.strftime("%H%M"))-int(start_time.strftime("%H%M"))
		print(str(elapsed_time).zfill(4))
except KeyboardInterrupt:
  print('stop')
