import logging
from flask import render_template

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_routes(app): 
    @app.route("/")
    def home_route():
        return render_template("home.html")
    
    @app.route("/mens-gezondheid")
    def mens_gezondheid_route():
        return render_template("category/mens_gezondheid.html")
    
    @app.route("/energie-water-veiligheid")
    def energie_water_veiligheid_route():
        return render_template("category/energie_water_veiligheid.html")
    
    @app.route("/voeding-natuur")
    def voeding_natuur_route():
        return render_template("category/voeding_natuur.html")
    
    @app.route("/voeding-natuur/makkelijk")
    def voeding_natuur_makkelijk_route():
        return render_template("quiz/voeding_natuur_makkelijk.html")
    
    @app.route("/voeding-natuur/normaal")
    def voeding_natuur_normaal_route():
        return render_template("quiz/voeding_natuur_normaal.html")
    
    @app.route("/voeding-natuur/moeilijk")
    def voeding_natuur_moeilijk_route():
        return render_template("quiz/voeding_natuur_moeilijk.html")
    
    @app.route("/wonen-werken-verkeer")
    def wonen_werken_verkeer_route():
        return render_template("category/wonen_werken_verkeer.html")
    
    @app.route("/wonen-werken-verkeer/makkelijk")
    def wonen_werken_verkeer_makkelijk_route():
        return render_template("quiz/wonen_werken_verkeer_makkelijk.html")
    
    @app.route("/wonen-werken-verkeer/normaal")
    def wonen_werken_verkeer_normaal_route():
        return render_template("quiz/wonen_werken_verkeer_normaal.html")
    
    @app.route("/wonen-werken-verkeer/moeilijk")
    def wonen_werken_verkeer_moeilijk_route():
        return render_template("quiz/wonen_werken_verkeer_moeilijk.html")
    
    @app.route("/ontwerp-productie-wereldhandel")
    def ontwerp_productie_wereldhandel_route():
        return render_template("category/ontwerp_productie_wereldhandel.html")
    
    @app.route("/digitaal-media-entertainment")
    def digitaal_media_entertainment_route():
        return render_template("category/digitaal_media_entertainment.html")
    
    @app.route("/digitaal-media-entertainment/makkelijk")
    def digitaal_media_entertainment_makkelijk_route():
        return render_template("quiz/digitaal_media_entertainment_makkelijk.html")
    
    @app.route("/digitaal-media-entertainment/normaal")
    def digitaal_media_entertainment_normaal_route():
        return render_template("quiz/digitaal_media_entertainment_normaal.html")
    
    @app.route("/digitaal-media-entertainment/moeilijk")
    def digitaal_media_entertainment_moeilijk_route():
        return render_template("quiz/digitaal_media_entertainment_moeilijk.html")
    
    @app.route("/hi-tech-science")
    def hi_tech_science_route():
        return render_template("category/hi_tech_science.html")
    
    @app.route("/mens-gezondheid/makkelijk")
    def mens_gezondheid_makkelijk_route():
        return render_template("quiz/mens_gezondheid_makkelijk.html")
    
    @app.route("/mens-gezondheid/normaal")
    def mens_gezondheid_normaal_route():
        return render_template("quiz/mens_gezondheid_normaal.html")
    
    @app.route("/mens-gezondheid/moeilijk")
    def mens_gezondheid_moeilijk_route():
        return render_template("quiz/mens_gezondheid_moeilijk.html")