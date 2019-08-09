#https://apps.twitter.com/app/-------/keys

import twitter

api = twitter.Api(consumer_key='###',
                      consumer_secret='###',
                      access_token_key='###',
                      access_token_secret='###')

#print(api.VerifyCredentials())
#users = api.GetFriends()
#print ([u.name for u in users])

twitter_rockstar = (api.GetUser(screen_name='andrewyng'))
followers_of_twitter_rockstar = api.GetFollowerIDs(twitter_rockstar)
#print(followers_of_twitter_rockstar)

my_followers = api.GetFollowerIDs()
my_friends = api.GetFriendIDs()

for i, follower_id in enumerate(followers_of_twitter_rockstar[0:1000]):
    try:

        user = (api.GetUser(user_id=follower_id))
        is_user_protected = int(user.protected)
        if not is_user_protected:
            aim_user_user_name = user.screen_name
            user_id = user.id_str
            user_created_at = int(user.created_at[-4:])
            user_favourites_count = user.favourites_count
            user_followers_count = user.followers_count
            user_friends_count = user.friends_count
            user_name = user.name
            user_statuses_count = user.statuses_count
            user_follows_me = int(follower_id in my_followers)
            user_is_friend = int(follower_id in my_friends)
            last_post_created_at = user.status.created_at
            user_bio = user.description.lower()


            interests = ['python', 'machine', 'deep', 'code', 'engineer', 'software', 'data', 'developer',
                                 'artificial', 'programmer', 'science', 'statistic', 'nlp', 'learning', 'tech','computer',
                                 'cs','programming','computers','scientist']

            if any(interest in user_bio for interest in interests) \
                    and user_favourites_count > 20 \
                    and user_friends_count > 100:
              pass

    except:
       continue

import sqlite3

#conn = sqlite3.connect('twitter.sqlite')
#cur = conn.cursor()

import os.path

BASE_DIR = os.path.dirname(os.path.abspath("DB_TWITTER.db"))
db_path = os.path.join(BASE_DIR, "DB_TWITTER.db")
conn = sqlite3.connect(db_path)
cur = conn.cursor()
#...
#...
#...


# main loop, where we get information interesting users:
new_friend = api.CreateFriendship(user_id=user.id_str, follow=False, retweets=False)
create_mute = api.CreateMute(user_id=user.id_str)

cur.execute('''INSERT OR REPLACE INTO users
                  (
                    id,
                    user_name,
                    created_at,
                    favourites_count,
                    followers_count,
                    friends_count,
                    name,
                    statuses_count,
                    follows_me,
                    i_am_following
                  ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (id,
                             user_name,
                             user_created_at,
                             user_favourites_count,
                             user_followers_count,
                             user_friends_count,
                             user_name,
                             user_statuses_count,
                             user_follows_me,
                             user_is_friend))
conn.commit()
