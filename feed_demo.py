"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    
    user1 = User('Roman')
    user2 = User('Hudson')
    users = [user1, user2]

    post1 = Tweet('Roman', 'Hello world! #firstpost')
    post2 = Tweet('Hudson', 'Excited to be here!')
    post3 = Tweet('Roman', 'Check out my new post!')
    posts = [post1, post2, post3]

    user1.follow()
    user1.unfollow()
    post1.like()
    post1.unlike()

    return users, posts

def main():
    # Call build_feed and display the returned objects and hashtags.

    users, posts = build_feed()
    for user in users:
        print(user)
    for post in posts:
        print(post)
        print(post.hashtags())

if __name__ == '__main__':
    main()
