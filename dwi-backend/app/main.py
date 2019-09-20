from flask import Flask
from flask import render_template
from flask_caching import Cache
from flask_compress import Compress


app = Flask(__name__)
#cache = Cache(app, config={"CACHE_TYPE": "simple"})
Compress(app)


@app.route("/api/upload")
#@cache.cached(timeout=60)
def uploader():
    return "Success"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
