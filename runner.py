import tdapi
import strategy

stock_list = tdapi.getScreenedList()

print(len(stock_list))
for index, stock in enumerate(stock_list):
    result = strategy.run(stock['symbol'])
    # print(index, result)
    if result['condition'] == True:
        break