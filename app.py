from flask import Flask, request, jsonify
from selenium_script import run_selenium_script

app = Flask(__name__)

# Define the endpoint
@app.route('/run_selenium', methods=['POST'])
def run_selenium():
    # Get data from the request
    data = request.json
    
    # Extract parameters from the request body
    report_type = data.get('report_type')
    release_date = data.get('release_date')
    country = data.get('country')
    app_type = data.get('app_type')
    number_of_apps = data.get('number_of_apps')
    rank_lower = data.get('rank_lower')
    rank_upper = data.get('rank_upper')
    
    # Run the Selenium script with the provided data
    try:
        run_selenium_script(report_type, release_date, country, app_type, number_of_apps, rank_lower, rank_upper)
        return jsonify({"status": "success", "message": "Selenium script executed successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
