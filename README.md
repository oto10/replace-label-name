## replace-label-name

labelmeで作成したCOCO形式のアノテーションファイルにおける特定のラベル名を変更します。

## 使い方

- COCO形式のアノテーションファイルが格納されたフォルダパスを設定してください。
- 変更前のラベル名（pre-label-name）と変更後のラベル名（post-label-name）を指定して以下のコードを実行すると、先程指定したフォルダに格納されたアノテーションファイルのラベル名が「pre-label-name」から「post-label-name」になります。

```
$ python replace_label.py [pre-label-name] [post-label-name]
```