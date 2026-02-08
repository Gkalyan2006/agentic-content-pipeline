import requests
from requests.auth import HTTPBasicAuth
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
WP_URL = "https://saiagent.local/wp-json/wp/v2/posts"
WP_USER = "sairam"
WP_APP_PASSWORD = "TO1UeXeQ WlAM4T4DvRhOuSwY"

def publish_agent(title, content):

    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    response = requests.post(
        WP_URL,
        auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD),
        json=data,verify=False
    )

    if response.status_code == 201:
        print(" Article published successfully!")
    else:
        print(" Publish failed:", response.text)
