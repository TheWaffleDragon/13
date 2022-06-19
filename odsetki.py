# import numpy as np

# freq = 12
# rate = 0.0675
# years = 30
# pv = 200000

# rate /= freq  # konwersja stopy do okresu miesięcznego
# nper = years * freq  # liczba wszystkich okresów

# periods = np.arange(1,nper+1,dtype=int)

# import numpy_financial as npf
# interest_equal = - np.around(npf.ipmt(rate,periods,nper,pv),2)
# interest_equal[:10]

# np.set_printoptions(suppress=True)

# principal_decreasing = np.around(np.zeros(nper)+(pv/nper),2)
# principal_decreasing[:10]

# balance = np.zeros(nper) + pv
# balance_close = np.around(balance - np.cumsum(principal_decreasing),2)
# balance_close[[0,1,2,-3,-2,-1]]

# np.cumsum(principal_decreasing)[:10]

# balance_open = balance_close + principal_decreasing

# interest_decreasing = np.around(balance_open * rate,2)
# interest_decreasing[:10]

# print("Wartość odsetek do zapłaty w wariancie kredytu w równych ratach wynosi: " + str("{:.2f}".format(interest_equal.sum())))
# print("Wartość odsetek do zapłaty w wariancie kredytu w ratach malejących wynosi: " + str("{:.2f}".format(interest_decreasing.sum())))


# import matplotlib.pyplot as plt

# plt.plot(interest_equal.cumsum(),label='raty równe')
# plt.plot(interest_decreasing.cumsum(),label='raty malejące')
# plt.legend()
# plt.xlabel('Liczba okresów')
# plt.ylabel('Skumulowana wartość odsetek')

#%% Zadanie 2: mieszaknie

import numpy as np
import numpy_financial as npf


price_0 = 120000
years = 5
freq=12
rate_price = 0.05
rate_price_minthly = rate_price/12

rate_return = 0.12
rate_return_monthly = rate_return/12


#cena mieszkania
nper = years * freq 
periods = np.arange(1,nper+1,dtype=int)

price = np.around(npf.fv(rate_price_minthly,periods,0,-price_0,when='begin'),2)
price_end = np.around(npf.fv(rate_price_minthly,nper,0,-price_0,when='begin'),2)

#oszczednosci

savings_0 = np.around(npf.pmt(rate_return_monthly,nper, 0, price_end, when='end'),2)
savings = -np.around(npf.fv(rate_return_monthly,periods,-savings_0,0,when='begin'),2)



import matplotlib.pyplot as plt

plt.plot(price,label='cena mieszakania')
plt.plot(savings,label='oszczednosci')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('Wartosc')















