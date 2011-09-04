<%inherit file="/base_html.mako"/>
<%namespace name="box" file="/engagement_box.mako"/>

<%def name="javascript_head()">
${box.javascript_head()}
</%def>

<%def name="content(r)">
% for item in r.engagements:
${box.content(item)}
% endfor
</%def>
