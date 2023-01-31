import requests
from main.settings import ebay_app_id as appId

keyword = "charizard psa 10"
maxEntries = 10

def get_data_from_api(keyword, maxEntries):
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
            else:
                raise Exception("Error: Invalid response data")
        else:
            raise Exception("Error: Invalid response status code")
    except Exception as e:
        return e
