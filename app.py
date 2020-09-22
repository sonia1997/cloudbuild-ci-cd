import os
from flask import Flask, render_template, request, jsonify

app=Flask(__name__)
@app.route('/')
def Main():
    project_id=os.environ.get('PROJECT_ID')
    return render_template('project_id.html', project_id=project_id)

@app.route('/projectname')
def getProjectName():
    project_name=os.environ.get('PROJECT_NAME')
    response={"Project_name": project_name}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
