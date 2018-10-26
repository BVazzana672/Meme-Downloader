import praw
import config
import requests

reddit = praw.Reddit(client_id=config.praw_client_id,
                     client_secret=config.praw_client_secret,
                     user_agent=config.praw_user_agent)

memes_submissions = reddit.subreddit('memes').top('week')
links = []

if __name__ == '__main__':
    path = ''
    number_of_memes = input('How many memes do you want? ')
    check_path = input('Specific file path? (y/n) ')

    if check_path.lower() == 'y':
        path = input('Enter full file path: ')

    for i in range(int(number_of_memes)):
        submission = next(meme for meme in memes_submissions if not meme.stickied)
        links.append(submission.url)
    
    i = 0
    for link in links:
        i += 1
        extension = link[-4:]
        with open('Meme #{}{}'.format(i, extension), 'wb') as f:
            r = requests.get(link)
            f.write(r.content)