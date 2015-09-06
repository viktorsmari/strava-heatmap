strava
======


This repo will allow you to see your Strava heatmap on your local machine.

(If you are a paying (premimum) Strava user you should be able to see this somewhere on Strava's website)


After you clone this repo do the following:


1. Download your Strava files from: https://www.strava.com/settings/profile - You should receive an email with the link to your files.
2. Unzip all files into the folder 'files/' at the root of this project
3. From terminal run `python create.py` which creates a single file called "rides.dat"
4. From treminal run `python server.py` to start a webserver
5. Visit 0.0.0.0:8080 in browser to see the results.







Issues
======

1. The starting point is Copenhagen so you need to navigate to yours
2. The file rides.dat can be heavy for the browser with all the rides so maybe you need to remove some of them from "files/" and rerun create.py
