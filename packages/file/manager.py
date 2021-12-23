from packages.file.handler.config import generate_config
import yaml
import os

# Used to manage internal files dynamically
config = "config.yml"

rw_files = [
    config
]

class DataManager(object):
    def read_yaml(self,file:str,in_path:str):
        """ Requires a directory specified to read yaml files """
        scanner = os.scandir(in_path)
        for _file in scanner:
            with open(file,"r") as stream:
                try:
                    yml = yaml.safe_load(stream)
                    return yml
                except yaml.YAMLError as e:
                    raise e

class FileManager(object):
    """ Manages the files required for an application """
    
    def __init__(self,file_path:str,**files_in_path):
        """
        Initializes the parent directory for files and folders
        path_to_files: sets the location of the applications yamls, jsons and other information.
        files_in_path: list of files to check for or create.
        """
        path = [file_path if os.path.exists(file_path) else "No file/path set, please consider adding it upon initialization..."]
        os.chdir(str(path[0]))
        
        # Checks for system files
        file_names = files_in_path['files_in_path']
        if len(file_names) ==0:
            print(f"\n files_in_path = {file_names}. Fill params to create your files, this also generate internal library files into the parent path.")
        elif len(file_names)>0:
            for file_name in file_names:
                try:
                    if os.path.exists(file_name):
                        print(f"{file_path}/{file_name} exists, skipping...")
                        dm = DataManager()
                        yml = dm.read_yaml(file_name,file_path)
                        print(f"{file_name} settings:\n",yaml.dump(yml))

                    elif (~(os.path.exists(file_name))):
                            # Generates files for a path
                            open(file_name,"x")                        
                            
                            # Writes to generated 'config' file
                            with open(config,"w") as cfg:
                                yaml.dump(generate_config(), cfg)
                except Exception:
                    pass      

class Generator(object):
    def gen_file(file_path:str,file_name:str,extension:str,amount:int=0):
        """ 
        Statically generates interative files:
        
            file_path: path to generate files to,
            file_name: explicitly state a file_name. If no value specified it will gen a name with 'amount' interation,
            extension: the type of extension to use on the file.
            amount: of generated files. Cannot be used if file_name is not None. Any input will be considered as None.
        """
        if file_name is None:
            for i in range(0,amount):
                FileManager(file_path=file_path,files_in_path=[str(i)+"."+extension])
        elif file_name is not None:
            amount = None
            FileManager(file_path=file_path,files_in_path=[file_name+"."+extension])