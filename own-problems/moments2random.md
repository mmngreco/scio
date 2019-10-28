## Problema

Conocidos los 4 primeros momentos (`m0`, `m1`, `m2`, `m3`), queremos generar
series de números aleatorios que cumplan dichas restricciones.

## Solución

### Programación

#### Rlang

* https://www.r-bloggers.com/four-moments-of-portfolios/
* https://stackoverflow.com/questions/4807398/how-to-generate-distributions-given-mean-sd-skew-and-kurtosis-in-r
* https://www.rdocumentation.org/packages/SuppDists/versions/1.1-9.4/topics/Johnson

#### Python

* http://www.statsmodels.org/devel/generated/statsmodels.sandbox.distributions.extras.pdf_mvsk.html#statsmodels.sandbox.distributions.extras.pdf_mvsk 

### Literatura

* http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=A697CE774599705FDB0EFD8E9444D088?doi=10.1.1.106.6130&rep=rep1&type=pdf
* https://www.cambridge.org/core/books/systems-of-frequency-curves/D19ED98FD264F6B282C5DCE5EB60DA47
* https://www.jstor.org/stable/2346692?origin=JSTOR-pdf&seq=1#page_scan_tab_contents
* https://stats.stackexchange.com/questions/380422/how-do-you-find-shape-parameters-of-a-johnson-distribution-from-skew-and-kurtosi
* https://en.wikipedia.org/wiki/Johnson%27s_SU-distribution
* https://www.jstor.org/stable/pdf/2285407.pdf?seq=1#page_scan_tab_contents

#### Usando "moment generating function"

* https://uwaterloo.ca/waterloo-research-institute-in-insurance-securities-and-quantitative-finance/sites/ca.waterloo-research-institute-in-insurance-securities-and-quantitative-finance/files/uploads/files/2010-07.pdf
* https://math.stackexchange.com/questions/2649611/generate-random-numbers-using-moment-information
* https://code.i-harness.com/en/q/495ae6

### El problema de Pearson

* https://www-cdf.fnal.gov/physics/statistics/notes/cdf6820_pearson4.pdf

### Discusión

* https://mathoverflow.net/questions/3525/when-are-probability-distributions-completely-determined-by-their-moments
* https://stats.stackexchange.com/questions/341458/generate-random-variable-with-given-moments
* https://projecteuclid.org/download/pdfview_1/euclid.lnms/1249305333

## Relacionado

* https://en.wikipedia.org/wiki/Moment_problem
* https://www.one-tab.com/page/rF3z76YCQjqozMgCMv6vUg
* http://www.columbia.edu/~ld208/psymeth97.pdf

### Python library:

#### Method : johnson

Fork : `git@github.com:mmngreco/connorav.git`

```python
import connorav
import numpy as np
from scipy import stats
from pprint import pprint
from matplotlib import pyplot as plt
plt.ion()

N = 100000
# moments desired
mu = 1
std = 0.2
skew = 0.0
kurt = 8

def describe(x):
    out = dict(
        N = len(x),
        MU = np.mean(x),
        STD = np.std(x),
        SKEW = stats.skew(x),
        KURT = stats.kurtosis(x),
    )
    return out

# creating distribution
if __name__ == "__main__":
    k_values = []
    for i in range(100):
        d = connorav.MSSKDistribution(mu, std, skew, kurt)
        x_rand = d.rvs(N)
        k = stats.kurtosis(x_rand)
        k_values.append(k)
        if i % 20 == 0:
            _ = plt.hist(x_rand, bins=50, alpha=0.5)
        pprint(f"kurtosis: {k:.2f}({kurt})")

    print(f"{np.mean(k_values): .3f} ( {np.std(k_values): .3f} )")
    plt.hist(x_rand, bins=100)

```

#### Method : statsmodels

```python
# ============================================================
# Statsmodels

from statsmodels.sandbox.distributions.extras import pdf_mvsk
import numpy as np
from matplotlib import pyplot as plt
plt.ion()

if __name__ == "__main__":
    pdf = pdf_mvsk([mu, std, skew, kurt])
    x = np.linspace(pdf(1e-4), pdf(1-1e-4))
    y = np.array([pdf(xi) for xi in x])

    plt.plot(x,y)
    plt.show()
```

#### Method : Fleishman

Source : https://gist.github.com/zeimusu/7432603b85dc6406c6ea

