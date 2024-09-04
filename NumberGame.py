# many = input("金額を入力してください")
# print(many)
# print((int(many) * 0.1) + int(many))

# banana = ""
# while banana != "banana":
#     banana = input("入力してください:")

import random

print("数当てゲーム開始")
print("10から99の数を当ててください")

# get a random number from 10 to 99
get_number = random.randint(10, 99)

# a function that continue util result is correct
result = True

# add cnt
cnt = 1

#judgmnt started
while(result):
    receive = int(input("いくつかな？:"))


    #the value entered by the user is incorrect
    if receive != get_number:

        # get_number is greater than receive
        if receive < get_number:
            print("もっと大きな数だよ")
        else:
            print("もっと小さな数だよ")
        cnt += 1
    else:

        result = False

print(f"{cnt} 回目で正解しました")