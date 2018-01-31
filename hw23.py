# Author: Jake VanderPlas
# License: BSD
#   The figure produced by this code is published in the textbook
#   "Statistics, Data Mining, and Machine Learning in Astronomy" (2013)
#   For more information, see http://astroML.github.com
#   To report a bug or issue, use the following forum:
#    https://groups.google.com/forum/#!forum/astroml-general
import numpy as np
from scipy.stats import binom,poisson,norm
from matplotlib import pyplot as plt

#----------------------------------------------------------------------
# This function adjusts matplotlib settings for a uniform feel in the textbook.
# Note that with usetex=True, fonts are rendered with LaTeX.  This may
# result in an error if LaTeX is not installed on your system.  In that case,
# you can set usetex to False.

#------------------------------------------------------------
# Define the distribution parameters to be plotted
n_values = [40, 4]
b_values = [0.35, 0.35]
linestyles = ['-', '--']
color=['red','blue']
color2=['yellow','green']
x = np.arange(-1, 200)

#------------------------------------------------------------
# plot the distributions
fig, ax = plt.subplots(figsize=(5, 3.75))

for (n, b, ls,col,col2) in zip(n_values, b_values, linestyles,color,color2):
    # create a binomial distribution
    dist = binom(n, b)
    poi = poisson(n*b)
    mu=dist.mean()
    std = dist.std()
    mu2 = poi.mean()
    std2 = poi.std()

    plt.plot(x, dist.pmf(x), ls=ls, c=col,
             label=r'$b=%.2f,\ n=%i$' % (b, n), linestyle='steps-mid')
    plt.plot(x, poi.pmf(x), ls=ls, c=col2,
             label=r'$b=%.2f,\ n=%i$' % (b, n), linestyle='steps-mid')
    xmin, xmax = plt.xlim()
    x1 = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=1,label="Fit results: mu = %.2f,  std = %.2f" % (mu, std),c=col)
    x2 = np.linspace(xmin, xmax, 100)
    p2 = norm.pdf(x, mu2, std2)
    plt.plot(x, p2, 'k', linewidth=1,label="Fit results: mu = %.2f,  std = %.2f" % (mu, std),c=col2)


plt.xlim(-0.5, 35)
plt.ylim(0, 0.55)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|b, n)$')
plt.title('Binomial Distribution')

plt.legend()
plt.show()
