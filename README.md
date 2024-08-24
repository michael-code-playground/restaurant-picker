**Restaurant picker** 

The aim of the project is to reduce decision fatigue regarding restaurant choice. The web app picks out a restaurant randomly from my google sheet, where I saved decent spots to have some food. 
The file includes only places in Lisbon, where I currently live. 

Another feauture is to allow users put their own suggestions. I set up Google Maps API, so any record user enteres is validated i.e. the function makes a request to check if a particular place exists, the API returns a corresponding response.

I extended the validation feature by comparing returned coordinates to those of Lisbon. So that I can filter out the results and exclude spots whose name match, but the location differs. Specificyng location bias in requests is not always accurate. 

Application is deployed on Google Cloud, where I used the app engine service. 
