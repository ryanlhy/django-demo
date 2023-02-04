import requests
from main.settings import ebay_app_id as appId
import cors

keyword = "charizard psa 10"
maxEntries = 10
#https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={appid}&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&paginationInput.entriesPerPage=100&keywords=pikachu%22
def get_data_from_ebay_api(keyword, maxEntries=10):
    url = (
        "http://svcs.ebay.com/services/search/FindingService/v1?"
        f"OPERATION-NAME=findItemsByKeywords&"
        f"SERVICE-VERSION=1.0.0&"
        f"SECURITY-APPNAME={appId}&"
        "RESPONSE-DATA-FORMAT=JSON&"
        "REST-PAYLOAD&"
        f"paginationInput.entriesPerPage={maxEntries}&"
        f"keywords={keyword}"
    )

    response = requests.get(url)
    try:
        if response.status_code == 200:
            data = response.json()
            if "findItemsByKeywordsResponse" in data:
                listings = data["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]
                return listings
                # return data
            else:
                raise Exception("Error: Invalid response data")
        else:
            raise Exception("Error: Invalid response status code")
    except Exception as e:
        return e
