'''
实现计算求最大公约数和最小公倍数的函数。
'''

def gcd( x , y ):
    ( x , y ) = ( y , x ) if x > y else ( x , y )
    for factor in range( x , 0 , -1 ):
        if x % factor == 0 and y % factor == 0 :
            return factor

def lcm( x , y ):
    return x * y //gcd( x , y )

def main():
    x = int(input("Enter  x :"))
    y = int(input("Enter  y :"))
    print("最大公因数是：%d " % ( gcd( x , y)))
    print("最小公倍数是：%d " % ( lcm( x , y)))
    pass

if __name__ == '__main__':
    main()

