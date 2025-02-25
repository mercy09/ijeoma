Flask Survey Tool

Project Overview

This project is a survey tool built using Flask to collect and analyze participants' income and spending data. The application stores data in MongoDB, processes it into CSV format, and visualizes key insights using Python.

Features

Web interface to collect user details (age, gender, income, and expenses across various categories).

Data storage in MongoDB.

Data processing and export to CSV.

Data visualization using Matplotlib and Seaborn.

Deployment on AWS using EC2, Nginx, and Gunicorn.

Installation and Setup

the following was installed:

Python 3.x

Flask

MongoDB

Pandas, Matplotlib, Seaborn

Gunicorn (for deployment)

Local Setup

Clone the repository:

git clone <repo_url>
cd flask-survey-tool

Install dependencies:

pip install -r requirements.txt

Start MongoDB (ensure it is running on mongodb://localhost:27017/):

mongod --dbpath <your_db_path>

Run the Flask application:

python app.py

Access the web interface at http://127.0.0.1:5000.

Data Processing

Collected data is stored in MongoDB.

Data is exported to CSV format for further analysis.

Data visualizations include:

Income distribution by age.

Spending patterns across genders.

Processed charts are saved for PowerPoint presentations.

Deployment on AWS

Steps:

Launch an AWS EC2 instance (Ubuntu recommended).

Install dependencies:

sudo apt update && sudo apt install python3-pip nginx
pip install flask pymongo pandas matplotlib seaborn gunicorn

Clone the repository onto the EC2 instance:

git clone <repo_url>
cd flask-survey-tool

Start the Flask application using Gunicorn:

gunicorn -w 4 -b 0.0.0.0:5000 app:app

Configure Nginx as a reverse proxy to forward traffic to Gunicorn.

Ensure security group settings allow HTTP (port 80) and SSH (port 22).

Access the application using the EC2 instance’s public IP.

