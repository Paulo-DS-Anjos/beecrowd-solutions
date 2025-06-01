while True:
    n1 = float(input())
    if 0 <= n1 <=10:
        while True:
            n2 = float(input())
            if 0 <= n2<= 10:
                media = (n1 + n2)/2
                print(f'media = {media:.2f}')
                break
            else:
                print('nota invalida')
        break
    else:
        print('nota invalida')