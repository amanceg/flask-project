from flask import Flask, request, render_template, jsonify

app=Flask(__name__)
JOBS=[
    {   
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi',
        'salary':'Rs. 100000'
    },
    {   
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi',
        'salary':'Rs. 100000'

    },
    {   
        'id':1,
        'title':'Data Analyst',
        'location':'Delhi',
        'salary':'Rs. 100000'

    }

]

@app.route("/")
def hello_world():
    return render_template('Home.html',
                           jobs=JOBS)
@app.route("/api/jobs")
def job_list():
    return jsonify(JOBS)




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)