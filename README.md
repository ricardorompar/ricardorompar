
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

<h4>Check the latest news from: Mon 20 Jul 2026</h4>
<ol>
<li>
    <a href=https://robotics.xiaomi.com/xiaomi-robotics-1.html target="_blank">
        Xiaomi-Robotics-1 |
    </a>
    By: ilreb
</li>

<li>
    <a href=https://github.com/Saivineeth147/lora-speedrun target="_blank">
        LoRA Speedrun – a public wall-clock leaderboard for fine-tuning techniques |
    </a>
    By: Vineeth147
</li>

<p>
Text: I might be the only SRE on Earth with his own bowling center. It&#x27;s a more in-depth gig than you&#x27;d think.<p>My family and I bought an abandoned 8-lane bowling center in the rural mid-west. In our small town there weren&#x27;t many recreation options for families. You&#x27;ve heard of a food desert? This is an R&amp;R desert.<p>It had been abandoned for a good reason. The roof leaks, the electrical system was constantly surging, and my 70-year-old bowling equipment (still) doesn&#x27;t work perfectly. The system that keeps your score is particularly interesting to me. It&#x27;s the thing you watch during your game, but it fades into the background beyond that. Turns out these things are really cool, but absurdly expensive.<p>Ours was installed in 2008 and cost six figures. It&#x27;s calculating ball speed and trajectory, camera-based pin detection (object detection and trig, on ICs!), runs the fouling, the animations, the pinsetting machine and ball return. Very cool stuff for its age.<p>From the business perspective, my facility only cost me $105k. To forklift-replace the score keeping system runs anywhere between $80-$120k, depending on features, vendor, and unit age. No upgrades or service contracts, mind you, and every feature and customization is a new line item. That&#x27;s for a 1:1 replacement on a system installed in 2008. Incredible, given how fast the tech world moves.<p>Replacement parts cost a shocking $4000 per pair of lanes. But wait, the bowling machines themselves are 70 years old, so what&#x27;s this &quot;advanced&quot; system actually doing back there? Actuating a single relay to trigger that big old machine. Everything else is strictly mechanical. Meanwhile I&#x27;ve got a six-figure invoice in my hand. I&#x27;m upset.<p>Given the state of open hardware, computer vision, real-time event streaming, and open source running megascale products worldwide, there had to be a way to do this myself.<p>So far I&#x27;ve built an equivalent prototype for about $200 per lane-pair, $400 if you&#x27;re fancy. ESP32 and ESPNow with an RS485 fallback, reporting to a raspberry pi lane computer that&#x27;s really just redis and a state machine bolted to an ESP32 gateway for the mesh.<p>Since it&#x27;s all ESP32, I&#x27;ve got a fistful of spare controllers in a drawer, pre-flashed or waiting to be. All common off-the-shelf hardware: microcontrollers wired to relays, optocouplers, and IR-break-beam sensors, each running slightly different firmware. Writing the firmware and protocol is the actual hard part.<p>It&#x27;s an ESPNow star-topology mesh: each node emits events from its sensors and accepts commands for its controls, reporting to a gateway node connected to the raspi over UART. From there it&#x27;s event streaming: RX packets get translated and tossed into redis, commands relay back out to the mesh as needed. RS485 sits underneath as a wired fallback for noisy RF environments.<p>Once the data&#x27;s in redis, it&#x27;s familiar middleware&#x2F;React&#x2F;websocket&#x2F;pub-sub stuff. Any React dev can build their own UI and bowling animations. Since it all runs on commodity hardware, I can do legit anything I want as the proprietor, and I own all my data. Repairs take five minutes; I can swap the rig on a lane pair in under 10. I&#x27;d bet a house like mine could go from zero to running in an hour or two.<p>We&#x27;re calling it OpenLaneLink, and I plan to open source the hardware, firmware, and software stack when it&#x27;s ready. Bowling is fun, and I want to help keep it affordable for alleys like mine.
I hate vendor lock-in. I&#x27;m not a fan of closed systems, calling support for every hiccup, or paying to &quot;white label&quot; my own equipment. Want to go Tron-themed for a night? Good luck finding a neon neumorphic theme in something bought at the turn of the century.<p>All that bugged me. Sure, bowling equipment is niche, but the open hardware and software landscape is amazing.<p>Thanks for reading! Let me know if anyone&#x27;s interested in more posts about this bowling nonsense. </br>
</p>

<li>
    <a href=https://github.com/hgaiser/moonshine target="_blank">
        Moonshine: Lets you stream games from your PC to any device running Moonlight |
    </a>
    By: wertyk
</li>

<li>
    <a href=https://spectrum.ieee.org/self-powered-trailers-freight-decarbonization target="_blank">
        Self-Powered Trailers Promise Leaner Freight Runs |
    </a>
    By: rbanffy
</li>
</ol>