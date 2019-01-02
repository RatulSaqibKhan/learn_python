def arithmatic_mean(list):
    length_of_list = len(list)
    summation = sum(list)
    return summation / length_of_list

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
mean = arithmatic_mean(x)
print('Mean of', x,'is',mean)