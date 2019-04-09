# Introduction
This is a full-stack web application that uses Python Flask framework. It provides features to a logged in user to make a list of countries they want to travel and then a sub-list of destinations inside each country. Countries can be selected from the list dropdown. Inside each country, user can add valid addresses(uses [axios](https://github.com/axios/axios)) inside that country. The database saves a valid address with actual google maps latitude and longitude. Each country and spot inside country can be added or deleted. Comments can be added, or updated for each sub-list item inside a country => (CRUD). The user needs to log in using their Google account.       

## Dependencies
The application is based on the following Python(3.7.1) packages:
- SQLAlchemy==1.2.15
- Flask==1.0.2
- Flask_OAuthlib==0.9.5
- geocoder==1.38.1
To install the above, use `pip install <package>`. Or using the provided reqs file: `pip install -r requirements.txt`.

- Bootstrap 3.4.0 [CDN](https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js)
- jQuery 3.3.1 [CDN](https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js)


## Run the app
There are two ways to run this full-stack application.
1. Check this [heroku](http://destinationplanner.herokuapp.com/) application!
2. Follow these steps:
   - Clone this [repository](https://github.com/mannanrehbari/DestinationPlanner).
   - Install the requirements mentioned above.
   - Navigate into application directory and run `python destplanner.py`.
   - From your browser, go to `localhost:5000` to access the index!


## Demonstration
See this  [heroku](http://destinationplanner.herokuapp.com/) application!

## License
See [license](LICENSE)
