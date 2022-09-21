from authy import authpy
api = authpy('credentials.json')

if __name__ == '__main__':
    credentials = 'credentials.json'
    api = authpy(credentials)
    mention = 'PPhutsay'
    post_title = 'Post on Twitter API using Tweepy and Python'
    
    status = f"@{mention} 早く宿題やれ"
    
    api.update_status(status=status)