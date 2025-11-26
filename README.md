
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

<h4>Check the latest news from: Wed 26 Nov 2025</h4>
<ol>
<li>
    <a href=https://www.joshwcomeau.com/css/subgrid/ target="_blank">
        Brand New Layouts with CSS Subgrid |
    </a>
    By: joshwcomeau
</li>

<li>
    <a href=https://www.mikeayles.com/#kidoom target="_blank">
        Show HN: KiDoom – Running DOOM on PCB Traces |
    </a>
    By: mikeayles
</li>

<p>
Text: I got DOOM running in KiCad by rendering it with PCB traces and footprints instead of pixels.<p>Walls are rendered as PCB_TRACK traces, and entities (enemies, items, player) are actual component footprints - SOT-23 for small items, SOIC-8 for decorations, QFP-64 for enemies and the player.<p>How I did it:<p>Started by patching DOOM&#x27;s source code to extract vector data directly from the engine. Instead of trying to render 64,000 pixels (which would be impossibly slow), I grab the geometry DOOM already calculates internally - the drawsegs[] array for walls and vissprites[] for entities.<p>Added a field to the vissprite_t structure to capture entity types (MT_SHOTGUY, MT_PLAYER, etc.) during R_ProjectSprite(). This lets me map 150+ entity types to appropriate footprint categories.<p>The DOOM engine sends this vector data over a Unix socket to a Python plugin running in KiCad. The plugin pre-allocates pools of traces and footprints at startup, then just updates their positions each frame instead of creating&#x2F;destroying objects. Calls pcbnew.Refresh() to update the display.<p>Runs at 10-25 FPS depending on hardware. The bottleneck is KiCad&#x27;s refresh, not DOOM or the data transfer.<p>Also renders to an SDL window (for actual gameplay) and a Python wireframe window (for debugging), so you get three views running simultaneously.<p>Follow-up: ScopeDoom<p>After getting the wireframe renderer working, I wanted to push it somewhere more physical. Oscilloscopes in X-Y mode are vector displays - feed X coordinates to one channel, Y to the other. I didn&#x27;t have a function generator, so I used my MacBook&#x27;s headphone jack instead.<p>The sound card is just a dual-channel DAC at 44.1kHz. Wired 3.5mm jack → 1kΩ resistors → scope CH1 (X) and CH2 (Y). Reused the same vector extraction from KiDoom, but the Python script converts coordinates to ±1V range and streams them as audio samples.<p>Each wall becomes a wireframe box, the scope traces along each line. With ~7,000 points per frame at 44.1kHz, refresh rate is about 6 Hz - slow enough to be a slideshow, but level geometry is clearly recognizable. A 96kHz audio interface or analog scope would improve it significantly (digital scopes do sample-and-hold instead of continuous beam tracing).<p>Links:<p>KiDoom GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;MichaelAyles&#x2F;KiDoom" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;MichaelAyles&#x2F;KiDoom</a>, writeup: <a href="https:&#x2F;&#x2F;www.mikeayles.com&#x2F;#kidoom" rel="nofollow">https:&#x2F;&#x2F;www.mikeayles.com&#x2F;#kidoom</a><p>ScopeDoom GitHub: <a href="https:&#x2F;&#x2F;github.com&#x2F;MichaelAyles&#x2F;ScopeDoom" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;MichaelAyles&#x2F;ScopeDoom</a>, writeup: <a href="https:&#x2F;&#x2F;www.mikeayles.com&#x2F;#scopedoom" rel="nofollow">https:&#x2F;&#x2F;www.mikeayles.com&#x2F;#scopedoom</a> </br>
</p>

<li>
    <a href=https://kristofferbalintona.me/posts/202505291438/ target="_blank">
        Surprisingly, Emacs on Android is pretty good |
    </a>
    By: harryday
</li>

<li>
    <a href=https://alienseries.wordpress.com/2012/10/23/space-truckin-the-nostromo/ target="_blank">
        Space Truckin' – The Nostromo (2012) |
    </a>
    By: exvi
</li>

<li>
    <a href=https://wordpress.org/plugins/bandwidth-saver/ target="_blank">
        Show HN: A WordPress plugin that rewrites image URLs for near-zero-cost delivery |
    </a>
    By: cr1st1an
</li>

<p>
Text: Hi HN,<p>I built a WordPress plugin called Bandwidth Saver. It takes the images your site already has and serves them through Cloudflare R2 and Workers, which means zero egress fees and extremely low storage cost. The goal is to make image delivery fast and cheap without adding any of the complexity of traditional optimization plugins.<p>The idea is simple. WordPress keeps generating images normally. The plugin rewrites the URLs on the frontend so images are served from a Cloudflare Worker. On the first request, the Worker fetches the original image and stores it in R2. After that, Cloudflare’s edge serves the image from its global cache with no egress charges. There’s no need to preload or sync anything, and if something fails, the original image loads. That’s the entire system.<p>I built this because most image CDN plugins try to do everything: compression, resizing, AI transforms, asset management, custom dashboards, and monthly fees. That’s useful for some users, but it’s unnecessary for most sites that just want their existing media to load faster without breaking the bank. Bandwidth Saver focuses only on delivery, not transformations. It’s intentionally minimal.<p>There are two ways to use it. The plugin is completely free if you want to run your own Cloudflare Worker. I included the Worker code and the steps needed to deploy it. If you don’t want to deal with any Cloudflare setup, there’s a managed option for $2.99 per month that uses my Worker and my R2 bucket. I’m trying to keep it accessible while also covering operational costs.<p>The plugin works with any theme or builder and doesn’t modify the database. It only rewrites URLs on output. WordPress remains the system of record for all media. R2 simply becomes a cheap, durable cache layer backed by Cloudflare’s edge.<p>I’m especially interested in feedback about the approach. Does the fetch-on-first-request model make sense? Is the pricing fair for a plugin of this scope? Should I prioritize allowing users to connect their own R2 buckets or the managed service? And for those with experience in edge compute or CDNs, I would love thoughts on how to improve the Worker or the rewrite strategy.<p>Thanks for reading, happy to answer any questions. </br>
</p>
</ol>