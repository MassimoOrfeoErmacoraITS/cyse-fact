num = 5

def fattoriale(num, sum) :
    if num > 1 :
        sum = fattoriale(num - 1, sum * num)
    return sum
        
print(fattoriale(num, 1))