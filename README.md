
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

<h4>Check the latest news from: Fri 10 Jul 2026</h4>
<ol>
<li>
    <a href=https://github.com/JustVugg/colibri target="_blank">
        Show HN: Getting GLM 5.2 running on my slow computer |
    </a>
    By: vforno
</li>

<p>
Text: A few days ago I found myself trying out GLM 5.2 and was really positively impressed. The capabilities and security I was getting from this LLM are similar to those I&#x27;ve gotten from models like Claude or GPT, and this really surprised me.<p>But then I thought, &quot;I wonder how it would work on a normal computer like mine,&quot; and above all, &quot;I wonder if it would work without going into OOM on a computer like mine.&quot; So I started working with the help of agents to test this possibility.<p>I started converting the model to int4, understanding MTP usage, and if possible implementing DSA for long context. How it responds in int4 and whether the quality is maintained or not. Until I got to the point, on my computer with 32GB of RAM, I was able to communicate with GLM 5.2 with times that, of course, aren&#x27;t high in cold start, but even then, we&#x27;re talking about 0.1 tok&#x2F;s, but that wasn&#x27;t important to me. The important thing was the journey to reach this goal. I just wanted it to work at all costs, even slowly.<p>So I created Colibrì, which was born from a very simple idea, to be honest, but tested in every way, where a 744B Mixture-of-Experts model activates only ~40B parameters per token—and only ~11 GB of those change from token to token (the routed experts). So:<p>The dense part (attention, shared experts, embeddings—~17B params) stays resident in RAM at int4 (~9.9 GB); The 21,504 routed experts (75 MoE layers × 256 experts + the MTP head, ~19 MB each at int4) live on disk (~370 GB) and are streamed on demand, with a per-layer LRU cache, an optional pinned hot-store, and the OS page cache as a free L2.<p>The engine is a single C file (c&#x2F;glm.c, ~1,300 lines) plus small headers. No BLAS, no Python at runtime, no GPU.No GPU or serious hardware because I don&#x27;t have that hardware so I can&#x27;t test it on hardware that is more powerful than my computer.Colibrì is a one-person project, written and tested entirely on a 12-core laptop with 25 GB of RAM — the numbers above are the ceiling of what I can measure at home.<p>Any feedback is welcome! (and if anyone wanted to participate in the project I would be delighted)<p>Repo: <a href="https:&#x2F;&#x2F;github.com&#x2F;JustVugg&#x2F;colibri" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;JustVugg&#x2F;colibri</a> </br>
</p>

<li>
    <a href=https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/ target="_blank">
        EU Parliament greenlights Chat Control 1.0 |
    </a>
    By: rapnie
</li>

<li>
    <a href=https://kotaku.com/a-train-sim-created-by-just-one-person-is-being-called-the-best-ever-made-2000699429 target="_blank">
        Train sim created by just one person is being called the best ever made |
    </a>
    By: oumua_don17
</li>

<p>
Text: <a href="https:&#x2F;&#x2F;store.steampowered.com&#x2F;app&#x2F;4630570&#x2F;RUNNING_TRAIN&#x2F;" rel="nofollow">https:&#x2F;&#x2F;store.steampowered.com&#x2F;app&#x2F;4630570&#x2F;RUNNING_TRAIN&#x2F;</a> </br>
</p>

<li>
    <a href=https://18words.com/ target="_blank">
        Show HN: 18 Words |
    </a>
    By: pompomsheep
</li>

<li>
    <a href=https://openai.com/index/gpt-5-6/ target="_blank">
        GPT-5.6 |
    </a>
    By: logickkk1
</li>

<p>
Text: <a href="https:&#x2F;&#x2F;deploymentsafety.openai.com&#x2F;gpt-5-6&#x2F;gpt-5-6.pdf" rel="nofollow">https:&#x2F;&#x2F;deploymentsafety.openai.com&#x2F;gpt-5-6&#x2F;gpt-5-6.pdf</a><p><a href="https:&#x2F;&#x2F;developers.openai.com&#x2F;api&#x2F;docs&#x2F;guides&#x2F;latest-model" rel="nofollow">https:&#x2F;&#x2F;developers.openai.com&#x2F;api&#x2F;docs&#x2F;guides&#x2F;latest-model</a><p><a href="https:&#x2F;&#x2F;x.com&#x2F;levie&#x2F;status&#x2F;2075287443411222628" rel="nofollow">https:&#x2F;&#x2F;x.com&#x2F;levie&#x2F;status&#x2F;2075287443411222628</a>, <a href="https:&#x2F;&#x2F;xcancel.com&#x2F;levie&#x2F;status&#x2F;2075287443411222628" rel="nofollow">https:&#x2F;&#x2F;xcancel.com&#x2F;levie&#x2F;status&#x2F;2075287443411222628</a> </br>
</p>
</ol>