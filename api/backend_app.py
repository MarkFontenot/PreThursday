#-----------------------------------------------------------
# Main application interface
#-----------------------------------------------------------

# Import the create app function 
# from backend/rest_entry.py
from backend.rest_entry import create_app

# create the app object
app = create_app()

if __name__ == '__main__':
    # we want to run in debug mode (for hot reloading) 
    # this app will be bound to port 4000. 
    # Take a look at the docker-compose.yml to see 
    # what port this might be mapped to... 
    app.run(debug = True, host = '0.0.0.0', port = 4000)
