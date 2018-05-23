"""
    This project is useful when you want to know about local time and weather
    of a city anywhere in the world. 
    User is asked to give the name of a city, then it provides local time and
    real-time weather of that city
    Program uses time and weather clients to read values and print it for you.

    Project teaches how to use API for web-scrapping and implement in
    practical use cases.

    Project uses https://www.wunderground.com/weather/// as a client to
    provide the information
"""
#To find short cut of a country
import pycountry
#To read contents of url
import requests
# To read text in the url
import bs4
#Printing output nicely
import collections

FinalWeatherReport = collections.namedtuple('FinalWeatherReport','localTime, location, weather_condition, temperature, temp_scale')
        


def main():
    print_header()
    get_user_and_client_data()


def print_header():
    print ()
    print ("################################################")
    print ("############# Tell me weather and time #########")
    print ("################   for a city    ###############")
    print ("################################################")
    print ()

def get_user_and_client_data():
    print ("This application provides weather and local time of city you provide. Pleas provide full name of city or state. If there are spaces between words please connect them with hyphen (-)" )
    city= input("Please enter name of CITY: ")
    country= input("Please enter name of COUNTRY or STATE: ")
    # city= "Austin"
    #country = "Texas"
    #Country code short cut. It is possible due to pycountry library
    #This is because the targeted URL uses the country and city in this format
    #https://www.wunderground.com/weather/US/AUSTIN
    mapping = {country.name: country.alpha_2 for country in pycountry.countries}
    country_code = mapping.get(country)
    if country_code is None:
        country_code= country
    #Weather and time client
    url=("https://www.wunderground.com/weather/{}/{}".format(country_code,city)) 
    print (url)
    #Read the url and find the values:
    url_content =requests.get(url)
    html= url_content.text
    """ To read the text of the content """
    #print (url_content.text[0:400])

    # cityCss = '.region-content-header find('h1')
    # weatherScaleCss = '.wu-unit-temperature find('class_.wu-label')
    # weatherTempCss = '.wu-unit-temperature find('class_.wu-value')
    # weatherConditionCss = '.condition-icon'

    b_soup = bs4.BeautifulSoup(html, 'html.parser')
    localTime=b_soup.find(class_="timestamp").get_text().split('|')[0].split(" ")
    localTime_formatted = localTime[1]+" "+localTime[2]+ " " +localTime[5]+ " "+ localTime[6]+ " "+ localTime[7]
    location = b_soup.find(class_='region-content-header').find('h1').get_text()
    weather_condition = b_soup.find(class_='condition-icon').get_text()
    temperature = b_soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    temp_unit = b_soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    location= remove_white_space(location) 
    weather_condition= remove_white_space(weather_condition)
    temperature= remove_white_space(temperature)
    temp_unit = remove_white_space(temp_unit)


    finalReport =FinalWeatherReport(localTime=localTime_formatted, location=location, weather_condition=weather_condition, temperature=temperature, temp_scale=temp_unit)
    #print (finalReport)

    print ()
    print ("--------------------------------------")
    print ("         ",finalReport.location,"    ")
    print ("        ","Time & Weather","            ")
    print ("--------------------------------------")
    print ("Date & Time :  {}".format(finalReport.localTime))
    print ("Temperature :  {} {}".format(finalReport.temperature,finalReport.temp_scale))
    print ("Weather Condition :  {}".format(finalReport.weather_condition))
    print ("--------------------------------------")
    print ()

def remove_white_space(text_string):
    #Remove white space in left and right of the text if there is 
    text_string= text_string.strip()
    return text_string



if __name__=="__main__":
    main()
