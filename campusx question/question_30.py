     
#     question(30). The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on
# c_pop = 10000
# ninth_y = 10000-(10 % 10000)
# print(ninth_y)
# eight = ninth_y-(10 % ninth_y)
# print(eight)
# seven = eight-(10 % eight)
# print(seven)
# six = seven-(10 % seven)
# print(six)
# five = six-(10 % six)
# print(five)
# four = five-(10 % five)
# three = four-(10 % four)
# two = three-(10 % three)
# one = two-(10 % two)
# print('ghjk',one)

#     question(30). The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years. For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on
current_population = 10000
growth_rate = 0.1
for year in range(10,0,-1):
    print(f"{year} the year - {int(current_population)}")

    factor = 1 + growth_rate
    current_population = current_population / factor



