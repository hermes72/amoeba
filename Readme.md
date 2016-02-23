# amoeba
## A micro-server for managing events and calendar data
A small api server to manage the events of any organisation. Contains fields
+ Name
+ TimeStamp
+ Genre
+ Venue
+ Description
+ Contact
+ Postscript
+ Links
+ PostedBy
+ Updated

And an auth based api server. Developers should obtain an api key from this server and use that to post events.
Their api key should be approved by the admin in the Django admin module for the events to be registered. Images can also be uploaded related to the particular event. Sample post page has be written in the url "http://[serverAddress]:[Port]/postpage"

### URL Patterns
#### /  
###### [root page]
This page is used to generate api key for a unique email-id and a name. When the form is posted, it generates an api key for the user and is displayed in the subsequent page.
#### /requestapi
This page follows the root page or the index page after filling the api key request form. This page displays the api-key. This key is to be kept safe and secret. This api-key won't be able to post data until the admin approves the key from the Django's inbuilt admin module.
#### /postpage
This page is a sample/skeleton page for posting events. Posting events can be done in REST API method but this POST transaction actually is a multipart form. As of now it can contain images. It could contain any other multimedia data. So sending binary data through REST API's can tamper the data. Therefore posting data to the server is done through conventional HTTP POST method. All languages including C can post form data including files(See the libcurl, libaria2 libraries).
#### /postevent
This is the POST url for the posting events. A http-request with the form data and parameters, same as /postpage form, should be the request body.
#### /api
This is the url pattern that returns the JSON string of all the events in the database. The JSON encoded string contains id which is used to get the events from the last id obtained and to get the image related to the specific event. For event id `i` : "http://[serverAddress]:[Port]/static/images/<b>i</b>" is the URI for the image.
```json
[
  {"ID" : "1",
    "Name" : "Sample Event",
    "TimeStamp" : "01-01-2001, 08-00",
    "Genre" : "Sample, Fun",
    "Venue" : "Sample Venue",
    "Description" : "This is a sample event for a sample cause.",
    "Contact" : "Sample Contact : 010-01010101",
    "Postscript" : "Please bring sample item 1.",
    "Links" : "http://sample1.org",
    "PostedBy" : "Sample Developer 1",
    "Updated" : false
  },
  {"ID" : "2",
    "Name" : "Sample Event 2",
    "TimeStamp" : "03-03-2003, 08-00",
    "Genre" : "Sample, Fun, Second",
    "Venue" : "Sample Venue 2",
    "Description" : "This is a sample event 2 for a sample cause 2.",
    "Contact" : "Sample Contact : 020-02020202",
    "Postscript" : "Please bring sample item 2.",
    "Links" : "http://sample2.org",
    "PostedBy" : "Sample Developer 2",
    "Updated" : true
  }
]
```
#### /api/[:number:]
This url displays the events after the id `[:number:]`. To eliminate redundancy of downloading the whole event list each time to update the calendar, simply use the id of the latest event in the app and call `/api/[:number:]`. This returns the events that are updated in the server after the given id. The `def api(request)` method in `views.py` gets the resource from `/api/0`. In the above example if `/api/1` is called the following JSON Data will be formed :
```json
[
  {"ID" : "2",
    "Name" : "Sample Event 2",
    "TimeStamp" : "03-03-2003, 08-00",
    "Genre" : "Sample, Fun, Second",
    "Venue" : "Sample Venue 2",
    "Description" : "This is a sample event 2 for a sample cause 2.",
    "Contact" : "Sample Contact : 020-02020202",
    "Postscript" : "Please bring sample item 2.",
    "Links" : "http://sample2.org",
    "PostedBy" : "Sample Developer 2",
    "Updated" : true
  }
]

```
#### /admin
This is the standard Django admin page.

### Running the micro-server
##### Requirements
+ Python 2.7 and above
+ Django 1.9 and above
+ Unix based OS
+ GNU Make
+ SQLite3

##### Initializing
```shell
git clone https://github.com/hermes72/amoeba.git
cd amoeba
make
./manage.py runserver
```

##### Contribute
Feel free to contribute....
