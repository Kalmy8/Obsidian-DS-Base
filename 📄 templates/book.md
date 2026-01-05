---
# BASE (same as note.md)
type: book                    # book | note
status: todo                  # inbox | wip | pending | done
tags: []                      # topic tags
sources:                       # optional: links to book MOC
- "[[Book MOC]]"
authors:                      # authors of the book
- "[[{{authors}}]]"
start:
end:
recommendedby:
cover: {{coverURL}}
zotero: {{pdfZoteroLink}}
children:
---

{%-
    set zoteroColors = {
        "#2ea8e5": "blue",
        "#5fb236": "green",
        "#f19837": "orange",        
        "#ffd400": "yellow",
        "#a28ae5": "purple",
        "#ff6666": "red",
        "#aaaaaa": "grey",
        "#e56eee": "magenta"
    }
-%}

{%-
   set colorHeading = {
		"blue": "Blue",
		"green": "Green 💚 Key Ideas",
		"purple": "Purple 💭 Citations",
		"red": "Red",
		"yellow": "Yellow 🔃 Outer Links",
		"orange": "Orange 🔎 Reference data",
		"grey": "Grey",
		"magenta": "Magenta"
   }
-%}

{%- macro calloutHeader(type) -%}
    {%- switch type -%}
        {%- case "highlight" -%}
        Highlight
        {%- case "image" -%}
        Image
        {%- default -%}
        Note
    {%- endswitch -%}
{%- endmacro %}

{%- set newAnnot = [] -%}
{%- set newAnnotations = [] -%}
{%- set annotations = annotations | filterby("date", "dateafter", lastImportDate) %}

{%- for annot in annotations -%}
    {%- if annot.color in zoteroColors -%}
        {%- set customColor = zoteroColors[annot.color] -%}
    {%- elif annot.colorCategory|lower in colorHeading -%}
    	{%- set customColor = annot.colorCategory|lower -%}
    {%- else -%}
	    {%- set customColor = "other" -%}
    {%- endif -%}
    {%- set newAnnotations = (newAnnotations.push({"annotation": annot, "customColor": customColor}), newAnnotations) -%}
{%- endfor -%}

{%- for color, heading in colorHeading -%}
{%- for entry in newAnnotations | filterby ("customColor", "startswith", color) -%}
{%- set annot = entry.annotation -%}

{%- if entry and loop.first %}
# {{colorHeading[color]}}
{%- endif %}

> [!quote]+ {{calloutHeader(annot.type)}} ([Page {{annot.page}}]({{annot.desktopURI}}))

{%- if annot.annotatedText %}
> {{annot.annotatedText}} {% if annot.hashTags %}{{annot.hashTags}}{% endif -%}
{%- endif %}

{%- if annot.imageRelativePath %}
> ![[{{annot.imageRelativePath}}]]
{%- endif %}

{%- if annot.ocrText %}
> {{annot.ocrText}}
{%- endif %}

{%- if annot.comment %}
> - **{{annot.comment}}**
{%- endif -%}

{%- endfor -%}
{%- endfor -%}
