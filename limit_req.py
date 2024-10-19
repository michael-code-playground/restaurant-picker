#pip install flask-limiter

#from flask_limiter import Limiter
#from flask_limiter.util import get_remote_address

#app = Flask(__name__)
#limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

#@app.route("/data")
#@limiter.limit("1 per second")  # Limit to 1 request per second