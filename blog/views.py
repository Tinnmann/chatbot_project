from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('tinbot', read_only = False, logic_adapters=[{
        'import_path':'chatterbot.logic.BestMatch',
        # 'default_response': 'Sorry, I am not sure what that means',
        # 'maximum_similarity_threshold':0.90
    }])

# training_list = [
#     "hi",
#     "hi, there",
#     "what's your name",
#     "I'm just a chatbot",
#     "what is your favourite food",
#     "I like pizza",
#     "what's your favourite sport",
#     "volleyball",
#     "do you have children",
#     "no"
# ]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

# list_trainer = ListTrainer(bot)
# list_trainer.train(training_list)

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)