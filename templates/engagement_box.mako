<%inherit file="/base_html.mako"/>

<%def name="content(e)">
<div>
<span>${e.players[0]}</span>
<span>0 : 0</span>
<span>${e.players[1]}</span>
</div>

% for index, item in enumerate(e.games):
<div>
<span><a href="${item.url}" target="_blank">Game ${index + 1}</a></span>
<span><a href="#" id="reval${item.id}" class="reveal_link">Reveal</a></span>
<span style='display:none' id="reval${item.id}_result">Winner: ${item.winner}</span>
</div>

% endfor
</%def>

<%def name="ready_javascript()">
$('a.reveal_link').click(function(){
    id = $(this).attr('id');
    $(this).fadeOut("slow", function(){
            $("#" + id + "_result").fadeIn("slow");
        });
});
</%def>

