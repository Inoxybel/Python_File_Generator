import os


def dot_validation(f_name: str) -> bool:  # validate if contains valid extension in file name
    f_name = f_name[::-1]
    test_dot = f_name.find('.')
    if test_dot == -1 or test_dot != 0:
        return True
    else:
        return False


def generate_parameters_by_file_name(f_name: str) -> list:  # make a list with number of files and extensions to copy
    parameters = []
    while True:
        if not (' ' in f_name):  # Space characters is never permitted in file name
            f_parameter = f_name.find('[')
            s_parameter = f_name.find(']')

            if f_parameter != -1:
                parameter = f_name[f_parameter + 1:s_parameter]
                if s_parameter != -1 and parameter.find('[') == -1:  # Checking if square brackets is closed
                    if dot_validation(parameter):
                        parameters.append(parameter)
                        f_name = f_name[s_parameter + 1:]
                    else:
                        parameters.append('ERROR: Invalid parameter! See readme file.')
                        return parameters
                else:
                    parameters.append('ERROR: You need to close square brackets opened!  Ex: [50.py].py')
                    return parameters

            elif len(parameters) == 0 and len(f_name) > 3:
                parameters.append('ERROR: Parameters must be within square brackets! Ex: [50.py][50.xml].py')
                return parameters

            else:
                return parameters
        else:
            parameters.append('ERROR: Space characters is never permitted in module name!')
            return parameters


def extract_extension_of_file(f_name: str) -> str:  # extract extension string of name of file
    if dot_validation(f_name):
        f_name = f_name[::-1]
        dot_position = f_name.find('.')

        if dot_position != -1:
            extension = f_name[:dot_position + 1]
            return extension[::-1]
        else:
            return ''


def generate_files(file_dir: str, files: list) -> str:  # create copies of configured list of files
    for file in files:  # checking if original 01 files exists
        if not os.path.exists(file_dir + '\\01' + extract_extension_of_file(file)):
            return f'01{extract_extension_of_file(file)} not finded'

        for file in files:  # opening and copying each file
            file_extension = extract_extension_of_file(file)
            only_file_name = file.replace(file_extension, "")
            original_file = open(file_dir + '\\01' + file_extension, 'rb')
            data = original_file.read()
            original_file.close()

            if only_file_name.isnumeric():  # checking if name of file is numeric
                for n in range(2, int(only_file_name) + 1):  # loop for make copies of files
                    new_file_name = '0' + str(n) + file_extension if n < 10 else str(n) + file_extension
                    new_file = open(file_dir + '\\' + new_file_name, 'wb')
                    new_file.write(data)
                    new_file.close()

            else:
                return f'The name of parameter is not numeric!'

        return 'The operation was completed successfully!'


file_name = os.path.basename(__file__)  # get only name and extension of file
file_directory = os.path.dirname(os.path.abspath(__file__))  # get directory of module without his name

list_of_files = generate_parameters_by_file_name(file_name)  # getting list of files by module name

print(generate_files(file_directory, list_of_files))

pause_system = input("Press Enter key to exit!")  # pause system to check returned message


