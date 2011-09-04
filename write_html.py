from mako.template import Template
from mako.lookup import TemplateLookup
from pprint import pprint

class EngagementRound():
    def __init__(self, col_span, engagements):
        #~ self.name = name
        self.col_span = col_span
        self.engagements = engagements

class Engagement():
    def __init__(self, players, games, predecessor=None):
        #~ self.name = name
        self.players = players
        self.games = games
        self.predecessor = predecessor

        #~ predecessor = None
        #~ for item in self.games:
            #~ if predecessor:
                #~ item.predecessor = predecessor
            #~ predecessor = item

class Game():
    __next_id__ = 1

    def __init__(self, url, winner):
        self.winner = winner
        self.url = url
        self.predecessor = []
        self.id = Game.__next_id__
        Game.__next_id__ += 1

Game('http://blip.tv/file/4534449', 'Sen')

engagements = {'Quarter Finals Group A':Engagement(('Machine', 'Sen'),
                              (Game('http://blip.tv/file/4534474', 'Sen'),
                               Game('http://blip.tv/file/4534449', 'Sen'))),
               'Quarter Finals Group B':Engagement(('Taurent', 'Socke'),
                              (Game('http://blip.tv/file/4532165', '???'),
                               Game('http://blip.tv/file/4532121', '???'),
                               Game('http://blip.tv/file/4532105', '???'))),
               'Quarter Finals Group C':Engagement(('Drewbie', 'DIMAGA'),
                              (Game('http://blip.tv/file/4528909', '???'),
                               Game('http://blip.tv/file/4528864', '???'),
                               Game('http://blip.tv/file/4528831', '???'))),
               'Quarter Finals Group D':Engagement(('PainUser', 'White-Ra'),
                              (Game('http://blip.tv/file/4526152', '???'),
                               Game('http://blip.tv/file/4526112', '???'),
                               Game('http://blip.tv/file/4526041', '???'))),
               'Semi Finals Group A':Engagement(('White-Ra', 'DIMAGA'),
                              (Game('', 'White-Ra'),
                               Game('', 'White-Ra'))),
               'Semi Finals Group B':Engagement(('Taurent', 'Sen'),
                              (Game('', '???'),
                               Game('', '???'),
                               Game('', '???'))),
               'Consolation Finals':Engagement(('Taurent', 'DIMAGA'),
                          (Game('', '???'),
                           Game('', '???'),
                           Game('', '???'))),
               'Grand Finals':Engagement(('Sen', 'White-rA'),
                          (Game('', '???'),
                           Game('', '???'),
                           Game('', '???')))}

#   ('Quarter Finals Group A', 'Quarter Finals Group B')
#~ Consolation Finals of Root Gamings WARZONE

class Dependency():
    def __init__(self, *args, **kwargs):
        if 'loser' in kwargs:
            self.loser = kwargs['loser']
        else:
            self.loser = False

rounds = {'Quarter Finals':EngagementRound(None, [
            'Quarter Finals Group A',
            'Quarter Finals Group B',
            'Quarter Finals Group C',
            'Quarter Finals Group D']),
         'Semi Finals':EngagementRound(2, [
            ('Semi Finals Group A',
                Dependency('Quarter Finals Group A', 'Quarter Finals Group B')),
            ('Semi Finals Group B',
                Dependency('Quarter Finals Group C', 'Quarter Finals Group D'))]),
         'Consolation Finals':EngagementRound(4,
            [('Consolation Finals',
                Dependency('Semi Final', loser=True))]),
         'Grand Finals':EngagementRound(4,
            [('Grand Finals',
                Dependency('Semi Final'))])}

#~ engagements = [EngagementRound('Quarter Finals', None, [
               #~ EngagementRound('Semi Finals', 2, [
               #~ EngagementRound('Semi Finals', 4, [
               #~ EngagementRound('Grand Finals', 4, [
#~ print(rounds.keys())
##~ mytemplate = Template(filename='engagement_box.mako', lookup=mylookup)
mylookup = TemplateLookup(directories=['templates'])

mytemplate = mylookup.get_template('engagement_box.mako')
##~ print mytemplate.render(c=engagements.engagements[1])
print mytemplate.get_def('content').render(e=engagements['Quarter Finals Group A'])

##~ mytemplate = mylookup.get_template('engagement_round.mako')
##~ print mytemplate.render(c=engagements[1])

##~ mytemplate = mylookup.get_template('engagements.mako')
##~ print mytemplate.render(c=engagements)


