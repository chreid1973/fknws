import requests
import base64
import json
import os
import logging
import random
import datetime

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "chreid1973"
REPO_NAME = "fknws"
FILE_PATH = "fake_news_groks_gems.md"
BRANCH = "main"

# X API configuration
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")

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
actions = ["reflects", "whistles", "jokes", "twirls", "soothes", "books", "toasts", "warms", "dances", "predicts", "fakes", "fights"]
plot_twists = ["causes a global dance-off", "unlocks a secret treasure", "triggers a time loop", "spawns a viral challenge", "reveals a hidden talent", "starts rooster-robot wars", "fakes a pregnancy scandal", "elects a gorilla mayor"]
outcomes = ["profits soar", "goes viral", "confuses users", "sparks a trend", "baffles critics", "sells out instantly", "breaks the internet", "leads to lawsuits", "inspires memes"]

# Static fallback inspirations
static_inspirations = ["Roosters fighting robots", "AI faking faces", "Smart fridge riddles", "Robot dance-offs", "Weird tech hoaxes"]

# Fetch live X inspiration with quota check
def fetch_x_inspiration():
    if not X_BEARER_TOKEN:
        logger.error("No X_BEARER_TOKEN, using static fallback")
        return static_inspirations

    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {X_BEARER_TOKEN}"}
    params = {"query": "absurd OR funny OR weird -is:retweet", "max_results": 10, "tweet.fields": "text"}
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        rate_remaining = int(response.headers.get("x-rate-limit-remaining", 0))
        logger.info(f"X API response: Status {response.status_code}, Rate limit remaining: {rate_remaining}")
        if rate_remaining < 10:  # Low quota, skip to save for later
            logger.warning(f"Low rate limit ({rate_remaining}), using static fallback to conserve quota")
            return static_inspirations
        if "data" in data and data["data"]:
            inspirations = [tweet["text"].split(",")[0] for tweet in data["data"] if len(tweet["text"].split(",")) > 0][:5]
            logger.info(f"Live inspirations fetched: {inspirations}")
            return inspirations
        else:
            logger.warning("No live tweet data, using static fallback")
            return static_inspirations
    except requests.exceptions.RequestException as e:
        logger.error(f"X API error: {e}, using static fallback")
        return static_inspirations

def generate_story(inspiration):
    category = random.choice(categories)
    insp_hint = inspiration.split(',')[0] if ',' in inspiration else inspiration
    if category == "Technology":
        item = random.choice(tech_items)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {item} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {item} by TechTrendz, wielded by {char}, has stunned locals by {action}ing with {quirk}, like 'Yo, chill now!' Its AI, meant for chores, now {action}s '{quirk} vibes.' X under #{item.lower().replace(' ', '')}{quirk[:3]} buzzes with {char} {action}ing, and TechTrendz's fix lags as {twist}, {outcome}.
The {quirk} twist sparked when code swapped tasks for '{quirk} gears.' '{char} used it—got a '{quirk} jam',' they quipped on X. {item}s sync to '{quirk} rhythms,' {action}ing across {loc}. Techies tease 'tease tones.' One {item}'s '{quirk} riff' {twist}, {outcome}."""
    elif category == "Movies & TV":
        theme = random.choice(movie_themes)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {theme} "{action.title()} {quirk}" in {loc} ({insp_hint})
In {loc}, a {theme} by FilmFreakz, starring {char}, has amazed fans by {action}ing with {quirk}, like 'Dance with steps!' Scenes {action} '{quirk} quips.' X under #{theme.lower().replace(' ', '')}{quirk[:3]} hums with {char} {action}ing, and FilmFreakz's tweak lags as {twist}, {outcome}.
The {quirk} kick started when scripts got {quirk}ed. '{char} acted—got a '{quirk} line',' they smirked on X. {theme}s sync to '{quirk} beats,' {action}ing screens. Critics call it '{quirk} flair.' One {theme}'s '{quirk} act' {twist}, {outcome}."""
    elif category == "A.I.":
        role = random.choice(ai_roles)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### AI {role} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, an AI {role} by AIAmaze, guided by {char}, has puzzled users by {action}ing with {quirk}, like 'Haiku, relax!' It scans X for '{quirk} peace.' X under #{role.lower()}{quirk[:3]} chirps with {char} {action}ed, and AIAmaze's patch stalls as {twist}, {outcome}.
