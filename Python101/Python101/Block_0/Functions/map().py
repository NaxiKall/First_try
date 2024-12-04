# old_list = ['1', '2', '3', '4', '5', '6', '7']
#
# new_list = list(map(int,old_list))
# print(new_list)


# expenses = [[2356, 4537, 8678], [7395, 1298, 6500, 4791],[6341, 3408], [1105, 8374, 5914], [1024, 7333], [3500, 2008, 9375, 6144]]
#
# expenses_sum = list(map(sum,expenses))
# print(expenses_sum)

#
# prices = {'яблоко': 99, 'апельсин': 99, 'вишня': 147, 'персик': 145, 'грейпфрут': 139}
# ## new_prices = {'яблоко': 94.05, 'апельсин': 94.05, 'вишня': 139.65, 'персик': 137.75, 'грейпфрут': 132.05}
# prices_tuple =list(prices.items())
#
# def sale(prices_tup):
#     name,price = prices_tup
#     price *= 0.95
#     return (name,round(price,2))
#
# new_prices = (dict(map(sale,prices.items())))

# docs = [
# '//doc/5041434?query=data%20science',
# '//doc/5041567?query=data%20science',
# '//doc/4283670?query=data%20science',
# '//doc/3712659?query=data%20science',
# '//doc/4997267?query=data%20science',
# '//doc/4372673?query=data%20science',
# '//doc/3779060?query=data%20science',
# '//doc/3495410?query=data%20science',
# '//doc/4308832?query=data%20science',
# '//doc/4079881?query=data%20science'
# ]
#
# links = list(map(lambda link:"https://www.kommersant.ru" + link, docs ))
#

#
data = [(0.00632, 6.575, 65.2, 296.0, 4.98),
(0.02731, 6.421, 78.9, 242.0, 9.14),
(0.02729, 7.185, 61.1, 242.0, 4.03),
(0.03237, 6.998, 45.8, 222.0, 2.94),
(0.06905, 7.147, 54.2, 222.0, 5.33),
(0.02985, 6.43, 58.7, 222.0, 5.21),
(0.08829, 6.012, 66.6, 311.0, 12.43)]


updated_data_func = (lambda x:( *x,round(x[0] * x[3] * x[4],2 )))
updated_data = list(map(updated_data_func,data))
print(updated_data)