from fastapi import FastAPI

app = FastAPI()

# @app.get("/hello-world")
# def hello_world():
#     return {"message": "hello world"} #json

text_posts={
  "1":{"title":"new post", "content":"cool test post"}
}
@app.get("/posts")
def get_all_posts():
    return text_posts





