##  PlantUML
- option + Dでプレビュー表示

## 参考リンク
https://qiita.com/ogomr/items/0b5c4de7f38fd1482a48

https://qiita.com/nirperm/items/2b5c6f39beb70448e6c1

下が読めればいいかも
http://doloopwhile.hatenablog.com/entry/20110207/1297068455


## パッケージ類(strategyより追加)
- flake8
  - flake8 --show-source たーげっと.py 
- mypy
  - mypy check_type.py 
  - https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
- autopep8
  - autopep8 -i url.py

## まとめ
- 全体：IFを作ってやることや流れと実際の挙動をわける！（カプセル化）
- 2 adapter: IFに名前をあわせて、昔のメソッド呼ぶかかりをつくる
- 3 template: 継承で差分プログラミング
- 4 factory method: 継承で差分プログラミング２。IFで作る人の関係を書いておいて、実装は子で。
  今回ならインスタンス作って、登録するの流れはIFがもっていて、中身を子がメソッドとして実装している
- 6 prototype: インスタンスコピーして、状態を独自に変えたいとき
- 7 builder: 大きい１つのインスタンスを組み合わせでつくろう！
  DirectorがBuilderに対してやってほしい具体的な値をもっていて、Builderはどう実現するかをサブクラスで表現
  Mainがどっちの分岐を使うかを決める、みたいな
- 9 bridge: 機能一覧と実装一覧をわける。関係をIFで定義しておいて、サブクラスで具体的にかく
  機能はラッパークラスをサブクラスに書いていく感じ。機能は実装を持っていて、委譲する
