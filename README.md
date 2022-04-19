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
 - Type **python [App Name]**. eg: python house_price.py
 - Copy paste the IP Address into browser
 **OR**
 - Open Spyder and Run house_price.py file and copy paste IP Addr into browser.

## Heruko Deployment
 - Create a **Requirement.txt** file which has all the libraries requirement
 - Create a **Procfile** which has **web: gunicorn house_price**(Flask file name)**:app**(application name in flask file)
 - Upload all the files in Github.
 - Create App on heruko and link it with your Github & Repository.
 - Select Manual Deployment.
 - Open the URL in a browser.
<img width="1310" alt="image" src="https://user-images.githubusercontent.com/84242964/163476602-6d02bb2e-1ab7-4699-9fca-3246aed9be97.png">

## AWS EC2 Deployment
  - Create EC2 Instane on AWS.
    - Select Ubuntu free tier server t2-micro.
    - Create a new key-value-pair(.pem file) and download it.
    - Create a new Security group with all Type(All traffic) and source (Anywhere).
    - Add this security group to the EC2 Instance by going into Network Interfaces-->select security group-->change security-->Add new security group.
    - Get the Public DNS(eg. ec2-13-59-212-30.us-east-2.compute.amazonaws.com)
    ![image](https://user-images.githubusercontent.com/84242964/163756196-8a729f83-0c30-4d8f-ba0c-46c8db34100a.png)
    
    
  - Open 2 Terminal shell
    - 1st Terminal-->Master Terminal(Virtual Machine)
      - Set the working Directory where all the files are located(.pem,.py,.pkl,.txt etc).
      - Connect this terminal to the EC2 Instance using SSH Command eg. ssh -i MLDeployment.pem ubuntu@ec2-13-59-212-30.us-east-2.compute.amazonaws.com.
      - connection is established, we will see something like "ubuntu@ip-172-31-17-92: $".
      - To create folder/derictory USE **mkdir folder name** eg.mkdir static && mkdir static/css ,static-->css.
    - 2ns Terminal--> Local Terminal (Local server)
      - Set the working Directory where all the files are located(.pem,.py,.pkl etc).
      - To send files into EC2 Instance use SCP command eg. scp -i **'.pem file'** **'file to send'** ubuntu@ec2-13-59-212-30.us-east-2.compute.amazonaws.com:(home directory). 
      ![image](https://user-images.githubusercontent.com/84242964/163755894-b467aa6c-20d8-4463-ae9f-fc107b215e20.png)
      - To send files to existing folder/directory eg. scp -i **'.pem file'** **'file to send'** ubuntu@ec2-13-59-212-30.us-east-2.compute.amazonaws.com:templates/ (send files to templates folder/directory).
  - Check all the files in Master Terminal using **ls** command.
  - Run command **sudo apt-get update && sudo apt-get install python3-pip** in Master terminal to install python3.
  - Run command **pip3 install -r requirements.txt** in Master Terminal.
  - To Run .py file command **python3 file_name.py**
  - Connect EC2 Instance and run it's URL(DNS) into browser with port(8080) eg.ec2-13-59-212-30.us-east-2.compute.amazonaws.com:8080.
  <img src="https://user-images.githubusercontent.com/84242964/163756845-28c9d8ac-2f24-4973-92d7-6e43eff1210f.png" width="600" height="500">
      
