#Insert sort
import random
random_list20 = list(random.sample(range(1, 51), 20))
print("生成随机数组为：",random_list20)
n = len(random_list20)
for i in range(1,n):
    key = random_list20[i] # key 指的是当前需要比较的数字，我们从数组的第二个数字开始
    j = i-1 # i和谁比较呢？当然是和前一个数字比较（也就是数组的第一个数字）
    while j>=0 and random_list20[j] > key: # 如果 key 小于前一个数字，即第二个数字小于第一个数字
        random_list20[j+1] = random_list20[j] # 考虑到j+1 = i, 其实就是第二个数字的位置给第一个数字
        j = j-1 #制造循环终止的条件
    random_list20[j+1] = key #经历了上面的 while 循环后，j=0 或者 i-1. 这一步是始终把 key 保持在最前（整列最前或者当前比较的最前）
print("经过insert sort后的数组为：",random_list20)
