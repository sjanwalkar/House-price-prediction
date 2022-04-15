# House price prediction
 ## This Project Predicting showcases Real case scenerio in predicting Banglore House price, and is an illustration of End to End Data Science Project.
 - ### Topics Include
  - Web Scraping Data from Magicbricks.com
  - Data Cleaning
  - Feature Engineering
  - Outlier Removal
  - Modeling ML
  - Creating Python Flask Server: **house_price.py**
  - Creating Front end UI: **Index.html**  & For styling : **style.css**
  - Deploying Model
    - Local server
    - Global server


----------------
- Index.html file will contain all the input fields that we need in the UI.
- Style.css file contains various styling like background etc.


### App UI
<img width="890" alt="image" src="https://user-images.githubusercontent.com/84242964/163471156-803fbfe0-88e8-4001-b9f9-b8c95e780b56.png">

## Running App on Local server
 - Open Terminal, Change the directory to the Application Folder through **cd** command.
 - Type **python run [App Name]**. eg: python run house_price.py
 - Copy paste the URL into browser
 **OR**
 - Open Spyder and Run house_price.py file and copy paste URL into browser.

## Heruko Deployment
 - Create a **Requirement.txt** file which has all the libraries requirement
 - Create a **Procfile** which has **web: gunicorn house_price**(Flask file name)**:app**(application name in flask file)
 - Upload all the files in Github.
 - Create App on heruko and link it with your Github & Repository.
 - Select Manual Deployment.
<img width="1310" alt="image" src="https://user-images.githubusercontent.com/84242964/163476602-6d02bb2e-1ab7-4699-9fca-3246aed9be97.png">
