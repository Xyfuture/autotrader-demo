from autotrader import AutoTrader

at = AutoTrader()

# 设置config文件夹下的keys.yaml文件
# keys中的sandbox_mode 为模拟交易
at.configure(verbosity=2, show_plot=True,broker='ccxt:okx',feed='ccxt:okx')
at.add_strategy('ema_crossover_paper')

at.run()
