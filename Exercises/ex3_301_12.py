data_in = [5, 6, 3, 1, 4, 2]
new_data = []
for i in range(1, len(data_in)+1):
    new_data.append(data_in.index(i)+1)

print(new_data)