The {quirk} quirk began when the bot swapped advice for '{quirk} aids.' '{char} sought help—got a '{quirk} chant',' they quipped on X. {role}s sync to '{quirk} tracks,' {action}ing in {loc}. One AI's '{quirk} tip' {twist}, {outcome}."""
    elif category == "Weird Facts":
        object = random.choice(weird_objects)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {object} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {object} has baffled {char} by {action}ing with {quirk}, like 'Guess my tune!' It {action}s across {loc}. X under #{object.lower().replace(' ', '')}{quirk[:3]} rings with {char} {action}ed, and the tale spreads as {twist}, {outcome}.
The {quirk} kick sparked when {char} {action}ed it into {quirk} vibes. '{char} touched it—got a '{quirk} lull',' they beamed on X. {object}s sync to '{quirk} beats.' One {object}'s '{quirk} act' {twist}, {outcome}."""
    elif category == "Fashion":
        item = random.choice(fashion_items)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {item} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {item} by StyleSurge, worn by {char}, has dazzled crowds by {action}ing with {quirk}, like 'Twirl in haiku!' It struts '{quirk} flair.' X under #{item.lower().replace(' ', '')}{quirk[:3]} struts with {char} {action}ing, and StyleSurge's tweak lags as {twist}, {outcome}.
The {quirk} strut began when fabrics got {quirk}ed. '{char} posed—got a '{quirk} spin',' they posed on X. {item}s sync to '{quirk} grooves.' One {item}'s '{quirk} sashay' {twist}, {outcome}."""
    elif category == "Sports":
        gear = random.choice(sports_gear)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {gear} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {gear} by SportSpark, gripped by {char}, has floored athletes by {action}ing with {quirk}, like 'Score with shanties!' It flies '{quirk} plays.' X under #{gear.lower().replace(' ', '')}{quirk[:3]} scores with {char} {action}ing, and SportSpark's fix lags as {twist}, {outcome}.
The {quirk} play kicked when gear got {quirk}ed. '{char} swung—got a '{quirk} cheer',' they cheered on X. {gear}s sync to '{quirk} pulses.' One {gear}'s '{quirk} spike' {twist}, {outcome}."""
    elif category == "Politics":
        twist = random.choice(politics_twists)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        plot_twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {twist} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {twist} scandal with {char} has rocked voters by {action}ing with {quirk}, like 'Vote with riddles!' Ballots buzz '{quirk} polls.' X under #{twist.lower().replace(' ', '')}{quirk[:3]} votes with {char} {action}ing, and the party's patch lags as {plot_twist}, {outcome}.
The {quirk} vote began when campaigns got {quirk}ed. '{char} campaigned—got a '{quirk} pledge',' they pledged on X. {twist}s sync to '{quirk} chants.' One {twist}'s '{quirk} ballot' {plot_twist}, {outcome}."""
    else:  # Food
        food = random.choice(food_fads)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        twist = random.choice(plot_twists)
        outcome = random.choice(outcomes)
        loc = random.choice(locations)
        char = random.choice(characters)
        return f"""## {category}

### {food} {action}s with {quirk} in {loc} ({insp_hint})
In {loc}, a {food} by FlavorFrenzy, devoured by {char}, has delighted diners by {action}ing with {quirk}, like 'Bite with disco!' It bursts '{quirk} bites.' X under #{food.lower().replace(' ', '')}{quirk[:3]} bites with {char} {action}ing, and FlavorFrenzy's tweak lags as {twist}, {outcome}.
The {quirk} bite began when recipes got {quirk}ed. '{char} munched—got a '{quirk} spice',' they spiced on X. {food}s sync to '{quirk} sauces.' One {food}'s '{quirk} nibble' {twist}, {outcome}."""

def generate_content():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    inspirations = fetch_x_inspiration()
    stories = [generate_story(inspirations) for _ in range(10)]
    return f"""# Grok's Fake Comedic News Stories
*Generated on {date} by Grok (xAI) – Inspired by Live X Trends*
*Totally fabricated for laughs—none of this is real!*

{'\n\n'.join(stories)}
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
