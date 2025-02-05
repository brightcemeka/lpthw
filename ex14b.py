from sys import argv

script, user_name, profession = argv
prompt = ':: '

print(f"Hi {profession}, {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you love your job {user_name}?")
response = input(prompt)

print(f"Where do you live {user_name}?")
residence = input(prompt)

print("What's your favorite sports team?")
favorite_team = input(prompt)

print(f"""
Alright, so {user_name} says, {response} about liking what he does.
{user_name} lives in {residence}. Not sure where that is.
And {user_name}'s favorite sport's team is {favorite_team}, Nice!!!
""")