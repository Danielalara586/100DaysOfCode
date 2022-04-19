# Day 73: Story Generator

import random

names = ['Daniela', 'Paola', 'Diego', 'Pablo', 'Jose', 'Carlos', 'Emily', 'Mariana']
places = ['Italy', 'France', 'Mexico', 'Canada', 'Argentina', 'United Kingdom']
quests = ['find the most beautiful bird of the city', 'drive all across the country to save a friend', 'train hard enough to defeat the class bully',
          'win a marathon and pursue the dream of being a runner']
roles = ['normal person', 'teenager', 'high-school student', 'college student', 'Starbucks worker']
weather = ['a sunny day', 'a very humid and hot day', 'a cold night', 'a cloudy day', 'a rainy day']

random_name = random.choice(names)
random_place = random.choice(places)
random_quest = random.choice(quests)
random_roles = random.choice(roles)
random_weather = random.choice(weather)

story = f'Once upon a time a {random_roles} called {random_name} lived in a beautiful placed called {random_place}. \n'\
        f'It was {random_weather} when {random_name} decided to {random_quest}.'

print(story)
