from django.views.generic.base import TemplateView
from django.http import HttpResponse
from chatterbot import ChatBot
class ChatterBotAppView(TemplateView):
    template_name = "app.html"

def myview(request):

	# Create a new chat bot named Charlie
	bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.MathematicalEvaluation",
        "chatterbot.adapters.logic.TimeLogicAdapter",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    database="../../../../database.db"
	)
	# Get a response to the input "How are you?"
	response = bot.get_response("How are you?")
	return HttpResponse(response)
