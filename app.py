{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "fapp",
      "provenance": [],
      "mount_file_id": "1f26E8d4GTkFvdmeL3t6WSIa5KHYqUS3U",
      "authorship_tag": "ABX9TyNFwY8EGoLHvFHfCZjjStRN"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "MTXTMK8j6l4e"
      },
      "source": [
        "import pickle\n",
        "import numpy as np\n",
        "from flask import Flask, request, jsonify, render_template"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bm4VozNmNwfz"
      },
      "source": [
        "app = Flask(__name__)\n",
        "model = pickle.load(open(\"model.pkl\", \"rb\"))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ezypp1RORYhk"
      },
      "source": [
        "@app.route(\"/\")\n",
        "def home():\n",
        "    return render_template(\"home.html\")\n",
        "\n",
        "\n",
        "@app.route(\"/predict\", methods = [\"GET\", \"POST\"])\n",
        "def predict():\n",
        "    if request.method == \"POST\":\n",
        "      message = request.form['message']\n",
        "    \tdata = [message]\n",
        "    \tvect = cv.transform(data).toarray()\n",
        "    \tmy_prediction = classifier.predict(vect)   \n",
        "\n",
        "      return render_template('prediction.html',prediction_text=my_prediction)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    app.run(debug=True)"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}