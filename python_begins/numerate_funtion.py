markes = [23, 45, 67, 89, 98, 76, 54, 32]
# mark (i) for mark enumerate(markes) :
# index = 0
# for mark in markes:
#     if mark == 98:
#         print(f"the index of the {mark} is :", index)
#     index += 1

for index, mark in enumerate(markes):
    if mark == 98:
        print(f"the index of the {mark} is :", index)


for index, mark in enumerate(markes, start=1):
    if mark == 98:
        print(f"the index of the {mark} is :", index)
