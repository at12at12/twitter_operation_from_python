import twitter
import json

def get_api_data(api_path):
    api_open = open(api_path, 'r')
    api_load = json.load(api_open)

    api = twitter.Api(
        consumer_key = api_load["consumer_key"],
        consumer_secret = api_load["consumer_secret"],
        access_token_key = api_load["access_token_key"],
        access_token_secret = api_load["access_token_secret"],
    )
    return api

def print_frend_name(api):
    users = api.GetFriends()
    #print(users)
    print([user.screen_name for user in users])

def tweet_load(tweet_log_file):
    json_open = open(tweet_log_file, 'r')
    tweet_json_load = json.load(json_open)
    return tweet_json_load

def find_keyword_tweets(tweet_json_load,keyword_list):
    for tweet in tweet_json_load:
        for keyword in keyword_list:
            if keyword in tweet["tweet"]['full_text']:
                print(tweet["tweet"]['full_text'])
                print()

def delete_tweets(api,tweet_json_load,year,month):
    dic_month = {
        'Jan' : 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' : 6,
        'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12,
        }
    total = 0
    ok = 0
    ng = 0
    for tweet in tweet_json_load:
        if int(tweet["tweet"]["created_at"][-4:]) == year:
            MM = dic_month[tweet["tweet"]["created_at"][4:7]]
            if MM == month:
                total += 1
                try:
                    api.DestroyStatus(tweet["tweet"]['id'])
                    ok += 1
                except Exception as e:
                    print(e.args)
                    ng += 1
    print("{}年{}月のツイートの件数：{}".format(year,month,total))
    print("ツイート削除成功した件数：{}".format(ok))
    print("ツイート削除失敗した件数：{}".format(ng))

if __name__ == "__main__":
    api_path = "ignored_dir/secret.json"
    tweet_log_file = "ignored_dir/tweet.js"
    keyword_list = ["XXX","YYY","ZZZ"]
    year = 2021
    month = 7

    api = get_api_data(api_path)
    tweet_json_load = tweet_load(tweet_log_file)
    
    print_frend_name(api)
    find_keyword_tweets(tweet_json_load,keyword_list)
    # 使う場合にはコメントアウトを消してから実行
    # delete_tweets(api,tweet_json_load,year,month)
