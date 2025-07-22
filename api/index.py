from flask import Flask, Response, request, jsonify, abort
import random

app = Flask(__name__)

data = {
    "relations": {
        "basic": [
            "{user1}  is son of {user2}",
            "{user1}  is daughter of {user2}",
            "{user1}  is husband of {user2}",
            "{user1}  is wife of {user2}",
            "{user1}  will propose {user2} toda{user2}",
            "{user1}  wants to marry {user2}"
        ],
        "family": [
            "{user1}  is father of {user2}",
            "{user1}  is mother of {user2}",
            "{user1}  is brother of {user2}",
            "{user1}  is sister of {user2}",
            "{user1}  is grandfather of {user2}",
            "{user1}  is grandmother of {user2}",
            "{user1}  is uncle of {user2}",
            "{user1}  is aunt of {user2}",
            "{user1}  is cousin of {user2}",
            "{user1}  is stepbrother of {user2}",
            "{user1}  is stepsister of {user2}",
            "{user1}  is son-in-law of {user2}",
            "{user1}  is daughter-in-law of {user2}"
        ],
        "romantic": [
            "{user1}  is dating {user2}",
            "{user1}  has a crush on {user2}",
            "{user1}  is engaged to {user2}",
            "{user1}  is married to {user2}",
            "{user1}  broke up with {user2}",
            "{user1}  dumped {user2}",
            "{user1}  secretly loves {user2}",
            "{user1}  wrote a love letter to {user2}",
            "{user1}  confessed feelings to {user2}",
            "{user1}  is in a long-distance relationship with {user2}"
        ],
        "friendship": [
            "{user1}  is best friend of {user2}",
            "{user1}  is childhood friend of {user2}",
            "{user1}  is enemy of {user2}",
            "{user1}  is frenemie of {user2}",
            "{user1}  met {user2} at a party",
            "{user1}  plays games with {user2} every night",
            "{user1}  trusts {user2} with everything",
            "{user1}  gossips with {user2} every day",
            "{user1}  and {user2} are partners in crime"
        ],
        "funny": [
            "{user1}  is stalking {user2}",
            "{user1}  is {user2}'s biggest fan",
            "{user1}  simps for {user2}",
            "{user1}  just ghosted {user2}",
            "{user1}  blocked {user2} last night",
            "{user1}  and {user2} eloped to Vegas",
            "{user1}  sent {user2} 99 roses",
            "{user1}  and {user2} have a secret affair",
            "{user1}  stole {user2}'s heart",
            "{user1}  rejected {user2} in public",
            "{user1}  is writing fanfiction about {user2}"
        ]
    },
    "wants_to": [
        "{user1}  wants to marry {user2}",
        "{user1}  wants to date {user2}",
        "{user1}  wants to hug {user2}",
        "{user1}  wants to kiss {user2}",
        "{user1}  wants to cuddle {user2}",
        "{user1}  wants to hold hands with {user2}",
        "{user1}  wants to spend the rest of their life with {user2}",
        "{user1}  wants to dance with {user2}",
        "{user1}  wants to take {user2} on a date",
        "{user1}  wants to propose to {user2}",
        "{user1}  wants to run away with {user2}",
        "{user1}  wants to cook dinner for {user2}",
        "{user1}  wants to watch the stars with {user2}",
        "{user1}  wants to sing a love song to {user2}",
        "{user1}  wants to protect {user2} forever",
        "{user1}  wants to start a family with {user2}",
        "{user1}  wants to confess their feelings to {user2}",
        "{user1}  wants to write poems for {user2}",
        "{user1}  wants to grow old with {user2}",
        "{user1}  wants to make {user2} smile every day"
    ],
    "doing_together": {
        "wholesome": [
            "{user1}  and {user2} are watching a movie together",
            "{user1}  and {user2} are stargazing together",
            "{user1}  and {user2} are cuddling under a blanket together",
            "{user1}  and {user2} are cooking dinner together",
            "{user1}  and {user2} are walking in the rain together",
            "{user1}  and {user2} are dancing slowly together",
            "{user1}  and {user2} are building a life together",
            "{user1}  and {user2} are planning their wedding together",
            "{user1}  and {user2} are holding hands at sunset together",
            "{user1}  and {user2} are writing love letters together"
        ],
        "fun": [
            "{user1}  and {user2} are playing video games together",
            "{user1}  and {user2} are binge-watching a series together",
            "{user1}  and {user2} are exploring a haunted house together",
            "{user1}  and {user2} are pulling an all-nighter together",
            "{user1}  and {user2} are starting a podcast together",
            "{user1}  and {user2} are going on a road trip together",
            "{user1}  and {user2} are studying for finals together",
            "{user1}  and {user2} are creating a meme page together"
        ],
        "chaotic": [
            "{user1}  and {user2} are plotting world domination together",
            "{user1}  and {user2} are robbing a bank together (in GTA, hopefully)",
            "{user1}  and {user2} are causing drama together",
            "{user1}  and {user2} are stalking their exes together",
            "{user1}  and {user2} are spreading rumors together",
            "{user1}  and {user2} are prank-calling people together",
            "{user1}  and {user2} are running from the cops together",
            "{user1}  and {user2} are summoning a demon together",
            "{user1}  and {user2} are drunk texting their exes together"
        ],
        "flirty": [
            "{user1}  and {user2} are getting cozy together",
            "{user1}  and {user2} are having a late-night call together",
            "{user1}  and {user2} are cuddling under the covers together",
            "{user1}  and {user2} are watching a romantic movie together",
            "{user1}  and {user2} are flirting shamelessly together",
            "{user1}  and {user2} are sharing a bed (just sleeping... maybe)",
            "{user1}  and {user2} are enjoying a candlelit dinner together",
            "{user1}  and {user2} are slow dancing in the dark together",
            "{user1}  and {user2} are whispering sweet nothings together",
            "{user1}  and {user2} are feeding each other strawberries together",
            "{user1}  and {user2} are giving each other back massages together",
            "{user1}  and {user2} are teasing each other non-stop together",
            "{user1}  and {user2} are enjoying a \"do not disturb\" night together",
            "{user1}  and {user2} are making everyone else jealous together",
            "{user1}  and {user2} are disappearing for hours together 👀",
            "{user1}  and {user2} are having a \"Netflix and chill\" kind of night together",
            "{user1}  and {user2} are sharing steamy looks across the room together",
            "{user1}  and {user2} are lost in each other’s eyes together",
            "{user1}  and {user2} are tangled up on the couch together",
            "{user1}  and {user2} are being dangerously cute together"
        ],
        "spicy": [
            "{user1}  and {user2} are making out on the couch together",
            "{user1}  and {user2} are tangled up under the sheets together",
            "{user1}  and {user2} are sharing one very steamy night together",
            "{user1}  and {user2} are whispering dirty thoughts to each other together",
            "{user1}  and {user2} are losing sleep over each other together",
            "{user1}  and {user2} are testing the limits of their self-control together",
            "{user1}  and {user2} are exploring each other’s fantasies together",
            "{user1}  and {user2} are enjoying some very close body heat together",
            "{user1}  and {user2} are doing things that would make a movie blush together",
            "{user1}  and {user2} are leaving bite marks and lipstick stains together",
            "{user1}  and {user2} are making sparks (and maybe more) fly together",
            "{user1}  and {user2} are getting hot and breathless together",
            "{user1}  and {user2} are locking the door behind them together",
            "{user1}  and {user2} are taking \"Netflix and chill\" a bit too literally together",
            "{user1}  and {user2} are pushing each other up against the wall together",
            "{user1}  and {user2} are exchanging heated looks across the room together",
            "{user1}  and {user2} are whispering things that can't be repeated here together",
            "{user1}  and {user2} are exploring each other’s limits (safely 😉) together",
            "{user1}  and {user2} are making the bed creak... from jumping, obviously 🙃",
            "{user1}  and {user2} are having a night they'll never forget together"
        ],
        "spiciest_safe": [
            "{user1}  and {user2} are getting lost in each other tonight",
            "{user1}  and {user2} are tangled in tension together",
            "{user1}  and {user2} are turning the lights down low together",
            "{user1}  and {user2} are sharing a night full of stolen touches",
            "{user1}  and {user2} are dangerously close right now",
            "{user1}  and {user2} are blurring the line between love and lust",
            "{user1}  and {user2} are caught in the heat of the moment",
            "{user1}  and {user2} are exchanging looks that say it all",
            "{user1}  and {user2} are exploring the art of seduction together",
            "{user1}  and {user2} are wrapped in each other's arms... and intentions",
            "{user1}  and {user2} are playing a very intimate game together",
            "{user1}  and {user2} are toeing the edge of self-control together",
            "{user1}  and {user2} are sharing a night full of tension and teasing",
            "{user1}  and {user2} are enjoying the silence between heartbeats",
            "{user1}  and {user2} are up to something they won’t talk about in public",
            "{user1}  and {user2} are spending the night behind locked doors",
            "{user1}  and {user2} are leaving nothing to the imagination tonight",
            "{user1}  and {user2} are turning whispers into actions together",
            "{user1}  and {user2} are pushing each other’s buttons — in all the right ways",
            "{user1}  and {user2} are making memories they'll never admit to"
        ]
    }
}

def flatten_categories(data_dict):
    flat = {}
    for key, val in data_dict.items():
        if isinstance(val, dict):
            for subkey, subval in val.items():
                flat[f"{key}.{subkey}"] = subval
        else:
            flat[key] = val
    return flat

flat_data = flatten_categories(data)

@app.route('/relation', methods=['GET'])
def get_relation():
    person_a = request.args.get("person1")
    person_b = request.args.get("person2")

    json_flag = request.args.get("json")
    category = request.args.get('category')
    if not person_a or not person_b:
        abort(400, description="Missing required query parameters 'person1' and 'person2'")

    if not category:
        abort(400, description="Missing required query parameter 'category'")

    if category == "random":
        category = random.choice(list(flat_data.keys()))

    if category not in flat_data:
        abort(404, description=f"Category '{category}' not found")

    text = random.choice(flat_data[category])
    result_text = text.replace("{user1}", person_a).replace("{user2}", person_b)

    if json_flag == "true":
        return jsonify({
            "category": category,
            "text": result_text
        })
    else:
        return Response(result_text, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
