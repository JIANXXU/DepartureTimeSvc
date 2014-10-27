DepartureTimeSvc
================

Introduction
------------
This is the service that powers the DepartureTimeApp.

Technical Choices
-----------------
* Python / Django
* Django REST framework is used to create the RESTful services (Experience < 1 Week)
* Django Cache framework is used to cache service response.  If the size of the application is much larger, a distributed cache will be considered, such as memcached.
* Heroku is used to host the service.  Amazon EC2 is also considered, but due to limited time and the scale of the application, Heroku appears to be best fit.  (Heroku Experience < 1 Week)
* Simple test cases are added, more test cases are desired in future.
* Location is curated and stored in a local database.  Currently only BART is supported

Design Overview
---------------
* services/application.py - is the main service logics, which builds a smart cache to reduce unnecessary hits to the underlying traffic information service.
* services/views.py - defines RESTful operations.
* services/serializers.py - defines serializers that transforms data model to REST response or vice versa.
* services/models.py - defines Location data model and DepartureTime data model
* services/tests.py - contains test classes
