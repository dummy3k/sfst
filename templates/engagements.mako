<%inherit file="/base_html.mako"/>
<%namespace name="round" file="/engagement_round.mako"/>

<%def name="javascript_head()">
${round.javascript_head()}
</%def>

<%def name="content(c)">
<table border="1">
%for item in c:
${round.tr(item)}
%endfor
</table>
</%def>
