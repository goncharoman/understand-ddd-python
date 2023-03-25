from apiflask import APIFlask

app = APIFlask(__name__)


@app.get("/healthcheck")
def healthcheck():
    return {"health": "ok"}


if __name__ == "__main__":
    # Run dev server
    app.run(host="localhost", port=8080, debug=True)
