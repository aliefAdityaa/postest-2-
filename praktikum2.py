W = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]
def linearsearch(arr,x):
    for l in range(len(arr)):
        if type(arr[l]) == list:
            hasil_x = linearsearch(arr[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f'{x} ditemukan pada index {l} kolom {hasil_x}')
                exit()
        elif arr[l] == x:
            return l
    return -1
print(W)
P = input('Masukan nama yang anda inginkan: ')
hasil_y = linearsearch(W,P)
if hasil_y == -1:
    print(f'{P} ditemukan pada index {hasil_y}')
else:
    print(f'{P} ditemukan pada index {hasil_y}')