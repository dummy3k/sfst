<%inherit file="/base_html.mako"/>
<%namespace name="box" file="/engagement_box.mako"/>

<%def name="javascript_head()">
${box.javascript_head()}
</%def>

<%def name="tr(r)">
<tr>
    <td>${r.name}</td>
% for item in r.engagements:
    %if r.col_span:
    <td colspan=${r.col_span}>
    %else:
    <td>
    %endif
        ${box.content(item)}</td>
% endfor
</%def>

<%def name="content(r)">
<table border="1">
${tr(r)}
</tr>
</table>
</%def>
