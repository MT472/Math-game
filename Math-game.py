import random

while True :   
    coin = random.randint(0 , 9)
    coin1 = random.randint(0,9)
    x = int(input(f"what is {coin} multiplayby {coin1} ? "))
    if x == (coin * coin1):
        print('afarin')
        break
    else :
        print('dobare')


