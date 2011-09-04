<div>
<span>${e.players[0]}</span>
<span>0 : 0</span>
<span>${e.players[1]}</span>
</div>

% for index, item in enumerate(e.games):
<div>
<span><a href="${item.url}">Game ${index + 1}</a></span>
<span><a href="#" id="reval${index + 1}" class="reveal_link">Reveal</a></span>
<span style='display:none' id="reval${index + 1}_result">Winner: ${item.winner}</span>
</div>

% endfor
