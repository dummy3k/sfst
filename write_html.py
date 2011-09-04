from mako.template import Template
from mako.lookup import TemplateLookup
from pprint import pprint

class EngagementRound():
    def __init__(self, name, col_span, engagements):
        self.name = name
        self.col_span = col_span
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



engagements = [EngagementRound('Quarter Finals', None, [
               Engagement('Quarter Finals Group A',
                          ('Machine', 'Sen'),
                          (Game('http://blip.tv/file/4534474', 'Sen'),
                           Game('http://blip.tv/file/4534449', 'Sen'))),
               Engagement('Quarter Finals Group B',
                          ('Taurent', 'Socke'),
                          (Game('http://blip.tv/file/4532165', '???'),
                           Game('http://blip.tv/file/4532121', '???'),
                           Game('http://blip.tv/file/4532105', '???'))),
               Engagement('Quarter Finals Group B',
                          ('Drewbie', 'DIMAGA'),
                          (Game('http://blip.tv/file/4528909', '???'),
                           Game('http://blip.tv/file/4528864', '???'),
                           Game('http://blip.tv/file/4528831', '???'))),
               Engagement('Quarter Finals Group B',
                          ('PainUser', 'White-Ra'),
                          (Game('http://blip.tv/file/4526152', '???'),
                           Game('http://blip.tv/file/4526112', '???'),
                           Game('http://blip.tv/file/4526041', '???')))]),
               EngagementRound('Semi Finals', 2, [
               Engagement('Semi Finals Group A',
                          ('White-Ra', 'DIMAGA'),
                          (Game('', 'White-Ra'),
                           Game('', 'White-Ra'))),
               Engagement('Semi Finals Group B',
                          ('Taurent', 'Sen'),
                          (Game('', '???'),
                           Game('', '???'),
                           Game('', '???')))]),
               EngagementRound('Semi Finals', 4, [
               Engagement('Semi Finals Group B',
                          ('Taurent', 'DIMAGA'),
                          (Game('', '???'),
                           Game('', '???'),
                           Game('', '???')))]),
               EngagementRound('Grand Finals', 4, [
               Engagement('Grand Finals Group B',
                          ('Sen', 'White-rA'),
                          (Game('', '???'),
                           Game('', '???'),
                           Game('', '???')))])]


mylookup = TemplateLookup(directories=['templates'])
#~ mytemplate = Template(filename='engagement_box.mako', lookup=mylookup)

#~ mytemplate = mylookup.get_template('engagement_box.mako')
#~ print mytemplate.render(c=engagements.engagements[1])
#~ print mytemplate.get_def('content').render(c=engagements.engagements[1])

#~ mytemplate = mylookup.get_template('engagement_round.mako')
#~ print mytemplate.render(c=engagements[1])

mytemplate = mylookup.get_template('engagements.mako')
print mytemplate.render(c=engagements)


