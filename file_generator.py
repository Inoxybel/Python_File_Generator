import os

class Generator:
    
        def dot_validation(self, f_name: str) -> bool:  # validate if contains valid extension in file name
            f_name = f_name[::-1]
            test_dot: int = f_name.find('.')
        
            if test_dot == -1 or test_dot != 0:
                return True
            
            return False


        def generate_parameters(self, f_name: str) -> list:  # make a list with number of files and extensions to copy
            parameters: list = []

            if ' ' in f_name:  # Space characters is never permitted in file name
                parameters.append('ERROR: Space characters is never permitted in module name!')
                return parameters

            while True:
                f_parameter: int = f_name.find('[')  # get start position of parameter
                s_parameter: int = f_name.find(']')  # get end position of parameter

                if f_parameter != -1:
                    parameter: str = f_name[f_parameter + 1:s_parameter]
                    if s_parameter != -1 and parameter.find('[') == -1:  # Checking if square brackets is closed
                        if self.dot_validation(self, parameter):
                            parameters.append(parameter)
                            f_name = f_name[s_parameter + 1:]
                        else:
                            parameters.append('ERROR: Invalid parameter! See readme file.')
                    else:
                        parameters.append('ERROR: You need to close square brackets opened!  Ex: [50.py].py')

                elif len(parameters) == 0 and len(f_name) > 3:
                    parameters.append('ERROR: Parameters must be within square brackets! Ex: [50.py][50.xml].py')
               
                return parameters


        def extract_extension(self, f_name: str) -> str:  # extract extension string of name of file
            if self.dot_validation(self, f_name):
                f_name = f_name[::-1]
                dot_position: int = f_name.find('.')

                if dot_position != -1:
                    extension: str = f_name[:dot_position + 1]
                    return extension[::-1]

                return ''


        def generate_files(self, file_dir: str, files: list) -> str:  # create copies of configured list of files
            for file in files:  # checking if original 01 files exists
                if not os.path.exists(file_dir + '\\01' + self.extract_extension(self, file)):
                    return f'01{self.extract_extension(self, file)} not finded'

            # opening and copying each file
                file_extension: str = self.extract_extension(self, file)
                only_file_name: str = file.replace(file_extension, "")
                original_file = open(file_dir + '\\01' + file_extension, 'rb')  # how can i define typing of this
                data = original_file.read()  # and this ? o.O
                original_file.close()

                if only_file_name.isnumeric():  # checking if name of file is numeric
                    for n in range(2, int(only_file_name) + 1):  # loop for make copies of files
                        new_file_name: str = '0' + str(n) + file_extension if n < 10 else str(n) + file_extension
                        new_file = open(file_dir + '\\' + new_file_name, 'wb')
                        new_file.write(data)
                        new_file.close()

                else:
                    return f'The name of parameter is not numeric!'

            return 'The operation was completed successfully!'


if __name__ == '__main__':
    g = Generator
    file_name: str = os.path.basename(__file__)  # get only name and extension of file
    file_directory: str = os.path.dirname(os.path.abspath(__file__))  # get directory of module without his name

    list_of_files: list = g.generate_parameters(file_name)  # getting list of files by module name

    print(g.generate_files(file_directory, list_of_files))

    input("Press Enter key to exit!")  # pause system to check returned message3