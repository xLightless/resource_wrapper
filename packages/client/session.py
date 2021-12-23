from packages.file.manager import FileManager
from packages.file.manager import Generator

user = "C:/Programming/Local/Projects/resource_wrapper/User/file_creation"

cock = "cock.yml"
fm = FileManager(user,files_in_path=[Generator.gen_file(user,None,"yml",amount=30),cock])

class Session(object):
    """ Interprets the session of the user """
    pass
