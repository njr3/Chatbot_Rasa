

from rasa_core.actions import Action
from rasa_core.events import SlotSet
class GetTodaysHoroscope((Action):
   def name(self):
      return "hi"
   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
      user_horoscope_sign = tracker.get_slot('horoscope_sign')
return [SlotSet("horoscope_sign", user_horoscope_sign)]
