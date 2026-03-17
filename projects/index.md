---
title: Projects
nav:
  order: 2
  tooltip: Software and pipelines
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

These projects reflect the way I approach scientific computing: build tools that are methodologically serious, realistic about messy imaging data, and practical enough that collaborators can run them, inspect them, and extend them.

{% include tags.html tags="software, imaging, hr-pqct, ct, slicer" %}

{% include search-info.html %}

{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include section.html %}

## More Work

{% assign more_projects = site.data.projects | where_exp: "item", "item.group != 'featured'" %}
{% for item in more_projects %}
  {% include citation.html title=item.title subtitle=item.subtitle publisher=item.repo date="" id="" link=item.link description=item.description tags=item.tags style="rich" %}
{% endfor %}

{% include section.html %}

## Data

Some project outputs also ship with public datasets and benchmark resources. The current public dataset section lives on the [Datasets](../datasets/) page and is set up to expand over time.
