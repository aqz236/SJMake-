import phoneHead.seven
import time
T1 = time.time()

#自定义批量生成任务
#格式为 ('省名称','运营商名称 移动/联通/电信')
province = '江苏'
Operators = '联通'
def main(province,Operators):
  phoneHead.seven.randomSeven(province,Operators)
  T2 = time.time()
  print('生成完毕！一共花费:%s秒' % ((T2 - T1)))

main(province,Operators)




# 如有循环需要可以自行开启循环
# if __name__ == '__main__':
#     while True:
#         main(province,Operators)







