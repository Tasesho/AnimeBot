<div align="center">

# 📺 Anime Schedule

*A lightweight Discord bot that notifies you when new anime episodes are released.*

[![CI](https://img.shields.io/github/actions/workflow/status/Tasesho/AnimeBot/ci.yml?label=CI&logo=githubactions)](#)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?logo=python&logoColor=white)
![discord.py](https://img.shields.io/badge/discord.py-2.x-5865F2?logo=discord&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-Linting-D7FF64?logo=ruff&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

*A simple Discord bot that tracks airing anime and sends personalized release notifications only for the series you follow.*

</div>

---

## Overview

Anime Notify is a self-hosted Discord bot designed to solve a simple problem:

Instead of receiving notifications for every seasonal anime, users subscribe only to the titles they care about. Whenever a new episode is released, the bot automatically sends a rich Discord embed containing useful information and links to supported providers.

---

##  Features

-  Follow your favorite anime
-  Personal release notifications
-  User-specific subscriptions
-  Asynchronous architecture
-  PostgreSQL persistence
-  Docker deployment
-  GitHub Actions CI/CD
-  Ruff code formatting & linting

---

##  Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12+ |
| Discord API | discord.py |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| HTTP Client | aiohttp |
| Scheduler | APScheduler |
| Validation | Pydantic |
| Linting | Ruff |
| Testing | Pytest |
| Containers | Docker |
| CI/CD | GitHub Actions |

---

##  Project Structure

```text
.
├── .github/
│   └── workflows/
├── .venv/
├── src/
│   ├── commands/
│   ├── database/
│   ├── models/
│   ├── scheduler/
│   ├── services/
│   └── utils/
├── .env.example
├── .gitignore
├── bot.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml
└── README.md
```

---

##  Planned Commands

```text
/follow <anime>

/unfollow <anime>

/list

/search <anime>

/schedule
```

---

##  Notification Flow

```text
User
 │
 │  /follow Frieren
 ▼
Database
 │
 ▼
Scheduler
 │
 ▼
AniList
 │
 ▼
New Episode?
 │
 ├── No → Wait
 │
 └── Yes
        │
        ▼
 Discord Embed Notification
```

---

##  Roadmap

### Version 0.1

- [x] Repository initialization
- [x] GitHub Actions
- [x] Ruff integration
- [x] Discord bot bootstrap
- [ ] AniList client
- [ ] PostgreSQL integration

### Version 0.5

- [ ] `/follow`
- [ ] `/unfollow`
- [ ] Episode scheduler
- [ ] Rich embed notifications

### Version 1.0

- [ ] Multiple providers
- [ ] Docker deployment
- [ ] Production ready

---

> [!NOTE]
>
> This project is currently under active development.
>
> The main goal of the first release is to provide reliable anime episode notifications with a clean and maintainable architecture.

---

##  License

Distributed under the MIT License.