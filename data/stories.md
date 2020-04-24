## story_0
* chitchat
  - respond_chitchat

## story_11
* greet
  - utter_greet
* weather_information
  - action_weather
*  inform_location 
    - action_restaurant
* goodbye
  - utter_goodbye  


## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## interactive_story_11
* greet
    - utter_greet
* getNews
    - action_get_news
      - slot {"topic_news": "sports news"}
    - slot {"topic_news": null}
* affirm
    - utter_ask_continue
* noo
    - utter_goodbye

    

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye


## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## say ask fine
* greet
  - utter_greet
* ask_fine
  - utter_fine_answer
* affirm
  - utter_happy 
  

## say weather 
* greet
  - utter_greet
* weather_information
  - action_weather
* affirm
  - utter_happy 
  
## say GreenHouse 
* GlobalWarming
  - utter_global_answer

## say world
* bot_world
  - action_hello_world




## interactive_story_1
* greet
    - utter_greet
* bot_world{"world_hello": "world"}
    - action_hello_world


## story weather
* greet
  - utter_greet
* weather_information
    - action_weather
 * deny
  - utter_goodbye      



## story location_1
* greet
  - utter_greet
* inform_location 
    - action_access_location
 * inform_restaurant {"hotel_info": "Hotels near by"}
    - action_access_location



## story location_1
* greet
  - utter_greet
* inform_location {"place": "Islamabad"}
    - action_restaurant
 * inform_restaurant {"place": "Hotels near by"}
    - action_access_location

 


## story location_1
* greet
  - utter_greet
* inform_location 
    - action_access_location
 * inform_restaurant {"hotel_info": "Hotels near by"}
    - action_restaurant

## story hotels
* greet
  - utter_greet
* inform_restaurant {"hotel_info": "Hotels in lahore"}
    - action_restaurant
 * deny
  - utter_goodbye 

## story_hotels
* greet
  - utter_greet
* inform_restaurant {"hotel_info": "Hotels in lahore"}
    - action_restaurant
 * deny
  - utter_goodbye 

## story_hotels_2
* greet
  - utter_greet
* inform_restaurant {"hotel_info": "Hotels in rawalpindi"}
    - action_restaurant
 * deny
  - utter_goodbye 

## story_hotels_3
* greet
  - utter_greet
* inform_restaurant {"hotel_info": "Hotels in karachi"}
    - action_restaurant
 * deny
  - utter_goodbye 


## interactive_story_1
* bot_world
    - action_hello_world
* weather_information
    - action_weather
* inform_restaurant
    - action_restaurant

## interactive_story_1
* greet
    - utter_ask_howcanhelp
* inform_restaurant
    - action_restaurant

## interactive_story_1
* bot_world
    - action_hello_world
* weather_information
    - action_weather
* weather_information
    - action_weather

## say WeatherFav
* favourite_weather  
 - utter_like_weather

## say weather forecast
* greet
  - utter_greet
* weather_forecast
  - utter_weather_forecast
* affirm
  - utter_happy  

## debate weather

* greet
  - utter_greet
* weather_discusstion
  - utter_weather_debate{"weather_debate":"weather debate"}
* affirm
  - utter_happy  

## Weather Affects

* greet
 - utter_greet
 * weather_emotions
 - utter_weather_influence{"weather_affect":"effect of weather"}
 * affirm
  - utter_happy  

## hotels Story

* greet
 - utter_greet
 * inform_restaurant
 - action_restaurant
 * affirm
  - utter_happy  


## interactive_story_1
* greet
    - utter_greet
* GlobalWarming
    - utter_global_answer


## interactive_story_1

* weather_forecast
    - utter_weather_forecast


## interactive_story_1
* weather_forecast
    - utter_weather_forecast


## interactive_story_1

* Favourite_weather
    - utter_like_weather
* favourite_weather{"favourite_weath": "season"}
    - utter_like_weather



## interactive_story_1
* greet
    - utter_greet
* ask_fine
    - utter_fine_answer
* weather_discusstion
    - utter_weather_debate
* weather_discusstion{"weather_debate": "debate on weather"}

* weather_discusstion
    - utter_weather_debate
* weather_discusstion


## interactive_story_1
* greet
    - utter_greet
* ask_fine
    - utter_fine_answer
* weather_information
    - action_weather
* weather_information{"location": "dubai"}
    - slot{"location": "dubai"}
    - action_weather
* greet
    - utter_greet
* weather_information{"location": "scotland"}
    - slot{"location": "scotland"}
    - action_weather
* weather_information{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_weather
* inform_location{"place": "near by restaurants"}
    - slot{"hotel_info": "near by restaurants"}
    - action_access_location
* inform_location{"place": "near by parks"}
    - slot{"place": "near by parks"}
    - action_access_location
    - action_restart

## interactive_story_2
* inform_location{"place": "islamabad"}
    - slot{"place": "islamabad"}
    - action_access_location
* inform_location{"place": "parks"}
    - slot{"place": "parks"}
    - action_access_location
    
