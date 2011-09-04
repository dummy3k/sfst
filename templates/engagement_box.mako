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
%if item.predecessor:
<script type="text/javascript">
predecessor['reval${item.id}'] = 'reval${item.predecessor.id}';
</script>
%endif

% endfor
</%def>

<%def name="javascript_head()">
revealed = new Array();
predecessor = new Array();

$(document).ready(function(){
    $('a.reveal_link').click(function(){
        id = $(this).attr('id');
        reveal_result(id);
    });

    function reveal_result(id){
        if (revealed[id]) {
            console.log('id %d already revealed', id);
            return;
        }
        revealed[id] = true;
        console.log("reveal id: " + id);
        $("#" + id).fadeOut("slow", function(){
                $("#" + id + "_result").fadeIn("slow");
            });

        if (predecessor[id]) {
            reveal_result(predecessor[id]);
        }
    }
});

</%def>

