import requests
from main.settings import ebay_app_id as appId
# from main.utils.ebay_data_manipulation import handle_negative_keywords

keyword = "charizard psa 10"
maxEntries = 10
#https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME={appid}&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&paginationInput.entriesPerPage=100&keywords=pikachu%22
def get_data_from_ebay_api(keyword, maxEntries=100):
    url = (
        "https://svcs.ebay.com/services/search/FindingService/v1?"
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
            # data = json.loads(response.text) #deserialise the data
            if "findItemsByKeywordsResponse" in data:
                if data["findItemsByKeywordsResponse"][0]["searchResult"][0]["@count"] == "0": # zero results returned
                    return []
                listings = data["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]
                # listings = handle_negative_keywords("cgc", listings)
                return listings
                # return data
            else:
                raise Exception("Error: Invalid response data")
        else:
            raise Exception("Error: Invalid response status code")
    except Exception as e:

        return e

# def handle_negative_keywords(negativeKeyword, listingsData):
#     neg_indexes = []
#     negativeKeyword.lower()
#     for index, item in enumerate(listingsData):
#         title = item["title"][0].lower() # need to do error handling here
#         print(title)
#         if negativeKeyword in title.lower():
#             neg_indexes.append(index)
#     return neg_indexes