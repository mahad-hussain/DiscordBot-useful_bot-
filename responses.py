import random
import weather
import converter
import calculator


def get_response(message: str) -> str:

    #Changing the discord message to fit certain conditions
    p_message = message.lower()

    weatherarray = p_message.split('of')

    convertarray = p_message.split(" ")

    wordsarray = p_message.split("of")

    calculatearray = p_message.split("calculate")
    


    #checks if the message meets the correct requirements and returns a message based on what the user has typed
    if p_message == 'hello' or p_message == '/hello':
        return 'Hey there!, type `commands` or `/commands` to get started!'

    
    if p_message == 'coinflip' or p_message == '/coinflip':
        if random.randint(1,2) == 1:
            return "Heads!"  
        else: 
            return("Tails!")
    
    if weatherarray[0] == 'weather' or weatherarray[0] == '/weather':
        return weather.weathercity(weatherarray[1])
    
    if convertarray[0] == "convert" or convertarray[0] == '/convert':
        return converter.convert(convertarray[2], convertarray[4], float(convertarray[1]))
    
    if wordsarray[0] == 'definition' or wordsarray[0] == '/definition':
        return converter.definition(wordsarray[1])
    if wordsarray[0] == 'synonym' or wordsarray[0] == '/synonym':
        return converter.synonyms(wordsarray[1])
    
    if calculatearray[0] == "" or calculatearray[0] =="/":
        return calculator.calculate(calculatearray[1])
    
    #returns a message displaying the current commands the bot is capable of completing
    if p_message == "commands" or p_message == "/commands":
        return (f"""`Use commands in the birthday channel or put a \'/' infront of the commands to use in another channel. 
(put a ? infront of commands for private messages)\n 1. hello\t\t\t\n 2. coinflip\t\t\n 3. weatherof'city'\t\n 4. convert 'amount cur to cur'\t 
 5. definitionof'word'\t\n 6. synonymof'word'\t\n 7. calculate 'expression'\t`""")

    if p_message =='!help':
        return '`Try entering /commands or ask someone for help!`'
        

