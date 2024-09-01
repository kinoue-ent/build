# 制作した課題概要

 ## python課題１

  ### 製作者の当時の環境実行
  　実行環境
   
   ```
　　　   MacOS version
     - MacOS 14.4.1
    python3 version
     -　Python 3.9.6
   ```

  ### 1. Pythonのインストール確認
   macOSには通常Pythonがプリインストールされていますが、念のため確認します。ターミナルを開いて以下のコマンドを実行します。

   #### *pythonがインストールされているか確認*
   
```
    python3 --version
```
</bn>
    もしPythonがインストールされていなければ、以下の手順でインストールできます。

   #### *Homebrewのインストール*

    まず、Homebrewをインストールします。ターミナルで以下のコマンドを実行します。

```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
</bn>

   #### *Pythonのインストール*
    Homebrewをインストールしたら、以下のコマンドでPythonをインストールします。
    
```
    brew install python
```
</bn>

 ### 2. 必要なライブラリのインストール
 subprocessライブラリはPythonの標準ライブラリなので、追加のインストールは不要です。

 ### 3. Pythonスクリプトの準備
 以下のPythonスクリプトをテキストエディタ（例: VSCode、Sublime Text、Atom）にコピーし、ファイルとして保存します。例: system_info.py

 ### 4. スクリプトの実行
 ターミナルで上記ファイル（スクリプト）が保存されているディレクトリに移動し、以下のコマンドを実行します。
 
```
  python3 system_info.py
```
</bn>

 ### 5. スクリプトの実行結果
 スクリプトが実行されると、以下のようにシステム情報が表示されます。

```
  Hardware Overview:
  Processor Name: Intel Core i7
  Memory: 16 GB
  Serial Number: ABC123XYZ
```
</bn>
 以上が、macOS環境でシステム情報を取得するPythonスクリプトを実行するための具体的な手順です。



 ## python課題2

  ### 製作者の当時の環境実行
  　実行環境
   
```
   　　MacOS version
     - MacOS 14.4.1
    python3 version
     -　Python 3.9.6
```
</bn>

  ### 1. Pythonのインストール確認
   macOSには通常Pythonがプリインストールされていますが、念のため確認します。ターミナルを開いて以下のコマンドを実行します。

   #### *pythonがインストールされているか確認*
   
```
    python3 --version
```
</bn>
    もしPythonがインストールされていなければ、以下の手順でインストールできます。

   #### *Homebrewのインストール*

    まず、Homebrewをインストールします。ターミナルで以下のコマンドを実行します。

```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
</bn>

   #### *Pythonのインストール*
    Homebrewをインストールしたら、以下のコマンドでPythonをインストールします。
    
```
    brew install python
```
</bn>

 ### 2. 必要なライブラリのインストール
 subprocessライブラリはPythonの標準ライブラリなので、追加のインストールは不要です。

 ### 3. Pythonスクリプトの準備
 以下のPythonスクリプトをテキストエディタ（例: VSCode、Sublime Text、Atom）にコピーし、ファイルとして保存します。例: system_info.py

 ### 4. 実行方法
コードの保存

上記のPythonコードをテキストエディタにコピーし、weather_forecast.py という名前で保存します。
APIキーの設定

YOUR_API_KEY の部分を、OpenWeatherMapから取得したAPIキーに置き換えます。
スクリプトの実行

ターミナル（またはコマンドプロンプト）を開き、スクリプトが保存されたディレクトリに移動します。
bash
コードをコピーする
cd /path/to/directory
以下のコマンドでスクリプトを実行します。
bash
コードをコピーする
python weather_forecast.py
都市名の入力

プログラムが実行されると、天気情報を取得したい都市名を入力するよう求められます。例えば「Tokyo」や「Osaka」と入力します。

### 結果の確認

```
#プログラムの実行 プログラムを実行すると、まず次のように都市名の入力が求められます。

#天気情報を取得したい都市名を入力してください: Tokyo
#都市名の入力 Tokyo と入力してEnterキーを押します。

#出力結果 天気情報が正常に取得できた場合、次のような情報が出力されます。

都市: Tokyo
天気: 曇り
気温: 22.5℃
湿度: 60%
風速: 3.1m/s

#都市名が間違っている場合

天気情報を取得したい都市名を入力してください: InvalidCity
Error: 404
天気データを取得できませんでした。
```

入力した都市の天気情報が表示されます。表示される情報には、都市名、天気の説明、気温、湿度、風速が含まれます。

--------------------以下はまだ未作成--------------------

4. 応用課題
1. 複数都市の天気情報取得

複数都市の天気情報を取得し、一括で表示するには、リストを使用して複数の都市を指定し、ループでAPIリクエストを送ることで実現できます。
2. データの保存

csvモジュールを使用して、取得した天気情報をCSVファイルに保存できます。
3. グラフの作成

matplotlibライブラリを使って、取得した天気データをグラフ化することも可能です。例えば、複数の都市の気温を棒グラフで比較することが考えられます。
