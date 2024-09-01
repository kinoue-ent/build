import requests

def get_weather_data(city_name, api_key):
    """
    指定された都市の天気データをOpenWeatherMap APIから取得する。
    """
    # OpenWeatherMapのAPIエンドポイント
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # APIリクエストのパラメータ
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # 摂氏温度を取得
        'lang': 'ja',       # 日本語の天気説明を取得
    }
    
    # APIリクエストを送信
    response = requests.get(base_url, params=params)
    
    # レスポンスのステータスコードを確認
    if response.status_code == 200:
        # 成功した場合、JSONデータを返す
        return response.json()
    else:
        # 失敗した場合、エラーメッセージを表示してNoneを返す
        print(f"Error: {response.status_code}")
        return None

def display_weather_data(weather_data):
    """
    取得した天気データを表示する。
    """
    if weather_data:
        city = weather_data['name']
        weather_desc = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        
        print(f"都市: {city}")
        print(f"天気: {weather_desc}")
        print(f"気温: {temperature}℃")
        print(f"湿度: {humidity}%")
        print(f"風速: {wind_speed}m/s")
    else:
        print("天気データを取得できませんでした。")

def main():
    # OpenWeatherMap APIキーを入力してください
    api_key = "YOUR_API_KEY"  # 取得したAPIキーに置き換えてください
    
    # ユーザーに都市名を入力させる
    city_name = input("天気情報を取得したい都市名を入力してください: ")
    
    # 天気データを取得
    weather_data = get_weather_data(city_name, api_key)
    
    # 天気データを表示
    display_weather_data(weather_data)

if __name__ == "__main__":
    main()
