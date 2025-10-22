import requests
import base64
import json
import os
import logging
import random
import datetime
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "chreid1973"
REPO_NAME = "fknws"
current_date = datetime.datetime.now().strftime("%B %d, %Y")
FILE_PATH = f"daily_reports/FKNWS Report for {current_date}.md"  # Dynamic filename with folder
BRANCH = "main"

# X API configuration
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")  # Use if available, fallback to OAuth 1.1a

# Story generation components
categories = ["Technology", "Movies & TV", "A.I.", "Weird Facts", "Fashion", "Sports", "Politics", "Food"]
tech_items = ["Smart Mirror", "Kettle", "Toaster", "Drone", "Refrigerator", "Headphones", "Vacuum", "Smart Fridge"]
movie_themes = ["Sitcom", "Reality Show", "Superhero Flick", "Horror Movie", "Documentary", "Rom-Com"]
ai_roles = ["Therapist", "Travel Planner", "Chef", "Fitness Coach", "Tutor", "Detective"]
weird_objects = ["Coaster", "Socks", "Lamp", "Umbrella", "Clock", "Spoon", "Hat Rack"]
fashion_items = ["Hat", "Shoes", "Jacket", "Sunglasses", "Scarf", "Belt", "Gloves"]
sports_gear = ["Soccer Ball", "Basketball", "Helmet", "Tennis Racket", "Running Shoes", "Golf Club", "Yoga Mat"]
politics_twists = ["Election Hoax", "Viral Ballot Mix-Up", "AI Candidate"]
food_fads = ["Burger", "Pizza", "Ice Cream", "Taco", "Sushi Roll"]
locations = ["Tokyo", "New York", "Paris", "Sydney", "London", "Rio", "Oklahoma", "Cleveland", "Harambe Zoo"]
characters = ["Clumsy Inventor", "Dancing Grandma", "Tech-Savvy Kid", "Mysterious Chef", "Athletic Alien", "Fake Reporter", "Rooster Trainer"]
quirks = ["rap lyrics", "opera arias", "Morse code", "fairy tale steps", "pirate shanties", "game show slogans", "riddles", "lullabies", "haiku poems", "disco beats", "AI deepfakes", "robot fights"]
actions = ["reflects", "whistles", "jokes", "twirls", "soothes", "books with", "toasts", "warms", "dances", "predicts", "fakes", "fights"]
plot_twists = ["causes a global dance-off", "unlocks a secret treasure", "triggers a time loop", "spawns a viral challenge", "reveals a hidden talent", "starts rooster-robot wars", "fakes a pregnancy scandal", "elects a gorilla mayor"]
outcomes = ["profits soar", "goes viral", "confuses users", "sparks a trend", "baffles critics", "sells out instantly", "breaks the internet", "leads to lawsuits", "inspires memes"]

