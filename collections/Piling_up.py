for t in range(int(input())):
    l = int(input())
    lst = list(map(int, input().split()))
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print("Yes" if i == l - 1 else "No")













'''
    left=True
    valid=True

    while len(lst)!=0:
        if left:
            #print(lst)
            if lst[0]<lst[-1]:
                left='False'
            lst.popleft()
            k= lst.pop()
            if len(lst)!=0 and k<lst[0]:
                valid='False'
                break
        else:
            #print(lst)
            if l[-1]<l[0]:
                valid='False'
            lst.pop()
            k=lst.popleft()
            if len(lst)!=0 and k<l[-1]:
                valid='False'
                break
    print('No' if valid=='False' else 'Yes')
'''














    
        
    


    
