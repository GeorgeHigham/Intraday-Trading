import pandas as pd
import numpy as np

stock_data = np.array(pd.read_csv('data/S&P500_CSV.csv'))[:, 1]

def Gradient_Strategy(data):
    current_t = 51

    holding_position = False
    current_holding_price = None

    gradient_period = 20
    threshold = 0.15
    
    returns = 0

    returns_list = []
    gradient_list = []

    while current_t < len(data)-1:
        
        gradient_t = (data[current_t] - data[current_t-gradient_period]) / gradient_period

        # buying when gradient over period is higher than buy_threshold
        if holding_position == False and gradient_t > threshold:
            current_holding_price = data[current_t]
            holding_position = True
        # selling once gradient falls below negative buy_threshold
        if holding_position == True and gradient_t < -threshold:
            returns += (data[current_t] - current_holding_price)
            holding_position = False

        returns_list.append(returns)
        gradient_list.append(gradient_t)

        current_t += 1

    # replacing last value with actual value after selling off holding position at end of period
    if holding_position == True:
        returns += (data[current_t] - current_holding_price)
        returns_list[-1] = returns

    
    return returns_list, gradient_list

trade_returns, gradients = Gradient_Strategy(stock_data)

np.save('results_arrays/GradientReturns.npy', trade_returns)
np.save('results_arrays/gradients.npy', gradients)