# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests, json
import pyowm

from newsapi import NewsApiClient
from rasa_sdk import ActionExecutionRejection

from rasa_sdk.events import  FollowupAction

import sqlite3

#%%

##############################################################################################################
# Global Constants

newsapi = NewsApiClient(api_key='72fe1c62948942129c94bef6122d60e7')


class ActionHelloWorld(Action):
#
     def name(self) -> Text:
         return "action_hello_world"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello World!")

         return []




class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         api_address='http://api.openweathermap.org/data/2.5/weather?appid=d98a9aede73d2bfa92fd53cabc6a3497&q='
         city = tracker.get_slot('location')
         url = api_address + city
         json_data = requests.get(url).json()
         format_add = json_data['weather'][0]['description']
         temp = json_data['main']['temp']
         temp_min = json_data['main']['feels_like']
         temp_max = json_data['main']['temp_max']
         temp_pree = json_data['main']['pressure']
         temp_hum = json_data['main']['humidity']
         vis=json_data['wind']
         cun=json_data['sys']['country']

         response = """It is currently {} in {} at the moment. The temperature is {} farenhite, the humidity is {} and the wind speed is {} mph.""".format(format_add, city, temp, temp_hum,temp_pree)        

         
         dispatcher.utter_message(response)
         #dispatcher.utter_message(text="temperature in kalvin")
         #dispatcher.utter_message(temp)
         #dispatcher.utter_message(text="feels like")
         #dispatcher.utter_message(temp_min)
         #dispatcher.utter_message(text="temperture maximum")
         #dispatcher.utter_message(temp_max)
         #dispatcher.utter_message(text="pressure")
         #dispatcher.utter_message(temp_pree)
         #dispatcher.utter_message(text="humidity")
         #dispatcher.utter_message(temp_hum)
         #dispatcher.utter_message(text="visibility")
         #dispatcher.utter_message(vis)
         #dispatcher.utter_message(text="country")
         dispatcher.utter_message(text="The country of this city is")
         dispatcher.utter_message(cun)
         
		
		 
         return

class ActionRestaurant(Action):
    def name(self):
        return 'action_restaurant'

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


         import requests

         api_key = 'AIzaSyAua4KDwvXA4KK2ZZNy4Cs_UmGVC1JeqFM'
         url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
         query = tracker.get_slot('hotel_info')
         r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
         x = r.json() 
         y = x['results']
         for i in range(len(y)):
            response=y[i]['name']  
            dispatcher.utter_message(response)
         return	     

class ActionAccessLocation(Action):
    def name(self):
        return 'action_access_location'

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


         import requests

         api_key = 'AIzaSyAua4KDwvXA4KK2ZZNy4Cs_UmGVC1JeqFM'
         url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
         query = tracker.get_slot('place')
         r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
         x = r.json() 
         y = x['results']
         for i in range(len(y)):
            response=y[i]['name']  
            dispatcher.utter_message(response)
         return  


		
 



class ActionGetNews(Action):
    def name(self):
        return "action_get_news"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["topic_news"]

    def slot_mappings(self):
        return {
            "topic_news": [
                self.from_entity(entity="topic_news", intent =["getNews"])]
        }

    # def validate(self,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict]:
    #     """Validate extracted value of requested slot
    #         else reject execution of the form action
    #         Subclass this method to add custom validation and rejection logic
    #     """
    #     # extract other slots that were not requested
    #     # but set by corresponding entity
    #     slot_values = self.extract_other_slots(dispatcher, tracker, domain)

    #     # extract requested slot
    #     slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
    #     if slot_to_fill:
    #         for slot, value in self.extract_requested_slot(dispatcher,
    #                                                        tracker,
    #                                                        domain).items():
    #             validate_func = getattr(self, "validate_{}".format(slot),
    #                                     lambda *x: value)
    #             slot_values[slot] = validate_func(value, dispatcher, tracker,
    #                                               domain)

    #         if not slot_values:
    #             # reject to execute the form action
    #             # if some slot was requested but nothing was extracted
    #             # it will allow other policies to predict another action
    #             raise ActionExecutionRejection(self.name(),
    #                                            "Failed to validate slot {0} "
    #                                            "with action {1}"
    #                                            "".format(slot_to_fill,
    #                                                      self.name()))

    #     # validation succeed, set slots to extracted values
    #     return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        """Define what the form has to do
            after all required slots are filled"""

        topic_news = tracker.get_slot("topic_news")

        pageSize = 1 # Set the number to how many news articles you want to fetch 

        all_articles = newsapi.get_everything(q=topic_news, language='en', sort_by='relevancy',page=pageSize)

        # data = all_articles.json() # extracting data in json format
        data = all_articles['articles']

        dispatcher.utter_message("Here is some news I found!")

        for i in range(len(data)):
            output = data[i]['title'] + "\n" + data[i]['description'] + "\n"
            dispatcher.utter_message(output)

        dispatcher.utter_message(template="utter_confirm_if_service_is_correct")

        # utter submit template
        return []

