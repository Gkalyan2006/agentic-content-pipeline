
import requests

TAVILY_KEY = "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"

def research_agent(topic):

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_KEY,
        "query": topic,
        "max_results": 6
    }

    try:
        response = requests.post(url, json=payload, timeout=20)

        if response.status_code != 200:
            print("Tavily API Error")
            return topic   # fallback

        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            print("No research results found")
            return topic   # fallback

        results = ""

        for item in data["results"]:
            results += item.get("content", "") + "\n"

        return results

    except Exception as e:
        print("Research agent failed:", e)
        return topic   # fallback

