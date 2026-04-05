---
layout: page
title: Blogs
subtitle: Notes and updates
---

<div style="font-size: 13pt; line-height: 1.8; margin-bottom: 24px;">
  Short posts from Tong Lab will appear here.
</div>

{% if site.posts.size > 0 %}
  <ul style="list-style:none; padding-left:0;">
  {% for post in site.posts %}
    <li style="padding:16px 0; border-bottom:1px solid #e5e7eb;">
      <div style="font-size:12px; color:#666;">{{ post.date | date: "%B %-d, %Y" }}</div>
      <div style="font-size:20px; font-weight:600; margin:6px 0;"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></div>
      <div style="color:#555;">{{ post.excerpt | strip_html | truncate: 180 }}</div>
    </li>
  {% endfor %}
  </ul>
{% else %}
  <p>No posts yet.</p>
{% endif %}
