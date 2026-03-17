---
title: Datasets
nav:
  order: 4
  tooltip: Public datasets and releases
---

# {% include icon.html icon="fa-solid fa-database" %}Datasets

This page lists public datasets and related releases connected to my work.

{% include tags.html tags="zenodo, dataset, ct, imaging" %}

{% include section.html %}

## Dataset List

{% assign datasets = site.data.orcid_datasets | sort: "date" | reverse %}
{% for item in datasets %}
  {% include citation.html title=item.title subtitle=item.subtitle authors=item.authors publisher=item.publisher date=item.date id=item.id link=item.link type=item.type description=item.description tags=item.tags %}
{% endfor %}
