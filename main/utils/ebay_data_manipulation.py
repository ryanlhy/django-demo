from django.core.serializers import serialize
from django.core import serializers
from django.http import JsonResponse
import json
from model.models import CardSets


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

keywords = ["holofoil", "reverse holo", "1st edition", "1st ed", "1st"]


# Test 1: find variation, grading company and grade (required parameters)
def find_keywords(sentence, keywords_list):
    words = sentence.lower()
    for keyword in keywords_list:
        if keyword not in words:
            return False
    return True

def remove_keywords(sentence, keywords_list):
    words = sentence.split()
    new_sentence = []
    for word in words:
        if word not in keywords_list:
            new_sentence.append(word)
    return ' '.join(new_sentence)



def main_filter_keywords(sentence, query):

    # check if pass the first test. 
    keywords = ["holofoil", "psa 9",]
    proceed = False # determine if code should break or proceed
    # must have holo & !reverse holo & PSA & 9
    proceed = find_keywords(sentence, keywords)
    if (proceed == True):

        # make pokemon api calls and find ... later stage
        # extract 3 values from query
        queryList = [query["name"], query["number"], query["set"]["printedTotal"]]
        # test these 3 parameters exist in sentence: name, number, set.printedTotal
        find_keywords(sentence, keywords)



card_sets1 = CardSets.objects.all()[:1] # get the first object in the db
card_sets1 = serializers.serialize("python", card_sets1) # convert to python object
print(card_sets1)
print(card_sets1[0]["fields"])
card_sets1 = card_sets1[0] # get the fields from the first object in the list
# for cardset in card_sets1:
#     print(cardset)

# print(main_filter_keywords("charizard xy evolutions holofoil reverse holo PSA 9"))