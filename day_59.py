# Day 59: Chat bot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name="PyBot", read_only=True,
                 logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])

small_talk = [
    "Hi there!",
    "Hi!",
    "How are you?",
    "I'm cool.",
    "Fine, you?",
    "Always cool",
    "I'm ok.",
    "Glad to hear that."
    "I feel awesome.",
    "Excellent, glad to hear that.",
    "Not so good.",
    "Sorry to hear that.",
    "What's your name?",
    "I'm Pybot. Ask me a math question, please."
]

math_talk1 = [
    "Pythagorean Theorem",
    "'A' squared plus 'B' squared equals 'C' squared.",
]

math_talk2 = [
    "Law of Cosines",
    "c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)"
]

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk1, math_talk2):
    list_trainer.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train("chatterbot.corpus.english")

while True:
    try:
        bot_input = input("You: ")
        bot_response = my_bot.get_response(bot_input)
        print(f"{my_bot.name}: {bot_response}")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
