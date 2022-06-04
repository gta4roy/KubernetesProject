4 Componenents 

WEB UI to query address in the UI to CRUD operations on Address Structure 

Flask Based Web Service to Provide service functionality 

Redis DB 

Kubernetes Components 

web-ui-deployment -- WEB UI Container POD 
		     WEB UI Service 
		     Config MAP to provide url and port for REST API

rest-api-deployment -- flask REST API SERVER Container POD 
			Flask SERVICE
			
			redis-config-map keeping url and port 
			redis-db-secret --: Keeping username and password

REDIS DB DEPLOYMENT ---- REDIS DB Container POD 
		   --- REDIS DB Service 

		Future 
			Shared PV for SAVE Functionality 

			
UI Options 

Create 
List 
Delete 
Update 

 




