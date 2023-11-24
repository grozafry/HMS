# from app import app

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template

import requests

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from config import Config



app = Flask(__name__)
# app.config.from_object(Config)

# from app import views
# from app import models

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_headers', methods=['POST'])
def get_headers():
    domain = request.form['domain']
    
    try:
        

        from rules import Rules
        rules = Rules(domain)
    
    
        # res_csp = rules.check_csp()
        # return render_template('headers.html', domain=domain, csp_valid=res_csp[0], csp_remarks=res_csp[1], headers=headers)
    
        res_rules, score = rules.run_rules()

        return render_template('headers.html', data=res_rules, score=score, domain=domain)
    
    except requests.exceptions.RequestException:
        return "Error: Unable to fetch headers."

if __name__ == '__main__':
    app.run(debug=True)