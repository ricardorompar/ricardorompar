
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

<h4>Check the latest news from: Mon 27 Oct 2025</h4>
<ol>
<li>
    <a href=https://github.com/dvir-biton/MyraOS target="_blank">
        Show HN: MyraOS – My 32-bit operating system in C and ASM (Hack Club project) |
    </a>
    By: dvirbt
</li>

<p>
Text: Hi HN, I’m Dvir, a young developer. Last year, I got rejected after a job interview because I lacked some CPU knowledge. After that, I decided to deepen my understanding in the low level world and learn how things work under the hood. I decided to try and create an OS in C and ASM as a way to broaden my knowledge in this area.<p>This took me on the most interesting ride, where I’ve learned about OS theory and low level programming on a whole new level.  I’ve spent hours upon hours, blood and tears, reading different OS theory blogs, learning low level concepts, debugging, testing and working on this project.<p>I started by reading University books and online blogs, while also watching videos.  
Some sources that helped me out were OSDev Wiki (<a href="https:&#x2F;&#x2F;wiki.osdev.org&#x2F;Expanded_Main_Page" rel="nofollow">https:&#x2F;&#x2F;wiki.osdev.org&#x2F;Expanded_Main_Page</a>), OSTEP (<a href="https:&#x2F;&#x2F;pages.cs.wisc.edu&#x2F;~remzi&#x2F;OSTEP" rel="nofollow">https:&#x2F;&#x2F;pages.cs.wisc.edu&#x2F;~remzi&#x2F;OSTEP</a>), open-source repositories like MellOS and LemonOS (more advanced), DoomGeneric, and some friends that have built an OS before.<p>This part was the longest, but also the easiest. I felt like I understood the theory, but still could not connect it into actual code. Sitting down and starting to code was difficult, but I knew that was the next step I needed to  take! 
I began by working on the bootloader, which is optional since you can use a pre-made one (I switched to GRUB later), but implementing it was mainly for learning purposes and to warm up on ASM. These were my steps after that:<p><pre><code>  1) I started implementing the VGA driver, which gave me the ability to display text.
  2) Interrupts - IDT, ISR, IRQ, which signal to the CPU that a certain event occurred and needs handling (such as faults, hardware connected device actions, etc).
  3) Keyboard driver, which enables me to display the same text I type on my keyboard.
  4) PMM (Physical memory management)
  5) Paging and virtual memory management
  6) RTC driver - clock addition (which was, in my opinion, optional)
  7) PIT driver - Ticks every certain amount of time, and also  
  8) FS (File System) and physical HDD drivers - for the HDD I chose PATA (HDD communication protocol) for simplicity (SATA is a newer but harder option as well).
     For the FS I chose EXT2 (The Second Extended FileSystem), which is a foundational linux FS structure introduced in 1993. This FS structure is not the simplest,
     but is very popular in hobby-OS, it is very supported, easy to set up and upgrade to newer EXT versions, it has a lot of materials online, compared to other
     options. This was probably the longest and largest feature I had worked on.
  9) Syscall support.
  10) Libc implementation.
  11) Processing and scheduling for multiprocessing.
  12) Here I also made a shell to test it all.
</code></pre>
At this point, I had a working shell, but later decided to go further and add a GUI! I was working on the FS (stage 8), when I heard about Hack Club’s Summer of Making (SoM). This was my first time practicing in HackClub, and I want to express my gratitude and share my enjoyment of participating in it.<p>At first I just wanted to declare the OS as finished after completing the FS, and a bit of other drivers, but because of SoM my perspective was changed completely. Because of the competition, I started to think that I needed to ship a complete OS, with processing, GUI and the bare minimum ability to run Doom. I wanted to show the community in SoM how everything works.<p>Then I worked on it for another 2 months, after finishing the shell, just because of SoM!,  totalling my project to almost 7 months of work. At this time I added full GUI support, with dirty rectangles and double buffering, I made a GUI mouse driver, and even made a full Doom port! things I would&#x27;ve never even thought about without participating in SoM.<p>This is my SoM project: <a href="https:&#x2F;&#x2F;summer.hackclub.com&#x2F;projects&#x2F;5191" rel="nofollow">https:&#x2F;&#x2F;summer.hackclub.com&#x2F;projects&#x2F;5191</a>.<p>Every project has challenges, especially in such a low level project. I had to do a lot of debugging while working on this, and it is no easy task. I highly recommend using GDB which helped me debug so many of my problems, especially memory ones.<p>The first major challenge I encountered was during the coding of processes - I realized that a lot of my paging code was completely wrong, poorly tested, and had to be reworked. During this time I was already in the competition and it was difficult keeping up with devlogs and new features while fixing old problems in a code I wrote a few months ago.<p>Some more major problems occurred when trying to run Doom, and unlike the last problem, this was a disaster. I had random PFs and memory problems, one run could work while the next one wouldn’t, and the worst part is that it was only on the Doom, and not on processes I created myself. These issues took a lot of time to figure out. I began to question the Doom code itself, and even thought about giving up on the whole project.<p>After a lot of time spent debugging, I fixed the issues. It was a combination of scheduling issues, Libc issues and the Qemu not having enough (wrongfully assuming 128MB for the whole OS was enough).<p>Finally, I worked throughout all the difficulties, and shipped the project! In the end, the experience working on this project was amazing. I learned a lot, grew and improved as a developer, and I thank SoM for helping to increase my motivation and make the project memorable and unique like I never imagined it would be.<p>The repo is at <a href="https:&#x2F;&#x2F;github.com&#x2F;dvir-biton&#x2F;MyraOS" rel="nofollow">https:&#x2F;&#x2F;github.com&#x2F;dvir-biton&#x2F;MyraOS</a>. I’d love to discuss any aspect of this with you all in the comments! </br>
</p>

<li>
    <a href=https://lalinsky.com/2025/10/26/zio-async-io-for-zig.html target="_blank">
        How I turned Zig into my favorite language to write network programs in |
    </a>
    By: 0x1997
</li>

<li>
    <a href=https://www.smithsonianmag.com/science-nature/these-sandhill-cranes-have-adopted-a-canadian-gosling-and-birders-have-flocked-to-watch-the-strange-family-180986828/ target="_blank">
        Sandhill cranes have adopted a Canada gosling |
    </a>
    By: NaOH
</li>

<li>
    <a href=https://github.com/rochus-keller/Are-we-fast-yet target="_blank">
        Are-we-fast-yet implementations in Oberon, C++, C, Pascal, Micron and Luon |
    </a>
    By: luismedel
</li>

<li>
    <a href=https://maurycyz.com/misc/easy_git/ target="_blank">
        You already have a Git server |
    </a>
    By: chmaynard
</li>
</ol>