# Hi there, I'm Bảo Trương 👋

I am a **Robotics and Mechatronics Engineering (Honours)** student at RMIT University, blending hardware design with intelligent software. My focus lies at the intersection of **Edge AI, Embedded Systems, and Computer Vision**—bringing intelligence directly to the physical world.

Currently, I act as a Team Lead & Hardware/Software Architect for technical group projects, building end-to-end intelligent systems.

---

### 🚀 What I'm Working On
* **Edge AI & TinyML:** Deploying and quantizing models (CNNs, LLMs) for resource-constrained hardware.
* **Intelligent Mechatronics:** Designing smart, automated mechanical systems from scratch (CAD to firmware).
* **Agentic Workflows:** Experimenting with local AI agents and local LLM deployments to optimize developer workflows.

---

### 🛠️ Tech Stack & Tools

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python, C/C++, MATLAB |
| **AI / ML** | PyTorch, LangChain, Computer Vision (CNNs), Time-Series Forecasting |
| **Hardware & Firmware** | Arduino, ESP32, Raspberry Pi, Microcontrollers, RTOS |
| **EDA & 3D Design** | Fusion 360, Shapr3D, KiCad (PCB Design), 3D Printing (Bambu Lab) |
| **Tools & Workflow** | Git, Ollama, Linux, Notion |

---

### 📈 Featured Projects

#### 💊 [P.I.L.L.A.R.S: AIoT homecare for Parkinson's, First Runner-Up](https://github.com/baotrq/pillars-showcase)
<a href="https://github.com/baotrq/pillars-showcase"><img src="https://raw.githubusercontent.com/baotrq/pillars-showcase/main/assets/hero.jpg" alt="The P-Station pill dispenser with its kiosk tablet at the FPT IoT Challenge 2026 Grand Final" /></a>

* **Description:** A wristband that flags a possible fall, freeze or spoken "help" on-device, a home Station that dispenses the right pills to the right person (FaceID, 8 cups, IR pill counting) and keeps working offline, and a caregiver app with live alerts. Fall-direction and freezing-of-gait models run full-INT8 on Silicon Labs EFR32xG26, 1.23× faster on its MVP accelerator. I built the pill dispenser (2 × ESP32 motor layers, Pi-side pill counting, cup-pickup sensor) and the Station's kiosk UI. Team of four, **First Runner-Up** at the FPT IoT Challenge 2026 Grand Final.
* **Tech:** Silicon Labs EFR32xG26 + BGM220, TensorFlow Lite Micro, Raspberry Pi, ESP32, Python (FastAPI), Next.js, PostgreSQL, Redis, three.js.

#### 🌸 [S.C.E.N.T: an Edge AIoT perfume shelf, Second Prize](https://github.com/baotrq/scent-showcase)
<a href="https://github.com/baotrq/scent-showcase"><img src="https://raw.githubusercontent.com/baotrq/scent-showcase/main/assets/award.jpg" alt="Team Edgelectronix on stage with the Second Prize at the FPT IoT Challenge 2025" /></a>

* **Description:** A smart perfume shelf that recommends a fragrance from your personality and occasion and lights up the bottle, tracks stock with load cells and IR beams, and hears a glass bottle break, all over a Thread mesh. I built the recommendation model on the EFR32xG24: a 50-class MLTK classifier first, then a contrastive 64-D embedding ranked by cosine similarity, full INT8 on the microcontroller. Team of four, **Second Prize** at the FPT IoT Challenge 2025.
* **Tech:** Silicon Labs EFR32xG24 / xG26 / MG21, MLTK, TensorFlow / Keras, TensorFlow Lite Micro, OpenThread, Micrium OS, Raspberry Pi, Flask, PostgreSQL + TimescaleDB, Redis.

#### 🐈‍⬛ [Roll: Money habits, with a cat](https://github.com/baotrq/roll-showcase)
<a href="https://github.com/baotrq/roll-showcase"><img src="https://raw.githubusercontent.com/baotrq/roll-showcase/main/assets/gallery.png" alt="Roll app screenshots" /></a>

