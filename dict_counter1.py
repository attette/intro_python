# 다른 food 갯수를 count하는 가능
# defaultdict()을 사용하지 않는 경우
# dict_counter라는 딕셔너리에 미등록된 food의 경우 디폴트 값을 0으로 하고
# 1씩 증가시키므로 결국엔 defaultdict()을 사용한 경우와 동일함
dict_counter = {} 
for food in ['spam', 'spam','eggs','spam']:
    if not food in dict_counter :
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)
