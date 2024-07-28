# 課題１

import subprocess  # システムコマンドの実行に使用します
import json  # JSONデータの処理に使用します

def get_system_info():
    """
    system_profilerコマンドを実行してハードウェアデータをJSON形式で取得し、
    必要な情報を抽出して表示する関数。
    """
    # system_profilerコマンドを実行してハードウェアデータをJSON形式で取得
    process = subprocess.run(['system_profiler', 'SPHardwareDataType', '-json'], capture_output=True, text=True)
    
    # 実行結果の標準出力をJSON形式で読み込み
    system_info = json.loads(process.stdout)
    
    # "SPHardwareDataType"キーからハードウェア概要を取得
    # 結果が空の場合に備えて、デフォルトで空の辞書リストを返す
    hardware_overview = system_info.get('SPHardwareDataType', [{}])[0]
    
    # プロセッサ名を取得。キーが存在しない場合は 'N/A' を使用
    processor_name = hardware_overview.get('cpu_type', 'N/A')
    
    # メモリ情報を取得。キーが存在しない場合は 'N/A' を使用
    memory = hardware_overview.get('physical_memory', 'N/A')
    
    # シリアル番号を取得。キーが存在しない場合は 'N/A' を使用
    serial_number = hardware_overview.get('serial_number', 'N/A')
    
    # 取得したハードウェア情報を表示
    print("Hardware Overview:")
    print(f"Processor Name: {processor_name}")
    print(f"Memory: {memory}")
    print(f"Serial Number: {serial_number}")

# スクリプトが直接実行された場合、get_system_info関数を呼び出す
if __name__ == "__main__":
    get_system_info()