* **Description:** A cat-themed personal expense tracker where logging takes seconds: snap a photo, say it out loud, or let a bank notification fill it in. Offline-first, with sync between devices, a Wear OS companion and a native iOS port. Built from scratch to store-ready in six weeks.
* **Tech:** Kotlin, Jetpack Compose, Room, SwiftUI, Supabase (Postgres + RLS, Edge Functions), Gemini, RevenueCat.

#### 📸 [ONBOOTH: a virtual photobooth for friends far apart](https://github.com/baotrq/onbooth-showcase)
<a href="https://github.com/baotrq/onbooth-showcase"><img src="https://raw.githubusercontent.com/baotrq/onbooth-showcase/main/assets/real-strips.jpg" alt="Real ONBOOTH photo strips" /></a>

* **Description:** Up to 8 friends join one booth over live video from anywhere; one synced countdown takes everyone's photo at once, and every browser composites the identical strip, no server touching an image. Live at [onboothvn.com](https://www.onboothvn.com) in English and Vietnamese, with **10,367 users** so far (Oct 2026).
* **Tech:** Next.js 16, React 19, TypeScript, LiveKit (WebRTC), MediaPipe, Upstash Redis, Vercel.

#### 🥚 [Egg Gripper: force-controlled, 97/100 demo](https://github.com/baotrq/egg-gripper-showcase)
<a href="https://github.com/baotrq/egg-gripper-showcase"><img src="https://raw.githubusercontent.com/baotrq/egg-gripper-showcase/main/assets/build.jpg" alt="Egg gripper build photos" /></a>

* **Description:** A two-finger gripper that lifts a raw egg 90 cm, holds it 30 s and puts it down unbroken. ESP32 firmware closes until the fingertip load cell reads the target force, re-tightens if the grip sags and backs off on over-force; egg-shaped TPU fingertips; a live 3D dashboard over Wi-Fi or USB. Team project, MIET2561 Mechatronic Design (RMIT), **97/100** on the demo.
* **Tech:** C++ (ESP32, PlatformIO), CAD + 3D printing (PETG, TPU), HX711 load cell, three.js.

#### 🎵 [SimpMusic (Bao): my fork of SimpMusic](https://github.com/baotrq/simpmusic-bao-showcase)
<a href="https://github.com/baotrq/simpmusic-bao-showcase"><img src="https://raw.githubusercontent.com/baotrq/simpmusic-bao-showcase/main/assets/led-car.gif" alt="A car's LED strip changing colour with each song's album art" /></a>

* **Description:** My daily-driver build of the open-source YouTube Music client. A car LED strip follows each song's album art over a Bluetooth protocol I reverse-engineered from HCI snoop logs; playback and encrypted sign-ins follow me between phones through my own Cloudflare Worker; the player is rebuilt for Samsung DeX.
* **Tech:** Kotlin Multiplatform, Compose, Bluetooth LE, Cloudflare Workers + D1, AES-GCM, Gemini.

#### ⏳ [Age in Motion: your age, live on your home screen](https://github.com/baotrq/age-in-motion-showcase)
<a href="https://github.com/baotrq/age-in-motion-showcase"><img src="https://raw.githubusercontent.com/baotrq/age-in-motion-showcase/main/assets/hero.gif" alt="Age in Motion: a dot-matrix age counter ticking up" /></a>

* **Description:** An age counter whose Android home-screen widget counts up in real time to eight decimal places, by handing the fast digits to the launcher's own ViewFlippers instead of redrawing. Three widgets, three digit styles, iOS WidgetKit too.
* **Tech:** Flutter, Dart, Kotlin (RemoteViews, AlarmManager), Swift (WidgetKit).

#### 📊 [Project Name: Predictive AI Forecasting]
* **Description:** Built a time-series forecasting system utilizing Prophet to optimize supply chain and manufacturing demand.
* **Tech:** Python, Prophet, Pandas.

---

### ⚡ Fun Facts About Me
* 🏀 When I'm not debugging code or calibrating 3D printers, you'll find me on the basketball court.
* 🛠️ Huge fan of local AI tools and tweaking agentic workflows to make coding faster.
* 🐈 Proud parent of a chaotic black kitten.

---

### 🤝 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/your-username)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:your.email@example.com)
