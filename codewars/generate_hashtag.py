def generate_hashtag(hashtag):
    if not hashtag or not hashtag.strip():
        return False
    if hashtag.startswith("#"):
        hashtag = hashtag[1:]

    hashtag = '#'+''.join([word.capitalize() for word in hashtag.split()])
    return hashtag if len(hashtag)<=140 else False
