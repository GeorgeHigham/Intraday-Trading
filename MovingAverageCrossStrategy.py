import pandas as pd
import numpy as np

stock_data = np.array(pd.read_csv('data/S&P500_CSV.csv'))[:, 1]

def MA_strategy(data):
    current_t = 51
    t_0 = current_t - 1

    holding_position = False
    current_holding_price = None

    short_period = 20
    long_period = 50

    last_MA_short_dat = data[t_0-short_period:t_0]
    last_MA_long_dat = data[t_0-long_period:t_0]

    last_MA_short = last_MA_short_dat.sum() / len(last_MA_short_dat)
    last_MA_long = last_MA_long_dat.sum() / len(last_MA_long_dat)
    
    returns = 0

    returns_list = []
    short_MA_list = []
    long_MA_list = []


    while current_t < len(data)-1:

        MA_short_dat = data[current_t-short_period:current_t]
        MA_long_dat = data[current_t-long_period:current_t]

        MA_short = MA_short_dat.sum() / len(MA_short_dat)
        MA_long = MA_long_dat.sum() / len(MA_long_dat)

        # buying the stock at 'Golden Cross'
        if last_MA_short <= last_MA_long and MA_short > MA_long and holding_position == False:
            current_holding_price = data[current_t]
            holding_position = True
        # selling the stock at 'Death Cross'
        if last_MA_short > last_MA_long and MA_short <= MA_long and holding_position == True:
            returns += (data[current_t] - current_holding_price)
            holding_position = False

        short_MA_list.append(MA_short)
        long_MA_list.append(MA_long)
        returns_list.append(returns)

        last_MA_short = MA_short
        last_MA_long = MA_long
        last_MA_short_dat = MA_short_dat
        last_MA_long_dat = MA_long_dat

        current_t += 1

    # replacing last value with actual value after selling off holding position at end of period
    if holding_position == True:
        returns += (data[current_t] - current_holding_price)
        returns_list[-1] = returns

    
    return returns_list, short_MA_list, long_MA_list
    
trade_returns, short_MA_list, long_MA_list = MA_strategy(stock_data)

np.save('results_arrays/MA_returns.npy', trade_returns)
np.save('results_arrays/MA_short.npy', short_MA_list)
np.save('results_arrays/MA_long.npy', long_MA_list)


