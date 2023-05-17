# reddit = praw.Reddit(client_id='QL9yW5E8djQGTG_WP7LVyg', 
#                         client_secret='nkDL-CHZR8CSXkANn0vLfl2I46QbgQ', 
#                         redirect_uri="", 
#                         user_agent='Pragadesh')



from flask import Flask, render_template, request
import praw

app = Flask(__name__)

# Set up the Reddit API
reddit = praw.Reddit(client_id='QL9yW5E8djQGTG_WP7LVyg', 
                        client_secret='nkDL-CHZR8CSXkANn0vLfl2I46QbgQ', 
                        redirect_uri="", 
                        user_agent='Pragadesh')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    # Get the user's query from the form
    query = request.form["query"]

    # Search for posts that match the query
    results = reddit.subreddit("all").search(query, limit=10)

    # Get the relevant comments for each post
    posts = []
    for post in results:
        post_data = {
            "title": post.title,
            "url": post.url,
            "comments": []
        }
        post.comments.replace_more(limit=0)
        for comment in post.comments:
            post_data["comments"].append(comment.body)
        posts.append(post_data)
			
		# posts=posts[0]
    # Render the results template with the posts and comments
    return render_template("results.html", query=query, posts=posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)












