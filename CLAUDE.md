# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a collection of independent Python learning projects, each demonstrating different Python concepts, libraries, and frameworks. Each project is self-contained in its own directory.

## Project Structure

The repository contains the following types of projects:

### Web Applications (Flask/FastAPI/Django)
- `EPOS RestAPI Flask/` - Flask REST API using flask_restful (in-memory restaurant management system)
- `fastAPICrud/` - FastAPI CRUD application with uvicorn server
- `weatherData/` - Flask weather dashboard using OpenWeatherMap API
- `stockapp/` - Flask stock profile finder using Financial Modeling Prep API
- `adsearch/` - Django web app for finding related ads and keywords using NLTK

### Games
- `Meteor Shooter game/` - Python game (likely using pygame)
- `wordle/` - Wordle implementation
- `secretNumber/` - Number guessing game

### Utilities and Tools
- `Freight-Manager/` - SQLite database application for freight/box management
- `libraryMgmtSystem/` - Library management system
- `loginSystem/` - User authentication system
- `Customer Cash Register/` - Cash register simulation with OOP design
- `blockchain/` - Blockchain implementation
- `Matrix Terminal ScreenSaver/` - Terminal screensaver

### API Integrations
- `nasaImagesAPI/` - NASA API image fetcher
- `redditAPI/` - Reddit API integration
- `openWeatherAutomate/` - Automated weather reporting
- `countrynewsapp/` - News API integration
- `cryptotracker/` - Cryptocurrency tracking

### Web Scraping
- `githubRepoScraping/` - GitHub repository scraper
- `googleFinanceScraping/` - Google Finance scraping
- `web-checker/` - Website monitoring tool

### Data Structures & Algorithms
- `Python Projects/python-ds-algo/` - Data structures and algorithms practice
- `caeser-cipher/` - Caesar cipher implementation

## Running Projects

### Flask Applications
Most Flask apps follow this pattern:
```bash
cd <project-directory>
python <main_file>.py
# Server starts on http://127.0.0.1:5000 (or port specified in file)
```

Key Flask projects:
- `EPOS RestAPI Flask/main.py` - Restaurant API endpoints at `/restaurant`, `/menu`, `/menu/<item>`
- `weatherData/app.py` - Weather dashboard (requires `config.ini` with OpenWeatherMap API key)
- `stockapp/server.py` - Stock profile app

### FastAPI Applications
```bash
cd fastAPICrud/app
python main.py
# Server starts on port 8000 with hot reload
```

### Django Applications
```bash
cd adsearch/mysite
python manage.py runserver
```

### Standalone Scripts
Most other projects can be run directly:
```bash
cd <project-directory>
python main.py
# or
python <filename>.py
```

## Common Dependencies

Projects use various external APIs that require configuration:

- **OpenWeatherMap API** - Used by `weatherData/`, `CityWeather/`, `openWeatherAutomate/`
- **Financial Modeling Prep API** - Used by `stockapp/`, `stockProfileFinder/`
- **NASA API** - Used by `nasaImagesAPI/`
- **Reddit API** - Used by `redditAPI/`

API keys are typically stored in:
- `config.ini` files (e.g., `weatherData/config.ini`)
- Environment variables or config files in individual project directories

## Database Projects

- **Freight-Manager** - Uses SQLite with custom schema for boxes, containers, and freight management
- **adsearch** - Uses Django ORM with SQLite (models in `myapp/models.py`)

## Important Notes

- Each project is independent with its own structure
- Many projects are learning exercises with in-memory data stores
- No centralized dependency management (no root `requirements.txt`)
- Projects may contain virtual environments (`venv/`, `env/`) that should be excluded from git
- The `.gitignore.txt` file exists but should be renamed to `.gitignore` for proper git exclusion