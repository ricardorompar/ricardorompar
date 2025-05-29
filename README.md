
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

<h4>Check the latest news from: Thu 29 May 2025</h4>
<ol>
<li>
    <a href=https://github.com/livingbio/typed-ffmpeg target="_blank">
        Show HN: Typed-FFmpeg 3.0–Typed Interface to FFmpeg and Visual Filter Editor |
    </a>
    By: lucemia51
</li>

<p>
Text: Hi HN,<p>I built typed-ffmpeg, a Python package that lets you build FFmpeg filter graphs with full type safety, autocomplete, and validation. It’s inspired by ffmpeg-python, but addresses some long-standing issues like lack of IDE support and fragile CLI strings.<p>What’s New in v3.0:
 •  Source filter support (e.g. color, testsrc, etc.)
 •  Input stream selection (e.g. [0:a], [1:v])
 •  A new interactive playground where you can:
 • Build filter graphs visually
 • Generate both FFmpeg CLI and typed Python code
 • Paste existing FFmpeg commands and reverse-parse them into graphs<p>Playground link: <a href="https:&#x2F;&#x2F;livingbio.github.io&#x2F;typed-ffmpeg-playground&#x2F;" rel="nofollow">https:&#x2F;&#x2F;livingbio.github.io&#x2F;typed-ffmpeg-playground&#x2F;</a>
(It’s open source and runs fully in-browser.)<p>The internal core also supports converting CLI → graph → typed Python code. This is useful for building educational tools, FFmpeg IDEs, or visual editors.<p>I’d love feedback, bug reports, or ideas for next steps. If you’ve ever struggled with FFmpeg’s CLI or tried to teach it, this might help.<p>Thanks!
— David (maintainer) </br>
</p>

<li>
    <a href=https://milwaukeerecord.com/city-life/long-live-american-science-surplus-which-needs-your-help/ target="_blank">
        Long live American Science and Surplus |
    </a>
    By: thinkalone
</li>

<li>
    <a href=https://velzie.rip/blog/celeste-wasm target="_blank">
        Porting Terraria and Celeste to the Browser with WebAssembly |
    </a>
    By: coolelectronics
</li>

<li>
    <a href=https://prettygoodblog.com/p/what-threads-are-part-2 target="_blank">
        A toy RTOS inside Super Mario Bros. using emulator save states |
    </a>
    By: notorious_pgb
</li>

<p>
Text: This started as a throwaway metaphor in a blog post, but is now fully runnable: a toy RTOS with preemptive multitasking inside of Super Mario Bros. on the NES.<p>Essentially, this is:<p>- A rudimentary preemptive RTOS<p>- Using an unmodified NES emulator (FCEUX) as the CPU<p><pre><code>    - &quot;Unmodified&quot; depending on how you define terms
</code></pre>
- With emulator save states as the thread contexts<p>- With support for (very basic) mutexes, interrupt masking, and condition variables<p>- Demonstrated using Super Mario Bros. 1-1 with sections of the map dedicated to various synchronization primitives<p>There are many simplifications and shortcuts taken (doesn&#x27;t even have task priorities), and it doesn&#x27;t map 1:1 to true multithreading (e.g., emulator save states represent the state of the entire machine including RAM, whereas thread contexts represent a much more minimal slice), but I think it&#x27;s A) pretty interesting and B) a unique visceral explanation of threads. </br>
</p>

<li>
    <a href=https://desktopdocs.com/?v=2025 target="_blank">
        Show HN: I rewrote my Mac Electron app in Rust |
    </a>
    By: katrinarodri
</li>

<p>
Text: A year ago, my co-founder launched Desktop Docs here on HN. It&#x27;s a Mac app we built with Electron that uses CLIP embeddings to search photos and videos locally with natural language. We got positive feedback from HN and our first paying customers, but the app was almost 1GB and clunky to use.<p>TLDR; rebuilding in Rust was the right move.<p>So we rewrote the app with Rust and Tauri and here are the results:<p>- App size is 83% smaller: 1GB → 172MB
- DMG Installer is 70% smaller: 232MB → 69.5MB
- Indexing files is faster: A 38-minute video now indexes in ~3 minutes instead of 10-14 minutes
- Overall more stability (old app used to randomly crash)<p>The original version worked, but it didn&#x27;t perform well when you tried indexing thousands of images or large videos. We lost a lot of time struggling to optimize Electron’s main-renderer process communication and ended up with a complex worker system to process large batches of media files.<p>For months we wrestled with indecision about continuing to optimize the Electron app vs. starting a full rebuild in Swift or Rust. The main thing holding us back was that we hadn’t coded in Swift in almost 10 years and we didn’t know Rust very well.<p>What finally broke us was when users complained the app crashed their video calls just running in background. I guess that’s what happens when you ship an app with Chromium that takes up 200mb before any application code.<p>Today the app still uses CLIP for embeddings and Redis for vector storage and search, except Rust now handles the image and video processing pipeline and all the file I&#x2F;O to let users browse their entire machine, not just indexed files.<p>For the UI, we decided to rebuild it from scratch instead of porting over the old UI. This turned out well because it resulted in a cleaner, simpler UI after living with the complexity of the old version.<p>The trickiest part of the migration was learning Rust. LLMs definitely help, but the Rust&#x2F;Tauri community just isn’t as mature compared to Electron. Bundling Redis into the app was a permissioning nightmare, but I think our solution with Rust handles this better than what we had with Electron.<p>All in, the rebuild took about two months and still needs some more work to be at total parity with its Electron version, but the core functionality of indexing and searching files is way more performant than before and that made it worth the time. Sometimes you gotta throw away working code to build the right thing.<p>AMA about Rust&#x2F;Tauri migration, Redis bundling nightmares, how CLIP embeddings work for local semantic search, or why Electron isn&#x27;t always the answer. </br>
</p>
</ol>