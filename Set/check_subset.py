for _ in range(int(input())):
    int(input())
    A=set(input().split())
    int(input())
    B=set(input().split())
    if(len(A.difference(B))==0):
        print("True")
    else:
        print("False")

