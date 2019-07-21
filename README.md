# mean-of-brightness-

・使い方
jupyter notebook上でソースコードを「shift+Enter」で実行する。
次に、webカメラ（ノートpcのカメラ）が起動するので、そのカメラに映る画像の平均値が、毎フレームごとにノートブック上に出力されていく。
最後に、「Enter」を押すと、カメラが停止し、輝度値の平均値のグラフが出力される。



・ライブラリー・モジュールのバージョン
- python3:version 3.72
- jupyter notebook:version 5.74
- numpy:version 1.154
- matplotlib:version 3.02
- opencv:version 3.42


・実行の様子
ソースコードをjupyter notebookで実行し、カメラに指をのせる。
そして毎フレームごとの画像の輝度の平均値が表示され、Enterキーを押してカメラを停止させると輝度の平均値のグラフが表示される。

![mean-brightness](https://user-images.githubusercontent.com/48341900/61589868-47b1a700-abeb-11e9-89f6-ff62b84beb75.gif)

・参考にしたサイト
 - OpenCVで監視カメラを自作してみよう：https://news.mynavi.jp/article/zeropython-35/
 「Webカメラをセットアップしよう」という項目を参考にした。とくにソースコードに関してはシンプルで扱いやすく、
 
