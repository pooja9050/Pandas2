#1148. Article Views I
#drop_duplicates(subset, inplace)
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df.drop_duplicates(subset = ['author_id'], inplace = True)
    df.sort_values(by = ['author_id'], inplace = True)
    return df[['author_id']].rename(columns = {'author_id' : 'id'})

#unique()
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] ==views['viewer_id']]
    df = df['author_id'].unique()
    df = pd.DataFrame(df, columns = ['id'])
    return df.sort_values(by=['id'])

#1683. Invalid Tweets
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[(tweets['content'].str.len()> 15)]
    return df[['tweet_id']]

    
#Alternative approach
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    is_valid = tweets['content'].str.len() > 15
    print(is_valid)
    df = tweets[is_valid]
    return df[['tweet_id']]


import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # df = pd.DataFrame(columns=["tweet_id"])
    s = tweets["content"].apply(lambda x: True if len(x)>15 else False)
    # df["tweet_id"] = 
    return pd.DataFrame(tweets[s]["tweet_id"])



