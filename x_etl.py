import os
import json
import tweepy
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.environ.get("BEARER_TOKEN")

client = tweepy.Client(bearer_token)
user = client.get_user(username = "HazmiAmzar") #User id=1030689165443121152 name=hazmi username=HazmiAmzar
user_id = user.data.id
print(user_id)

def extract():

    url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    params = {
            "user.fields": "created_at",
            "expansions": "author_id",
            "tweet.fields": "created_at",
            "max_results": 5}
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'User-Agent': 'v2UserTweetsPython'}

    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    return response.json()

def transform(extracted_tweets):
    tweet_list = []

    # Extract user information once from the "includes" section
    user_info = extracted_tweets.get("includes", {}).get("users", [])[0]
    username = user_info.get("username")
    handle_name = user_info.get("name")

    # Iterate over each tweet in the "data" section
    for tweet in extracted_tweets.get("data", []):
        transform_tweets = {
            "user_id": tweet.get("author_id"),
            "username": username,
            "handle_name": handle_name,
            "tweets": tweet.get("text"),
            "created_at": tweet.get("created_at")
        }
        tweet_list.append(transform_tweets)

    return tweet_list

def load(transformed_tweets):
    df = pd.DataFrame(transformed_tweets)
    df.to_csv("x_etl.csv")
    return df

extracted_tweets = extract()
transformed_tweets = transform(extracted_tweets)
load_tweets = load(transformed_tweets)

print(load_tweets)