---
title: Pythonのlinterとformatter事情(@VisualStudioCode)
description: flake8とblackが良さそうだけど、今後に期待なのかしら
author: Snitch
date: "2022-09-21"
categories:
  - Python
  - VSCode
tags:
  - python
  - vscode
  - linter
  - formatter
format: hugo
slug: "python-linter-formatter"
jupyter: python3
html-math-method: webtex
---



# LinterとFormatterにも色々あることを知る

先日Twitterを徘徊していたら、ruffというrust製のpython linterのレポジトリを発見した。試しに使ってみたら本当に爆速で驚き😲

で、自分はVSCodeユーザーなので、どうやったらVSCodeのlinterとしてruffを使えるのだろうと思ったら[現時点では対応してないみたいだった](https://github.com/charliermarsh/ruff/issues/118)。詳しいことはよく分からないが、どうやらVSCodeのpython拡張側での対応が必要らしく、[少なくともVSCode python拡張のメンテナが実装することはないらしい](https://github.com/microsoft/vscode-python/issues/19843)。

残念だなぁと思ったが、実際VSCode公式のpylint以外の選択肢についてあんまり知らなかったので調べてみることに。

## 現在サポートされているlinter

Command palletteから「Python: リンターを選択」を実行したとき、`bandit`、`flake8`、`mypy`、`prospector`、`pycodestyle`、`pydocstyle`、`py lama`、`pylint`の8つが選択可能だった。

<br>

違いは以下の記事がとても参考になった。

{{< blog-card url="https://zenn.dev/yhay81/articles/yhay81-202102-pythonlint" >}}

### linter

flake8 + mypy が自分的には必須かなと思った。

flake8はざっと見た感じ、コーディング規約を必要十分な感じに網羅していると思った。
mypyは型チェックするのに必須。

でもせっかく調べたので、banditも入れてみた。セキュリティを気をつけ無きゃいけない機会は仕事上ほとんどないけど。

### formatter

現状あまり選択肢があるわけではないが、blackが割と厳しめでよさそう。

使ってみたら一行あたりの文字数制限がblackとflake8で食い違ってしまったので、flake8の実行オプションを設定してやる必要があるのと、エディタの縦線の位置をずらしてあげる。

``` json
{
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length", "88", "--ignore=E203,W503,W504"
    ],
}
```

コレに関しては以下の記事を参考にさせていただいた。

{{< blog-card url="https://www.macky-studio.com/entry/2019/07/04/152323" >}}

## 完成品

結局あれこれいじってこうなった。

WSL2の設定ファイルなのでスリムだが、気づけばpython系とneovim系ぐらいしか設定してないのか。

``` json

{
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length", "88", "--ignore=E203,W503,W504"
    ],
    "python.linting.mypyEnabled": true,
    "python.languageServer": "Pylance",
    "python.analysis.completeFunctionParens": true,
    "python.analysis.logLevel": "Warning",
    "python.linting.banditEnabled": true,
    "python.testing.pytestEnabled": true,
    "[python]": {
        "editor.defaultFormatter": null,
        "editor.formatOnSave": true
    },
    "python.formatting.provider": "black",
    "python.analysis.typeCheckingMode": "basic",
    "vscode-neovim.mouseSelectionStartVisualMode": false,
    "vscode-neovim.neovimInitVimPaths.linux": "~/.config/nvim/init.lua",
    "editor.lineNumbers": "relative",
}
```
