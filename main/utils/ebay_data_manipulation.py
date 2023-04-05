from django.core.serializers import serialize
from django.core import serializers
from django.http import JsonResponse
import json
from model.models import CardSets
from utils.data import variation, grading_company, grades, combine_grade, company_and_grade, special_characters
from services.ebay_api_services import get_data_from_ebay_api

# define global variables where loops are needed to retrieve data - prevent duplicate calls


def remove_special_characters(sentence):
    # print("sentence: ", sentence)
    for character in special_characters:
        sentence = sentence.replace(character, "")
    return sentence


def convert_json_to_dict(data):
    return json.loads(data)


def handle_negative_keywords(negativeKeyword, listingsData):
    if listingsData == None:
        return []
    neg_indexes = []
    negativeKeyword.lower()
    for index, item in enumerate(listingsData):
        title = item["title"][0].lower()  # need to do error handling here
        if negativeKeyword in title.lower():
            neg_indexes.append(index)
    return neg_indexes

# Test 1: find variation, grading company and grade (required parameters)


def find_keywords(sentence, keywords_list):
    words = sentence.lower()
    for keyword in keywords_list:
        if keyword not in words:
            # print("keyword not in words: ", keyword, words)
            return False
    return True


def find_which_keywords_exists(sentence, keywords_list1):
    words = sentence.lower()
    for keyword in keywords_list1:
        if (keyword in words):
            return keyword  # not sure why function is not breaking out of loop
    return False

# def remove_keywords(sentence, keywords_list):
#     words = sentence.split()
#     new_sentence = []
#     for word in words:
#         if word not in keywords_list:
#             new_sentence.append(word)
#     return ' '.join(new_sentence)

# function to return true if all keywords that in the ebay_title


def filter_keywords(param_search_query, ebay_title, param, company_and_grade, variation, ebay_id):
    keywords_list_response = []  # list of keywords that are in the sentence/query

    # find out what psa number exist in search query (not in use yet)
    # query_grade = find_which_keywords_exists(param_search_query, company_and_grade)

    grade_condition_keyword = find_which_keywords_exists(
        ebay_title, company_and_grade)
    # if grade_condition_keyword does not exist in keywords_list_response, then append
    keywords_list_response.append(grade_condition_keyword)
    if grade_condition_keyword == False:
        grade_condition_keyword = 'Raw'

    # find out what variation exist in search query (not in use yet).
    # edge case: only 1 can exist,
    # variation_keyword = find_which_keywords_exists(ebay_title, variation)

    proceed = False  # default to false, if all keywords exist in ebay_title, then return true
    # determine exact match .. must match all required variables (not implemented fully yet)
    if (grade_condition_keyword != False):
        # make pokemon api calls and find ... add later
        # extract 3 values from param
        param_list = [param["name"], param["number"],
                      param["set"]["printedTotal"]]
        # lowercase and convert to string
        param_list = [str(num).lower() for num in param_list]
        # print(param_list)
        # test these 3 parameters exist in ebay_title: name, number, set.printedTotal
        keywords = find_keywords(ebay_title, param_list)
        return {
            "keywords": keywords,
            "keyword_list": {grade_condition_keyword: [ebay_id]},
            # "keyword_list":keywords_list_response
        }  # return true if all keywords exist in ebay_title, and the keywords that exist in the ebay_title
    else:
        return {
            "keywords": False,
            "keyword_list": {}
        }


def main_match_exact_keywords(ebay_data, param):
    param_obj = param["searchObj"]
    param_search_query = param["search"]
    # ebay_id = param["searchObj"]["itemId"][0]
    ebay_id_filtered = []
    keywords_list_response = {}  # list of keywords that are in the sentence/query

    for index, item in enumerate(ebay_data):
        title = item["title"][0].lower()
        ebay_id = item["itemId"][0]
        # if consist of all keywords, then append to ebay_id_filtered
        filter_keywords_result = filter_keywords(
            param_search_query, title, param_obj, company_and_grade, variation, ebay_id)
        if (filter_keywords_result["keywords"] == True):
            ebay_id_filtered.append(item["itemId"][0])
            # check if key in filter_keywords_result["keyword_list"] exists in keywords_list_response dictionary

            # if it does, then append the ebay_id to the list
            # if it does not, then create a new key and append the value which is ebay_id to the list
            for key in filter_keywords_result["keyword_list"]:
                keywords_list_response.setdefault(key, []).append(ebay_id)

            # if filter_keywords_result["keyword_list"] not in keywords_list_response:
            # keywords_list_response += (filter_keywords_result["keyword_list"])
    # print("ebay_id_filtered:")
    # print(ebay_id_filtered)
    return {"ebay_id_filtered": ebay_id_filtered, "keywords_list_response": keywords_list_response}

# function that returns a list of keywords that exist in the ebay_title

# function that returns a list of negative keywords

# function that collate the responses and returns to views.py


def main_response_data_handler(param):
    # print(param["search"])
    # print(type(param["search"]))
    search_param = remove_special_characters(str(param["search"]))
    # print("search_param: ", search_param)
    ebay_data = get_data_from_ebay_api(search_param)
    keywords_list_response = []  # list of keywords that are in the sentence/query
    # check if "searchObj" is in param aka the FE is sending the searchObj
    if "searchObj" in param:
        filter_keywords_result = main_match_exact_keywords(ebay_data, param)
        # filter the data
        exact_match = filter_keywords_result["ebay_id_filtered"]
        keywords_list_response = filter_keywords_result["keywords_list_response"]
        print("keywords_list_response: ", keywords_list_response)
    else:
        # need to create another function that deals with the data without the searchObj
        exact_match = []

    # dictionary object that returns the data
    data = {
        "ebayData": ebay_data,
        "filterCalls": {
            "keywordsListResponse": keywords_list_response,
            "exactMatch": exact_match
        },
    }
    return data

# card_sets1 = CardSets.objects.all()[:1] # get the first object in the db
# card_sets1 = CardSets.objects.all() # get the first object in the db
# card_sets2 = serializers.serialize("python", card_sets1) # convert to python object
# print(card_sets2)
# print(card_sets1[0]["fields"])
# print("printing")
# card_sets1 = card_sets1[0] # get the fields from the first object in the list


# for cardset in card_sets1:
#     print(cardset)

# print(filter_keywords("charizard xy evolutions holofoil reverse holo PSA 9"))
