from mako.template import Template
from pprint import pprint

#~ Machine vs Sen Game 2 Quarter Finals of Root Gamings WARZONE
#~ Machine vs Sen Game 1 Quarter Finals of Root Gamings WARZONE

#~ Taurent vs Socke Game 3 Quarter Finals of Root Gamings WARZONE
#~ Taurent vs Socke Game 2 Quarter Finals of Root Gamings WARZONE
#~ Taurent vs Socke Game 1 Quarter Finals of Root Gamings WARZONE

class EngagementRound():
    def __init__(self, engagements):
        self.engagements = engagements

class Engagement():
    def __init__(self, name, players, games):
        self.players = players
        self.games = games

class Game():
    def __init__(self, url, winner):
        self.winner = winner
        self.url = url

engagements = EngagementRound([
               Engagement('Quarter Finals Group A',
                          ('Machine', 'Sen'),
                          (Game('http://blip.tv/file/4534474', 'Sen'),
                           Game('http://blip.tv/file/4534449', 'Sen'))),
               Engagement('Quarter Finals Group B',
                          ('Taurent', 'Socke'),
                          (Game('http://blip.tv/file/4532165', '???'),
                           Game('http://blip.tv/file/4532121', '???'),
                           Game('http://blip.tv/file/4532105', '???')))])


#~ print Template("hello ${data}!").render(data="world")

mytemplate = Template(filename='templates/engagement_box.mako')

#~ print mytemplate.render(e=engagements.engagements[1])


pprint(engagements)
