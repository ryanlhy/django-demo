# def handle_negative_keywords(negativeKeyword, originalData):
#     neg_indexes = []
#     for index, item in enumerate(originalData):
#         title = item["title"][0].lower() # need to do error handling here
#         if negativeKeyword in title.lower():
#             neg_indexes.append(index)
#     # append the arr to the originalData
#     originalData.append({"negativeKeyword": neg_indexes})
#     print(originalData)
#     return originalData