from bs4 import BeautifulSoup

followers = 'instagram-wizrd25-2025-12-01-IwfJ4AY4/connections/followers_and_following/followers_1.html'
following = 'instagram-wizrd25-2025-12-01-IwfJ4AY4/connections/followers_and_following/following.html'

with open(followers, 'r', encoding='utf-8') as f:
    followers_content = f.read()
    print("followers content successfully read into a variable.")
with open(following, 'r', encoding='utf-8') as f:
    following_content = f.read()
    print("following content successfully read into a variable.")
    # print(followers_content)
    # print(following_content)

soup_followers = BeautifulSoup(followers_content, 'html.parser') 
soup_following = BeautifulSoup(following_content, 'html.parser')

all_followers = [a.get_text() for a in soup_followers.find_all('a')]
all_a_tags_following = [a.get_text() for a in soup_following.find_all('a')]

def extract_username_from_link(link_url):
    # Split the URL by '/' and take the second-to-last part (the username)
    parts = link_url.strip('/').split('/')
    # The username should be the last element after splitting off potential trailing slashes
    return parts[-1]

# Convert the list of links into a list of usernames
all_following_usernames = [extract_username_from_link(link) for link in all_a_tags_following]

followers_set = set(all_followers)
following_set = set(all_following_usernames)

def find_unfollowers(followers_set, following_set):
    unfollowers = following_set - followers_set
    return unfollowers

unfollowers = find_unfollowers(followers_set, following_set)
print("Users who do not follow back:")
for user in unfollowers:
    print(user)