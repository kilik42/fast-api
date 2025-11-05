from fastapi import FastAPI, HTTPException

app = FastAPI()

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "hello world"} #json

text_posts={
   "1": {"title": "New Post", "content": "Cool test post"},
  "2": {"title": "My First Blog", "content": "Learning how to create posts with JSON!"},
  "3": {"title": "Weekend Vibes", "content": "Relaxing and recharging for the week ahead."},
  "4": {"title": "Tech News", "content": "AI models are evolving faster than ever."},
  "5": {"title": "Motivation Monday", "content": "Stay positive and keep coding!"},
  "6": {"title": "Recipe Drop", "content": "Tried a new pasta recipe today. Amazing!"},
  "7": {"title": "Workout Log", "content": "Chest and triceps day — feeling strong."},
  "8": {"title": "Daily Journal", "content": "Just a chill day at the park with friends."},
  "9": {"title": "Quote of the Day", "content": "‘Do one thing every day that scares you.’ — Eleanor Roosevelt"},
  "10": {"title": "Project Update", "content": "Finished the login page and started working on comments."},
  "11": {"title": "Travel Thoughts", "content": "Can’t wait to visit Japan next summer."},
  "12": {"title": "Book Review", "content": "Just finished reading ‘Atomic Habits’ — 10/10!"},
  "13": {"title": "Music Pick", "content": "Been looping ‘Midnight City’ by M83 all week."},
  "14": {"title": "Coding Tip", "content": "Always use version control — future you will thank you."},
  "15": {"title": "Random Thought", "content": "What if clouds are just nature’s data storage?"},
  "16": {"title": "Photo Drop", "content": "Sunset over the lake — pure peace."},
  "17": {"title": "Dev Log", "content": "API routes are live! Next up: frontend integration."},
  "18": {"title": "Life Update", "content": "Got a new puppy — meet Luna!"},
  "19": {"title": "App Idea", "content": "A mindfulness timer that uses your heartbeat."},
  "20": {"title": "Thankful", "content": "Grateful for small wins and good people."}
}
@app.get("/posts")
def get_all_posts():
    return text_posts

# get individual posts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
      raise HTTPException(status_code=404, detail="post not found")
    return text_posts.get(id)


# create posts

@app.post("/posts")
def create_post(post: PostCreate) -> PostCreate:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys(), default=0) + 1] = new_post
    return new_post

