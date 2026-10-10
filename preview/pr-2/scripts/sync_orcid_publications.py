#!/usr/bin/env python3

import json
import re
import subprocess
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urljoin


ORCID = "0000-0003-3250-8143"
URL = f"https://pub.orcid.org/v3.0/{ORCID}/works"
DATA_DIR = Path(__file__).resolve().parents[1] / "_data"
PUBLICATIONS_OUT = DATA_DIR / "orcid_publications.json"
DATASETS_OUT = DATA_DIR / "orcid_datasets.json"

PUBLICATION_TYPES = {
    "journal-article",
}

DATASET_TYPES = {
    "data-set",
    "dataset",
    "software",
    "online-resource",
    "physical-object",
    "research-technique",
}

FEATURED_TITLE_SNIPPETS = (
    "Comparing linear and nonlinear finite element models of vertebral strength",
    "Tracking of spaceflight-induced bone remodeling reveals a limited time frame",
    "Bone remodeling and responsiveness to mechanical stimuli in individuals with type 1 diabetes mellitus",
    "A multi-stack registration technique to improve measurement accuracy and precision across longitudinal HR-pQCT scans",
    "Precision of bone mechanoregulation assessment",
)

FEATURED_IMAGE_OVERRIDES = {
    "Comparing linear and nonlinear finite element models of vertebral strength across the thoracolumbar spine: a benchmark from density-calibrated computed tomography": "https://opengraph.githubassets.com/1/Bonelab/spineFE-benchmark",
    "Tracking of spaceflight-induced bone remodeling reveals a limited time frame for recovery of resorption sites in humans": "https://raw.githubusercontent.com/wallematthias/TimelapsedHRpQCT/main/assets/TimelapsedHRpQCT-logo.png",
    "Bone remodeling and responsiveness to mechanical stimuli in individuals with type 1 diabetes mellitus": "https://raw.githubusercontent.com/wallematthias/TimelapsedHRpQCT/main/assets/TimelapsedHRpQCT-logo.png",
    "A multi-stack registration technique to improve measurement accuracy and precision across longitudinal HR-pQCT scans": "https://opengraph.githubassets.com/1/wallematthias/MultistackRegistration",
    "Precision of bone mechanoregulation assessment in humans using longitudinal high-resolution peripheral quantitative computed tomography in vivo": "https://raw.githubusercontent.com/wallematthias/TimelapsedHRpQCT/main/assets/TimelapsedHRpQCT-logo.png",
}


def get_value(node, *keys):
    for key in keys:
        if not isinstance(node, dict):
            return None
        node = node.get(key)
    return node


def format_date(node):
    year = get_value(node, "year", "value")
    month = get_value(node, "month", "value") or "01"
    day = get_value(node, "day", "value") or "01"
    if not year:
        return None
    return f"{year}-{month}-{day}"


def type_tag(work_type):
    return (work_type or "work").replace("_", "-")


def is_featured(title):
    lowered = title.lower()
    return any(snippet.lower() in lowered for snippet in FEATURED_TITLE_SNIPPETS)


