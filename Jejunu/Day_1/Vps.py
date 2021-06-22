num = int(input())

for i in range(num):
    vps = input()
    vps_list = list(vps)
    sum = 0
    for i in vps_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')