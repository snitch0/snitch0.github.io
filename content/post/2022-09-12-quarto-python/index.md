---
title: "QuartoでPythonを使うときの注意とか"
description: 意外と複雑な仕様?😈
author: Snitch
date: "2022-09-11"
categories:
  - Quarto
  - R
  - Python
  - Reticulate
  - Linux
tags:
  - quarto
  - R
  - Python
format: hugo
slug: "python-and-quarto"
html-math-method: webtex
---



## QuartoにおけるPythonの仕様

Quartoは以下のようにRでもPythonでも一つのファイルでレンダリングできるのが素晴らしい✨

しかし、Python単独なら特に難しいことは無いが、RとPythonが共存すると**ある問題**が生じる。

``` r
result = lm(data = iris, Sepal.Width ~ Sepal.Length)
summary(result)
```


    Call:
    lm(formula = Sepal.Width ~ Sepal.Length, data = iris)

    Residuals:
        Min      1Q  Median      3Q     Max
    -1.1095 -0.2454 -0.0167  0.2763  1.3338

    Coefficients:
                 Estimate Std. Error t value Pr(>|t|)
    (Intercept)   3.41895    0.25356   13.48   <2e-16 ***
    Sepal.Length -0.06188    0.04297   -1.44    0.152
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 0.4343 on 148 degrees of freedom
    Multiple R-squared:  0.01382,   Adjusted R-squared:  0.007159
    F-statistic: 2.074 on 1 and 148 DF,  p-value: 0.1519

``` python
from sklearn.datasets import load_iris
from sklearn import linear_model
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])

df["Name"] = pd.Series(iris.target)

model = linear_model.LinearRegression()
ft = model.fit(df[["SepalLength"]], df[["SepalWidth"]])
print(f"Intercept: {ft.intercept_[0]:.6}, Coef: {ft.coef_[0][0]:.6}")
```

    Intercept: 3.41895, Coef: -0.0618848

### エンジンにjupyterを使う場合

Pythonを使うなら、おそらくこれが一番明快でおすすめの方法になる。

qmdのyamlヘッダにて`engine: jupyter`を選択しておく方法。たとえば、以下のようにする。

``` yaml
title: "QuartoでPythonを使うときの注意とか"
description: 意外と複雑な仕様?😈
author: Snitch
date: "2022-09-11"
categories:
  - Quarto
  - R
  - Python
  - Reticulate
  - Linux
tags:
  - quarto
  - R
  - Python
format: hugo
slug: "python-and-quarto"
jupyter: python3
html-math-method: webtex
```

一部はhugo関係のものもあるが、`jupyter`や`html-math-method`
の部分はquartoに由来する。(いずれこのヘッダオプションも研究しなければ・・・)

要は`jupyter`の`python3`カーネルを使っているというだけなので、bashカーネルだってRカーネルだって存在さえしてれば使えるということなのだろう。

このオプションを指定している間に起こる諸問題[^1]はjupyter由来のものになると思われるので、対処はしやすそう。しかしipywidgetなどはhugoへのレンダリングは厳しそう。qmdではなくipynbからやる方が無難だろう。

しかし、このjupyterカーネルでは<mark>単一のカーネルしか指定できない</mark>ので、RとPythonの共存は不可能である･･･。

### エンジンにjupyterを使用しない場合

jupyterを指定しない場合は<mark>pythonセルがreticulate+knitr経由で実行される</mark>。PythonとR両方を使ったドキュメントを気軽に書くことが出来るのはreticulate様のおかげだったのだ。万歳。

しかし、reticulateは親切なんだかお節介なんだか分からないが、python実行バイナリのパス指定方法が複数あるせいで設定変更が一発で効かないことがしばしばあり、個人的にそれがreticulateを使う気にならない理由の一つ🐍[^2]

そして、reticulateの設定で見事にハマった。

備忘録も兼ねてこのハマりポイント2つを残しておきたいと思う。

## reticulateのハマりポイント

### 仮想環境には気をつける

自分は普段pyenvとmambaforgeの二つを主なpythonソースとして使っている。前者は汎用的なコーディング(シェルスクリプト作成など)用で、後者はガッツリバイオインフォ解析する時用で使い分けている。

今回何も考えずに実行しようとしたら、pyenvがうまく認識されてくれなかった。

調べてみたところ、[shared libraryを作らないpyenvはそれを必須とするreticulateと相性が悪いらしい](https://firas.io/post/pyenv_rstudio/)。このページに書かれた手順を試してはみたが、やはり同じエラーが出るだけだった。

諦めてmambaforgeに専用の仮想環境を用意してやったところ、うまく動作した。

``` bash
mamba create -n pyr python=3.10
```

### `RETICULATE_PYTHON`環境変数に注意する

要はこの変数に適切なパスが通っていれば問題ないが、環境変数であるせいか、セッションステータスによっては反映されたりされなかったりするのが面倒だった。

ネットを見ると色々と対処方法が書いてあり、`use_conda()`を使うだとか、`use_python()`を使うとかの情報があるが、``./Renviron\`に変数を記入してやるのが一番問題が起きにくかった。根拠が曖昧な経験則でアレだが、reticulateはこういう「なんでうまく行ったのがが分からない」ケースがちょいちょいある。

```bash {name=".Renviron"}
RETICULATE_PYTHON="~/mambaforge/envs/pyr/bin/python"
```


他にも`.Rprofile`に`Sys.setenv(RETICULATE_PYTHON=)`などと定義してやる方法もあるらしいが、なんとなくOS側で定義されていた方が安心な気がする。

[^1]: matplotlibのplot inlineとか。

[^2]: ならRstudio使いなさいよみたいな声が聞こえてきそうだが、Rstudioでpythonコーディングは結構キツい。pythonコーディングはVSCodeやPyCharmの方が圧倒的に優れており、めいっぱいPython書く人ならこれに同意してくれると思う。
