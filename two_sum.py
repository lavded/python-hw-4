# Дано масив цілих чисел nums і ціле число, 
# поверніть індекси двох чисел так, щоб їх сума дала передане ціле число.

# Ви можете припустити, що кожен вхід матиме рівно одне рішення, 
# і ви не можете використовувати той самий елемент двічі.

# Ви можете повернути відповідь у будь-якому порядку.


def twoSum(nums, target):
    arr_nums=nums.copy()
    rez=target
    index=[]
    for i in range(len(arr_nums)):
        for j in range(i+1, len(arr_nums)):
            if (rez-arr_nums[i])!=arr_nums[j]:
                continue
            else:
                index.append(i)
                index.append(j)
    return(index)
try:
    nums_inp=list(map(int, input("Enter numbers separated by commas/ ").split(',')))
    sum_inp=int(input("Enter sum "))
    print('Array index of terms',twoSum(nums_inp,sum_inp))
except ValueError:print('Type only numbers')

twoSum([1, 2, 3], 4)        # [0, 2]
twoSum([2, 7, 11, 15], 9)   # [0, 1]
twoSum([3, 2, 4], 6)        # [1, 2]
twoSum([3, 3], 6)           # [0, 1]