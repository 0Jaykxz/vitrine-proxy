# é us guri não tem jeito

from flask import Flask, Response, stream_with_context
import requests

app = Flask(__name__)

RADIO_URL = "https://casthttps.suaradionanet.net/13615/stream"

@app.route('/')
def proxy():
    def generate():
        with requests.get(RADIO_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk
    return Response(stream_with_context(generate()), content_type='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
