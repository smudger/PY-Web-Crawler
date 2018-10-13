import os

# each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists('projects/' + directory):
        print('Creating project directory ' + directory)
        os.makedirs('projects/' + directory)

# create queue and crawled lists (if not already created)
def create_data_files(project_name, base_url):
    queue = 'projects/' + project_name + '/queue.txt'
    crawled = 'projects/' + project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create a new file
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)

# append data to file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# clear the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

# read a file and convert each line to an item of a set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.rstrip('\n'))
    return results

# convert a set to a file, with a line for each item
def set_to_file(links, file_name):
    delete_file_contents(file_name)
    for link in sorted(links):
        append_to_file(file_name, link)
