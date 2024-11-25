# Intraday-Trading
Utilising three trading strategies on intraday S&P 500 data over a month.

## Results
Returns from different trading strategies.

<img src="visualisations/Trading Returns.png" alt="alt text" width="700" height="500">

## Strategies' Explanations
### Gradient Trading Strategy
This strategy is a momentum based strategy that will buy and sell stock based on the gradient of price change over a set period of time. Stocks are bought if the gradient is sufficiently high and sold if it is sufficiently low.

<img src="visualisations/Gradient Trading Gradients.png" alt="alt text" width="700" height="500">

### Moving Average Cross Strategy
This strategy is also a momentum strategy and involves using two moving window averages, one of a longer period and one of a shorter period. When the shorter moving average crosses and exceeds the longer the stock is bought, and the stock is sold on the reverse.

<img src="visualisations/Moving Average Crossover Trading.png" alt="alt text" width="700" height="500">

### Mean Reversion Strategy
This strategy is based on the logic that short-term fluctuations in prices will tend to revert back to a longer-term average price. For this stocks were bought once prices dropped under a threshold below this historical average and sold once they rose over the same threshold above the price. The threshold was calculated from historical deviations in prices.

<img src="visualisations/Mean Reversion Trading.png" alt="alt text" width="700" height="500">

## Assumptions and Limitations
This project has made a number of assumptions and limitations:

- instantaneous buying and selling of stock
- no trade costs
- no short selling stock
- purchases and sales do not affect the market
- maximum one share to be owned at any given time

## Sources
Data dowloaded from library yfinance. Prices are adjusted close of '^GSPC' ticker between dates (non inclusive) 28-10-2024 & 25-11-2024 saved to csv.

