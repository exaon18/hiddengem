# 💎 Hidden Gem | 3x3 Grid Game

**Hidden Gem** is a high-stakes, strategy-based mini-game built for the Telegram ecosystem. Players navigate a 3x3 grid to uncover sparkling gems while avoiding hidden bombs. Every successful find increases your multiplier, but one wrong move ends the round!

---

## 🎮 Gameplay Mechanics
- **The Grid:** A 3x3 layout containing 9 mystery tiles.
- **The Risk:** Before each round, 1 to 3 tiles are randomly assigned as bombs.
- **The Reward:** Uncover gems to build your multiplier. Cash out at any time or keep pushing for a "Full Board" bonus.
- **Instant Play:** Zero-friction entry via Telegram Mini App integration.

---

## 🛠 Tech Stack
- **Backend:** [Django 5.0+](https://www.djangoproject.com/)
- **Asynchronous Server:** [Daphne](https://github.com/django/daphne) (ASGI)
- **Frontend:** HTML5, CSS3, & Vanilla JavaScript
- **API Integration:** Telegram Web Apps SDK
- **Database:** SQLite (Development) / PostgreSQL (Production)

---

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone [https://github.com/exaon18/hiddengem.git](https://github.com/exaon18/hiddengem.git)
cd hiddengem

# Install dependencies
pip install django daphne python-decouple
