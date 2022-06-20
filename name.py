names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
name_list = names.split(",")

cnt_k = 0
cnt_l = 0

for name in name_list:
    if name[0] == "김":
        cnt_k += 1
    if name[0] == "이":
        cnt_l += 1

name_set = set(name_list)



for name in sorted(name_set):
    print(name)
