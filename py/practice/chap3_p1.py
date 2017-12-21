def collaze(number):
    if(number%2):
        return 3*number+1
    else:
        return number//2


for ii in range(8):
    print('Enter number:', end=' ')
    print(collaze(int(input())))

