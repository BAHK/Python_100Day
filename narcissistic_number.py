def narcissistic_number_1(num):
    length = len(str(num))
    count = length    
    num_sum = 0    
    while count:        
        num_sum += ((num // 10 ** (count - 1)) % 10) ** length     
        count -= 1    
    else:       
        if num_sum == num:            
            print("%d is %d bit narcissistic_number" % (num, length))
        else:                        
            print("%d is not a narcissistic_number" % num)


def narcissistic_number_2(num): 
    original_num = num 
    s = str(original_num)    
    length = len(s)    
    count = length    
    sum_num = 0    
    while count:        
        sum_num += int(s[count - 1]) ** length        
        count -= 1    
    else:       
        if sum_num == num:           
            print("%d is a %d bit narcissistic_number" % (num, length))
        else:            
            print("%d is not a narcissistic_number" % num)

def narcissistic_number_3(num):
    original_num = num 
    s = str(original_num)    
    length = len(s)    
    i = num // 100
    j = ( num // 10 ) % 10
    k = num % 10
    num_sum = 0
    if num == i ** 3 + j ** 3 + k ** 3:
        print("%d is a %d bit narcissistic_number" % (num, length))
    else:            
        print("%d is not a narcissistic_number" % num)

max_num = int(input('请输入最大范围'))
# 获取小于指定数的阿姆斯特朗数
for num in range(0, max_num):
    narcissistic_number_1(num)        #调用方法一,方法二均可



