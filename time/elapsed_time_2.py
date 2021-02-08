#時間の経過を時分で1分ごとに取得
#参考にしたサイト
#https://note.nkmk.me/python-while-usage/
#https://qiita.com/cyrus_qiita/items/9da73a6687c00ddf9a31

import time

#開始時間
start_time = time.time()


#経過時間
try:
	while True:
  		time.sleep(60)
  		end_time = time.time()


		# calculate elapsed time
  		elapsed_time = int(end_time - start_time)

		  # convert second to hour, minute and seconds
  		elapsed_hour = elapsed_time // 3600
  		elapsed_minute = (elapsed_time % 3600) // 60

		  # print as 00:00
  		print(str(elapsed_hour).zfill(2) + ":" + str(elapsed_minute).zfill(2))

except KeyboardInterrupt:
  	print('stop')
