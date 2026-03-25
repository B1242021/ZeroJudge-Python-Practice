r ={0:'BNZ',1:'AMW',2:'KLY',3:'JVX',4:'HU',5:'GT',6:'FS',7:'ER',8:'DOQ',9:'CIP'}
while True:
    try:
        total =0
        x = str(input())
        for i in range(0,8):
            total += int(x[i])*(8-i)
        print(r[(10-int(x[8])-(total%10))%10])
    except EOFError:
        break