def fetch_html(url):
    try:
        result = subprocess.run(
            ["curl", "-L", "-s", "-A", "Mozilla/5.0", url],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except Exception:
        return ""
    body = result.stdout
    return body if "<html" in body.lower() else ""


def extract_meta_image(html, base_url):
    if not html:
        return None
    patterns = (
        r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',
        r'<meta[^>]+name="twitter:image"[^>]+content="([^"]+)"',
        r'<meta[^>]+name="citation_figure"[^>]+content="([^"]+)"',
        r'<meta[^>]+name="citation_image"[^>]+content="([^"]+)"',
        r"<meta[^>]+property='og:image'[^>]+content='([^']+)'",
        r"<meta[^>]+name='twitter:image'[^>]+content='([^']+)'",
        r'<img[^>]+src="([^"]+\.(?:png|jpg|jpeg|webp|gif))"',
        r"<img[^>]+src='([^']+\.(?:png|jpg|jpeg|webp|gif))'",
    )
    for pattern in patterns:
        match = re.search(pattern, html, flags=re.IGNORECASE)
        if match:
            candidate = urljoin(base_url, match.group(1))
            if "favicon" not in candidate.lower() and "logo" not in candidate.lower():
                return candidate
    return None


def resolve_publication_image(link):
    if not link:
        return None
    try:
        html = fetch_html(link)
    except Exception:
        return None
    return extract_meta_image(html, link)


def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", "", title.lower())


def dedupe_records(records):
    grouped = {}
    for record in records:
        key = normalize_title(record["title"])
        current = grouped.get(key)
        if current is None:
            grouped[key] = record
            continue

        current_score = (
            int("journal-article" in current.get("tags", [])),
            int(bool(current.get("link"))),
            current.get("date", ""),
        )
        new_score = (
            int("journal-article" in record.get("tags", [])),
            int(bool(record.get("link"))),
            record.get("date", ""),
        )
        if new_score > current_score:
            grouped[key] = record

    return list(grouped.values())


def fetch():
    request = urllib.request.Request(
        URL,
        headers={"Accept": "application/vnd.orcid+json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_work_detail(put_code):
    request = urllib.request.Request(
        f"https://pub.orcid.org/v3.0/{ORCID}/work/{put_code}",
        headers={"Accept": "application/vnd.orcid+json"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def extract_authors(work):
    authors = []
    for contributor in get_value(work, "contributors", "contributor") or []:
        role = get_value(contributor, "contributor-attributes", "contributor-role")
        if role and role.lower() != "author":
            continue
        name = get_value(contributor, "credit-name", "value")
        if name:
            authors.append(name)
    return authors


def is_first_author(authors):
    if not authors:
        return False
    first = authors[0].strip().lower()
    return first in {
        "matthias walle",
        "m. walle",
        "walle",
    }


def extract_doi(work):
    for ext_id in get_value(work, "external-ids", "external-id") or []:
        if (ext_id.get("external-id-type") or "").lower() == "doi":
            return ext_id.get("external-id-value")
    return None


def fetch_crossref_metadata(doi):
    if not doi:
        return {}
    url = f"https://api.crossref.org/works/{doi}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except Exception:
        return {}
    return payload.get("message") or {}


def crossref_authors(message):
    names = []
    for author in message.get("author", []):
        given = (author.get("given") or "").strip()
        family = (author.get("family") or "").strip()
        full = " ".join(part for part in (given, family) if part).strip()
        if full:
            names.append(full)
    return names


def make_record(summary, detail):
    title = get_value(detail, "title", "title", "value") or get_value(summary, "title", "title", "value")
    if not title:
        return None

    journal = get_value(detail, "journal-title", "value") or get_value(summary, "journal-title", "value")
    work_type = detail.get("type") or summary.get("type")
    published = format_date(detail.get("publication-date") or summary.get("publication-date") or {})
    year = published[:4] if published else "undated"
    doi = extract_doi(detail)
    link = get_value(detail, "url", "value") or (f"https://doi.org/{doi}" if doi else None)
    authors = extract_authors(detail)
    crossref = fetch_crossref_metadata(doi) if doi and not authors else {}
    if not authors:
        authors = crossref_authors(crossref)
    if not journal:
        journal = (
            (crossref.get("container-title") or [None])[0]
            or (crossref.get("publisher") or None)
        )
    first_author = is_first_author(authors)

    if journal:
        subtitle = f"{journal} ({year})"
    else:
        subtitle = f"{(work_type or 'work').replace('-', ' ').title()} ({year})"

    featured = is_featured(title)
    record = {
        "title": title,
        "subtitle": subtitle,
        "description": "",
        "link": link,
        "date": published or str(date.today()),
        "authors": authors,
        "publisher": journal or (work_type or "work").replace("-", " ").title(),
        "id": f"doi:{doi}" if doi else (work_type or "work"),
        "type": "paper" if work_type in PUBLICATION_TYPES else "data",
        "tags": [type_tag(work_type), "orcid"],
        "featured": featured,
        "first_author": first_author,
    }
    if featured:
        image = resolve_publication_image(link)
        record["image"] = image or FEATURED_IMAGE_OVERRIDES.get(title) or "images/photo.png"
    return record


def transform(data):
    publications = []
    datasets = []
    for group in data.get("group", []):
        summaries = group.get("work-summary", [])
        if not summaries:
            continue

        work = summaries[0]
        detail = fetch_work_detail(work["put-code"])
        record = make_record(work, detail)
        if not record:
            continue

        work_type = detail.get("type") or work.get("type")
        if not record.get("authors"):
            continue
        if work_type in PUBLICATION_TYPES:
            publications.append(record)
        if work_type in DATASET_TYPES:
            datasets.append(record)

    publications = dedupe_records(publications)
    datasets = dedupe_records(datasets)
    publications.sort(key=lambda item: item["date"], reverse=True)
    datasets.sort(key=lambda item: item["date"], reverse=True)
    return publications, datasets


def main():
    data = fetch()
    publications, datasets = transform(data)
    PUBLICATIONS_OUT.write_text(json.dumps(publications, indent=2) + "\n")
    DATASETS_OUT.write_text(json.dumps(datasets, indent=2) + "\n")
    print(f"Wrote {len(publications)} ORCID publications to {PUBLICATIONS_OUT}")
    print(f"Wrote {len(datasets)} ORCID datasets/software records to {DATASETS_OUT}")


if __name__ == "__main__":
    main()
