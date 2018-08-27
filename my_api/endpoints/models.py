import datetime

commentslist = []

def save_comment(data):
    """Add comment to list"""
    data['comment_id'] = len(commentslist) + 1
    data['message'] ="message"
    data['author'] = "author"
    data['date_created'] = datetime.datetime.now()
    # save to list
    commentslist.append(data)