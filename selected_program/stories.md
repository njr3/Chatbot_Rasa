

## path 1               
* query_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_organisation


## path 2               
* query_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_organisation


## path 3               
* greet
  - utter_greet 
* query_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_organisation


  
## path 4                
* query_attend_per_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_attend_per_organisation


## path 5                
* query_attend_per_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_attend_per_organisation


## path 6               
* query_attend_per_organisation{"Organisation":"Chamber of commerce"} 
  - utter_action_query_attend_per_organisation



## path 7                
* query_attend_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_attend_organisation

 
## path 8               
* query_attend_per_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_attend_per_organisation


## path 9               
* query_attend_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_attend_organisation

  
## path 10               
* query_infoattend_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_infoattend_organisation

   

## path 11               
* query_infoattend_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_infoattend_organisation

  
  
## path 12                
* query_infoattend_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_infoattend_organisation


## path 13              
* query_join_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_join_organisation

  
## path 14                
* query_join_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_join_organisation

   

## path 15                
* query_join_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_join_organisation
 

## path 16             
* query_services_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_services_organisation

  
## path 17               
* query_services_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_services_organisation

   

## path 18              
* query_services_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_services_organisation
 


## path 19              
* query_location_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_location_organisation

  
## path 20                
* query_location_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_location_organisation
 
   

## path 21              
 
* query_location_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_location_organisation



## path 22              
* query_document1_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_document1_organisation

  
## path 23               
* query_document1_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_document1_organisation

   

## path 24              
* query_document1_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_document1_organisation
 

## path 25           
* query_document2_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_document2_organisation

  
## path 26                
* query_document2_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_document2_organisation

   

## path 27              
* query_document2_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_document2_organisation
 

## path 28            
* query_offeerdocument1_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_offeerdocument1_organisation
 
  
## path 29               
* query_offeerdocument1_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_offeerdocument1_organisation
 
   

## path 30              
* query_offeerdocument1_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_offeerdocument1_organisation


## path 31           
* query_invest_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_invest_organisation

  
## path 32               
* query_invest_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_invest_organisation
 
   

## path 33             
* query_invest_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_invest_organisation



## path 32           
* query_economic{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_economic

  
## path 35             
* query_economic{"Organisation":"CCIMA"} 
  - utter_action_query_economic

   

## path 36             
* query_economic{"Organisation":"CCIMC"} 
  - utter_action_query_economic


## path 37           
* query_support{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_support

  
## path 38            
* query_support{"Organisation":"CCIMA"} 
  - utter_action_query_support

   

## path 39             
* query_support{"Organisation":"CCIMC"} 
  - utter_action_query_support

  
## path 40              
* query_list_organisation{"Organisation":"Chamber of Commerce"} 
  - utter_action_query_list_organisation

  
## path 41               
* query_list_organisation{"Organisation":"CCIMA"} 
  - utter_action_query_list_organisation
 
   

## path 42               
* query_list_organisation{"Organisation":"CCIMC"} 
  - utter_action_query_list_organisation

## path 43              
* greet
  - utter_greet 

## path 44               
* affirm 
  - utter_affirm

## path 45               
* bye 
  - utter_bye
 
## fallback
- utter_default
