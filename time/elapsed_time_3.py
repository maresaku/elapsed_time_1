#1分ごとの時間の差分その2
#今回はほぼ自作

from datetime import datetime
import pytz
import time

#タイムゾーンの設定
Tokyo=pytz.timezone("Asia/Tokyo")

#開始時間の取得
start_time = datetime.now(Tokyo)

#Ctrl+Cが押されるまで繰り返し
try:
	while True:
		#スリープ60秒
		time.sleep(60)
		#終了時間の取得
		end_time = datetime.now(Tokyo)
		#経過時間終了時間-開始時間 strtimeでHHMM表記に文字列変換 → 数値として引き算 → 文字列として4桁####表記
		elapsed_time = str(int(end_time.strftime("%H%M"))-int(start_time.strftime("%H%M"))).zfill(4)
		#4桁####表記を2文字ずつにして間に':'を入れて、HH:MM表記で出力
		print(elapsed_time[:2]+str(':')+elapsed_time[2:])
except KeyboardInterrupt:
  print('stop')
