from mako.template import Template
from mako.lookup import TemplateLookup
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

        predecessor = None
        for item in self.games:
            if predecessor:
                item.predecessor = predecessor
            predecessor = item

class Game():
    __next_id__ = 1

    def __init__(self, url, winner):
        self.winner = winner
        self.url = url
        self.predecessor = None
        self.id = Game.__next_id__
        Game.__next_id__ += 1

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


mylookup = TemplateLookup(directories=['templates'])
#~ mytemplate = Template(filename='engagement_box.mako', lookup=mylookup)

#~ mytemplate = mylookup.get_template('engagement_box.mako')
#~ print mytemplate.render(c=engagements.engagements[1])
#~ print mytemplate.get_def('content').render(c=engagements.engagements[1])


mytemplate = mylookup.get_template('engagement_round.mako')
print mytemplate.render(c=engagements)


