# food 갯수를 count하는 가능

from collections import defaultdict
food_counter = defaultdict(int)
#print(food_counter) : food_counter는 class임
for food in ['spam', 'spam','eggs','spam']:
    print(food)
    # food_counter['spam']의 최초 값은 디폴트 값인 0 이됨
    print(food_counter[food])
    food_counter[food] += 1
    print(food_counter[food])
    # food_counter['spam']는 1 증가한 1의 값을 갖고
    # 다시 for loop을 돌때 'spam'에 대해서는 이전 값을 기억을 하고 1씩 증가됨
    # 'eggs'는 다른 food이므로 디폴트값 0부터 시작 후 1이 증가되게 됨

# dictionary를 만드는 for loop
for food, count in food_counter.items():
    print(food, count)
