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

    もしPythonがインストールされていなければ、以下の手順でインストールできます。

   #### *Homebrewのインストール*

    まず、Homebrewをインストールします。ターミナルで以下のコマンドを実行します。

    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```
   #### *Pythonのインストール*
    Homebrewをインストールしたら、以下のコマンドでPythonをインストールします。
    ```
    brew install python
    ```
 ### 2. 必要なライブラリのインストール
 subprocessライブラリはPythonの標準ライブラリなので、追加のインストールは不要です。

 ### 3. Pythonスクリプトの準備
 以下のPythonスクリプトをテキストエディタ（例: VSCode、Sublime Text、Atom）にコピーし、ファイルとして保存します。例: system_info.py

 ### 4. スクリプトの実行
 ターミナルで上記ファイル（スクリプト）が保存されているディレクトリに移動し、以下のコマンドを実行します。
  ```
  python3 system_info.py
  ```
 ### 5. スクリプトの実行結果
 スクリプトが実行されると、以下のようにシステム情報が表示されます。

  ```
  Hardware Overview:
  Processor Name: Intel Core i7
  Memory: 16 GB
  Serial Number: ABC123XYZ
  ```
 以上が、macOS環境でシステム情報を取得するPythonスクリプトを実行するための具体的な手順です。
