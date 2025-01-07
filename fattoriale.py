num = 100

def fattoriale(num, sum) :
    if num != 1 :
        sum *= num
        sum = fattoriale(num - 1, sum)
    return sum
        
print(fattoriale(num, 1))