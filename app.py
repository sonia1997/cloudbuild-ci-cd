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
    build=os.environ.get('BUILD')
    tag=os.environ.get('tag')
    repo=os.environ.get('repo')
    branch=os.environ.get('branch')
    short=os.environ.get('short')
    rev=os.environ.get('REV')
    commit=os.environ.get('commit')

    response={"Project_name": project_name, "Build": build, "Branch": branch, "Commit": commit, "Tag": tag, "Repo": repo, "Short": short}
    return jsonify(response)

if __name__ == "__main__":
    app.run()
