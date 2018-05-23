# -*- coding: utf-8 -*-
import time
#time.sleep(5)


path_down = ['rn','niv','advi','vrli','vid','sual','rajp','vbw','nan','kkw','sndd','kudl','zarp','swv','End']
#path_up = []

path_down_time = [0,15,14,10,17,11,9,15,19,19,17,13,17,19,0]
#path_down_time = [0,1,1,1,1,1,2,2,1,1,1,2,1,2,0]

A10103 = ['rn','R']


def train_move_down(train_postion,next_signal):
    stn = path_down.index(train_postion)
    next_stn = stn + 1
    next_signal = raw_input("What is Signal(R or G):")        
    if next_signal == 'R':
        return([path_down[stn],'R'])
    print('Wait:'+str(path_down_time[next_stn]))
    time.sleep(path_down_time[next_stn])
    return ([path_down[next_stn],next_signal])
while A10103!='End':
    A10103 = train_move_down(A10103[0],A10103[1])
    print(A10103)

    