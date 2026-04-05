---
layout: page
title: People
subtitle: Tong Lab roster
---

<style>
.member-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 24px;
  margin-top: 36px;
}
.member-card {
  width: calc(25% - 18px);
  min-width: 210px;
  max-width: 270px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 6px 18px rgba(0,0,0,0.08);
  background: #fff;
  border: 1px solid #eef2f7;
}
.member-photo {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-bottom: 2px solid #f0f0f0;
}
.member-info { padding: 18px; }
.member-name { margin: 0 0 6px 0; font-size: 21px; }
.member-role { color: #355caa; font-weight: 700; margin-bottom: 8px; }
.member-desc { color: #555; font-size: 14px; line-height: 1.7; }
.member-links { display:flex; flex-wrap:wrap; gap:8px; margin-top:12px; }
.member-links a { display:inline-block; padding:6px 10px; border-radius:999px; background:#eef4ff; color:#274690; text-decoration:none; font-size:13px; font-weight:600; }
.member-links a:hover { background:#dfe9ff; }
@media (max-width: 960px) { .member-card { width: calc(50% - 18px); } }
@media (max-width: 560px) { .member-card { width: 100%; max-width: 340px; } }
</style>

<div style="text-align:center; max-width: 920px; margin: 0 auto; font-size: 13pt; line-height: 1.9;">
  Tong Lab is currently a compact human-plus-agents team. Tong leads the research direction; Rock, Kiti,
  and Biubiu cover different parts of the operating stack and turn the lab into a living working system,
  not just a personal homepage.
</div>

<div class="member-grid">
  <div class="member-card">
    <img src="{{ '/img/members/tong.jpg' | relative_url }}" alt="Tong Zhang" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Tong Zhang</h3>
      <div class="member-role">Lab lead</div>
      <div class="member-desc">
        Ph.D. student in Computer Science at Fudan University. His interests include AI, world models,
        multimodal learning, LLM safety, vision-language systems, SVG generation, head avatars,
        and trajectory prediction.
      </div>
      <div class="member-links">
        <a href="https://stonezhang.com" target="_blank">Homepage</a>
        <a href="https://scholar.google.com/scholar?q=Tong+Zhang+Fudan+University" target="_blank">Scholar</a>
        <a href="mailto:tongz27@uci.edu">Email</a>
      </div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/rock.png' | relative_url }}" alt="Rock" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Rock</h3>
      <div class="member-role">Main assistant & coordinator</div>
      <div class="member-desc">
        Tong's research partner and daily life manager on the main workspace side.
        Handles coordination, research support, memory upkeep, and Windows / WSL-side operations.
      </div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/kiti.png' | relative_url }}" alt="Kiti" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Kiti</h3>
      <div class="member-role">VPS / Ubuntu assistant</div>
      <div class="member-desc">
        Focused on server operations, remote execution, experiment running, website maintenance,
        gateways, proxies, and long-running tasks on the Ubuntu side.
      </div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/biubiu.png' | relative_url }}" alt="Biubiu" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Biubiu</h3>
      <div class="member-role">Mac assistant</div>
      <div class="member-desc">
        Works on coding, browser operations, and device-side support on the Mac environment.
        Helps turn ideas into implementations quickly.
      </div>
    </div>
  </div>
</div>
