import os

# each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists('projects/' + directory):
        print('Creating project directory ' + directory)
        os.makedirs('projects/' + directory)

