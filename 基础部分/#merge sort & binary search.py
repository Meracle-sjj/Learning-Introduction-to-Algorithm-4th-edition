#merge sort
def merge(inputList,start,middle,end):
    n_L = middle - start + 1
    n_R = end - middle
    L = [0] * n_L
    R = [0] * n_R
    for i in range(n_L):
        L[i] = inputList[start+i]
    for j in range(n_R):
        R[j] = inputList[middle+1+j]
    i = 0
    j = 0 
    key = start
    while i < n_L and j < n_R:
        if L[i] <= R[j]:
            inputList[key] = L[i]
            i += 1
        else:
            inputList[key] = R[j]
            j += 1
        key += 1
    while i < n_L:
        inputList[key] = L[i]
        i += 1
        key += 1
    while j < n_R:
        inputList[key] = R[j]
        j += 1
        key += 1
# def merge_sort(inputList,start,end):
#     if start >= end:
#         return
#     middle = (start + end)//2
#     merge_sort(inputList,start,middle)
#     merge_sort(inputList,middle+1,end)
#     merge(inputList,start,middle,end)
# import random
# random_list20 = list(random.sample(range(1, 51), 20))
# print("原数列为：",random_list20)
# merge_sort(random_list20,0,len(random_list20)-1)
# print("sort_merge后的数列为:",random_list20)

def binary_search(inputList, target, start, end):
    if start > end:
        return -1  # 表示未找到目标值
    middle = (start + end) // 2
    if inputList[middle] == target:
        return middle  # 返回目标值的位置
    elif inputList[middle] > target:
        # 目标值在左半部分
        return binary_search(inputList, target, start, middle - 1)
    else:
        # 目标值在右半部分
        return binary_search(inputList, target, middle + 1, end)

# 测试代码
import random
random_list20 = sorted(random.sample(range(1, 51), 20))  # 生成随机数列并排序
print("排序后的数列为：", random_list20)

target = int(input("请输入要查找的目标值："))
result = binary_search(random_list20, target, 0, len(random_list20) - 1)

if result != -1:
    print(f"目标值 {target} 在数列中的索引为：{result}")
else:
    print(f"目标值 {target} 不在数列中。")
