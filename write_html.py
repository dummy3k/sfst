from mako.template import Template
from mako.lookup import TemplateLookup
from pprint import pprint

class EngagementRound():
    def __init__(self, col_span, engagements):
        self.name = None
        self.col_span = col_span
        self.engagements = engagements

class Engagement():
    __next_id__ = 1
    def __init__(self, players, games):
        self.id = Engagement.__next_id__
        Engagement.__next_id__ += 1

        self.name = None
        self.best_of = 5
        self.players = players
        self.games = games
        #~ self.predecessor = predecessor

        score = [0, 0]
        predecessor = None
        for item in self.games:
            #~ if predecessor:
                #~ item.predecessor.append(predecessor)
            #~ predecessor = item

            if item.winner == players[0]:
                score[0] += 1
            else:
                score[1] += 1

            item.score = "%s : %s" % (score[0], score[1])

    def to_dict(self):
        return {'name':self.name,
                'id':self.id,
                'games':map(lambda x: x.to_dict(), self.games)}

class Game():
    __next_id__ = 1

    def __init__(self, url, winner):
        self.id = Game.__next_id__
        Game.__next_id__ += 1

        self.winner = winner
        self.url = url
        self.predecessor = []
        self.score = None

    def to_dict(self):
        return {'id':self.id, 'url':self.url, 'winner':self.winner,
                'score':self.score}

engagements = {'Quarter Finals Group A':Engagement(('Machine', 'Sen'),
                              (Game('http://blip.tv/file/4534474', 'Sen'),
                               Game('http://blip.tv/file/4534449', 'Sen'))),
               'Quarter Finals Group B':Engagement(('Taurent', 'Socke'),
                              (Game('http://blip.tv/file/4532165', 'Socke'),
                               Game('http://blip.tv/file/4532121', 'Taurent'),
                               Game('http://blip.tv/file/4532105', 'Socke'))),
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

        self.engagement = args[0]

rounds = {'Quarter Finals':EngagementRound(None, [
            Dependency(engagements['Quarter Finals Group A']),
            Dependency(engagements['Quarter Finals Group B']),
            Dependency(engagements['Quarter Finals Group C']),
            Dependency(engagements['Quarter Finals Group D'])]),
         'Semi Finals':EngagementRound(2, [
            Dependency(engagements['Semi Finals Group A'],
                'Quarter Finals Group A', 'Quarter Finals Group B'),
            Dependency(engagements['Semi Finals Group B'],
                'Quarter Finals Group C', 'Quarter Finals Group D')])
            #~ ('Semi Finals Group A',
                #~ Dependency('Quarter Finals Group A', 'Quarter Finals Group B')),
            #~ ('Semi Finals Group B',
                #~ Dependency('Quarter Finals Group C', 'Quarter Finals Group D'))]),
         #~ 'Consolation Finals':EngagementRound(4,
            #~ [('Consolation Finals',
                #~ Dependency('Semi Final', loser=True))]),
         #~ 'Grand Finals':EngagementRound(4,
            #~ [('Grand Finals',
                #~ Dependency('Semi Final'))])
        }

for k, v in engagements.items():
    v.name = k
for k, v in rounds.items():
    v.name = k

#~ print(rounds.keys())
##~ mytemplate = Template(filename='engagement_box.mako', lookup=mylookup)
mylookup = TemplateLookup(directories=['templates'])

#~ import json
#~ print json.dumps(Game('', '???'))
#~ print json.dumps(('', '???'))
#~ print json.dumps({'foo':1, 'bar':2})
#~ print Game('', '???').to_dict()
#~ pprint(engagements['Quarter Finals Group B'].to_dict())
#~ pprint(json.dumps(engagements['Quarter Finals Group B'].to_dict()))

#~ mytemplate = mylookup.get_template('engagement_box.mako')
#~ print mytemplate.render(c=engagements['Quarter Finals Group A'])
#~ print mytemplate.get_def('content').render(e=engagements['Quarter Finals Group A'])
##~ print mytemplate.render(c=engagements.engagements[1])

mytemplate = mylookup.get_template('engagement_round.mako')
print mytemplate.render(c=rounds['Quarter Finals'])
#~ print mytemplate.get_def('tr').render(r=rounds['Quarter Finals'])

#~ mytemplate = mylookup.get_template('engagements.mako')
#~ print mytemplate.render(c=rounds.values())
#~ print mytemplate.render(c=engagements)


