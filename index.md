---
---

<div class="home-hero">
  <div class="home-hero-copy">
    <span class="home-kicker">Bone Imaging, Biomechanics, AI, And Scientific Software</span>
    <h1>Matthias Walle, PhD</h1>
    <p class="home-lead">
      I am a postdoctoral associate at the McCaig Institute, University of Calgary. My work connects mechanobiology, musculoskeletal imaging, and computational methods, with a focus on longitudinal HR-pQCT, opportunistic CT, vertebral strength assessment, and translational research software that stays useful beyond a single paper.
    </p>
    <p class="home-lead">
      Before Calgary, I completed my doctorate at ETH Zurich on mechanoregulation of bone remodelling in diabetes. Across projects, I build imaging methods, quantitative pipelines, and open tools that help turn complex skeletal data into interpretable, reproducible measurements.
    </p>
    <div class="home-actions">
      {% include button.html link="research" text="Research" %}
      {% include button.html link="projects" text="Projects" %}
      {% include button.html link="datasets" text="Datasets" %}
      {% include button.html type="github" text="GitHub" link="wallematthias" %}
    </div>
  </div>

  <a class="home-portrait-card" href="{{ '/team/' | relative_url }}">
    <img src="{{ '/images/MatthiasWalle.png' | relative_url }}" alt="Matthias Walle">
    <div class="home-portrait-note">
      <strong>About Matthias Walle</strong>
      <span>Postdoctoral associate at the McCaig Institute working across bone imaging, biomechanics, AI, and open scientific software.</span>
    </div>
  </a>
</div>

{% include section.html %}

<div class="home-strip">
  <div class="home-strip-card">
    <span class="home-strip-label">Mechanobiology</span>
    <p>Methods for mapping bone formation and resorption relative to local mechanical environment.</p>
  </div>
  <div class="home-strip-card">
    <span class="home-strip-label">Clinical Translation</span>
    <p>Applications in altered loading, metabolic disease, spaceflight, fracture healing, and routine CT.</p>
  </div>
  <div class="home-strip-card">
    <span class="home-strip-label">Software</span>
    <p>Open pipelines, CLI tools, and reproducible workflows designed for real imaging datasets and collaboration.</p>
  </div>
  <div class="home-strip-card">
    <span class="home-strip-label">Teaching And Open Science</span>
    <p>Public repositories, datasets, trainee support, and methods that remain understandable after publication.</p>
  </div>
</div>

{% include section.html %}

<div class="home-panels">
  <article class="home-panel">
    <h2>Research And Methods</h2>
    <p>I develop quantitative imaging methods for bone structure, strength, and remodelling across longitudinal HR-pQCT, opportunistic CT, and finite element modelling workflows.</p>
    <ul>
      <li>Localized remodelling analysis in vivo</li>
      <li>Vertebral strength assessment from routine CT</li>
      <li>Segmentation, calibration, and quality control pipelines</li>
    </ul>
    {% include button.html link="research" text="Explore Research" %}
  </article>

  <article class="home-panel">
    <h2>Projects And Tools</h2>
    <p>Much of the research lives as software. I build practical codebases that collaborators can run, inspect, validate, and extend.</p>
    <ul>
      <li>Longitudinal HR-pQCT processing</li>
      <li>Motion scoring and imaging QC</li>
      <li>Benchmarking and analysis infrastructure</li>
    </ul>
    {% include button.html link="projects" text="Browse Projects" %}
  </article>

  <article class="home-panel">
    <h2>Teaching, Data, And Collaboration</h2>
    <p>Alongside research, I contribute teaching materials, public datasets, mentorship, and collaborative workflows that support more reproducible musculoskeletal imaging science.</p>
    <ul>
      <li>Publications, datasets, and reusable resources</li>
      <li>Teaching repositories and course materials</li>
      <li>Collaboration across imaging, biomechanics, and translation</li>
    </ul>
    {% include button.html link="teaching" text="View Teaching" %}
  </article>
</div>
