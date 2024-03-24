import time 
from social_media import *
from user import *

def calculate_results(arg1,func):
    start_time = time.perf_counter()
    user = func(arg1)
    end_time = time.perf_counter()
    total_time = round(end_time-start_time,2)
    return total_time , user


if __name__=='__main__':
    with open('output1.txt', 'w') as file:
        platform = SocialMediaPlatform()
        # register users
        sum = 0
        for i in range(1, 100001):
            username = f"user{i}"
            time1,u = calculate_results(username, platform.register_user)
            sum += time1
     

        avg = sum/100000
        file.write(f"the time of register user is {avg}\n")

# Generate 1000 posts
        sum1 = 0
        sum2 = 0
        for i in range(1, 100001):
            username = f"user{i}"
            time1,user = calculate_results(username,platform.get_user_by_username)
            sum1 += time1
            if user:
                time2,u = calculate_results(f"This is post {i}",user.post_message)
                sum2 += 0
        avg1 = sum1/100000
        file.write(f"the Time of get user is {avg1}\n")
        avg2 = sum2/100000
        file.write(f"the time of post is {avg2}\n") 

        sum3 = 0
        for i in range(1, 100001):
            follower_username = f"user{i}"
            follower = platform.get_user_by_username(follower_username)
            if follower:
                followee_username = f"user{(i % 1000) + 1}"  # Rotate through users to follow
                time1,u = calculate_results(followee_username,follower.follow)
                sum3 += time1
        avg = sum3/100000
        file.write(f"the time of follow is {avg}\n")

        sum4 = 0
        for i in range(1, 100001):
            username = f"user{i}"
            user = platform.get_user_by_username(username)
            if user:
                time1,u = calculate_results(username,platform.generate_timeline)
                sum4 += time1
        avg = sum4/100000
        file.write(f"the time of generate timeline is {avg}\n")
    file.close()
            