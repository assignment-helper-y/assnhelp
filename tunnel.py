file_name = input('Enter file name')
try:
    with open(file_name) as f:
        data = f.readlines()
        f.close()
except FileNotFoundError:
    raise FileNotFoundError

try:
    if len(data)>2:
        raise Exception('More than 2 lines are present in the file')
    data[0] = list(map(int,list(map(str.strip,data[0].split(' ')))))
    data[1] = list(map(int,list(map(str.strip,data[1].split(' ')))))
    if len(data[0]) != len(data[1]):
        raise Exception('Floor and ceiling dont have equal tiles')
    for check_grtr in range(len(data[0])):
        if data[0][check_grtr]<data[1][check_grtr]:
            raise Exception('Floor is above the ceiling')
    data[:] = data[::-1]
    data = list(zip(*data))
except Exception as e:
    print(e)
#data is in 2d list format
#[[min1,max1],
# [min2,max2]]

beggmax = 1
maxval = 1
#maximum value of gap between walls
#1 is min, when there is wall in front

#key is the array number of the input data
for currpos in range(len(data)):
    #currpos is the array number on which the code
    #is checking the inner visibility
    
    #val is used to check the visibility
    #of each value in that range of min to max
    for val in range(data[currpos][0]+1,data[currpos][1]+1):
        #It is used to know if that value val is above current maximum or not
        #if it is not then the loop will be break
        is_above_min = True
        for check_data in data[currpos+1:currpos+maxval+1]:
            
            if not(check_data[0] < val <= check_data[1]):
                is_above_min = False
                break
        if not(is_above_min):
            continue
        for checkers_val in range(currpos+maxval+1,len(data)):
            if not(data[checkers_val][0] < val <= data[checkers_val][1]):
                maxval = checkers_val-currpos if checkers_val-currpos > maxval else maxval
                if currpos == 0:
                    beggmax = maxval
                break
print('the distance over which one can see into the tunnel when looking outside the tunnel from the West:')
print(beggmax)
print()
print('the maximum distance over which one can see into the tunnel when being inside the tunnel.')
print(maxval)
