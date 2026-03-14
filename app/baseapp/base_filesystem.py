import os


class BaseFilesystem:

    def make_folder_if_not_exists(self, folder) -> bool:
        if os.path.exists(folder):
            return True
        else:
            try:
                print(f'Create {folder} folder')
                os.mkdir(folder)
                return True
            except PermissionError:
                print(f"Folder does not exists and can't be created! -> {folder} : Permission Denied!")
                return False
            except Exception as error:
                print(f"Folder does not exists and can't be created! -> {folder} : {error}")
                return False

    def get_files_in_folder_list(self, folder, mask=""):
        _files_list = os.listdir(folder)
        files_list = []
        for file in _files_list:
            if file[-len(mask):] == mask:
                files_list.append(os.path.join(folder, file))
        return files_list

    def get_all_objects_in_folder_list(self, folder, mask=""):
        _objects_list = os.walk(folder)
        all_files_list = []

        for fs_object in _objects_list:

            for file in fs_object[2]:
                if file[-len(mask):] == mask:
                    all_files_list.append(os.path.join(fs_object[0], file))

            # for dir in fs_object[1]:
            #     print(dir)

        return all_files_list

    def read_text_file(self, file):
        return self.__read_text_file(file)

    def append_text_file(self, file, data):
        self.__write_text_file(file, data, "append")

    def rewrite_text_file(self, file, data):
        self.__write_text_file(file, data, "overwrite")

    def __write_text_file(self, file, data, type="append"):
        write_type = "a" if type == "append" else "w"
        try:
            raw = open(file, write_type)
            raw.write(data)
            raw.close()
        except PermissionError:
            raise PermissionError(f"Error when writing file -> {file} : Permission Denied!")
        except Exception as error:
            raise Exception(f"Error when writing file -> {file} : {error}!")

    def __read_text_file(self, file):
        try:
            raw = open(file, 'r')
            data = raw.read()
            raw.close()
            return data
        except PermissionError:
            raise PermissionError(f"Error when writing file -> {file} : Permission Denied!")
        except Exception as error:
            raise Exception(f"Error when writing file -> {file} : {error}!")