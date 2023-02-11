def handle_negative_keywords(negativeKeyword, listingsData):
    neg_indexes = []
    negativeKeyword.lower()
    for index, item in enumerate(listingsData):
        title = item["title"][0].lower() # need to do error handling here
        print(title)
        if negativeKeyword in title.lower():
            neg_indexes.append(index)
    return neg_indexes

# handle search query - tokenisaiont? break down the query into keywords?