import pandas as pd
import numpy as np

stock_data = np.array(pd.read_csv('data/S&P500_CSV.csv'))[:, 1]

def Mean_Reversion_Strategy(data):
    current_t = 51

    holding_position = False
    current_holding_price = None

    window_period = 10
    historical_prices = data[0:current_t]
    
    returns = 0

    returns_list = []
    average_list = []
    buy_list = []
    sell_list = []

    while current_t < len(data)-1:

        # calculating current window average
        window_dat = data[current_t-window_period:current_t]
        window_average = np.mean(window_dat)
        # calculating historical average
        historical_average = np.mean(historical_prices)
        # calculating threshold of buy and sell window according to the standard deviation of historical prices
        historical_deviation = np.std(historical_prices)
        threshold = historical_deviation
        buy_level = historical_average - threshold
        sell_level = historical_average + threshold

        # buying when current prices are lower than historical prices on the assumption they will increase back to previous levels
        if holding_position == False and window_average < buy_level:
            current_holding_price = data[current_t]
            holding_position = True
        # selling when current prices are higher than historical prices on the assumption they will decrease back to previous levels
        if holding_position == True and window_average > sell_level:
            returns += (data[current_t] - current_holding_price)
            holding_position = False

        returns_list.append(returns)
        average_list.append(historical_average)
        buy_list.append(buy_level)
        sell_list.append(sell_level)

        # updating historical prices and removing old prices after a certain period of time
        historical_prices = data[max(0, current_t-3000):current_t]

        current_t += 1

    # replacing last value with actual value after selling off holding position at end of period
    if holding_position == True:
        returns += (data[current_t] - current_holding_price)
        returns_list[-1] = returns
    
    return returns_list, average_list, buy_list, sell_list
    
trade_returns, average_list, buy_list, sell_list = Mean_Reversion_Strategy(stock_data)
formatted_trade_returns = [f"{num:.2f}" for num in trade_returns]

plot_stock_prices = np.array(stock_data[31:len(stock_data)-1])

np.save('results_arrays/StockPrices.npy', plot_stock_prices)
np.save('results_arrays/MR_average.npy', average_list)
np.save('results_arrays/MR_buy.npy', buy_list)
np.save('results_arrays/MR_sell.npy', sell_list)
np.save('results_arrays/MR_returns.npy', trade_returns)

