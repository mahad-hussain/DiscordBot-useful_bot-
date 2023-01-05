import requests

"""
Returns the new value of the money based on the currency stated and the previous currency using Frankfurter API
@param from_coun (str): the original currency
@param to_coun (str): the new currency
@param amount (int): the original amount of money
"""
def convert(from_coun, to_coun, amount):
    #gets the correct casing for the inputs
    from_coun = from_coun.upper()
    to_coun = to_coun.upper()

    #request to API
    response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_coun}&to={to_coun}")
    

    return(f"{amount} {from_coun} is {response.json()['rates'][to_coun]} {to_coun}")


"""
Returns the definition of a word using the dictionary API
@param word (str): the word that needs defining
"""
def definition(word):
    #request to the API
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    #gets Two definitions
    try:
        definition_one = (response.json()[0]['meanings'][0]['definitions'][0]['definition'])
    except Exception as e:
        print(e)

    try:
        definition_two = (response.json()[0]['meanings'][1]['definitions'][0]['definition'])
    except Exception as e:
        print(e)
    
    return f"The word '{word}' means {definition_one} Another defintion is {definition_two}"


"""
Returns Synonyms of a word using the dictionary API
@param word (str): the word that needs synonyms
"""
def synonyms(word):

    #requests
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    #Goes through the JSON file to get the synonyms, makes sure the array isn't empty
    count = 0
    check = True
    try:
        while(check):
            synonym = (response.json()[0]['meanings'][count]['synonyms'])
            if len(synonym) != 0:
                check = False
            else:
                count+=1

    except Exception as e:
        print(e)

    res = ""
    
    #formats thee array
    for i, syn in enumerate(synonym):
        res+=(f"->{i+ 1}. {syn} ")

    return f"Synoynms for '{word}' are: {res}"
