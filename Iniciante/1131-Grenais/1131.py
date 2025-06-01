# -*- coding: utf-8 -*-
grenais = 0
v_inter = 0
v_gremio = 0
empate = 0
while True:
    inter , gremio = map(int , input().split())
    grenais += 1
    if inter > gremio:
        v_inter += 1
    elif gremio > inter:
        v_gremio += 1
    else:
        empate += 1
    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())
    if resposta == 2:
        print(f'{grenais} grenais')
        print(f'Inter:{v_inter}')
        print(f'Gremio:{v_gremio}')
        print(f'Empates:{empate}')
        if v_gremio > v_inter:
            print('Gremio venceu mais')
        elif v_inter > v_gremio:
            print('Inter venceu mais')
        else:
            print('Nao houve vencedor')
        break