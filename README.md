# Social Media Platform

This is a simple implementation of a social media platform where users can register, follow other users, post messages, and generate timelines.

## Functionality

### User Registration:
Users can register for the social media platform by providing a unique username. 

```python
from user import SocialMediaPlatform

platform = SocialMediaPlatform()
platform.register_user("username")
```
### How to Use
Initialize the social media platform.
Register users using unique usernames.
Users can follow other users and post messages.
Generate timelines to view posts from followed users.

### Social Media Platform Flow:

#### User Registration:

Users can register for the social media platform by providing a unique username.
The register_user function in the SocialMediaPlatform class handles user registration by creating a new User object with the provided username.

#### Following Users:

Users can follow other users to see their posts on their timeline.
The follow method in the User class allows a user to follow another user.

#### Posting Messages:

Users can post messages on the platform.
The post_message method in the User class allows a user to post a message, which is stored in a global list named posts.

#### Generating Timeline:

Users can generate a timeline to see posts from users they follow.
The generate_timeline method in the SocialMediaPlatform class generates a timeline for a given user by aggregating posts from the users they follow.
