#print tweet_users ie, word starts with @

tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
# twt=tweets.split()
# for tweet_users in twt:
#     if "@" in tweet_users:
#         print(tweet_users)

 #OR

words=tweets.split(" ")
for w in words:
    if w.startswith("@"):
        print(w)
       
        