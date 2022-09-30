import os
lv = 1
start_num = 30
finish_num = 50

# 한번에 여러 문제 파일 만들기
def many_touch_file(lv, start_num, finish_num):
    for i in range(start_num, finish_num + 1):
        f = open(f'./programmers/Lv.0{lv}/Lv.0{lv}_{i}.py', 'w')
        f.close()
        
# many_touch_file(lv, start_num, finish_num)

# 다음 문제 파일 만들기
def touch_file(lv):
    path_lv = f'./programmers/Lv.0{lv}'
    file_lst = os.listdir(path_lv)
    file_lst.sort()
    last_file_num = int(file_lst[-1].split('.')[-2].split('_')[-1])
    
    if not os.stat(f'{path_lv}/{file_lst[-1]}').st_size:
        return None

    f = open(f'./programmers/Lv.0{lv}/Lv.0{lv}_{last_file_num + 1}.py', 'w')
    f.close()
    
touch_file(lv)