
# Python

## Matplotlib

```python
from statsmodels.formula.api import ols
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# format
plt.style.use(['seaborn-white', 'seaborn-paper'])
matplotlib.rc("font", family="Times New Roman")
sns.set_context("paper")
sns.set(font="Times")
```

### tsdisplay rlang function like

https://gist.github.com/mmngreco/76f1e480c8ccf1e4966addfb4e6481f6

```python
def tsdisplay(yt):
    import matplotlib.gridspec as gridspec
    from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

    plt.figure(figsize=(8,7))
    gs = gridspec.GridSpec(2, 2)
    ax1 = plt.subplot(gs[0, :])
    ax2 = plt.subplot(gs[1,0])
    ax3 = plt.subplot(gs[1,1])
    yt.plot(ylim=(0,max(yt)), ax=ax1)
    _ = plot_acf(yt, ax=ax2)
    _ = plot_pacf(yt, ax=ax3)
    plt.tight_layout()
```


# Condition number

One way to assess multicollinearity is to compute **the condition number**.
Values over 20 are worrisome (see Greene 4.9). The first step is to normalize
the independent variables to have unit length:

```python
norm_x = X.values
for i, name in enumerate(X):
    if name == "const": continue
    norm_x[:,i] = X[name] / np.linalg.norm(X[name])

norm_xtx = np.dot(norm_x.T,norm_x)

```

Then, we take the square root of the ratio of the biggest to the smallest eigen
values.

```python
eigs = np.linalg.eigvals(norm_xtx)
condition_number = np.sqrt(eigs.max() / eigs.min())
print(condition_number)

56240.8689371

```

