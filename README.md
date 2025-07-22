# :revolving_hearts: Relationship Generator API

A fun and expressive Flask API that generates dynamic relationship scenarios between two people. From wholesome to chaotic, romantic to spicy - this API delivers random, personalized relationship statements based on custom categories.

---

## :rocket: Features

* Generate randomized relationship lines between two people
* Multiple categories: **family, romantic, funny, spicy, wholesome**, and more
* JSON and plain text support
* Perfect for games, bots, and entertainment apps

---

## :link: Endpoint

### `GET /relation`

Generates a relationship scenario between two people.

#### :small_orange_diamond: Query Parameters:

| Parameter  | Required | Description                                                      |
| ---------- | -------- | ---------------------------------------------------------------- |
| `person1`  | :white_check_mark:        | Name to replace placeholder `1`                                  |
| `person2`  | :white_check_mark:        | Name to replace placeholder `2`                                  |
| `category` | :white_check_mark:        | Scenario category (see below). Use `random` for random selection |
| `json`     | :x:        | If set to `true`, returns a JSON object instead of plain text    |

---

## :open_file_folder: Available Categories

* `relations.basic`
* `relations.family`
* `relations.romantic`
* `relations.friendship`
* `relations.funny`
* `wants_to`
* `doing_together.wholesome`
* `doing_together.fun`
* `doing_together.chaotic`
* `doing_together.flirty`
* `doing_together.spicy`
* `doing_together.spiciest_safe`

---

## :test_tube: Example Requests

### Plain Text Response

```
GET /relation?person1=RKN&person2=Godz&category=relations.romantic
```

**Response:**

```
RKN is dating Godz
```

### JSON Response

```
GET /relation?person1=RKN&person2=Godz&category=doing_together.flirty&json=true
```

**Response:**

```json
{
  "category": "doing_together.flirty",
  "text": "RKN and Godz are sharing a bed (just sleeping... maybe)"
}
```

---

## 🔨 Running Locally

1. Clone this repository
2. Install Flask:

   ```bash
   pip install flask
   ```
3. Run the server:

   ```bash
   python app.py
   ```
4. Visit:

   ```
   http://localhost:5000/relation?person1=RKN&person2=Godz&category=random
   ```

---

## :pushpin: Notes

* Placeholders `1` and `2` in the template are automatically replaced with `person1` and `person2`.
* If the provided category doesn't exist, the API will return a 404 error.
* JSON output is optional and enabled using `json=true`.

---

## :orange_heart: License

This project is open-source and free to use. Customize and expand it for your own creative apps!

---

