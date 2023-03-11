---
title: このブログの書き方
description: "hugoとstack themeのスニペット+自作コードなど"
author: Snitch
date: "2023-03-11"
categories:
  - Hugo
  - etc
tags:
  - blog
  - Hugo
format: hugo
slug: hugo-blog-snippets
html-math-method: webtex
---

## この記事は自分のための備忘録です

[メインブログ](http://excel2rlang.com/)は執筆コストが高すぎるので、気軽にかけるこちらのHugoブログへコンテンツを集約しようと画策しています。

こちらで積極的な記事執筆に従事すべく、[`hugo-stack`theme]()にて定義されているスニペットやHugoそのもので定義されているスニペットをまとめておきます。あくまで自分用なので網羅はしていません。

自分のための備忘録ですが、`hugo-stack` themeをお使いの方の参考にもなれば。

ショートコードなどは追加するかもしれないので、随時この記事を更新します。

## Hugoで規定されているショートコード

### [`figure`](https://gohugo.io/content-management/shortcodes/#figure)

```markdown
{{</* figure src="https://d33wubrfki0l68.cloudfront.net/c38c7334cc3f23585738e40334284fddcaf03d5e/2e17c/images/hugo-logo-wide.svg" title="Hugo logo" */>}}
```

{{< figure src="https://d33wubrfki0l68.cloudfront.net/c38c7334cc3f23585738e4033284fddcaf03d5e/2e17c/images/hugo-logo-wide.svg" title="Hugo logo" >}}

Markdown記法で事足りることがほとんどなので、`figure`を使うことは無さそうです。

### [gist](https://gohugo.io/content-management/shortcodes/#gist)

{{< gist snitch0 364146db37e9866f49b0868cea4ca8b6 >}}

gistは今回初めて使ったくらいなので、これも使うことは無いかも。使い方は簡単。

### highlight

```
{{</* highlight python  >}}
...
{{< /highlight */>}}
```


{{< highlight python >}}
def bubbleSort(array):

  # loop to access each array element
  for i in range(len(array)):
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):
      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:
        # swapping elements if elements
        # are not in the intended order
        array[j], array[j+1] = array[j+1], array[j]
  return array

data = [-2, 45, 0, 11, -9]
sorted_data = bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(sorted_data)
{{< /highlight >}}

※AIが生成したコードなので間違ってるかもしれません(見た限り合ってるっぽいけど)

これもmarkdown記法で足りる。本当は行ハイライトなども可能ですが、stackテーマとは相性が悪いのか行番号がずれてしまいます。

### ref

```
[相模原サンキューキャンペーンの時の記事]({{</*  ref "2022-10-15-sagamihara-map/index.md"  */>}})
```

[相模原サンキューキャンペーンの時の記事]({{< ref "2022-10-15-sagamihara-map/index.md" >}})

サイト内リンクのURLを自動生成してくれるスニペット。

これ今まで全く活用してなかったけど、便利だし最適解だし使わなきゃだな。

[ページ内リンク]({{< ref "2023-03-09-how-to-write-hugo-blog/index.md#hugoで規定されているショートコード">}})も使ってみたけど、残念ながらうまくジャンプしてくれませんでした。

### tweet

```
{{</* tweet golang 1633151903352627207 */>}}
```

{{< tweet golang 1633151903352627207 >}}

ツイート引用もwordpressだと何かと面倒ですが、hugoのショートコードならかなり簡単に。

このブログで仕様しているstackテーマでは中心寄せのcssになっていなかったので、以下のように少し改変しました。

```css
    .twitter-tweet {
        color: var(--card-text-color-main);
        display:block;
        margin-left:auto;
        margin-right:auto;
    }
```

![css改変前後の比較](tweet-center.png)

### youtube

```
{{</* youtube weLaDoGBlxM */>}}
```

{{< youtube weLaDoGBlxM >}}

youtubeもidを入れるだけでページ内ビュワーが作られます。ショート動画は左右に暗幕が出来てしまうので、あまり見栄えが良くないかも。

{{< youtube id="wZmKzg-LceE" title="bayashiさんのショート動画" >}}

## 自分で追加したショートコード

### message box

```
{{%/* hint info */%}}
Info box.
{{%/* /hint */%}}

{{%/* hint warning */%}}
Warning box.
{{%/* /hint */%}}

{{%/* hint danger */%}}
Danger box.
{{%/* /hint */%}}

{{%/* hint normal */%}}
Normal box.
{{%/* /hint */%}}
```

{{% hint info %}}
Info box.P
{{% /hint %}}

{{% hint warning %}}
Warning box.
{{% /hint %}}

{{% hint danger %}}
Danger box.
{{% /hint %}}

{{% hint normal %}}
Normal box.
{{% /hint %}}

### blog-card

```
{{</* blog-card url="https://www.youtube.com" */>}}
```

{{<blog-card url="https://www.youtube.com" >}}

オシャンなblogカードが欲しくて過去に作ったもの。はてなのAPIを使って実装しています。

### accordion

```
{{</* accordion title="クリックで展開" >}}
{{< highlight python>}}
import pandas as pd
{{< /highlight >}}
{{< /accordion */>}}
```

{{< accordion title="クリックで展開" >}}
{{< highlight python>}}
import pandas as pd
{{< /highlight >}}
{{< /accordion >}}

[gkzz.devさんのブログ](https://gkzz.dev/posts/accordion-menu-hugo/)を参考にさせていただきました。

## スニペット

ショートコードの記法とは異なるが、html tagのようなスニペットが使える。

### mark
```
文章の中でも<mark>**特に強調したい部分**</mark>をハイライトできる。
```

文章の中でも<mark>**特に強調したい部分**</mark>をハイライトできる。


### sub, sup

```
文章の中で<sub>下付き</sub>や<sup>上付き</sup>を使うことが出来る。
```

文章の中で<sub>下付き</sub>や<sup>上付き</sup>を使うことが出来る。


### kbd

```
<kbd>Ctrl</kbd>キーを押しながら<kbd>C</kbd>を押す
```

<kbd>Ctrl</kbd>キーを押しながら<kbd>C</kbd>を押す