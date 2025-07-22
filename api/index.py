from flask import Flask, Response, request, jsonify, abort
import random

app = Flask(__name__)

data = {
    "relations": {
        "basic": [
            "1 is son of 2",
            "1 is daughter of 2",
            "1 is husband of 2",
            "1 is wife of 2",
            "1 will propose 2 toda2",
            "1 wants to marr2 2"
        ],
        "family": [
            "1 is father of 2",
            "1 is mother of 2",
            "1 is brother of 2",
            "1 is sister of 2",
            "1 is grandfather of 2",
            "1 is grandmother of 2",
            "1 is uncle of 2",
            "1 is aunt of 2",
            "1 is cousin of 2",
            "1 is stepbrother of 2",
            "1 is stepsister of 2",
            "1 is son-in-law of 2",
            "1 is daughter-in-law of 2"
        ],
        "romantic": [
            "1 is dating 2",
            "1 has a crush on 2",
            "1 is engaged to 2",
            "1 is married to 2",
            "1 broke up with 2",
            "1 dumped 2",
            "1 secretly loves 2",
            "1 wrote a love letter to 2",
            "1 confessed feelings to 2",
            "1 is in a long-distance relationship with 2"
        ],
        "friendship": [
            "1 is best friend of 2",
            "1 is childhood friend of 2",
            "1 is enemy of 2",
            "1 is frenemie of 2",
            "1 met 2 at a party",
            "1 plays games with 2 every night",
            "1 trusts 2 with everything",
            "1 gossips with 2 every day",
            "1 and 2 are partners in crime"
        ],
        "funny": [
            "1 is stalking 2",
            "1 is 2's biggest fan",
            "1 simps for 2",
            "1 just ghosted 2",
            "1 blocked 2 last night",
            "1 and 2 eloped to Vegas",
            "1 sent 2 99 roses",
            "1 and 2 have a secret affair",
            "1 stole 2's heart",
            "1 rejected 2 in public",
            "1 is writing fanfiction about 2"
        ]
    },
    "wants_to": [
        "1 wants to marry 2",
        "1 wants to date 2",
        "1 wants to hug 2",
        "1 wants to kiss 2",
        "1 wants to cuddle 2",
        "1 wants to hold hands with 2",
        "1 wants to spend the rest of their life with 2",
        "1 wants to dance with 2",
        "1 wants to take 2 on a date",
        "1 wants to propose to 2",
        "1 wants to run away with 2",
        "1 wants to cook dinner for 2",
        "1 wants to watch the stars with 2",
        "1 wants to sing a love song to 2",
        "1 wants to protect 2 forever",
        "1 wants to start a family with 2",
        "1 wants to confess their feelings to 2",
        "1 wants to write poems for 2",
        "1 wants to grow old with 2",
        "1 wants to make 2 smile every day"
    ],
    "doing_together": {
        "wholesome": [
            "1 and 2 are watching a movie together",
            "1 and 2 are stargazing together",
            "1 and 2 are cuddling under a blanket together",
            "1 and 2 are cooking dinner together",
            "1 and 2 are walking in the rain together",
            "1 and 2 are dancing slowly together",
            "1 and 2 are building a life together",
            "1 and 2 are planning their wedding together",
            "1 and 2 are holding hands at sunset together",
            "1 and 2 are writing love letters together"
        ],
        "fun": [
            "1 and 2 are playing video games together",
            "1 and 2 are binge-watching a series together",
            "1 and 2 are exploring a haunted house together",
            "1 and 2 are pulling an all-nighter together",
            "1 and 2 are starting a podcast together",
            "1 and 2 are going on a road trip together",
            "1 and 2 are studying for finals together",
            "1 and 2 are creating a meme page together"
        ],
        "chaotic": [
            "1 and 2 are plotting world domination together",
            "1 and 2 are robbing a bank together (in GTA, hopefully)",
            "1 and 2 are causing drama together",
            "1 and 2 are stalking their exes together",
            "1 and 2 are spreading rumors together",
            "1 and 2 are prank-calling people together",
            "1 and 2 are running from the cops together",
            "1 and 2 are summoning a demon together",
            "1 and 2 are drunk texting their exes together"
        ],
        "flirty": [
            "1 and 2 are getting cozy together",
            "1 and 2 are having a late-night call together",
            "1 and 2 are cuddling under the covers together",
            "1 and 2 are watching a romantic movie together",
            "1 and 2 are flirting shamelessly together",
            "1 and 2 are sharing a bed (just sleeping... maybe)",
            "1 and 2 are enjoying a candlelit dinner together",
            "1 and 2 are slow dancing in the dark together",
            "1 and 2 are whispering sweet nothings together",
            "1 and 2 are feeding each other strawberries together",
            "1 and 2 are giving each other back massages together",
            "1 and 2 are teasing each other non-stop together",
            "1 and 2 are enjoying a \"do not disturb\" night together",
            "1 and 2 are making everyone else jealous together",
            "1 and 2 are disappearing for hours together 👀",
            "1 and 2 are having a \"Netflix and chill\" kind of night together",
            "1 and 2 are sharing steamy looks across the room together",
            "1 and 2 are lost in each other’s eyes together",
            "1 and 2 are tangled up on the couch together",
            "1 and 2 are being dangerously cute together"
        ],
        "spicy": [
            "1 and 2 are making out on the couch together",
            "1 and 2 are tangled up under the sheets together",
            "1 and 2 are sharing one very steamy night together",
            "1 and 2 are whispering dirty thoughts to each other together",
            "1 and 2 are losing sleep over each other together",
            "1 and 2 are testing the limits of their self-control together",
            "1 and 2 are exploring each other’s fantasies together",
            "1 and 2 are enjoying some very close body heat together",
            "1 and 2 are doing things that would make a movie blush together",
            "1 and 2 are leaving bite marks and lipstick stains together",
            "1 and 2 are making sparks (and maybe more) fly together",
            "1 and 2 are getting hot and breathless together",
            "1 and 2 are locking the door behind them together",
            "1 and 2 are taking \"Netflix and chill\" a bit too literally together",
            "1 and 2 are pushing each other up against the wall together",
            "1 and 2 are exchanging heated looks across the room together",
            "1 and 2 are whispering things that can't be repeated here together",
            "1 and 2 are exploring each other’s limits (safely 😉) together",
            "1 and 2 are making the bed creak... from jumping, obviously 🙃",
            "1 and 2 are having a night they'll never forget together"
        ],
        "spiciest_safe": [
            "1 and 2 are getting lost in each other tonight",
            "1 and 2 are tangled in tension together",
            "1 and 2 are turning the lights down low together",
            "1 and 2 are sharing a night full of stolen touches",
            "1 and 2 are dangerously close right now",
            "1 and 2 are blurring the line between love and lust",
            "1 and 2 are caught in the heat of the moment",
            "1 and 2 are exchanging looks that say it all",
            "1 and 2 are exploring the art of seduction together",
            "1 and 2 are wrapped in each other's arms... and intentions",
            "1 and 2 are playing a very intimate game together",
            "1 and 2 are toeing the edge of self-control together",
            "1 and 2 are sharing a night full of tension and teasing",
            "1 and 2 are enjoying the silence between heartbeats",
            "1 and 2 are up to something they won’t talk about in public",
            "1 and 2 are spending the night behind locked doors",
            "1 and 2 are leaving nothing to the imagination tonight",
            "1 and 2 are turning whispers into actions together",
            "1 and 2 are pushing each other’s buttons — in all the right ways",
            "1 and 2 are making memories they'll never admit to"
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
        abort(400, description="Missing required query parameters 'user1' and 'user2'")

    if not category:
        abort(400, description="Missing required query parameter 'category'")

    if category == "random":
        category = random.choice(list(flat_data.keys()))

    if category not in flat_data:
        abort(404, description=f"Category '{category}' not found")

    text = random.choice(flat_data[category])
    result_text = text.replace("1", person_a).replace("2", person_b)

    if json_flag == "true":
        return jsonify({
            "category": category,
            "text": result_text
        })
    else:
        return Response(result_text, mimetype="text/plain")

if __name__ == '__main__':
    app.run(debug=True)
