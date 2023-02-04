# services.py
import requests

def get_data_from_api(set_name):
    # url = f"https://api.pokemontcg.io/v2/cards?q=set.id:{set_name}&page=1&pageSize=2"
    url = f'https://api.pokemontcg.io/v2/cards?q=name:"*{set_name}*"&page=1&pageSize=2'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API request failed with status code: ", response.status_code)

# # views.py
# from .services_tcg import get_data_from_api

# def my_view(request):
#     data = get_data_from_api()
#     # Use the data to render the response
#     return render(request, "template.html", {"data": data})
