
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

<h4>Check the latest news from: Thu 22 Jan 2026</h4>
<ol>
<li>
    <a href=https://huggingface.co/sweepai/sweep-next-edit-1.5B target="_blank">
        Show HN: Sweep, Open-weights 1.5B model for next-edit autocomplete |
    </a>
    By: williamzeng0
</li>

<p>
Text: Hey HN, we trained and open-sourced a 1.5B model that predicts your next edits, similar to Cursor. You can download the weights here (<a href="https:&#x2F;&#x2F;huggingface.co&#x2F;sweepai&#x2F;sweep-next-edit-1.5b" rel="nofollow">https:&#x2F;&#x2F;huggingface.co&#x2F;sweepai&#x2F;sweep-next-edit-1.5b</a>) or try it in our JetBrains plugin (<a href="https:&#x2F;&#x2F;plugins.jetbrains.com&#x2F;plugin&#x2F;26860-sweep-ai-autocomplete--coding-agent" rel="nofollow">https:&#x2F;&#x2F;plugins.jetbrains.com&#x2F;plugin&#x2F;26860-sweep-ai-autocomp...</a>).<p>Next-edit autocomplete differs from standard autocomplete by using your recent edits as context when predicting completions. The model is small enough to run locally while outperforming models 4x its size on both speed and accuracy.<p>We tested against Mercury (Inception), Zeta (Zed), and Instinct (Continue) across five benchmarks: next-edit above&#x2F;below cursor, tab-to-jump for distant changes, standard FIM, and noisiness. We found exact-match accuracy correlates best with real usability because code is fairly precise and the solution space is small.<p>Prompt format turned out to matter more than we expected. We ran a genetic algorithm over 30+ diff formats and found simple `original`&#x2F;`updated` blocks beat unified diffs. The verbose format is just easier for smaller models to understand.<p>Training was SFT on ~100k examples from permissively-licensed repos (4hrs on 8xH100), then RL for 2000 steps with tree-sitter parse checking and size regularization. The RL step fixes edge cases SFT can’t like, generating code that doesn’t parse or overly verbose outputs.<p>We&#x27;re open-sourcing the weights so the community can build fast, privacy-preserving autocomplete for any editor. If you&#x27;re building for VSCode, Neovim, or something else, we&#x27;d love to see what you make with it! </br>
</p>

<li>
    <a href=https://www.jamf.com/blog/threat-actors-expand-abuse-of-visual-studio-code/ target="_blank">
        Threat actors expand abuse of Microsoft Visual Studio Code |
    </a>
    By: vinnyglennon
</li>

<li>
    <a href=https://www.kentik.com/blog/from-stealth-blackout-to-whitelisting-inside-the-iranian-shutdown/ target="_blank">
        From stealth blackout to whitelisting: Inside the Iranian shutdown |
    </a>
    By: oavioklein
</li>

<li>
    <a href=https://arxiv.org/abs/2201.01174 target="_blank">
        Binary fuse filters: Fast and smaller than xor filters (2022) |
    </a>
    By: redbell
</li>

<li>
    <a href=https://github.com/ChartGPU/ChartGPU target="_blank">
        Show HN: ChartGPU – WebGPU-powered charting library (1M points at 60fps) |
    </a>
    By: huntergemmer
</li>

<p>
Text: Creator here. I built ChartGPU because I kept hitting the same wall: charting libraries that claim to be &quot;fast&quot; but choke past 100K data points.<p>The core insight: Canvas2D is fundamentally CPU-bound. Even WebGL chart libraries still do most computation on the CPU. So I moved everything to the GPU via WebGPU:<p>- LTTB downsampling runs as a compute shader
- Hit-testing for tooltips&#x2F;hover is GPU-accelerated
- Rendering uses instanced draws (one draw call per series)<p>The result: 1M points at 60fps with smooth zoom&#x2F;pan.<p>Live demo: <a href="https:&#x2F;&#x2F;chartgpu.github.io&#x2F;ChartGPU&#x2F;examples&#x2F;million-points&#x2F;" rel="nofollow">https:&#x2F;&#x2F;chartgpu.github.io&#x2F;ChartGPU&#x2F;examples&#x2F;million-points&#x2F;</a><p>Currently supports line, area, bar, scatter, pie, and candlestick charts. MIT licensed, available on npm: `npm install chartgpu`<p>Happy to answer questions about WebGPU internals or architecture decisions. </br>
</p>
</ol>