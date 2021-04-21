import phoneHead.seven
import time
T1 = time.time()

#自定义批量生成任务
#格式为 ('省名称','运营商名称 移动/联通/电信')
# 如phoneHead.seven.randomSeven('北京','电信')
phoneHead.seven.randomSeven('广西','联通')
T2 = time.time()
print('生成完毕！一共花费:%s秒' % ((T2 - T1)))