```python
import numpy as np
from numpy.linalg import solve
import logging
logging.basicConfig(level=logging.DEBUG)
from scipy.stats import moment,norm


def fleishman(b, c, d):
    """calculate the variance, skew and kurtois of a Fleishman distribution
    F = -c + bZ + cZ^2 + dZ^3, where Z ~ N(0,1)
    """
    b2 = b * b
    c2 = c * c
    d2 = d * d
    bd = b * d
    var = b2 + 6*bd + 2*c2 + 15*d2
    skew = 2 * c * (b2 + 24*bd + 105*d2 + 2)
    kurt = 24 * (bd + c2 * (1 + b2 + 28*bd) + 
                 d2 * (12 + 48*bd + 141*c2 + 225*d2))
    return (var, skew, kurt)

def flfunc(b, c, d, skew, kurtosis):
    """
    Given the fleishman coefficients, and a target skew and kurtois
    this function will have a root if the coefficients give the desired skew and kurtosis
    """
    x,y,z = fleishman(b,c,d)
    return (x - 1, y - skew, z - kurtosis)

def flderiv(b, c, d):
    """
    The deriviative of the flfunc above
    returns a matrix of partial derivatives
    """
    b2 = b * b
    c2 = c * c
    d2 = d * d
    bd = b * d
    df1db = 2*b + 6*d
    df1dc = 4*c
    df1dd = 6*b + 30*d
    df2db = 4*c * (b + 12*d)
    df2dc = 2 * (b2 + 24*bd + 105*d2 + 2)
    df2dd = 4 * c * (12*b + 105*d)
    df3db = 24 * (d + c2 * (2*b + 28*d) + 48 * d**3)
    df3dc = 48 * c * (1 + b2 + 28*bd + 141*d2)
    df3dd = 24 * (b + 28*b * c2 + 2 * d * (12 + 48*bd + 
                  141*c2 + 225*d2) + d2 * (48*b + 450*d))
    return np.matrix([[df1db, df1dc, df1dd],
                      [df2db, df2dc, df2dd],
                      [df3db, df3dc, df3dd]])

def newton(a, b, c, skew, kurtosis, max_iter=25, converge=1e-5):
    """Implements newtons method to find a root of flfunc."""
    f = flfunc(a, b, c, skew, kurtosis)
    for i in range(max_iter):
        if max(map(abs, f)) < converge:
            break
        J = flderiv(a, b, c)
        delta = -solve(J, f)
        (a, b, c) = delta + (a,b,c)
        f = flfunc(a, b, c, skew, kurtosis)
    return (a, b, c)


def fleishmanic(skew, kurt):
    """Find an initial estimate of the fleisman coefficients, to feed to newtons method"""
    c1 = 0.95357 - 0.05679 * skew + 0.03520 * skew**2 + 0.00133 * kurt**2
    c2 = 0.10007 * skew + 0.00844 * skew**3
    c3 = 0.30978 - 0.31655 * c1
    logging.debug(f"inital guess c1={c1:.3f},c2={c2:.3f},c3={c3:.3f}")
    return (c1, c2, c3)


def fit_fleishman_from_sk(skew, kurt):
    """Find the fleishman distribution with given skew and kurtosis
    mean =0 and stdev =1
    Returns None if no such distribution can be found
    """
    if kurt < -1.13168 + 1.58837 * skew**2:
        return None
    a, b, c = fleishmanic(skew, kurt)
    coef = newton(a, b, c, skew, kurt)
    return(coef)

def fit_fleishman_from_standardised_data(data):
    """Fit a fleishman distribution to standardised data."""
    skew = moment(data,3)
    kurt = moment(data,4)
    coeff = fit_fleishman_from_sk(skew,kurt)
    return coeff

def describe(data):
    """Return summary statistics of as set of data"""
    mean = sum(data)/len(data)
    var = moment(data,2)
    skew = moment(data,3)/var**1.5
    kurt = moment(data,4)/var**2
    return (mean,var,skew,kurt)

def generate_fleishman(a,b,c,d,N=100):
    """Generate N data items from fleishman's distribution with given coefficents"""
    Z = norm.rvs(size=N)
    F = a + Z*(b +Z*(c+ Z*d))
    return F

"""
==============================================================================
Data in form of one number per line
"""

if __name__ == "__main__":
    data = np.random.randn(100)
    mean = data.mean()
    std = data.std()
    std_data = (data - mean)/std

    coeff = fit_fleishman_from_standardised_data(std_data)
    print(coeff)
    describe(std_data)
    print(describe(data))
    sim = (generate_fleishman(-coeff[1],*coeff, N=10000))*std+mean
    print(describe(sim))

```
