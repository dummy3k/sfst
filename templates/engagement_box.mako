<%inherit file="/base_html.mako"/>
<%! import json %>

<%def name="javascript_head()">
revealed = new Array();
##predecessor = new Array();
##reval_actions = new Array();
##scores = new Array();

function reveal_result(id){
    if (revealed[id]) {
        console.log('id %d already revealed', id);
        return;
    }
    revealed[id] = true;
    console.log("reveal id: " + id);
    $("#reval" + id).fadeOut("slow", function(){
            $("#reval" + id + "_result").fadeIn("slow");
        });
}

$(document).ready(function(){
    $('a.reveal_link').click(function(){
        id = $(this).attr('id');
        id_no = id.substr(5);
        eg.reveal(id_no);
    });

});



</%def>


<%def name="content(e)">
##<div>${e.name}</div>

<script type="text/javascript">
var eg = ${json.dumps(e.to_dict())}
eg.reveal = function(id_no) {
    console.log("id_no: " + id_no);
    for (key in eg.games) {
        console.log(eg.games[key].id)
        reveal_result(eg.games[key].id);
        if (eg.games[key].id == id_no) {
            change_content($("#score2"), eg.games[key].score);
            break;
        }
    }
};
</script>

<div>
<span>${e.players[0]}</span>
<span id="score${e.id}">0 : 0</span>
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

