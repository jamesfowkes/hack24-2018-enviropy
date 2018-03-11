
from flask import Flask, request, jsonify

from latlng import LatLng

import enviro
import mode

app = Flask(__name__)

@app.route("/score")
def get_route_score():
    try:
        latlng_start = LatLng.from_string(request.args["start"])
        latlng_end = LatLng.from_string(request.args["end"])
        transport_mode = enviro.get_mode(request.args["mode"])
        distance = float(request.args["distance"])
    except:
        abort(400)

    population_modifier = enviro.get_route_population_density_modifier(latlng_start, latlng_end)
    (co2_score, nox_score) = enviro.get_scores(transport_mode, distance, pop=population_modifier)

    return jsonify({
        "co2_score": co2_score,
        "nox_score": nox_score,
        "total_score": co2_score+nox_score
    })

if __name__ == "__main__":
    app.run()