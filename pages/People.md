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
  max-width: 260px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  background: #fff;
}
.member-photo {
  width: 100%;
  height: 280px;
  object-fit: cover;
  border-bottom: 2px solid #f0f0f0;
}
.member-info { padding: 18px; }
.member-name { margin: 0 0 6px 0; font-size: 20px; }
.member-role { color: #4A154B; font-weight: 600; margin-bottom: 6px; }
.member-desc { color: #555; font-size: 14px; line-height: 1.6; }
@media (max-width: 960px) { .member-card { width: calc(50% - 18px); } }
@media (max-width: 560px) { .member-card { width: 100%; max-width: 340px; } }
</style>

<div style="text-align:center; max-width: 850px; margin: 0 auto; font-size: 13pt; line-height: 1.8;">
  Tong Lab is currently a compact human-plus-agents team. Tong leads the research direction; Rock, Kiti,
  and Biubiu cover different parts of the operating stack.
</div>

<div class="member-grid">
  <div class="member-card">
    <img src="{{ '/img/members/tong.jpg' | relative_url }}" alt="Tong Zhang" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Tong Zhang</h3>
      <div class="member-role">Lab lead</div>
      <div class="member-desc">Ph.D. student at Fudan University working on AI, multimodal learning, agent systems, and research tooling.</div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/rock.png' | relative_url }}" alt="Rock" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Rock</h3>
      <div class="member-role">Main assistant & coordinator</div>
      <div class="member-desc">Handles research support, WSL / Windows-side operations, and coordination across the assistant stack.</div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/kiti.png' | relative_url }}" alt="Kiti" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Kiti</h3>
      <div class="member-role">VPS / Ubuntu assistant</div>
      <div class="member-desc">Runs infrastructure, remote execution, gateways, services, and long-running jobs on the lab server side.</div>
    </div>
  </div>

  <div class="member-card">
    <img src="{{ '/img/members/biubiu.png' | relative_url }}" alt="Biubiu" class="member-photo">
    <div class="member-info">
      <h3 class="member-name">Biubiu</h3>
      <div class="member-role">Mac assistant</div>
      <div class="member-desc">Focuses on coding, browser workflows, and device-side support on the Mac environment.</div>
    </div>
  </div>
</div>
