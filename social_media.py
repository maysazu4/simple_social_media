from user import *
class SocialMediaPlatform:
    def __init__(self):
        """
        Initializes a SocialMediaPlatform object.
        """
        # self.users = []
        self.users = {}
    
    # old time: O(N)
    # new time: O(1) average , O(N) worst case(if element not found)
    def register_user(self, username):
        """
        Registers a new user in the social media platform.

        Args:
            username (str): The username of the new user.
        """
        # if not self._is_username_taken(username):
        #     user = User(username)
        #     # self.users.append(user)
        #     self.users[username] = user

        if self.users.get(username) is None:
            user = User(username)
            # self.users.append(user)
            self.users[username] = user


    def _is_username_taken(self, username):
        """
        Checks if a username is already taken.

        Args:
            username (str): The username to check.

        Returns:
            bool: True if the username is already taken, False otherwise.
        """
        for name,user in self.users.items():
            if name == username:
                return True
        return False

    # old time: O(N)
    # new time: O(1) average , O(N) worst case(if element not found)
    def get_user_by_username(self, username):
        """
        Retrieves a user object by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The User object corresponding to the username, or None if not found.
        """
        # for user in self.users:
        #     if user.username == username:
        #         return user
        return self.users[username]

    # N the number of users
    # m the number of posts for each user
    # M the number of all posts, M = m * N
    # Old time = O(N*M)
    # New time = O(N*m)
    

    def generate_timeline(self, username):
        """
        Generates a timeline for a given user.

        Args:
            username (str): The username of the user whose timeline is to be generated.

        Returns:
            list: A list of posts in the timeline.
        """
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user_name in user.following:
            followed_user = self.get_user_by_username(followed_user_name)
            for post in followed_user.posts:
                timeline.append(post)
        return timeline
