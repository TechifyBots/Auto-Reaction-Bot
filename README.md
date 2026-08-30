<div align="center">

<img src="https://bannerrender.vercel.app/api?type=waving&height=300&color=gradient&text=𝗔𝘂𝘁𝗼%20𝗥𝗲𝗮𝗰𝘁𝗶𝗼𝗻%20𝗕𝗼𝘁&fontAlignY=35&fontSize=80&desc=𝗠𝗮𝗸𝗶𝗻𝗴%20𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗼𝗻𝘀%20𝗠𝗼𝗿𝗲%20𝗘𝗻𝗴𝗮𝗴𝗶𝗻𝗴&descAlignY=60"/>

<p align="center">
A <b>modern</b>, <b>open-source</b>, and <b>developer-friendly</b> Telegram bot designed to bring conversations to life through automated emoji reactions with a focus on <b>performance</b>, <b>flexibility</b>, and <b>ease of deployment</b>.


⚡ Fast • 🎨 Flexible • 🚀 Self-Hosted
</p>


[![Last Commit](https://img.shields.io/github/last-commit/TechifyBots/Auto-Reaction-Bot?style=for-the-badge)](https://github.com/TechifyBots/Auto-Reaction-Bot/commits)
<br>
[![GitHub Stars](https://img.shields.io/github/stars/TechifyBots/Auto-Reaction-Bot?style=for-the-badge)](https://github.com/TechifyBots/Auto-Reaction-Bot/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/TechifyBots/Auto-Reaction-Bot?style=for-the-badge)](https://github.com/TechifyBots/Auto-Reaction-Bot/fork)
<br>
[![Repo Size](https://img.shields.io/github/languages/code-size/TechifyBots/Auto-Reaction-Bot?style=for-the-badge&color=8B5CF6)](https://github.com/TechifyBots/Auto-Reaction-Bot)
<br>
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://telegram.me/AlyaReactionBot)

</div>

<p align="center">
  <img src="https://raw.githubusercontent.com/TechifyBots/TechifyBots/main/assets/divider.svg" width="600" alt="divider"/>
</p>

## 📑 Table of Contents

- 🌸 **[Overview](#-overview)**
- ✨ **[Features](#-features)**
- 🎥 **[Quick Start](#-quick-start)**
- ⚙️ **[Configuration](#-configuration)**
- 🤖 **[Commands](#-commands)**
- 🚀 **[Deployment](#-deployment)**
- 🤝 **[Contributing](#-contributing)**
- 📄 **[License](#-license)**
- 💬 **[Updates & Support](#-updates--support)**
- 🙌 **[Credits](#-credits)**
- 👨‍💻 **[Connect With Me](#-connect-with-me)**

---

## 🌸 Overview

**Auto Reaction Bot** is a modern, open-source Telegram bot built to automatically react to messages across private chats, groups, and channels. Designed with flexibility, performance, and ease of use in mind, it provides a clean and developer-friendly solution for creating more engaging conversations through customizable emoji reactions.

> 💡 *Simple to deploy, easy to customize, and built for reliable long-term use.*

#### 🤔 Why Choose This Project?

- ⚡ **Boost Engagement** — Keep conversations active with automatic emoji reactions.
- 🎨 **Highly Customizable** — Configure reaction emojis and behavior for every chat.
- 🚀 **Deploy Anywhere** — Run seamlessly on Cloudflare, Vercel, Docker, Railway, Render, VPS, and more.
- 🔧 **Developer Friendly** — Clean, well-structured codebase that's easy to customize and extend.

#### 🔄 How It Works

1. 📩 **Message Is Received** — The bot detects new messages from private chats, groups, or channels.
2. ⚙️ **Rules Are Evaluated** — It checks chat settings, reaction configuration, permissions, and randomization.
3. 😊 **Reaction Is Added** — A suitable emoji reaction is applied automatically based on your configuration.
4. 🚀 **Conversations Stay Engaging** — Chats remain interactive and lively without manual effort.

---

## ✨ Features

- 🤖 **Automatic Reactions** — React to messages across private chats, groups, and channels.
- 🎨 **Fully Customizable** — Configure emojis, random levels, and chat-specific reaction settings.
- 👥 **Multi-Bot Support** — Run multiple bots from a single deployment with independent configurations.
- 🔒 **Community Management** — Force Subscribe, Welcome/Goodbye messages, and chat controls.
- 📊 **Monitoring & Analytics** — Live statistics, reaction logs, and chat activity insights.
- 📢 **Broadcast & Administration** — Broadcast messages and manage chats with powerful owner controls.
- 🛡️ **Secure by Design** — Webhook validation, rate limiting, and permission-based access.
- 📸 **Rich User Experience** — Interactive menus, photo messages, and inline buttons.
- ⚙️ **Developer Friendly** — Clean, modular, and easy-to-customize source code.

---

## 🎥 Quick Start

New to this project?

Watch this short video to understand **what the bot is**, **why it's useful**, **how it works**, explore its **key features**, and learn the **required configuration** before deployment.

📺 **Watch on YouTube: *[Project Overview](https://youtu.be/U1tWvTR_OlM)***

---


## 📝 Configuration

| Variable | Description |
|:---------|:------------|
| `BOT_TOKEN` | Telegram Bot Token |
| `BOT_USERNAME` | Telegram Bot Username |
| `BOT_TOKENS` | Multi-Bot Configuration |
| `EMOJI_LIST` | Default Reaction Emojis |
| `RANDOM_LEVEL` | Default Reaction Randomness |
| `OWNER_ID` | Telegram User ID |
| `FORCE_SUBSCRIBE_CHANNELS` | Force Subscribe Channels |
| `RESTRICTED_CHATS` | Restricted Chat IDs |
| `BOT_PHOTO` | Bot Photo |
| `WEBHOOK_SECRET` | Webhook Secret Token |
| `UPSTASH_REDIS_REST_URL` | Upstash Redis URL *(Optional)* |
| `UPSTASH_REDIS_REST_TOKEN` | Upstash Redis Token *(Optional)* |
| `PORT` | Server Port |

### 📝 Notes

> **🤖 Multi-Bot Support**
> Use `BOT_TOKEN` + `BOT_USERNAME` for a single bot, or `BOT_TOKENS` for multiple bots.
>
> **Format:**
> ```env
> BOT_TOKENS=token1:BotOne,token2:BotTwo
> ```

> **🎲 Random Level**
> Accepts values from **0–10**.
> - `0` → Always react
> - `5` → Balanced *(Recommended)*
> - `10` → Very rare reactions

> **🔒 Force Subscribe**
> Supports multiple channels. Use **@username** for public channels and the **private channel ID** for private channels.
>
> **Format:**
> ```env
> FORCE_SUBSCRIBE_CHANNELS=@PublicChannel,-1001234567890
> ```

> **💾 Persistent Storage**
> Configure `UPSTASH_REDIS_REST_URL` and `UPSTASH_REDIS_REST_TOKEN` for persistent storage.
>
> 🌐 **Create a free database:** https://console.upstash.com

> **🛡️ Webhook Secret**
> If `WEBHOOK_SECRET` is not set, a secure secret is generated automatically.


### 📚 Setup Guides

- 🔑 **Telegram API ID & API Hash** — [Watch Tutorial](https://youtu.be/y5FwAobQ-Kc)
- 🤖 **Bot Token** — [Watch Tutorial](https://youtu.be/rUEKDOSPFho)

---

## 🤖 Commands

<details>
<summary><b>👤 User Commands</b></summary>

```text
/start - Start the bot and view the main menu.
/help - Display all available commands.
/about - Learn more about the project.
/ping - Check the bot's response time.
/stats - View bot statistics.
/reactions - View configured reaction emojis.
/donate - Support the development of the project.
```

</details>

<details>
<summary><b>👥 Chat Admin Commands</b></summary>

```text
/pause - Pause reactions in the current chat.
/resume - Resume reactions in the current chat.
/welcome - Configure welcome messages.
/goodbye - Configure goodbye messages.
/setreactions - Configure reaction emojis.
/randomlevel - Set the reaction frequency.
```

</details>

<details>
<summary><b>🔒 Owner Commands</b></summary>

```text
/log - View recent logs.
/chats - View connected chats.
/leave - Remove the bot from a chat.
/restrict - Restrict a chat.
/unrestrict - Remove chat restrictions.
/broadcast - Broadcast messages.
/setwebhook - Configure the webhook.
```
</details>


<p align="center">
  <img src="https://raw.githubusercontent.com/TechifyBots/TechifyBots/main/assets/divider.svg" width="600" alt="divider"/>
</p>

## 🚀 Deployment

Deploy **Auto Reaction Bot** on **Cloudflare Workers** or **Vercel** using the official one-click deployment buttons below.

<div align="center">

[![Vercel](https://img.shields.io/badge/Deploy_to-Vercel-black?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/new/clone?repository-url=https://github.com/TechifyBots/Auto-Reaction-Bot)
<br>
[![Deploy to Cloudflare Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/TechifyBots/Auto-Reaction-Bot)

</div>

> [!TIP]
> Ensure your deployment is live before configuring the webhook.

### 📡 Webhook Setup

#### 🤖 Single Bot

Open the URL below after replacing the placeholders with your own values.

```text
https://api.telegram.org/bot<BOT_TOKEN>/setWebhook?url=<DEPLOYMENT_URL>&secret_token=<WEBHOOK_SECRET>
```

**Example**

```text
https://api.telegram.org/bot1234567890:ABCDEF/setWebhook?url=https://mybot.workers.dev&secret_token=123
```


#### 🤖🤖 Multi Bot

If you're using `BOT_TOKENS`, open the endpoint below after deployment.

```text
https://your-domain.com/set-webhooks
```

**Example**

```text
https://mybot.workers.dev/set-webhooks
```

Each bot automatically receives its own webhook endpoint.

```text
https://mybot.workers.dev/bot/AutoReactionBot
https://mybot.workers.dev/bot/MySecondBot
```

---

## 🤝 Contributing

*Contributions are always appreciated! ❤️*

| 🐞 **Report Bugs** | 💡 **Suggest Features** | 🚀 **Submit PRs** |
|:------------------:|:-----------------------:|:-----------------:|
| Found an issue? | Have an idea? | Ready to contribute? |
| **[Open Issue](https://github.com/TechifyBots/Auto-Reaction-Bot/issues)** | **[Open Discussion](https://github.com/TechifyBots/Auto-Reaction-Bot/issues)** | **[Fork & Submit](https://github.com/TechifyBots/Auto-Reaction-Bot/fork)** |

> [!IMPORTANT]
> *Before opening an issue, please ensure you're using the **[latest version](https://github.com/TechifyBots/Auto-Reaction-Bot)** and have followed the **[deployment guide](https://www.youtube.com/playlist?list=PLQrMSile4s5UnIEvWyKM1MKFuNg8Wfh2S)**.*

---

## 📄 License

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="License" />
  </a>
</p>

> [!WARNING]
> *This project is intended **strictly for educational purposes only**. The author is **not responsible** for any misuse or abuse. Please comply with all applicable laws and the terms of any third-party services. If you modify or redistribute this project, please provide proper credit to the original repository.*

See the **[LICENSE](./LICENSE)** file for complete details.

---

## 🫂 Updates & Support

<div align="center">

<a href="https://telegram.me/TechifyBots"><img src="https://tgcards.vercel.app/?username=TechifyBots&theme=light&verified=true" alt="Channel"></a>
<br>
<a href="https://telegram.me/TechifySupport"><img src="https://tgcards.vercel.app/?username=TechifySupport&theme=light" alt="Group"></a>

</div>

---

## 🙌 Credits

This repository is based on the original work of the following developers:

- **Original Developer:** [Shinei Nouzen](https://github.com/Shineii86)
- **Inspired by:** [Auto-Reaction-Bot](https://github.com/Malith-Rukshan/Auto-Reaction-Bot) by **Malith Rukshan**

> [!NOTE]
> This repository is maintained by **TechifyBots**, with improvements to the project presentation and user experience.

<p align="center">
  <img src="https://raw.githubusercontent.com/TechifyBots/TechifyBots/main/assets/divider.svg" width="600" alt="divider"/>
</p>

## 👤 Connect With Me

<p align="center">
  <b style="font-size: 5.5em;">Rahul Dhankhar</b>
  <br/>
  <sub><i>Open Source Maintainer • TechifyBots</i></sub>
<br/><br/>
<a href="https://github.com/TechifyBots"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://telegram.me/ImRahulDhankhar"><img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white"></a>
<a href="https://instagram.com/ImRahulDhankhar"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://youtube.com/@TechifyBots"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
<br>
<a href="https://techifybots.github.io/PayWeb">
  <img src="https://img.shields.io/badge/💖-Support_Development-ff4d6d?style=for-the-badge">
</a>
</p>
