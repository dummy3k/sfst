<%inherit file="/base_html.mako"/>
<%! import json %>

<%def name="javascript_head()">
revealed = new Array();

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

$(document).ready(function() {
    $('a.reveal_blank').click(function(){
        id = $(this).attr('id');
        id_no = id.substr(5);
        console.log("id_no: " + id_no);
        eg.reveal_all(id_no);
    });
});
</%def>


<%def name="content(e)">
##<div>${e.name}</div>

<script type="text/javascript">
var eg = ${json.dumps(e.to_dict())}
eg.reveal = function(id_no) {
    console.log("id_no: " + id_no);
    if (id_no == eg.games[eg.games.length - 1].id) {
        this.reveal_all();
    } else {
        for (key in eg.games) {
            console.log(eg.games[key].id)
            reveal_result(eg.games[key].id);
            if (eg.games[key].id == id_no) {
                change_content($("#score1"), eg.games[key].score);
                break;
            }
        }
    }
};
eg.reveal_all = function() {
    console.log("this.id: " + this.id);
    for (key in eg.games) {
        console.log(eg.games[key].id)
        reveal_result(eg.games[key].id);
    }
    $("#egbox" + this.id).find("a.reveal_blank").css('display' , 'none');
    $("#egbox" + this.id).find("a.blank").css('text-decoration', 'line-through');
    $("#egbox" + this.id).find("a.blank").removeAttr('href');
    change_content($("#score" + this.id), eg.games[eg.games.length - 1].score);
};

</script>

<span id="egbox${e.id}">
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

% for n in range(len(e.games), e.best_of):
<div>
<span><a href="#" target="_blank" class="blank">Game ${n + 1}</a></span>
<span><a href="#" id="blank${e.id}" class="reveal_blank">Reveal</a></span>
</div>
% endfor
</span>

</%def>

