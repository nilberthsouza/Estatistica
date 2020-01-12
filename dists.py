from scipy.stats import binom
from scipy.stats import poisson
import numpy as np

#Um torno mecanico produz 25% de peças com defeito
#O lote é 16
#Queremos saber qual a probabilidade de 4 dentre 16 apresentarem defeito

binom.pmf(4,16,0.25)
#Outpub
#0.225199...

#lancaremos 7 moedas, qual a probabilidade de 5 serem caras
binom.pmf(5,7,0.5)
#output
#0.218750...

#Em um sinal passam 4 veiculos por minutos, queremos saber a probabilidade de passarem 7 veiculos em 2 minutos
poisson.pmf(7,8)
#output
#0.13958653...


#distruibuição normal
mu = 230
sigma = 15

s = np.random.normal(mu,sigma, 1000)
abs(mu - np.mean(s))<240

import matplotlib.pyplot as plt

count, bins , ignored = plt.hist(s,30,density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) * np.exp(- (bins -mu)**2 /(2 * sigma)),linewidth=2,color='r')
plt.show()


