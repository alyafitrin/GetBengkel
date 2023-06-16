# GetBengkel

# Cloud Computing - API
* gMaps_API - Java


### Using Visual Studio Code IDE
In this project, i am using Visual Studio Code IDE an environtment that i know to make it easy to use.
* New Project > choose programming language `Java` > (Make sure Java and Java Extention has been installed in your local)

### gMaps_API
* This API have function for connecting the getBengkel Android App and Google Maps API in Google Cloud Platform
to get access to Google Maps into the Android App

### How to make this API
* A. Get the API Key
* 1. Open the Google Cloud Developer Console at https://console.cloud.google.com.
* 2. Create a new project or select an existing project.
* 3. Enable the Google Maps API and obtain your API key. You need to enable the "Google Maps Android API" and "Google Maps Geocoding API".
* 4. Retrieve the generated API key.
* B. Get Users GPS Locations
* 1. Check the user's location permission. If permission has not been granted, use ActivityCompat.requestPermissions to request permission from the user.
* 2. Use FusedLocationProviderClient from Google Play Services to obtain the last known user location.
* 3. If a location is available (location != null), extract the latitude and longitude coordinates from the location.
* 4. Create a LatLng object with the obtained coordinates.
* 5. Add a marker to the map using mMap.addMarker and set its title as "My Location".
* 6. Move the map's camera to the user's location using mMap.moveCamera with CameraUpdateFactory.newLatLngZoom to apply a zoom effect to the map.
* 7. Provide a feature to track real-time changes in the user's location using LocationRequest and LocationCallback from Google Play Services.
 
### App Deployment
For this project deployment, i am using VM Instace as a compute engine for simple  and small configuration. It has been installed with python, Flask, and Tensorflow for process the machine learning that using TensorFlow Serving as deployment tools.
* Command that i run for setting up the environment
 ```
sudo apt-get update
sudo apt-get install python3
python /path/to/api.py

```
  
