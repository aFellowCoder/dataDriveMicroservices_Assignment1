Data-Driven Microservices Project

Overview

This project is part of a college assignment for the Data-driven Microservices module. The goal of the project is to develop a microservices-based system that processes and analyses a continuous stream of data using gRPC and presents the results on a web page.

Problem Description

The system simulates real-time data streaming from a file, where data is served to an analytics client through a gRPC stream channel. The client processes each data entry and computes various metrics, including:

	1.	An aggregate metric (e.g., total or average)
	2.	A rolling 3-minute metric (e.g., recent sentiment)
	3.	The maximum or minimum value based on specific criteria
	4.	A custom metric of choice

The results are displayed on a single web page, which refreshes with new data whenever loaded or updated.

Project Structure

This project consists of multiple microservices, each with a distinct responsibility:

	•	Data Stream Microservice: Reads data from a file and streams it via gRPC.
	•	Analytics Microservice: Processes incoming data to compute metrics.
	•	Web Server Microservice: Hosts a Flask-based dashboard that displays the calculated metrics.
	•	Data Storage Microservice (optional): Stores processed data for historical analysis.

Technologies Used

	•	gRPC for communication between microservices
	•	Docker and Docker Compose for containerization and orchestration

Features

	•	Simulated real-time data streaming at an average of 2 records per second with variability.
	•	Calculation of four distinct types of metrics:
	•	Aggregate metric (e.g., average value)
	•	Rolling 3-minute analysis (e.g., sentiment analysis)
	•	Extreme data value (e.g., maximum or minimum)
	•	Custom analysis
	•	A user-friendly dashboard that refreshes to display updated metrics.
