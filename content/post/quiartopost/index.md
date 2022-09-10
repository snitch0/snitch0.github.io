---
title: Hello, Quarto
date: "2022-04-06"
categories:
  - Matplotlib
  - Coordinates
format: hugo
slug: quarto-test
tags:
  - python
---



## Polar Axis

For a demonstration of a line plot on a polar axis, see **?@fig-polar**.

``` python
# !pip install nbclient
import sys
print(sys.executable)
```

    /home/oodake/.pyenv/versions/3.10.6/bin/python3

``` python
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```

<strong>aaaaaaaaaa太文字太文字</strong>あああああ

<img src="index_files/figure-gfm/cell-3-output-1.png" width="450" height="439" />

![](index_files/figure-gfm/cell-3-output-1.png)

![](img/avatar.png)
