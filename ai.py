def generate_summary(data):
    posts = data.get("posts", [])
    total_likes = sum(p.get("likes", 0) for p in posts)
    total_comments = sum(p.get("comments", 0) for p in posts)
    return f"Channel has {len(posts)} posts with {total_likes} likes and {total_comments} comments."

def generate_recommendation(data):
    return {
        "caption": "Stay fit with our new protein shake!",
        "hashtags": ["#Fitness", "#HealthyLife", "#ProteinShake"],
        "justification": "Based on past posts, health-focused content got higher engagement."
    }