# Fetch live X inspiration
def fetch_x_inspiration():
    if X_BEARER_TOKEN:
        url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {"Authorization": f"Bearer {X_BEARER_TOKEN}"}
        params = {"query": "absurd technology -is:retweet", "max_results": 5}
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            limit_remaining = int(response.headers.get("x-rate-limit-remaining", 0))
            limit_reset = int(response.headers.get("x-rate-limit-reset", time.time()))
            logger.info(f"X API response: Status {response.status_code}, Rate limit remaining: {limit_remaining}, Reset at: {datetime.datetime.fromtimestamp(limit_reset).strftime('%Y-%m-%d %H:%M:%S')}")
            if limit_remaining == 0:
                logger.warning(f"Low rate limit ({limit_remaining}), waiting until {datetime.datetime.fromtimestamp(limit_reset).strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(max(0, limit_reset - time.time() + 1))
                return fetch_x_inspiration()
            if "data" in data:
                return [tweet["text"].split(",")[0] for tweet in data["data"] if len(tweet["text"].split(",")) > 0][:5]
        except requests.exceptions.RequestException as e:
            logger.error(f"X API error: {e}")
    else:
        auth = requests.auth.OAuth1(X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET)
        try:
            response = requests.get(url, auth=auth, params=params)
            response.raise_for_status()
            data = response.json()
            limit_remaining = int(response.headers.get("x-rate-limit-remaining", 0))
            limit_reset = int(response.headers.get("x-rate-limit-reset", time.time()))
            logger.info(f"X API response: Status {response.status_code}, Rate limit remaining: {limit_remaining}, Reset at: {datetime.datetime.fromtimestamp(limit_reset).strftime('%Y-%m-%d %H:%M:%S')}")
            if limit_remaining == 0:
                logger.warning(f"Low rate limit ({limit_remaining}), waiting until {datetime.datetime.fromtimestamp(limit_reset).strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(max(0, limit_reset - time.time() + 1))
                return fetch_x_inspiration()
            if "data" in data:
                return [tweet["text"].split(",")[0] for tweet in data["data"] if len(tweet["text"].split(",")) > 0][:5]
        except requests.exceptions.RequestException as e:
            logger.error(f"X API error: {e}")
    return ["No live data"]  # Simplified fallback to avoid list confusion

def generate_story(inspirations):
    category = random.choice(categories)
    inspiration = random.choice(inspirations)
    insp_hint = inspiration if inspiration != "No live data" else "Random Vibes"  # Clean fallback
    if category == "Technology":
        item = random.choice(tech_items)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {item} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {item} by TechTrendz, wielded by {char}, has stunned locals by {action}ing {quirk}, like 'Yo, chill now!' Its AI, meant for chores, now {action}s '{quirk} vibes.' X under #{item.lower()} buzzes with {char} {action}ing, and TechTrendz’s fix lags as {twist}, {outcome}.  
The {quirk} twist sparked when code swapped tasks for '{quirk} gears.' '{char} used it—got a "{quirk} jam,"' they quipped on X. {item}s sync to '{quirk} rhythms,' {action}ing across {loc}. Techies tease 'tease tones.' One {item}’s '{quirk} riff' {twist}, {outcome}."""
    elif category == "Movies & TV":
        theme = random.choice(movie_themes)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {theme} {action}s {quirk} in {loc} ({insp_hint})  
In {loc}, a {theme} by FilmFreakz, starring {char}, has amazed fans by {action}ing {quirk}, like 'Dance with steps!' Scenes {action} '{quirk} quips.' X under #{theme.lower()}{quirk[:3]} hums with {char} {action}ing, and FilmFreakz’s tweak lags as {twist}, {outcome}.  
The {quirk} kick started when scripts got {quirk}ed. '{char} acted—got a "{quirk} line,"' they smirked on X. {theme}s sync to '{quirk} beats,' {action}ing screens. Critics call it '{quirk} flair.' One {theme}’s '{quirk} act' {twist}, {outcome}."""
    elif category == "A.I.":
        role = random.choice(ai_roles)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### AI {role} {action}s {quirk} in {loc} ({insp_hint})  
In {loc}, an AI {role} by AIAmaze, guided by {char}, has puzzled users by {action}ing {quirk}, like 'Haiku, relax!' It scans X for '{quirk} peace.' X under #{role.lower()}{quirk[:3]} chirps with {char} {action}ed, and AIAmaze’s patch stalls as {twist}, {outcome}.  
The {quirk} quirk began when the bot swapped advice for '{quirk} aids.' '{char} sought help—got a "{quirk} chant,"' they quipped on X. {role}s sync to '{quirk} tracks,' {action}ing in {loc}. One AI’s '{quirk} tip' {twist}, {outcome}."""
    elif category == "Weird Facts":
        object = random.choice(weird_objects)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {object} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {object} has baffled {char} by {action}ing {quirk}, like 'Guess my tune!' It {action}s across {loc}. X under #{object.lower()}{quirk[:3]} rings with {char} {action}ed, and the tale spreads as {twist}, {outcome}.  
The {quirk} kick sparked when {char} {action}ed it into {quirk} vibes. '{char} touched it—got a "{quirk} lull,"' they beamed on X. {object}s sync to '{quirk} beats.' One {object}’s '{quirk} act' {twist}, {outcome}."""
    elif category == "Fashion":
        item = random.choice(fashion_items)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {item} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {item} by StyleSurge, worn by {char}, has dazzled crowds by {action}ing {quirk}, like 'Twirl in haiku!' It struts '{quirk} flair.' X under #{item.lower()}{quirk[:3]} struts with {char} {action}ing, and StyleSurge’s tweak lags as {twist}, {outcome}.  
The {quirk} strut began when fabrics got {quirk}ed. '{char} posed—got a "{quirk} spin,"' they posed on X. {item}s sync to '{quirk} grooves.' One {item}’s '{quirk} sashay' {twist}, {outcome}."""
    elif category == "Sports":
        gear = random.choice(sports_gear)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {gear} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {gear} by SportSpark, gripped by {char}, has floored athletes by {action}ing {quirk}, like 'Score with shanties!' It flies '{quirk} plays.' X under #{gear.lower()}{quirk[:3]} scores with {char} {action}ing, and SportSpark’s fix lags as {twist}, {outcome}.  
The {quirk} play kicked when gear got {quirk}ed. '{char} swung—got a "{quirk} cheer,"' they cheered on X. {gear}s sync to '{quirk} pulses.' One {gear}’s '{quirk} spike' {twist}, {outcome}."""
    elif category == "Politics":
        twist = random.choice(politics_twists)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        plot_twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {twist} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {twist} scandal with {char} has rocked voters by {action}ing {quirk}, like 'Vote with riddles!' Ballots buzz '{quirk} polls.' X under #{twist.lower()}{quirk[:3]} votes with {char} {action}ing, and the party’s patch lags as {plot_twist}, {outcome}.  
The {quirk} vote began when campaigns got {quirk}ed. '{char} campaigned—got a "{quirk} pledge,"' they pledged on X. {twist}s sync to '{quirk} chants.' One {twist}’s '{quirk} ballot' {plot_twist}, {outcome}."""
    else:  # Food
        food = random.choice(food_fads)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {food} {action} {quirk} in {loc} ({insp_hint})  
In {loc}, a {food} by FlavorFrenzy, devoured by {char}, has delighted diners by {action}ing {quirk}, like 'Bite with disco!' It bursts '{quirk} bites.' X under #{food.lower()}{quirk[:3]} bites with {char} {action}ing, and FlavorFrenzy’s tweak lags as {twist}, {outcome}.  
The {quirk} bite began when recipes got {quirk}ed. '{char} munched—got a "{quirk} spice,"' they spiced on X. {food}s sync to '{quirk} sauces.' One {food}’s '{quirk} nibble' {twist}, {outcome}."""

def generate_content():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    inspirations = fetch_x_inspiration()
    stories = [generate_story(inspirations) for _ in range(10)]  # 10 random stories
    return f"""# NWS not fit to print...
*Generated on {date} by Grok (xAI) – Inspired by Live X Trends*
*Totally fabricated for laughs—none of this is real!*

{''.join(stories)}
"""

def upload_to_github():
    if not GITHUB_TOKEN:
        logger.error("GITHUB_TOKEN environment variable not set")
        return

    content = generate_content()
    content_b64 = base64.b64encode(content.encode()).decode()

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FILE_PATH}?ref={BRANCH}"
    response = requests.get(url, headers=headers)
    sha = None
    if response.status_code == 200:
        sha = response.json().get("sha")
        logger.info(f"File {FILE_PATH} exists, SHA: {sha}")
    elif response.status_code == 404:
        logger.info(f"File {FILE_PATH} does not exist, will create new")
    else:
        logger.error(f"Failed to check file existence: {response.status_code} - {response.json().get('message', 'Unknown error')}")
        return

    payload = {
        "message": f"Add/Update 10 dynamic fake news stories to {FILE_PATH} on {BRANCH}",
        "content": content_b64,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code in [200, 201]:
        logger.info(f"Successfully {'updated' if sha else 'created'} {FILE_PATH} in {REPO_OWNER}/{REPO_NAME}")
    else:
        logger.error(f"Failed to upload: {response.status_code} - {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    upload_to_github()
