# Objective: The aim of this assignment is to refactor an existing Python script for a weather
#forecast application into a more structured, object-oriented, and modular format. The focus
#will be on identifying parts of the script that can be encapsulated into classes and organizing
#these classes into appropriate modules to enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes: Analyze the provided script and identify distinct
#functionalities that can be encapsulated into classes. Create classes that represent different 
#aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

#Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

# Weather Forecast Application Script

#def fetch_weather_data(city):
    # Simulated function to fetch weather data for a given city
#    print(f"Fetching weather data for {city}...")
    # Simulated data based on city
#    weather_data = {
#        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
#        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
#        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
#    }
#    return weather_data.get(city, {})

#def parse_weather_data(data):
    # Function to parse weather data
#    if not data:
#        return "Weather data not available"
#    city = data["city"]
#    temperature = data["temperature"]
#    condition = data["condition"]
#    humidity = data["humidity"]
#    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

#def get_detailed_forecast(city):
    # Function to provide a detailed weather forecast for a city
#    data = fetch_weather_data(city)
#    return parse_weather_data(data)

#def display_weather(city):
    # Function to display the basic weather forecast for a city
#    data = fetch_weather_data(city)
#    if not data:
#        print(f"Weather data not available for {city}")
#    else:
#        weather_report = parse_weather_data(data)
#        print(weather_report)

#def main():
#    while True:
#        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#        if city.lower() == 'exit':
#            break
#        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#        if detailed == 'yes':
#            forecast = get_detailed_forecast(city)
#        else:
#            forecast = display_weather(city)
#        print(forecast)

#if __name__ == "__main__":
#    main()



class FetchData:                                                                                                                                   #defining class named FetchData
    def __init__(self, path):                                                                                                                      #initializing class    
        self.path = path                                                                                                                           #attribute

    def open_weather_data(self):                                                                                                                   #method for opening file
        try:                                                                                                                                       #try block to help with error handling
            with open(self.path) as file:                                                                                                          #opening file
                for line in file:                                                                                                                  #'for' loop cycling through each line of the file
                    city, temperature, condition, humidity = line.strip().split(",")                                                               #splitting each line up by based on commas and turning that into multiple variables
                    weather_data[city] = {"temperature": temperature, "condition": condition, "humidity": humidity}                                #creating a dictionary using the imported variables
        except FileNotFoundError:                                                                                                                  #except block for FileNotFoundError
            print("File not found.")                                                                                                               #print statement informing the user the file couldnt be found


class ParseData:                                                                                                                                   #defining class named ParseData
    def __init__(self, city, temperature, condition, humidity):                                                                                                 #intializing class
        self.__city = city                                                                                                                                      #private attribute
        self.__temperature = temperature                                                                                                                        #private attribute
        self.__condition = condition                                                                                                                            #private attribute
        self.__humidity = humidity                                                                                                                              #private attribute

    def get_city(self):                                                                                                                                         #getter for city
        return self.__city

    def get_temperature(self):                                                                                                                                  #getter for temperature
        return self.__temperature

    def get_condition(self):                                                                                                                                    #getter for condition
        return self.__condition

    def get_humidity(self):                                                                                                                                     #getter for humidity
        return self.__humidity    

    def get_weather_data(self):                                                                                                                                 #method to print wether data in an unformatted way
        print(f"\n{self.get_city()}, temperture: {self.get_temperature()}, condition: {self.get_condition()}, humidity: {self.get_humidity()}\n")               #print statement

    def get_detailed_report(self):                                                                                                                              #method to print weather datat in a formatted way
        print(f"\nCity: {self.get_city()}\nTemperature:{self.get_temperature()}\u00B0F\nCondition:{self.get_condition()}\nHumidity:{self.get_humidity()}\n")    #print statement
    

def create_parse_dictionary(city):                                                                                                                 #function to create a dictionary
    city_value = city
    city_key = city
    city_value = ParseData(city, weather_data[city]["temperature"], weather_data[city]["condition"], weather_data[city]["humidity"])               #creating a ParseData class object
    parsed_data[city_key] = city_value                                                                                                             #creating dictionary of ParseData class objects

   
weather_data = {}                                                                                                                                  #setting up empty dictionary named weather_data
parsed_data = {}                                                                                                                                   #setting up empty dictionary named parsed_data


def main():                                                                                                                                        #main program function
   import_weather_data = FetchData("Module4Lesson4Assignment\weather data.txt")                                                                    #setting up a FetchData class object
   import_weather_data.open_weather_data()                                                                                                         #opening a file to obtain weather data

   for city in weather_data:                                                                                                                       #'for' loop to cycle through weather_data dictionary
       create_parse_dictionary(city)                                                                                                               #calling funciton create_parse_dictionary using the 'for' loop
        
   print("Welcome to the Weather Forecast Application.\n")                                                                                         #welcome statement for the user
   
   while True:                                                                                                                                     #infinite while loop to cycle through user choices
    print("1.Get weather data\n2.Get detailed forecast\n3.Exit\n")                                                                                 #print statement providing the user with options
    user_choice = input("Enter the your selection (1-3): ")                                                                                        #obtaining user input and making it variable called user_choice       

    if user_choice == "1":                                                                                                                         #'if', 'elif' block determining user choice
        print("These are the cities we currently have data for:")                                                                                  #print statement for user

        for city in parsed_data:                                                                                                                   #'for' loop to cycle through cities in parsed_data dictionary
            print(city)                                                                                                                            #printing the city

        user_city = input("\nEnter the city you'd like to get data for: ").title()                                                                 #getting user city input and making it variable called user_city, also using .title() to help with error handling

        if user_city in parsed_data:                                                                                                               #'if' statement determining if user_city input is in parsed_data dictionary
            parsed_data[user_city].get_weather_data()                                                                                              #calling method get_weather_data
        
        else: print("\nForecast data for city currently unavailable.\n")                                                                             #'else' statement letting the user know the forecast data couldnt be found

    elif user_choice == "2":
        print("These are the cities we currently have data for:")

        for city in parsed_data:
            print(city)
       
        user_city = input("\nEnter the city you'd like to get data for: ").title()                                                                 #getting user city input and making it user_city variable

        if user_city in parsed_data:                                                                                                               #'if' statement determining if user_city input is in parsed_data dictionary                                                                                                                    
          parsed_data[user_city].get_detailed_report()                                                                                             #calling method get_detailed_report   

        else: print("\nForecast data for city currently unavailable.\n")                                                                           #'else' statement letting the user know the forecast data couldnt be found
            
    elif user_choice == "3":
        print("\nThank you for using the Weather Forecast Application. Have a good day!\n")                                                        #goodbye statement for the user
        break                                                                                                                                      #break to end the 'while' loop
    
    else: print("\nInput not recognized. Please enter a number 1-3.\n")                                                                            #else statement to let the user know their input wasnt recognized     


if __name__ == "__main__":
    main()                                                                                                                                         #calling 'main' function
