# Heroku-App-Deployment-Demo
<html>
  <body>
  <p align="justify">
  Flask is a straightforward and lightweight web application framework for Python applications. This guide walks you through how to write an application using Flask with a deployment on Heroku.

  Prerequisites :
   <ol> <li>Python</li>
    <li>Flask</li>
    <li>Git</li>
    <li>Heroku CLI</li>

  
I assume Python is installed already to system.We need to install flask with command `$pip install Flask`

We can work with any of the IDE and define below file structure<br><pre>
  static[optional]
    |_main.css 
templates
    |_index.html
app.py
model.py
model.pkl
requirements.txt
</pre>
The static directory contains your CSS files, and the template contains the HTML file, which is used for rendering.

  <h4>Step 1 : create model.py </h4>
                You can create a separate .py file for your logic and other operations or write code in the same app.py. I suggest creating a separate file will reduce 
                the confusion.
                Here `model.py` file was used to train the ML model.After model is trained dump the model to `.pkl` file

  <h4>STEP 2 : Create your app.py file</h4>
               We use `request.form.values()` to get values from the form.
               `predict()` has business logic to perform predictions on the input values.You can create seperate file with function and import it to app.py
               After collecting the data and performing the predictions, we can render the output using an HTML file.The output data will be displayed on the HTML page.
  
  <h4>Step 3:  Create an .html file</h4>
               Create an .HTML file to render the output that you collected from the response object.Here my html file is  `index.html` where we take input values from the form and render the output.
   
  Now, we are done with coding part we need few configuration files to proceed with deployment.
  1. Procfile<br>
     Procfile is a Process file that is required for all Heroku applications. Procfile specifies the commands that are executed by the app on startup.Enter the following in Procfile:<br>
    `web: gunicorn app:app`<br>
  2. requirements.txt<br>
     This file we have to include the required libraries.<br>
    
We will deploy app to Heroku by connecting to github reprository and thus you need to upload our all files to github repro.<br>
    Now go to [www.heroku.com](https://heroku.com/) , sign up or login.<br> 
    Step 1. Click on New and then click on Create new app<br>
    Step 2. Add App name , choose region and click on create app<br>
    Step 3. We can use Heroku CLI or github for deployment, From section Deployment Method click on github(connect to github) and add your reprositry name<br>
    Step 4. Now Click on Deploy Branch from Manual Deploy section.This will take few minutes to deploy and you will see link generated for your application after successful  build<br>
    Your app is live now, and you can see your web app using the generated URL.

Please check out my demo web application at: https://salaryprediction-app-ml.herokuapp.com/
</p> 
  </body>
  </html>
