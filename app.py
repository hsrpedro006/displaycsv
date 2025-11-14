from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("csv_file")

        if not file:
            return render_template("index.html", table=None)

        # Lê o CSV enviado pelo usuário
        df = pd.read_csv(file)

        table_html = df.to_html(classes="table table-striped", index=False)

        return render_template(
            "index.html",
            table=table_html,
            total=len(df),
            colunas=df.columns
        )

    return render_template("index.html", table=None)


if __name__ == "__main__":
    app.run(debug=True)
