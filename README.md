# hashed font

## 概要

指定したTrueTypeフォントを使って
使用可能な文字をすべて0〜9(U+0030〜U+0039)が表す字形のどれかに
マッピングしたTrueTypeフォントを生成します。

pythonとfonttoolsが必要。

## 使用例

```
$ pip install -r requirements.txt
$ python make_hashed_font.py -i mplus-2-reqular.ttf -o out.ttf -s salt
input: mplus-2p-regular.ttf
wrote: out.ttf
```

```
$ python make_hashed_font.py -h
usage: make_hashed_font.py [-h] [-v] -i INPUT_TTF_PATH [-s SALT]
                           [-o OUTPUT_TTF_PATH]

make a hashed font from TrueType font

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INPUT_TTF_PATH, --input INPUT_TTF_PATH
                        input TTF file path
  -s SALT, --salt SALT  salt sting [default: SALT]
  -o OUTPUT_TTF_PATH, --output OUTPUT_TTF_PATH
                        output TTF file path [default: out.ttf]
```

## 仕様

マッピングを一意にするために、SHA256と指定したソルトを利用して
ある文字を0〜9のどれにマッピングするかを決定します。

したがって、同じソルトを指定すればマッピングは一意に決まります。

## 参考

サンプルとして[M+FONT](http://mplus-fonts.osdn.jp)を使用させていただきました。
