---
title: Research
nav:
  order: 1
  tooltip: Research directions and papers
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research

My research sits at the intersection of image analysis, musculoskeletal imaging, biomechanics, and scientific computing. I currently work on opportunistic CT for vertebral strength assessment and quality control, while continuing long-running work on HR-pQCT-based remodelling analysis, mechanoregulation, and spaceflight-related bone change.

{% include section.html %}

## Research Highlights

{% assign highlight_publications = site.data.orcid_publications | where_exp: "item", "item.first_author == true" %}
{% for item in highlight_publications %}
  {% include citation.html title=item.title subtitle=item.subtitle authors=item.authors publisher=item.publisher date=item.date id=item.id link=item.link image=item.image type=item.type description=item.description tags=item.tags %}
{% endfor %}

{% include section.html %}

## Publication List

{% assign publication_count = site.data.orcid_publications | size %}

{{ publication_count }} works

{% include search-box.html %}
{% include search-info.html %}

{% include list.html component="citation" data="orcid_publications" %}
