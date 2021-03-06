## KompoziteUploadMeshCSV
### Kompozite Technical Test for an internship in Backend Web Development Q1)

### Objectives: 
- Create a serializable class (ie whose instances can easily be transformed into dictionaries) which
reproduces the Meshes data model
- Expose an endpoint which allows to upload a csv containing Me type data sh • Read and
parse the data from the csv file and make the necessary transformations (ex: automatically
convert "true" to true.
  -You must be able to detect obvious errors and correct them
  - In the event of an error that is not easily correctable, you must return an explicit
error message.

- Store the data in a database

### Extras
Help and details :
• The work should preferably be done in Python. On the other hand, the choice of libraries used
is open
• A test CSV file will be provided
• For storage, the solution is free, you can choose to store in a local database of the SQLlite type,
store in a database hosted by a cloud provider or save the items locally as a pickle.

### Requirements
Please install the following libraries
1. Python 3
2. Django
3. Django Rest Framework

### Run Web App
After installing the dependencies, run the following commands
1. cd into /mesh_api/mesh_api (You should see the file 'manage.py' in the directory)
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py runserver
