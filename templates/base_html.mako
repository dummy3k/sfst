##<%def name="page()">
<html>
<head>
    <title>Spoiler Free Tournaments</title>
    <script type="text/javascript" src="static/jquery-1.6.2.min.js"></script>
</head>

<script type="text/javascript">

function change_content(el, new_text){
    el.fadeOut("slow", function(){
            el.html(new_text);
            el.fadeIn("slow");
        });
}

${self.javascript_head()}

</script>
<body>

${self.content(c)}

</body>
</html>
##</%def>
