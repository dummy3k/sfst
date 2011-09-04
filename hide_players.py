import logging
import logging.config
import re
from pprint import pprint

if __name__ == '__main__':
    logging.config.fileConfig("logging.conf")

log = logging.getLogger(__name__)

videos = []

with open('episodes_rest2.py') as f:
    for line in f:
        #~ print line
        if not line.startswith('#'):
            videos.append(eval(line))

#~ player_names = ['Boxer', 'Taeja', 'White-rA', 'Huk', 'Idra', 'QXC',
                #~ 'Tester', 'DeMusliM', 'Naniwa', 'LiquidTyler', 'Socke',
                #~ 'LiquidTLO', 'LucifroN']
player_names = ['Moon', 'Dimaga', 'Jinro', '(T)', 'coLFireZerg', 'Tarson', 'Lalush', 'Happy', 'elfi', 'MaNa', 'ValiditySAGA', 'NullityCF', 'NOVAStalife', 'Qxc', 'ActionJesuz', 'Yelp', 'Huk:', 'aktails', 'Taeja', 'IntoTheRainbow', '(P)', 'Saikou', 'LiquidTyler', 'qxc', 'Naama', 'IntoTheRainBOw', 'Sjow', 'Tyler', 'Strelok', 'LaLush', 'Destiny', 'QXC', 'Haypro', 'oGsInCa', 'PainUser', 'Killer', 'ThorZaIN', 'White-Ra', 'Amazon', 'Facebook', 'July', 'Zelniq', '(Z)', 'Microsoft', 'Fenix', 'MC', 'oGsTOP', 'UCSD', 'Socke', 'TheDoctor', 'Vibe', 'HuK', 'BoxeR', 'Drewbie', 'Mardow', 'Core', 'DaBoO', 'Huk', 'Boxer', 'Zynga', 'Moosegills', 'Liquid', 'Idra', 'LucifroN', 'TLO', 'Duke', 'KawaiiRice', 'Twitter', 'Whitera', 'NTT', 'White-rA', 'MorroW', 'inuh', 'Sen', 'Bomber', 'FuRy', 'Machine', 'LiquidTLO', 'Taurent', 'XlorD', 'Adelscott', 'Tester', 'EmpireKas', 'TaeJa', 'DIMAGA', 'Grubby', 'Dropbox', 'PredY', 'MaDFroG', 'Ace', 'Sase', 'Google', 'Mana', 'GoOdy', 'RaNgeD', 'Loner', 'RunA', 'TheLittleOne']
player_names = sorted(player_names, lambda x,y: -cmp(len(x), len(y)))

tournaments = ['GSPA', 'EU vs Asia', 'College Starleague', 'ZOTAC13',
               'Fragster Showmatch', 'King of the Beta Day',
               'Day9 Countdown', 'King of the Beta',
               'SC2 Countdown Party', 'Wednesday Night Fights',
               'DreamHack SteelSeries', 'Root Gamings']



#~ pprint(videos)

def get_player_names():
    player_names = set()
    for video_id, url, text in videos:
        if len(re.findall(' vs ', text)) > 1:
            continue

        matches = re.findall('([^ ]+) vs ([^ ]+)', text)
        if len(matches) > 1:
            raise Exception('wtf')

        if len(matches) < 1:
            log.error(text)
            continue

        for item in matches[0]:
            player_names.add(item)

    print(player_names)

def do_othter():
    videos.reverse()
    for video_id, url, text in videos:
        #~ for player_name in player_names:
            #~ text = re.sub('^%s ' % player_name, '??? ', text, flags=re.IGNORECASE)
            #~ text = re.sub(' %s ' % player_name, ' ??? ', text, flags=re.IGNORECASE)

        #~ knwon_tournament = False
        #~ for tournament in tournaments:
            #~ if tournament in text:
                #~ knwon_tournament = True
                #~ break

        #~ if not knwon_tournament:
        if 'Root Gamings' in text:
            print "<a href='%s'>%s</a></br>" % (url, text)
        #~ print text

do_othter()

