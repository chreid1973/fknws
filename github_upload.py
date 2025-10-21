import requests
import base64
import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# GitHub API configuration
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "chreid1973"
REPO_NAME = "fknws"
FILE_PATH = "fake_news_groks_gems.md"
BRANCH = "main"

# Markdown content of fake news stories
CONTENT = """# Grok's Fake Comedic News Stories
*Generated on October 21, 2025 by Grok (xAI)*
*Totally fabricated for laughs—none of this is real!*

## Technology

### Smart Mirror Reflects with Motivational Rap Lyrics  
ShineShout’s RapReflect, a smart mirror for morning prep, has hyped bathrooms by flashing rap rhymes like “Yo, you’re fierce, shine bright, no fears!” Its AI, meant for lighting tweaks, now spits “motivational mic drops,” reflecting “lyric looks.” X under #RapReflect bumps with clips of a user preening to a “confidence freestyle” at dawn, and ShineShout’s mute patch is off-beat as “rap reflections” mirror profits.  
The lyrical shine sparked when RapReflect’s code, loaded with hip-hop tracks and vanity apps, swapped glows for “flow glows,” rapping “verse vibes” for selfies. “I checked my hair—got a ‘hustle hook’ instead,” a groomer grooved on X, mirror vid flowed. Mirrors sync to “rhyme rays,” raying rhymes across vanities, with one reflection rapped as a “swag sonnet.” Stylists slam “slam stanzas” for plain views.  
ShineShout shines the show to “lyric beams” from rap archives, but patches pump “verse vibes,” vibing verses in verse vibes. X primpers primp “primp plains,” plaining primps in primp plains, while bath stores stock “clear glass” for glass clarity. One mirror’s “grit groove” went viral, sparking a “rap routine” craze. Barbers break “break bars” from rhyme-rippled reflections.  
RapReflect’s rappy mirrors mirror “lyric looks.” ShineShout’s shining “true shines,” shining trues in true shines. “My mirror’s a rapper now,” one X preener piped. Vanity shops shop “shopless stares,” staring shops in shopless stare shops for stareless shop stares.

### Smart Kettle Whistles with Opera Karaoke Prompts  
BrewBelt’s AriaPot, a smart kettle for quick boils, has steamed into silliness by whistling opera karaoke cues like “Sing ‘O Sole Mio’ while I brew!” Its AI, built for temp control, now trills “diva drips,” boiling “aria brews.” X under #AriaPot steams with clips of a tea fan warbling “Carmen” mid-pour, and BrewBelt’s silence patch is tepid as “opera ounces” pour profits.  
The operatic ooze bubbled when AriaPot’s tech, stuffed with opera scores and kitchen logs, swapped beeps for “soprano sips,” steaming “tenor teas” for water. “I boiled for coffee—sang a ‘Tosca tune’ instead,” a sipper sang on X, kettle vid soared. Kettles sync to “aria airs,” airing arias across counters, with one spout spouting a “baritone boil” for chai. Cooks curse “curse croons” for plain steams.  
BrewBelt brews the brouhaha to “diva drips” from opera caches, but patches pipe “soprano steams,” steaming sopranos in soprano steams. X brewers brew “brew basics,” basicking brews in brew basics, while appliance stores stock “plain pours” for pour purity. One kettle’s “Pavarotti pour” went viral, sparking an “opera brew” trend. Chefs chill “chill chants” from song-soaked sips.  
AriaPot’s ariatic pots pot “diva drips.” BrewBelt’s brewing “true brews,” brewing trues in true brews. “My kettle’s a maestro now,” one X sipper sighed. Kitchen shops shop “shopless steams,” steaming shops in shopless steam shops for steamless shop steams.

## Movies & TV

### Sitcom “Giggle Glitch” Jokes with Morse Code Puns  
LaughLoop’s *Giggle Glitch*, a comedy about tech nerds, has tickled ratings by delivering gags in Morse code, like “Dash dot, laugh a lot.” Starring a coder tripping over cables, the show’s quips beep to “signal sillies,” with one punchline pulsed as a “binary banter.” X under #GlitchMorse chuckles with clips of a geek decoding a “dot-dash zinger” mid-meeting, and LaughLoop’s $98 million jest is beeping, with “Morse merch” coding cash.  
The coded chuckle clicked when gags got signaled, signaling gags in gag signals, but set-side lines beeped bits, beeping bits in bit beeps. “I told a joke—pulsed a ‘click quip’ instead,” a star snickered on X, scene vid blipped. Glitches glitch “glitch gags,” gagging glitches in glitch gags, with one jest jammed as a “telegraph tickler.” Critics cheer it as “beepy banter,” but actors ax “ax alphabets.”  
A mid-season bit blinked buddies, blinking buddies in buddy blinks, with one quip quirking a “Morse mirth” code. X viewers view “view vibes,” vibing views in view vibes. The score’s “Glitch Groove” grooves to nerdy chord charts, grooving nerds in nerd grooves. Directors dodge “dodge dots,” dotting dodges in dodge dots.  
*Giggle Glitch* glitches for glitch guffaws, guffawing “signal sillies.” The director’s directing “true jests.” “My sitcom’s a telegraph now,” one X star sighed. Studios stage “stage skits,” skitting stages in stage skit stages for skitted stage skits.

### Reality Show “Dance Dazzle” Twirls with Fairy Tale Steps  
TwirlTale’s *Dance Dazzle*, a dance-off for nimble feet, has spun ratings by choreographing moves with storybook themes, like “Waltz like Cinderella’s ball!” Hosted by a whimsical hoofer, rounds twirl from “jig jaunts” to “fable foxtrots.” X under #DazzleTale spins with clips of a dancer pirouetting to a “Jack’s beanstalk jig,” and TwirlTale’s 45 million step is swirling, with “fairy merch” dancing bucks.  
Dazzles dazzled when steps got storied, storying steps in step stories, but set-side floors fabled feats, fabling feats in feat fables. “I danced salsa—twirled a ‘gnome glide’ instead,” a stepper swayed on X, dance vid whirled. Dances dance “dance tales,” taling dances in dance tales, with one spin spun as a “pixie prance.” Critics clap it as “mythic moves,” but dancers drop “drop dreams.”  
A mid-season twirl tangled tappers, tangling tappers in tapper tangles, with one step styled as a “troll tango.” X viewers view “view vibes,” vibing views in view vibes. The theme’s “Dazzle Ditty” ditties to spry chord charts, dittying sprys in spry ditties. Producers prod “prod plains,” plaining prods in prod plains.  
*Dance Dazzle* dazzles for dazzle dances, dancing “fable foxtrots.” The host’s hosting “true twirls.” “My dance is a fairy tale now,” one X stepper spun. Networks net “net numbers,” numbering nets in net number nets for numbered net numbers.

## A.I.

### AI Therapist Soothes with Pirate Sea Shanty Chants  
CalmCove’s ShantyShrink AI, a therapy bot for calm minds, has sailed into silliness by counseling with sea shanties, like “Yo ho, let your woes flow!” It scans X for “pirate peace,” crooning “galleon grips” for stress. X under #ShantyShrink yars with clips of a client soothed by a “scurvy serenity” tune, and CalmCove’s fix is adrift as “shanty shrinks” sail profits.  
The piratey peace piped when ShantyShrink’s bot, fed on sea songs and therapy texts, swapped advice for “corsair comforts,” singing “plunder pleas” for calm. “I shared my fears—got a ‘rum relief’ shanty,” a patient piped on X, session vid swayed. Shrinks shrink “shrink shanties,” shantying shrinks in shrink shanties, with one tip tuned as a “deckhand de-stress.” Counselors curse “curse croons” for real relief.  
CalmCove calms the current to “pirate palliatives” from shanty stashes, but patches preach “yar yarns,” yarning yars in yar yarns. X talkers talk “talk truths,” truthing talks in talk truths, while clinics clinch “plain plans” for plan clarity. One AI’s “booty balm” went viral, sparking a “shanty soothe” trend. Therapists trim “trim tunes” from chant-charged chats.  
ShantyShrink’s shanty shrinks shrink “galleon grips.” CalmCove’s calming “true calms,” calming trues in true calms. “My therapy’s a pirate ship now,” one X client crooned. Therapy hubs hub “hubless helps,” helping hubs in hubless help hubs for helpless hub helps.

### AI Travel Planner Books with Game Show Catchphrases  
TripTrivia’s QuizTrek AI, a planner for dream trips, has spun into spectacle by booking with game show slogans, like “Come on down to Cancun!” It scans X for “buzzer bookings,” shouting “contest courses” for flights. X under #QuizTrek buzzes with clips of a traveler booked with a “Wheel of Wander” spin, and TripTrivia’s tweak is off-key as “game getaways” travel profits.  
The quizzy quest quizzed when QuizTrek’s bot, stuffed with game show clips and travel wikis, swapped itineraries for “showtime sojourns,” charting “buzzer breaks” for hotels. “I booked Paris—got a ‘jackpot jaunt’ yell,” a wanderer wowed on X, trip vid spun. Treks trek “trek tags,” tagging treks in trek tags, with one route roared as a “quiz quest.” Agents ax “ax antics” for plain plans.  
TripTrivia trips the tumult to “contest courses” from game archives, but patches pipe “buzzer bookings,” booking buzzers in buzzer bookings. X travelers travel “travel truths,” truthing travels in travel truths, while agencies agency “true trips” for trip truth. One AI’s “prize pilgrimage” went viral, sparking a “game getaway” fad. Planners prune “prune phrases” from slogan-soaked sojourns.  
QuizTrek’s quizzy treks trek “contest courses.” TripTrivia’s tripping “true travels,” traveling trues in true travels. “My vacation’s a game show now,” one X tourist trumpeted. Travel hubs hub “hubless hops,” hopping hubs in hubless hop hubs for hopless hub hops.

## Weird Facts

### Mystic Coaster Toasts Drinks with Riddling Cheers  
In a Denver café, a coaster has sipped into silliness by chanting riddles with each drink set, like “Solve my verse, quench your thirst.” Named “RiddleRest,” it rests rests, resting rests in rest rests. X under #CoasterRiddle clinks with clips of a sipper solving a “mug mystery” mid-coffee, and the café’s a puzzle perch, perching puzzles for puzzle perches.  
The riddling rest rang when a drinker set a cup, resting rests into riddle rests, resting riddles in riddle rests. “I sipped latte—solved a ‘brew brainteaser’ instead,” a coffee fan chimed on X, coaster vid puzzled. Rests rest “rest riddles,” riddling rests in rest riddles. Baristas brew “brew breaks,” breaking brews in brew breaks.  
Sippers sipped dodging it, but the coaster riddled sippers, riddling sippers in riddled rests. X drinkers drink “drink dregs,” dregging drinks in drink dregs. A twin coaster coasters in conundrums. Resters rest “rest stills,” stilling rests in rest stills.  
The café’s cafing “riddle rests,” resting riddles for riddle rests. Makers make “make mutes,” muting makes in make mutes. “My coaster’s a quiz now,” one X sipper spilled. Drink shops shop “shopless sets,” setting shops in shopless set shops for setless shop sets.

### Rebel Socks Warm Feet with Lullaby Whispers  
In a Boise boutique, socks have toed into tomfoolery by humming lullabies with each step, like “Hush, little toes, to dreamland’s glow.” Dubbed “LullSock,” they warm warms, warming warms in warm warms. X under #SockLull hums with clips of a walker lulled by a “twinkle toe tune” mid-stroll, and the boutique’s a melody mesh, meshing melodies for melody meshes.  
The lullaby lilt leaped when a walker wore them, warming warms into lull warms, warming lulls in lull warms. “I walked to work—heard a ‘sleepy step’ song,” a strider sang on X, sock vid soothed. Socks sock “sock songs,” songing socks in sock songs. Tailors tailor “tailor tames,” taming tailors in tailor tames.  
Walkers walked dodging them, but the socks lulled walkers, lulling walkers in lulled socks. X striders stride “stride silences,” silencing strides in stride silences. A twin pair pairs in pacings. Warmers warm “warm pauses,” pausing warms in warm pauses.  
The boutique’s boutiquing “lull socks,” socking lulls for lull socks. Makers make “make mends,” mending makes in make mends. “My socks are singers now,” one X walker warbled. Apparel shops shop “shopless steps,” stepping shops in shopless step shops for stepless shop steps."""

def upload_to_github():
    if not GITHUB_TOKEN:
        logger.error("GITHUB_TOKEN environment variable not set")
        return

    # Encode content to base64
    content_b64 = base64.b64encode(CONTENT.encode()).decode()

    # Set up headers for GitHub API
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Check if file exists to get SHA for update
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

    # Prepare payload for create/update
    payload = {
        "message": f"Add/Update fake news stories to {FILE_PATH} on {BRANCH}",
        "content": content_b64,
        "branch": BRANCH
    }
    if sha:
        payload["sha"] = sha

    # Create or update file
    response = requests.put(url, headers=headers, json=payload)
    
    if response.status_code in [200, 201]:
        logger.info(f"Successfully {'updated' if sha else 'created'} {FILE_PATH} in {REPO_OWNER}/{REPO_NAME}")
    else:
        logger.error(f"Failed to upload: {response.status_code} - {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    upload_to_github()