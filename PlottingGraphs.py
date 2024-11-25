import matplotlib.pyplot as plt
import numpy as np

gradient_returns = np.load('results_arrays/GradientReturns.npy')
gradients = np.load('results_arrays/gradients.npy')

mean_reversion_returns = np.load('results_arrays/MR_returns.npy')
average_list = np.load('results_arrays/MR_average.npy')
buy_list = np.load('results_arrays/MR_buy.npy')
sell_list = np.load('results_arrays/MR_sell.npy')

MA_cross_returns = np.load('results_arrays/MA_returns.npy')
short_MA_list = np.load('results_arrays/MA_short.npy')
long_MA_list = np.load('results_arrays/MA_long.npy')

plot_stock_prices = np.load('results_arrays/StockPrices.npy', allow_pickle=True)
stock_returns = plot_stock_prices - plot_stock_prices[0]


# plotting returns
plt.clf()
plt.plot(stock_returns, label = 'Stock Returns', color = 'green')
plt.plot(gradient_returns, label = 'Gradient Returns', color = 'blue')
plt.plot(MA_cross_returns, label = 'Moving Average Crossover Returns', color = 'orange')
plt.plot(mean_reversion_returns, label = 'Mean Reversion Returns', color = 'red')

plt.title("Different Strategies' Trading Returns")
plt.ylabel('Value ($)')
plt.xlabel('Time (Minutes)')
plt.legend()
plt.grid()
plt.savefig('visualisations/Trading Returns', dpi=600)
plt.clf()

# plotting stock price graph
plt.plot(plot_stock_prices, label='Stock Price', color='green')
plt.ylabel('Price ($)', )
plt.xlabel('Time (Minutes)')
plt.title('S&P 500 Price Over Period')
leg = plt.legend()
for legobj in leg.get_lines():
    legobj.set_linewidth(2.0)
plt.grid()
plt.savefig('visualisations/S&P 500 Stock Price', dpi=600)
plt.clf()

# Gradients Strategy buy / sell rationale graph
plt.plot(gradients, label = f'Gradient (20 minutes)', color='green')
plt.axhline(y = 0.1, color='blue', label='Buy Threshold')
plt.axhline(y = -0.1, color='red', label='Sell Threshold')
plt.ylabel('Gradient')
plt.xlabel('Time (Minutes)')
plt.title('Price Gradients Over Time')
leg = plt.legend()
for legobj in leg.get_lines():
    legobj.set_linewidth(2.0)
plt.grid()
plt.savefig('visualisations/Gradient Trading Gradients', dpi=600)
plt.clf()

# Mean Reversion Strategy buy / sell rationale graph
plt.plot(plot_stock_prices, label='Stock Price', color='green')
plt.plot(average_list, label='Historical Average', color='tan')
plt.plot(buy_list, label='Buy Level', color='blue')
plt.plot(sell_list, label='Sell Level', color='red')
plt.ylabel('Price ($)', )
plt.xlabel('Time (Minutes)')
plt.title('Mean Reversion Trading')
leg = plt.legend()
for legobj in leg.get_lines():
    legobj.set_linewidth(2.0)
plt.grid()
plt.savefig('visualisations/Mean Reversion Trading', dpi=600)
plt.clf()

# Moving Average Cross Strategy buy / sell rationale graph
plt.plot(short_MA_list, label=f'Price MA (20 Minutes)', color='tomato')
plt.plot(long_MA_list, label = f'Price MA (50 Minutes)', color='royalblue')
plt.ylabel('Price ($)')
plt.xlabel('Time (Minutes)')
plt.title('Moving Average Crossover Trading')
leg = plt.legend()
for legobj in leg.get_lines():
    legobj.set_linewidth(2.0)
plt.grid()
plt.savefig('visualisations/Moving Average Crossover Trading', dpi=600)