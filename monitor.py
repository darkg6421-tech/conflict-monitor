import requests
import time

# Yahan apni NewsAPI key dalein
API_KEY = 'e2eb1ed6e1e349e3a0f061ef1975364a'
URL = f'https://newsapi.org/v2/everything'

def fetch_real_news():
    # Hum specific keywords search kar rahe hain: Israel, Iran, Dimona, Nuclear
    params = {
        'q': 'Israel OR Iran OR Dimona OR Nuclear',
        'sortBy': 'publishedAt',
        'language': 'en',
        'apiKey': API_KEY
    }
    
    try:
        response = requests.get(URL, params=params)
        data = response.json()
        
        if data['status'] == 'ok':
            articles = data['articles'][:5] # Sirf top 5 latest news
            print(f"\n--- Latest Security Updates ({time.ctime()}) ---")
            for i, art in enumerate(articles, 1):
                print(f"{i}. {art['title']}")
                print(f"   Source: {art['source']['name']}")
                print(f"   Link: {art['url']}\n")
        else:
            print("Error fetching news.")
    except Exception as e:
        print(f"Connection Error: {e}")

# Yeh loop har 10 minute (600 seconds) mein automatic update karega
while True:
    fetch_real_news()
    print("Waiting for next update... Press Ctrl+C to stop.")
    time.sleep(600) 
