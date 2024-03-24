class User:
    def __init__(self, username):
        """
        Initializes a User object with a username.

        Args:
            username (str): The username of the user.
        """
        self.username = username
        self.following = []
        self.posts = []

    def follow(self, other_user):
        """
        Allows a user to follow another user.

        Args:
            other_user (str): The username of the user to follow.
        """
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message):
        """
        Allows a user to follow another user.

        Args:
            other_user (str): The username of the user to follow.
        """
        post = {'username': self.username, 'message': message}
        self.posts.append(post)


