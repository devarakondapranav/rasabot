# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import time
#
#
class ActionGetweather(Action):

    def name(self) -> Text:
        return "action_getweather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        company = tracker.get_slot('company')
        dispatcher.utter_message("Please wait while I fetch info about  " + company +"'s shares")
        r = requests.get(url='https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + company +'&apikey=QI99AP1N26FY4SGH')
        data = r.json()

        share_price = float(data["Global Quote"]["05. price"])
        volume = float(data["Global Quote"]["06. volume"])

        market_cap = (share_price*volume)/1000000000
        time.sleep(1)


        dispatcher.utter_message("The current share price is $" + str(share_price))
        #dispatcher.utter_message("The market cap of " + company + " is $" + str(market_cap) +"bn." )

        change_percent = data['Global Quote']
        
        


        return []
# from rasa_sdk import Action
# from rasa_sdk.events import SlotSet

# class ActionGetweather(Action):
#    def name(self):
#       # type: () -> Text
#       return "action_getweather"

#    def run(self, dispatcher, tracker, domain):
#       # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

#       # company = tracker.get_slot('company')
#       # response = "You have requested for " + str(company) +"'s information!!!"

#       dispatcher.utter_message("heyyy")
      

#       return [SlotSet('company', company)]