from django.core.serializers import serialize
from django.core import serializers
from django.http import JsonResponse
import json
from model.models import CardSets
from utils.data import *

def convert_json_to_dict(data):
    return json.loads(data)

def handle_negative_keywords(negativeKeyword, listingsData):
    neg_indexes = []
    negativeKeyword.lower()
    for index, item in enumerate(listingsData):
        title = item["title"][0].lower() # need to do error handling here
        if negativeKeyword in title.lower():
            neg_indexes.append(index)
    return neg_indexes



# handle search param - tokenisaiont? break down the param into keywords?

# Test 1: find variation, grading company and grade (required parameters)
def find_keywords(sentence, keywords_list):
    words = sentence.lower()
    for keyword in keywords_list:
        if keyword not in words:
            print("keyword not in words: ", keyword, words)
            return False
    return True

def find_which_keywords_exists(sentence, keywords_list):
    words = sentence.lower()
    for keyword in keywords_list:
        if keyword in words:
            return keyword
    return False

# def remove_keywords(sentence, keywords_list):
#     words = sentence.split()
#     new_sentence = []
#     for word in words:
#         if word not in keywords_list:
#             new_sentence.append(word)
#     return ' '.join(new_sentence)

# function to return true if all keywords that in the sentence
def filter_keywords(paramSearchQuery, sentence, param, company_and_grade, variation):
    # find out what psa number exist in search query
    query_grade = find_which_keywords_exists(paramSearchQuery, company_and_grade)

    grade_condition_keyword = find_which_keywords_exists(sentence, company_and_grade)
    variation_keyword = find_which_keywords_exists(sentence, variation)
    proceed = False # determine if code should break or proceed
    # must have holo & !reverse holo & PSA & 9
    if (grade_condition_keyword != False and variation_keyword != False): 
        proceed = True

    if (proceed == True):
        # make pokemon api calls and find ... add later
        # extract 3 values from param
        paramList = [param["name"], param["number"], param["set"]["printedTotal"]]
        paramList = [str(num).lower() for num in paramList] # lowercase and convert to string
        print(paramList)
        # test these 3 parameters exist in sentence: name, number, set.printedTotal
        proceed = find_keywords(sentence, paramList)
        print(proceed)
        return proceed # return true if all keywords exist in sentence
    else:
        return False

def main_filter_keywords(listingsData, param):
    paramObj = param["searchObj"]
    paramSearchQuery = param["search"]
    ebay_Id_filtered = []
    for index, item in enumerate(listingsData):
        title = item["title"][0].lower()
        # if 
        if (filter_keywords(paramSearchQuery, title, paramObj, company_and_grade, variation) == True):
            ebay_Id_filtered.append(item["itemId"][0])
    return ebay_Id_filtered


card_sets1 = CardSets.objects.all()[:1] # get the first object in the db
card_sets1 = serializers.serialize("python", card_sets1) # convert to python object
# print(card_sets1)
# print(card_sets1[0]["fields"])
card_sets1 = card_sets1[0] # get the fields from the first object in the list
# for cardset in card_sets1:
#     print(cardset)

# print(filter_keywords("charizard xy evolutions holofoil reverse holo PSA 9"))