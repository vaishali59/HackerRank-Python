string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w=4

print('\n'.join([string[i:i+w] for i in range(0,len(string),w)]))

