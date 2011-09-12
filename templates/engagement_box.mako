<%inherit file="/base_html.mako"/>
<%! import json %>

<%def name="javascript_head()">
revealed = new Array();
engagments = new Array();
id_to_eg = new Array();

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
        //eg.reveal(id_no);
        id_to_eg[id_no].reveal(id_no);
    });

});

$(document).ready(function() {
    $('a.reveal_blank').click(function(){
        id = $(this).attr('id');
        id_no = id.substr(5);
        console.log("id_no: " + id_no);
//        eg.reveal_all(id_no);
        id_to_eg[id_no].reveal_all(id_no);
    });
});

function Engagement(data) {
    console.log("hi there: " + data.games);
    this.data = data;
    this.games = data.games;
};

Engagement.prototype.reveal = function(id_no) {
    console.log("id_no: " + id_no);
    if (id_no == this.games[this.games.length - 1].id) {
        this.reveal_all();
    } else {
        for (key in this.games) {
            console.log(this.games[key].id)
            reveal_result(this.games[key].id);
            if (this.games[key].id == id_no) {
                change_content($("#score1"), this.games[key].score);
                break;
            }
        }
    }
};

Engagement.prototype.reveal_all = function() {
    console.log("this.id: " + this.id);
    for (key in this.games) {
        console.log(this.games[key].id)
        reveal_result(this.games[key].id);
    }
    $("#egbox" + this.id).find("a.reveal_blank").css('display' , 'none');
    $("#egbox" + this.id).find("a.blank").css('text-decoration', 'line-through');
    $("#egbox" + this.id).find("a.blank").removeAttr('href');
    change_content($("#score" + this.id), this.games[this.games.length - 1].score);
};

</%def>


<%def name="content(e)">
##<div>${e.name}</div>


<a href="javascript:alert('hi');" >Say hi!</a>
<script type="text/javascript">
var eg = new Engagement(${json.dumps(e.to_dict())});
engagments.push(${json.dumps(e.to_dict())});


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
##<span><a href="#" id="reval${item.id}" class="reveal_link">Reveal</a></span>
<span><a href="javascript:reveal(${e.id}, ${index});" id="reval${item.id}">Reveal</a></span>
<span style='display:none' id="reval${item.id}_result">Winner: ${item.winner}</span>
</div>

<script type="text/javascript">
id_to_eg[${item.id}] = eg;
</script>

% endfor

<script type="text/javascript">
id_to_eg[${e.id}] = eg;
</script>

% for n in range(len(e.games), e.best_of):
<div>
<span><a href="#" target="_blank" class="blank">Game ${n + 1}</a></span>
<span><a href="#" id="blank${e.id}" class="reveal_blank">Reveal</a></span>
</div>
% endfor
</span>

</%def>

