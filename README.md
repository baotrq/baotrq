<a href="https://github.com/baotrq">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/baotrq/baotrq/main/card/dark.svg">
    <img alt="Bảo Trương: Robotics & Mechatronics engineering student at RMIT Vietnam. Edge AI, embedded systems and apps." src="https://raw.githubusercontent.com/baotrq/baotrq/main/card/light.svg">
  </picture>
</a>

<p align="center">
  <a href="https://baotrq.github.io/Personal-Portfolio/">Portfolio</a> ·
  <a href="https://www.onboothvn.com">ONBOOTH</a> ·
  <a href="mailto:tdmbao2005@gmail.com">Email</a>
</p>

I build things that sit between hardware and software: firmware and edge AI on microcontrollers, the
mechanisms they move, and the apps people actually use to talk to them. On team projects I'm usually
the hardware/software architect; on my own I ship products end to end.

---

### 📈 Featured Projects

#### 🐈‍⬛ [Roll: money habits, with a cat](https://github.com/baotrq/roll-showcase)
<a href="https://github.com/baotrq/roll-showcase"><img src="https://raw.githubusercontent.com/baotrq/roll-showcase/main/assets/gallery.png" alt="Roll app screenshots" /></a>

A cat-themed expense tracker where logging takes seconds: snap a photo, say it out loud, or let a bank
notification fill it in. Offline-first with sync between devices, a Wear OS companion and a native iOS
port. Empty scaffold to store-ready in **six weeks**.
<br /><sub>Kotlin · Jetpack Compose · Room · SwiftUI · Supabase · Gemini · RevenueCat</sub>

#### 📸 [ONBOOTH: a photobooth for friends far apart](https://github.com/baotrq/onbooth-showcase)
<a href="https://github.com/baotrq/onbooth-showcase"><img src="https://raw.githubusercontent.com/baotrq/onbooth-showcase/main/assets/real-strips.jpg" alt="Real ONBOOTH photo strips" /></a>

Up to eight friends join one booth over live video; one synced countdown takes everyone's photo at
once, and every browser composites the identical strip, with no server touching an image. Live at
[onboothvn.com](https://www.onboothvn.com) in English and Vietnamese, **10,367 users** so far.
<br /><sub>Next.js 16 · React 19 · TypeScript · LiveKit (WebRTC) · MediaPipe · Upstash Redis · Vercel</sub>

---

### 🏆 Competitions

#### 💊 [P.I.L.L.A.R.S: AIoT homecare for Parkinson's](https://github.com/baotrq/pillars-showcase) · First Runner-Up, FPT IoT Challenge 2026
<a href="https://github.com/baotrq/pillars-showcase"><img src="https://raw.githubusercontent.com/baotrq/pillars-showcase/main/assets/hero.jpg" alt="The P-Station pill dispenser with its kiosk tablet at the FPT IoT Challenge 2026 Grand Final" /></a>

A wristband that flags a possible fall, freeze or spoken "help" on-device, a home Station that hands
the right pills to the right person and keeps working offline, and a caregiver app with live alerts.
Fall and freezing-of-gait models run full INT8 on a Silicon Labs EFR32xG26. **My part:** the pill
dispenser (2 × ESP32 motor layers, Pi-side pill counting, cup-pickup sensor) and the Station's kiosk.
<br /><sub>EFR32xG26 + BGM220 · TensorFlow Lite Micro · Raspberry Pi · ESP32 · FastAPI · Next.js · PostgreSQL</sub>

#### 🌸 [S.C.E.N.T: an Edge AIoT perfume shelf](https://github.com/baotrq/scent-showcase) · Second Prize, FPT IoT Challenge 2025
<a href="https://github.com/baotrq/scent-showcase"><img src="https://raw.githubusercontent.com/baotrq/scent-showcase/main/assets/award.jpg" alt="Team Edgelectronix on stage with the Second Prize at the FPT IoT Challenge 2025" /></a>

A shelf that recommends a fragrance from your personality and occasion and lights up the bottle, tracks
stock with load cells and IR beams, and hears a glass bottle break, over a Thread mesh. **My part:** the
recommendation model on an EFR32xG24, from a 50-class classifier to a contrastive 64-D embedding ranked
by cosine similarity, full INT8.
<br /><sub>EFR32xG24 / xG26 / MG21 · Silicon Labs MLTK · TensorFlow Lite Micro · OpenThread · Raspberry Pi · Flask</sub>

#### 🩺 [Ecyce MediLink: a smart pill dispenser](https://github.com/baotrq/ecyce-showcase) · First Runner-Up, NEO League Season 2
<a href="https://github.com/baotrq/ecyce-showcase"><img src="https://raw.githubusercontent.com/baotrq/ecyce-showcase/main/assets/hero.jpg" alt="Ecyce MediLink: the web dashboard's Health Overview next to the phone sign-up screen" /></a>

Recognises who's in front of it, reads a paper prescription into a schedule, drops exactly one pill at
a time and confirms each drop, over a local MQTT loop that works offline. **My part:** the web
dashboard and app flow: FaceID onboarding, prescription scan, schedule and AI chat.
<br /><sub>ESP32 · Raspberry Pi 4 · MQTT · ArcFace · Tesseract OCR · Gemma · SQLite · AWS IoT Core</sub>

---

### 🛠️ More builds

| | |
| :--- | :--- |
| 🥚 **[Egg Gripper](https://github.com/baotrq/egg-gripper-showcase)** | Lifts a raw egg 90 cm, holds it 30 s, puts it down unbroken: ESP32 force control on a fingertip load cell, egg-shaped TPU tips, a live 3D dashboard. **97/100** on the demo, MIET2561 (RMIT). |
| 🎵 **[SimpMusic (Bao)](https://github.com/baotrq/simpmusic-bao-showcase)** | My fork of the open-source YouTube Music client: a car LED strip follows the album art over a BLE protocol I reverse-engineered, playback follows me between phones, a player rebuilt for Samsung DeX. |
| ⏳ **[Age in Motion](https://github.com/baotrq/age-in-motion-showcase)** | An Android home-screen widget that counts your age up live to eight decimals, by handing the fast digits to the launcher's own ViewFlippers. |
