from flask import Flask, request, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)


def extract_followers(html):
    soup = BeautifulSoup(html, 'html.parser')
    return [a.get_text().strip() for a in soup.find_all('a')]


def extract_following(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [a.get('href', '') for a in soup.find_all('a')]

    usernames = []
    for link in links:
        parts = link.strip('/').split('/')
        if parts:
            usernames.append(parts[-1])

    return usernames


def find_unfollowers(followers, following):
    return sorted(set(following) - set(followers))


@app.route('/', methods=['GET', 'POST'])
def index():

    unfollowers = None

    if request.method == 'POST':

        followers_file = request.files['followers']
        following_file = request.files['following']

        followers_html = followers_file.read().decode('utf-8', errors='ignore')
        following_html = following_file.read().decode('utf-8', errors='ignore')

        followers = extract_followers(followers_html)
        following = extract_following(following_html)

        unfollowers = find_unfollowers(followers, following)

    return render_template('index.html', unfollowers=unfollowers)


if __name__ == '__main__':
    app.run()
