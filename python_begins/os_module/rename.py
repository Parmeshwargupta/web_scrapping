import os
# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(1, 101):
#     os.mkdir(f"data/Day{i}")
for i in range(1, 101):
    os.rename(f"data/Day{i}", f"data/Tutorial{i}")
