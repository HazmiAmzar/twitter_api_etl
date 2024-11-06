# Twitter API ETL

This project, **Twitter API ETL**, is an Extract, Transform, Load (ETL) pipeline that pulls data from Twitter's API, processes it, and stores it in a structured format (CSV). The pipeline uses Python with Tweepy and the `requests` library to retrieve data from Twitter, processes it for specific fields, and saves the transformed data into a `.csv` file for further analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)

---

## Project Overview

This project is a simple ETL pipeline designed to fetch tweets from a specified Twitter user, transform selected data fields, and save it to a CSV file. The pipeline pulls the tweets using Twitter's API, extracts fields like `username`, `text`, `created_at`, and user `id`, then stores the results in a structured format for analysis.

## Features

- **Extract Tweets**: Uses Twitter's API v2 to fetch tweets by username.
- **Transform Data**: Selects specific fields from the tweet data, including author and tweet details.
- **Load to CSV**: Outputs the transformed data to a CSV file for easy viewing and analysis.
- **Pagination Support**: Handles multiple requests to retrieve more than the default number of tweets.

## Requirements

- Python 3.7+
- Twitter Developer Account (for API keys and tokens)