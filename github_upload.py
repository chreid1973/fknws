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

# Story generation components
categories = ["Technology", "Movies & TV", "A.I.", "Weird Facts"]
tech_items = ["Smart Mirror", "Kettle", "Toaster", "Drone"]
movie_themes = ["Sitcom", "Reality Show", "Superhero Flick"]
ai_roles = ["Therapist", "Travel Planner", "Chef"]
weird_objects = ["Coaster", "Socks", "Lamp"]
quirks = ["rap lyrics", "opera arias", "Morse code", "fairy tale steps", "pirate shanties", "game show slogans", "riddles", "lullabies"]
actions = ["reflects", "whistles", "jokes", "twirls", "soothes", "books", "toasts", "warms"]
outcomes = ["profits soar", "goes viral", "confuses users", "sparks a trend", "baffles critics"]

def generate_story():
    category = random.choice(categories)
    if category == "Technology":
        item = random.choice(tech_items)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        outcome = random.choice(outcomes)
        return f"""## {category}

### {item} {action} with {quirk}  
A new {item} from TechTrendz has stunned users by {action} with {quirk}, like "Yo, brew bold!" Its AI, meant for basic tasks, now delivers "{quirk.split()[0]} vibes," {action}ing "{quirk} tunes." X under #{item.lower()} buzzes with clips of a user grooving to a "{quirk} beat" mid-morning, and TechTrendz's fix is delayed as {outcome}.  
The {quirk} twist kicked in when the {item}'s code, loaded with {quirk} samples, swapped functions for "groove gears." "I toasted bread—got a '{quirk} jam' instead," a user joked on X, {item} vid popped. {item}s sync to "{quirk} rhythms," {action}ing across kitchens, with one {action}ing a "{quirk} hit." Techies tease "tease tones" for plain use.  
TechTrendz trends the tune to "{quirk} tracks" from archives, but patches pump "{quirk} pulses," pulsing {quirk}s in pulse {quirk}s. X fans fan "fan fads," fadding fans in fad fans, while stores stock "basic {item}s" for {item} basics. One {item}'s "{quirk} riff" {outcome}, sparking a "{quirk} craze." Users urge "urge updates" from {quirk}-soaked {item}s.  
The {item}'s {action}ing {quirk}s {action} "{quirk} hits." TechTrendz's trending "true {item}s," trending trues in true {item}s. "My {item}'s a {quirk} star now," one X user cheered. {item} shops shop "shopless {action}s," {action}ing shops in shopless {action} shops."""
    elif category == "Movies & TV":
        theme = random.choice(movie_themes)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        outcome = random.choice(outcomes)
        return f"""## {category}

### {theme} "{action.title()} {quirk}"  
A new {theme} from FilmFreakz has amazed viewers by {action}ing with {quirk}, like "Laugh with dot-dash!" Starring a quirky actor, the show’s scenes {action} "{quirk} quips," with one {action}ing a "{quirk} scene." X under #{theme.lower()}{quirk[:3]} hums with clips of a fan {action}ing to a "{quirk} plot," and FilmFreakz's tweak lags as {outcome}.  
The {quirk} kick started when scripts got {quirk}ed, {quirk}ing scripts in script {quirk}s, but set vibes {action}ed bits, {action}ing bits in bit {action}s. "I acted serious—got a '{quirk} line' instead," a star smirked on X, scene vid buzzed. {theme}s sync to "{quirk} beats," {action}ing across screens, with one {action}ing a "{quirk} twist." Critics call it "{quirk} flair," but cast cuts "cut cues."  
FilmFreakz films the fad to "{quirk} reels" from vaults, but patches push "{quirk} plays," playing {quirk}s in play {quirk}s. X viewers view "view vibes," vibing views in view vibes. One {theme}'s "{quirk} act" {outcome}, sparking a "{quirk} binge." Directors ditch "ditch drafts" from {quirk}-filled {theme}s.  
The {theme}'s {action}ing {quirk}s {action} "{quirk} scenes." FilmFreakz's filming "true {theme}s," filming trues in true {theme}s. "My {theme}'s a {quirk} show now," one X fan raved. Studios stage "stage shots," shooting stages in stage shot stages."""
    elif category == "A.I.":
        role = random.choice(ai_roles)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        outcome = random.choice(outcomes)
        return f"""## {category}

### AI {role} {action}s with {quirk}  
A new AI {role} from AIAmaze has puzzled users by {action}ing with {quirk}, like "Yo ho, relax now!" It scans X for "{quirk} peace," {action}ing "{quirk} notes" for tasks. X under #{role.lower()}{quirk[:3]} chirps with clips of a client {action}ed by a "{quirk} tune," and AIAmaze's patch stalls as {outcome}.  
The {quirk} quirk began when the {role}'s bot, fed with {quirk} files, swapped advice for "{quirk} aids," {action}ing "{quirk} tips." "I sought calm—got a '{quirk} chant' instead," a user quipped on X, session vid hummed. {role}s sync to "{quirk} tracks," {action}ing across devices, with one {action}ing a "{quirk} guide." Experts eye "eye edits" for plain help.  
AIAmaze aims the act to "{quirk} tunes" from stores, but updates usher "{quirk} waves," waving {quirk}s in wave {quirk}s. X users use "use updates," updating uses in use updates. One AI's "{quirk} tip" {outcome}, sparking a "{quirk} boom." {role}s request "request resets" from {quirk}-tuned AIs.  
The AI {role}'s {action}ing {quirk}s {action} "{quirk} aids." AIAmaze's aiding "true {role}s," aiding trues in true {role}s. "My {role}'s a {quirk} guru now," one X user grinned. AI hubs hub "hubless {action}s," {action}ing hubs in hubless {action} hubs."""
    else:  # Weird Facts
        object = random.choice(weird_objects)
        quirk = random.choice(quirks)
        action = random.choice(actions)
        outcome = random.choice(outcomes)
        return f"""## {category}

### {object} {action}s with {quirk}  
In a quirky shop, a {object} has baffled buyers by {action}ing with {quirk}, like "Guess my tune, sip your brew!" Dubbed "{object}Magic," it {action}s {action}s, {action}ing {action}s in {action} {action}s. X under #{object.lower()}{quirk[:3]} rings with clips of a user {action}ed by a "{quirk} riddle," and the shop's charm holds as {outcome}.  
The {quirk} kick sparked when a {object} {action}ed a use, {action}ing {action}s into {quirk} {action}s, {action}ing {quirk}s in {quirk} {action}s. "I wore it—heard a '{quirk} lull' instead," a buyer beamed on X, {object} vid sang. {object}s sync to "{quirk} beats," {action}ing across shelves, with one {action}ing a "{quirk} tale." Shoppers shrug "shrug styles" for plain {object}s.  
The shop shapes the show to "{quirk} rhythms" from racks, but tweaks tune "{quirk} tones," toning {quirk}s in tone {quirk}s. X fans fan "fan finds," finding fans in fan finds. One {object}'s "{quirk} act" {outcome}, sparking a "{quirk} fad." Sellers sell "sell silences" from {quirk}-lit {object}s.  
The {object}'s {action}ing {quirk}s {action} "{quirk} tales." The shop's shopping "true {object}s," shopping trues in true {object}s. "My {object}'s a {quirk} star now," one X user winked. {object} stores store "storeless {action}s," {action}ing stores in storeless {action} stores."""

def generate_content():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    stories = [generate_story() for _ in range(2)]  # Generate 2 random stories
    return f"""# Grok's Fake Comedic News Stories
*Generated on {date} by Grok (xAI)*
*Totally fabricated for laughs—none of this is real!*

{stories[0]}

{stories[1]}
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
        "message": f"Add/Update fake news stories to {FILE_PATH} on {BRANCH}",
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
