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

# Expanded story generation components (more variables!)
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

# Inspiration from X/Web pulls (seeded from recent queries for absurd/fake news vibes)
x_web_inspirations = [
    "AI faking faces in assault stories, turning gray out of the blue",
    "Roosters fighting robots in Oklahoma—poultry vs. bots, no harm to birds",
    "Fake pregnancy ultrasound scam exposed on TV, leading to fraud charges",
    "Harambe gets 11,000 write-in votes in election—gorilla power!",
    "France bans work emails after 6 PM? Nope, total hoax revival",
    "Woman poops on boss's desk after lottery win—viral fake arrest tale",
    "Pope endorses Trump? Classic 2016 fake that keeps resurfacing",
    "AI videos easing DDS conspiracy theories—clowns unite!",
    "LA riots as smokescreen for Palantir? All fake and gay now",
    "Fried chicken toothpaste and llama mayoral runs—2025 absurdities"
]

def generate_story():
    category = random.choice(categories)
    inspiration = random.choice(x_web_inspirations)  # Pull random X/web vibe
    insp_hint = inspiration.split(',')[0]  # Short hook for flavor
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
In {loc}, a {item} by TechTrendz, wielded by {char}, has stunned locals by {action}ing with {quirk}, like "Yo, chill now!" Its AI, meant for chores, now {action}s "{quirk} vibes," {action}ing "{quirk} tunes." X under #{item.lower()} buzzes with {char} {action}ing to a "{quirk} beat," and TechTrendz’s fix lags as {twist}, {outcome}.  
The {quirk} twist sparked when the {item}’s code, loaded with {quirk} files, swapped tasks for "{quirk} gears." "{char} used it—got a '{quirk} jam' instead," they quipped on X, {item} vid popped. {item}s sync to "{quirk} rhythms," {action}ing across {loc}, with one {action}ing a "{quirk} hit." Techies tease "tease tones" for plain use.  
TechTrendz trends to "{quirk} tracks" from archives, but patches pump "{quirk} pulses," pulsing {quirk}s. X fans fan "fan fads," fadding in {loc}. One {item}’s "{quirk} riff" {twist}, {outcome}. Users urge "urge updates" from {quirk}-soaked {item}s."""
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
In {loc}, a {theme} by FilmFreakz, starring {char}, has amazed fans by {action}ing with {quirk}, like "Dance with steps!" Scenes {action} "{quirk} quips," with one {action}ing a "{quirk} scene." X under #{theme.lower()}{quirk[:3]} hums with {char} {action}ing a "{quirk} plot," and FilmFreakz’s tweak lags as {twist}, {outcome}.  
The {quirk} kick started when scripts got {quirk}ed, {quirk}ing in {loc}’s sets. "{char} acted—got a '{quirk} line' instead," they smirked on X, scene vid buzzed. {theme}s sync to "{quirk} beats," {action}ing across screens, with one {action}ing a "{quirk} twist." Critics call it "{quirk} flair," but cast cuts "cut cues."  
FilmFreakz films to "{quirk} reels" from vaults, but patches push "{quirk} plays." X viewers view "view vibes" in {loc}. One {theme}’s "{quirk} act" {twist}, {outcome}. Directors ditch "ditch drafts" from {quirk}-filled {theme}s."""
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
In {loc}, an AI {role} by AIAmaze, guided by {char}, has puzzled users by {action}ing with {quirk}, like "Haiku, relax!" It scans X for "{quirk} peace," {action}ing "{quirk} notes." X under #{role.lower()}{quirk[:3]} chirps with {char} {action}ed by a "{quirk} tune," and AIAmaze’s patch stalls as {twist}, {outcome}.  
The {quirk} quirk began when the {role}’s bot, fed with {quirk} files, swapped advice for "{quirk} aids." "{char} sought help—got a '{quirk} chant' instead," they quipped on X, session vid hummed. {role}s sync to "{quirk} tracks," {action}ing in {loc}, with one {action}ing a "{quirk} guide." Experts eye "eye edits" for plain help.  
AIAmaze aims to "{quirk} tunes" from stores, but updates usher "{quirk} waves." X users use "use updates" in {loc}. One AI’s "{quirk} tip" {twist}, {outcome}. {role}s request "request resets" from {quirk}-tuned AIs."""
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
In {loc}, a {object} has baffled {char} by {action}ing with {quirk}, like "Guess my tune!" Dubbed "{object}Magic," it {action}s {action}s, {action}ing across {loc}. X under #{object.lower()}{quirk[:3]} rings with {char} {action}ed by a "{quirk} riddle," and the tale spreads as {twist}, {outcome}.  
The {quirk} kick sparked when {char} {action}ed it, {action}ing into {quirk} {action}s. "{char} touched it—got a '{quirk} lull' instead," they beamed on X, {object} vid sang. {object}s sync to "{quirk} beats," {action}ing shelves, with one {action}ing a "{quirk} tale." Shoppers shrug "shrug styles" for plain {object}s.  
The shop shapes "{quirk} rhythms" from racks, but tweaks tune "{quirk} tones." X fans fan "fan finds" in {loc}. One {object}’s "{quirk} act" {twist}, {outcome}. Sellers sell "sell silences" from {quirk}-lit {object}s."""
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
In {loc}, a {item} by StyleSurge, worn by {char}, has dazzled crowds by {action}ing with {quirk}, like "Twirl in haiku!" It struts "{quirk} flair," {action}ing "{quirk} steps." X under #{item.lower()}{quirk[:3]} struts with {char} {action}ing a "{quirk} pose," and StyleSurge’s tweak lags as {twist}, {outcome}.  
The {quirk} strut began when fabrics got {quirk}ed, {quirk}ing in {loc}’s runways. "{char} posed—got a '{quirk} spin' instead," they posed on X, {item} vid swirled. {item}s sync to "{quirk} grooves," {action}ing closets, with one {action}ing a "{quirk} trend." Designers dig "dig drapes" for plain fits.  
StyleSurge styles to "{quirk} seams" from ateliers, but patches push "{quirk} patterns." X trenders trend "trend twists" in {loc}. One {item}’s "{quirk} sashay" {twist}, {outcome}. Stylists stitch "stitch silks" from {quirk}-draped {item}s."""
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
In {loc}, a {gear} by SportSpark, gripped by {char}, has floored athletes by {action}ing with {quirk}, like "Score with shanties!" It flies "{quirk} plays," {action}ing "{quirk} goals." X under #{gear.lower()}{quirk[:3]} scores with {char} {action}ing a "{quirk} slam," and SportSpark’s fix lags as {twist}, {outcome}.  
The {quirk} play kicked when gear got {quirk}ed, {quirk}ing in {loc}’s fields. "{char} swung—got a '{quirk} cheer' instead," they cheered on X, {gear} vid flew. {gear}s sync to "{quirk} pulses," {action}ing arenas, with one {action}ing a "{quirk} win." Coaches coach "coach calls" for plain plays.  
SportSpark sparks to "{quirk} scores" from playbooks, but patches pump "{quirk} pumps." X fans fan "fan feats" in {loc}. One {gear}’s "{quirk} spike" {twist}, {outcome}. Teams tackle "tackle tactics" from {quirk}-geared {gear}s."""
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
In {loc}, a {twist} scandal starring {char}, has rocked voters by {action}ing with {quirk}, like "Vote with riddles!" Ballots buzz "{quirk} polls," {action}ing "{quirk} votes." X under #{twist.lower()}{quirk[:3]} votes with {char} {action}ing a "{quirk} rally," and the party's patch lags as {plot_twist}, {outcome}.  
The {quirk} vote began when campaigns got {quirk}ed, {quirk}ing in {loc}’s halls. "{char} campaigned—got a '{quirk} pledge' instead," they pledged on X, ballot vid swung. {twist}s sync to "{quirk} chants," {action}ing booths, with one {action}ing a "{quirk} upset." Pundits ponder "ponder polls" for plain picks.  
Parties party to "{quirk} platforms" from histories, but patches push "{quirk} pledges." X voters vote "vote vibes" in {loc}. One {twist}’s "{quirk} ballot" {plot_twist}, {outcome}. Leaders lead "lead laws" from {quirk}-rigged {twist}s."""
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
In {loc}, a {food} by FlavorFrenzy, devoured by {char}, has delighted diners by {action}ing with {quirk}, like "Bite with disco!" It bursts "{quirk} bites," {action}ing "{quirk} flavors." X under #{food.lower()}{quirk[:3]} bites with {char} {action}ing a "{quirk} crunch," and FlavorFrenzy’s tweak lags as {twist}, {outcome}.  
The {quirk} bite began when recipes got {quirk}ed, {quirk}ing in {loc}’s kitchens. "{char} munched—got a '{quirk} spice' instead," they spiced on X, {food} vid sizzled. {food}s sync to "{quirk} sauces," {action}ing plates, with one {action}ing a "{quirk} feast." Chefs chef "chef chills" for plain plates.  
FlavorFrenzy flavors to "{quirk} fusions" from cookbooks, but patches pump "{quirk} peppers." X eaters eat "eat epics" in {loc}. One {food}’s "{quirk} nibble" {twist}, {outcome}. Diners dine "dine delights" from {quirk}-stuffed {food}s."""

def generate_content():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    stories = [generate_story() for _ in range(10)]  # Generate 10 random stories
    return f"""# Grok's Fake Comedic News Stories
*Generated on {date} by Grok (xAI) – Inspired by X & Web Absurdities*
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
