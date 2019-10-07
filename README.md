# Data Science Pipeline
This project demonstrates all of the technologies needed to create an end-to-end data science pipeline. This includes consuming data from an original source, processing and storing it and finally providing machine-learning based results to end users.

### Technologies Used

This data science pipeline consists of the following applications and services:

* [Amazon AWS](https://github.com/nickruta/data_science_pipeline/tree/master/Amazon_AWS) - I used Amazon DynamoDB, Lambda, and Gateway API products to do calculations on a large database, stored in MongoDB, and provide a GET Endpoint.

* [Angular 8](https://github.com/nickruta/data_science_pipeline/tree/master/Angular_Front_End/AngularJwtAuth) - An Angular 8 front end to provide a dashboard demonstrating all of data collection and machine learning results.

* [Bash Scripts](https://github.com/nickruta/data_science_pipeline/tree/master/Bash_Scripts) - Linux Bash Scripts were needed to streamline the start-up processes for all services needed in this project.

* [Docker Compose](https://github.com/nickruta/data_science_pipeline/tree/master/Docker_Compose) - I used Docker Compose to connect microservice containers for the final product.

* [Kafka](https://github.com/nickruta/data_science_pipeline/tree/master/Kafka_Twitter) - To allow for multiple microservices and an HDFS-based Data Lake to consume live tweets, I set up a Kafka server.

* [Spring Boot REST Service](https://github.com/nickruta/data_science_pipeline/tree/master/Spring_REST_Service) - To authenticate users and store their data, I used a Sprint Boot REST Web Service backend.
* [Twitter Stream Consumer](https://github.com/nickruta/data_science_pipeline/blob/master/Kafka_Twitter/Twitter-Sentiment-Analysis-Using-Spark-Streaming-And-Kafka-master/app.py) - Python-based consumtion of tweets using the tweepy library.
* [Flask Machine Learning Service](https://github.com/nickruta/data_science_pipeline/tree/master/Flask_Twitter_Sentiment_Analysis_Service/api) - Flask-based application to provide machine learning results.
