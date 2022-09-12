---
title: subprocessライブラリの使い方って結局何が正解なん
description: 公式ドキュメント読もうぜ、という結論
author: Snitch
date: "2022-09-12"
categories:
  - Python
tags:
  - Python
  - subprocess
format: hugo
slug: "python-subprocess"
jupyter: python3
html-math-method: webtex
---



# pythonライブラリの使い方が分からなくなることがある

pythonライブラリにはド定番のライブラリがいくつもあるが、それらの仕様は結構忘れがち。

たとえば`csv`の`DictWriter`クラス。引数がファイルオブジェクトなのかそれともパスを文字列で与えるのか、刹那の思考をはさんだ後に`with open()`などと書き始める。

`csv.DictWriter`クラスならまだ良いが、やり方が複数通り存在する場合になるともうカオスだ。`urllib.request`と`requests`のどっち使うんだとか、はたまた`urllib3`はなんなんだとか。。そんな「結局何が正解なん」案件で`subprocess`の使い方についてちょっと思うところがあった。

## subprocessライブラリの使い方

色々やりたいときは`Popen`クラスを使う、簡単なユーズケースなら`run`メソッドを使う、という認識でいたので、基本的に何も考えず`Popen`クラスを毎回使っていた。

こんな感じ。

``` python
from subprocess import Popen

ps = Popen(['ls', '-lah'])
ps.wait()
```

`Popen.wait()`するタイミングをずらすことで非同期処理的にマルチプロセス化することもあるため、個人的にはシェルスクリプトとしてpythonを使う際には欠かせないやつ🤔

## stdoutを使おうとするとちょい面倒

標準出力を取得しようとすると`subprocess.PIPE`が必要になるのでちょいめんどくさい。バイト文字列で選ってくるところがなおさら😅

``` python
from subprocess import Popen, PIPE

ps = Popen(['echo', 'hello'], stdout=PIPE)
s_out = ps.stdout.readlines()
print([s.decode("utf-8") for s in s_out])
```

    ['hello\n']

## ググったらsubprocess.runの方が楽らしいと知る

[こちらのQiita記事](https://qiita.com/yutake27/items/033155608d64eac0adc2)を拝読すると、「`suborocess.run`を使うのが良いとされている」とか「`capture_output`を使ってもできる」というのを聞いて👀から🐟!

``` python
import subprocess

ps = subprocess.run(['echo', 'hello'], capture_output=True, text=True)
s_out = ps.stdout
print(s_out)
```

    hello

--はぁ･･･勉強不足でした。。すみません。。と思いつつ[document](https://docs.python.org/ja/3/library/subprocess.html)を見ると確かに以下のようにrunメソッドが推奨されていた。[^1]

> サブプロセスを起動するために推奨される方法は、すべての用法を扱える run() 関数を使用することです。より高度な用法では下層の Popen インターフェースを直接使用することもできます。

また、`capture_output`オプションはpython3.7で実装されたらしい。なるほど比較的新しいけど、少なくともセキュリティサポートされているバージョンをきちんと追ってる人なら間違えてはいけないポイントだろう。

## みんなちゃんと情報フォローしてるのか?と気になって調べてみた

結論、**Qiita記事はちょっと危険だな**と思った。自分も似たようなものだが･･･

### やばいパターン①推奨されていない書き方を解説している

`shell=True`を使えば簡単にパイプが使えるので、便利なことは便利。しかし、任意のコードを実行させられる可能性があるので、ウェブフレームワークなどで使うのは御法度というのが有名。
これを説明せずに「shell=Trueの方が初心者にはオススメ」などと平然と書かれているケースがあった。

### ちょっと気になったパターン②capture_outputオプションの言及がない

先に言っておくが、個人ブログは高確率でこれに言及している。最初の投稿時に言及が無くとも、ほぼ全員が追記していた。すごい😲きっと多分自分のコンテンツに責任を持っているのだろう。自分もそうならねば。

`Popen.PIPE`の方法はQiita記事だけをみていたらゴールドスタンダードに見えるだろう。現に自分がそうだった。

## やっぱ、公式ドキュメントはちゃんと読んだ方が良いわ

正直自分はpythonドキュメントきちんと読んでこなかった。だってフォントとかレイアウトとかのせいか、読みにくいんだもん。

しかし、細かい推奨レベルや後で追加されたオプションなど、知らないと恥かく内容も多いと感じた。

コツコツpythonドキュメントをちゃんと読み直してみるのもいい学習方法かもしれない。

[^1]: これを推奨ととるかは読解力次第な気もする
