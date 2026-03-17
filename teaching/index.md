---
title: Teaching
nav:
  order: 4
  tooltip: Teaching materials and course repositories
redirect_from:
  - /blog/
---

# {% include icon.html icon="fa-solid fa-chalkboard-user" %}Teaching

This page gathers public teaching materials and course repositories connected to my teaching work.

{% include tags.html tags="teaching, coursework, modelling, simulation" %}

{% include section.html %}

## Teaching Experience

<div class="profile-list">
  <article class="profile-item">
    <div class="profile-meta">2025</div>
    <div class="profile-body">
      <h3>Lecturer, OsNET Summer School</h3>
      <p class="profile-affiliation">University of Calgary</p>
      <p>Prepared and helped implement the first OsNET Summer School, including two lecture sessions for approximately 40 students.</p>
    </div>
  </article>
  <article class="profile-item">
    <div class="profile-meta">2020-2023</div>
    <div class="profile-body">
      <h3>Senior Teaching Assistant, Imaging and Computing in Medicine</h3>
      <p class="profile-affiliation">ETH Zurich</p>
      <p>Prepared and taught six flipped-classroom sessions, coordinated undergraduate tutors, and managed the Moodle page for a course with roughly 200 students.</p>
    </div>
  </article>
  <article class="profile-item">
    <div class="profile-meta">2021</div>
    <div class="profile-body">
      <h3>Examiner, Orthopaedic Biomechanics</h3>
      <p class="profile-affiliation">ETH Zurich</p>
      <p>Conducted oral examinations for bachelor students on musculoskeletal engineering, structural mechanics, and orthopaedic design.</p>
    </div>
  </article>
  <article class="profile-item">
    <div class="profile-meta">2016-2017</div>
    <div class="profile-body">
      <h3>Teaching Assistant, Principles of Modern Information Technology I and II</h3>
      <p class="profile-affiliation">TU Munich</p>
      <p>Developed and presented exercises on modern information technology for large engineering student cohorts.</p>
    </div>
  </article>
</div>

{% include section.html %}

## Guest Lectures

<div class="profile-list">
  <article class="profile-item">
    <div class="profile-meta">2024</div>
    <div class="profile-body">
      <h3>Modelling and Simulations</h3>
      <p class="profile-affiliation">Medical Imaging Applications, University of Calgary</p>
      <p>Guest lecture on modelling and simulation methods in medical imaging.</p>
    </div>
  </article>
  <article class="profile-item">
    <div class="profile-meta">2023</div>
    <div class="profile-body">
      <h3>Bones Under Pressure</h3>
      <p class="profile-affiliation">Mechanobiology, Boise State University</p>
      <p>Guest lecture on how mechanical forces influence bone remodelling in diabetes.</p>
    </div>
  </article>
</div>

{% include section.html %}

## Course Materials

{% for item in site.data.teaching %}
  {% include citation.html title=item.title subtitle=item.subtitle publisher=item.repo date="" id="" link=item.link description=item.description tags=item.tags style="rich" %}
{% endfor %}
