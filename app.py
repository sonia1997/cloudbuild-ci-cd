import os
from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def Main():
    project_id=os.environ.get('PROJECT_ID')
    return render_template('project_id.html', project_id=project_id)

if __name__ == "__main__":
    app.run()
