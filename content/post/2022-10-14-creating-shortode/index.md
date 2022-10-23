---
title: Hugoのショートコードを作る
description: "メッセージボックスを作る"
author: Snitch
date: "2022-10-14"
categories:
  - Hugo
tags:
  - hugo
format: hugo
slug: creating-hugo-shortcode
jupyter: python3
html-math-method: webtex
---


## 完成形

`info`, `warning`, `danger`, `normal`を用意。

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

## 作り方

{{< blog-card url=http://oostens.me/posts/hugo-hint/quote-shortcode/ >}}

全面的にNelis Oostens氏のコードをThe Unilicenseのもとで利用させていただいています。

### `layouts/shortcodes/hint.html`

Hugoのショートコードではどのテーマを利用しているかに関わらず、`layouts/shortcodes`がショートコードの定義ファイルの置き場であり、ファイル名(この場合は`hint`)がショートコード名になります。

```html {name="hint.html"}
{{ $type := .Get 0 }}
{{ printf "<blockquote class=\"md-hint %s\">" $type | htmlUnescape | safeHTML }}
{{ .Inner | safeHTML }}
{{ printf "</blockquote>" | htmlUnescape | safeHTML }}
```

### `theme/**/assets/scss/custom.scss`

scssにてcssを定義します。記述すべき場所はテーマによって違うと思います。
私が使用している[Stack theme]()では`theme/hugo-theme-stack/assets/scss/custom.scss`です。

冒頭紹介した参考記事では、カラーコードをどこかの変数から取ってきているようですが、参照すべきその変数が記事内には書かれていなかったのでハードコードしました。
Windows PowerToysのカラーピッカーを使用してちまちまとカラーピック。


```css {name="custom.scss"}
.md-hint {
    &.info {
        border-left-color: rgba(102, 187, 255, 1);
        background-color: rgba(102, 187, 255, 0.25);
    }

    &.warning {
        border-left-color: rgba(255, 221, 102, 1);
        background-color: rgba(255, 221, 102, 0.25);
    }

    &.danger {
        border-left-color: rgba(255, 102, 102, 1);
        background-color: rgba(255, 102, 102, 0.25);
    }

    &.normal {
        border-left-color: rgba(91, 93, 94, 1);
        background-color: rgba(91, 93, 94, 0.05);
    }
}
```


## あとは使うだけ!

以下のようにして使います。

```
{{%/* hint info */%}}
Info box.
{{%/* /hint */%}}
```

HugoではGo言語がバックエンドなので、ショートコードの作り方はややGoっぽい特殊な書き方です。
ただまあ･･･PHPよりは簡単なのかな。