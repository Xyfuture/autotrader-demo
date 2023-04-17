from autotrader import AutoTrader

# Create AutoTrader instance, configure it, and run backtest
at = AutoTrader()

at.configure(verbosity=1, show_plot=True, feed='yahoo',mode='continuous')

# 除ema_crossover策略之外的其他策略,要使用 mode='periodic' 的配置,如下
# at.configure(verbosity=1, show_plot=True, feed='yahoo',mode='periodic')

# 策略的名字与config文件夹下的文件名一致
# 该文件中的watchlist为交易对象,具体看API中的格式,ETH-USD表示ETH与USD之间的交易
at.add_strategy('ema_crossover')

# 时间
at.backtest(start = '1/4/2022', end = '1/4/2023')

at.virtual_account_config(initial_balance=1000, leverage = 1)
at.run()
