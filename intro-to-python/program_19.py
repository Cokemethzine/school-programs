#Name: Josiel Perez
#Email: josiel.perez13@myhunter.cuny.edu
#Date: October 7, 2021
#This program will follow the pseudocode

user_followers = int(input("Enter amount of social media followers: "))

if  0 < user_followers  and user_followers < 1000:
    print(" Your influencer tier is: Hyper Influencer")

elif 1000 <= user_followers < 10000:
    print(" Your influencer tier is: Nano Influencer")

elif 10000 <= user_followers < 100000:
    print(" Your influencer tier is: Micro Influencer")

elif 100000 <= user_followers < 500000:
    print(" Your influencer tier is: Mid-Tier Influencer")

elif 500000 <= user_followers < 1000000:
    print(" Your influencer tier is: Macro-Influencer")

elif 1000000 <= user_followers:
    print(" Your influencer tier is: Celebrity Influencer")

else:
    print(" Your influencer tier is: Error")