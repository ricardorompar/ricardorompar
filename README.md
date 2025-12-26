
<!-- This is an HTML comment in your markdown file -->

<h1 align="center">Hi there, I'm Ricardo</h1>
<p align="center">
  <a href="https://ricardorompar.com" target="_blank">Website</a> •
  <a href="https://www.linkedin.com/in/ricardorompar/" target="_blank">LinkedIn</a> •
  <a href="https://twitter.com/ricardorompar" target="_blank">X</a>
</p>
<img src="https://badges.pufler.dev/visits/{ricardorompar}/{ricardorompar}"/>

<h3 align="left">Languages and Tools:</h3>
<p align="center">
  <a href="https://skillicons.dev" target="_blank">
    <img src="https://skillicons.dev/icons?i=terraform,aws,gcp,azure,git,python,kubernetes,react,js,docker,ubuntu" />
  </a>
</p>

<h2>About Me</h2>
Engineer. Passionate about technology and science. Constantly in the pursuit of being more to serve better.

Currently helping businesses <i>do cloud right</i> @<a href="https://github.com/hashicorp" target="_blank">HashiCorp</a>.

<h2>Projects and ideas</h2>
Projects...
<ul>
  <li>🔭 I’m currently working on different projects like the <a href="https://github.com/ricardorompar/ricardorompar/blob/main/automate.py">automation</a> of this page, and some demos <a href="https://github.com/ricardorompar/boundary-ansible-demo">like this one</a>.
  </li>

  <li >A few months back I began my <a href="https://github.com/ricardorompar/cloudResumeChallenge">Cloud Resume Challenge</a> (and haven't yet finished). It's a web-based resume that helps you practice different technologies and tools like the cloud, infrastructure as code, continuous integration, versioning, etc. If you want to learn more visit <a href="https://cloudresumechallenge.dev/docs/the-challenge/aws/" target="_blank">check this out</a>.
  </li>

  <li>🔭 <a href="https://github.com/ricardorompar/capstoneT2">This</a> is the capstone (integration) project for the second term of the master in Computer Science. It is a basic 3-tier app that allows users to access, modify and create stock a portfolio of their favorite stocks.
  </li>
</ul>
...and Ideas
<ul>
  <li>🌱 I’m currently learning about the HashiCorp product suite (Terraform, Vault, etc.), Vim, AWS, GCP, Azure, Kubernetes, Flask, React, Docker, etc.
  </li>
  <li>👯 I’m open to collaborating on any project.</li>
  <li>💬 Ask me about anything. I love computers, science, outer space, businesses, money, etc.</li>
  <li>📫 How to reach me: <a href="https://www.linkedin.com/in/ricardorompar/" target="_blank">Linkedin</a></li>
</ul>

<h2>Today's top <a href='https://news.ycombinator.com/' target="_blank">Hacker News</a></h2>
How does this work? -> <a href='./AUTOMATIC.md'>here 💡</a>

<h4>Check the latest news from: Fri 26 Dec 2025</h4>
<ol>
<li>
    <a href=https://www.raptitude.com/2025/12/maybe-the-default-settings-are-too-high/ target="_blank">
        Maybe the default settings are too high |
    </a>
    By: htk
</li>

<li>
    <a href=https://www.minimaxi.com/news/minimax-m21 target="_blank">
        MiniMax M2.1: Built for Real-World Complex Tasks, Multi-Language Programming |
    </a>
    By: 110
</li>

<li>
    <a href=https://gamingcouch.com target="_blank">
        Show HN: Gaming Couch – a local multiplayer party game platform for 8 players |
    </a>
    By: ChaosOp
</li>

<p>
Text: Hi HN,<p>I’ve been working on Gaming Couch, a web-based game platform where up to 8 players use their smartphones as controllers to play real-time action mini-games on a central browser screen.<p>TL;DR:<p>- 18 competitive mini-games for up to 8 players<p>- Runs entirely in the browser<p>- Phones act as controllers (no apps, no accounts required)<p>- Focused on fast, chaotic, real-time party games (no trivia)<p>- Currently in public early access<p>Try it here: <a href="https:&#x2F;&#x2F;gamingcouch.com" rel="nofollow">https:&#x2F;&#x2F;gamingcouch.com</a>. Open the link on a computer, host a session, scan the QR code with your phone(s) and play!<p>What is it?<p>Gaming Couch is a party game platform where friends play short competitive action games together on one screen, using their phones as controllers (there&#x27;s also support for physical gamepads if that&#x27;s more your thing!)<p>I intentionally avoided trivia and text-heavy games. Many people don’t write or read English fluently, and I wanted games where reaction, timing, and chaos matter more than spelling.<p>It’s currently in early public access with 18 mini-games, all made by me and a two friends. All game rounds last ~1 minute, scores carry over, and after each round players vote on the next game. If you’re solo, 3 games support bots, but it’s best with a full couch of people as half the fun comes from the social aspect of playing together!<p>Why I built it:<p>For the last 15+ plus years, me and my friends have loved video game nights but organizing them has always been a PITA when you have more than 4 people playing:<p>- Different games were under different Steam accounts requiring downloads and installation.<p>- Extra controllers were missing (somebody forgot to bring theirs) or they wouldn’t pair.<p>- Consoles were expensive and not always available if we were on the road.<p>Once I started building it, other dev friends asked if they could make games for it too, which led me to realize this could also be a platform for small party games, especially for gamejam devs who don’t want to or have time to build multiplayer infrastructure from scratch. This is why supporting third-party games is the next major feature I’m working on.<p>Tech stack:<p>- Games run locally in the host’s browser (no streaming of games)<p>- Phones connect via WebRTC to the host session (1–10ms latency in ideal conditions with P2P connection)<p>- Fallback to TURN when direct P2P connection isn’t possible e.g. due to strict firewall settings in corporate networks or use of VPN&#x27;s<p>- Website&#x2F;Platform made with React + TypeScript<p>- Existing games made with Unity or just plain JS&#x2F;TS.<p>- Backend: Supabase (Postgres + auth only, currently only used for optional user accounts)<p>How is it different from e.g. Jackbox, Airconsole or Nintendo?<p>Jackbox is absolutely great, but it’s heavily dependent on English literacy and &quot;being funny&quot; on the spot. I wanted something focused on fast, chaotic, real-time action games that work even if your friends speak different languages or just want to smash buttons. Also, I&#x27;m not a fan of their party pack model...<p>AirConsole is the most well known comparison to Gaming Couch in terms of technology and execution, but I feel there is a gap for a curated experience where the UI is unified, rounds are 60 seconds, and the competitive &quot;meta-game&quot; (scoreboards&#x2F;voting) is baked into the platform. And in any case AirConsole was acquired by a car-software company and have pivoted their focus from couch gaming toward in-car entertainment.<p>Nintendo games are usually the gold standard in the party game category but the HW and games cost so much! With Gaming Couch, I want to keep the accessibility threshold as low as possible so everyone is able to play without upfront HW or SW costs.<p>What do you think of this? Are you an interested player or perhaps a developer who has had an idea to develop a fun 8 player mini-game but has been daunted by the idea thus far? </br>
</p>

<li>
    <a href=https://github.com/popovicu/ultimate-linux target="_blank">
        Ultimate-Linux: Userspace for Linux in Pure JavaScript |
    </a>
    By: radeeyate
</li>

<li>
    <a href=https://fidget-spinner.github.io/posts/no-longer-sorry.html target="_blank">
        Python 3.15’s interpreter for Windows x86-64 should hopefully be 15% faster |
    </a>
    By: lumpa
</li>
</ol>