import unittest
from file_generator import *

class TestGenerator(unittest.TestCase):
    
    def test_dot_validation(self):
        self.assertEqual(Generator.dot_validation(Generator, "5"), True)
        self.assertEqual(Generator.dot_validation(Generator, "5.py"), True)
        self.assertEqual(Generator.dot_validation(Generator, "5."), False)

    def test_generate_parameters(self):
        self.assertEqual(Generator.generate_parameters(Generator, "[5].py]"), ['5'])
        self.assertEqual(Generator.generate_parameters(Generator, "[5.py].py]"), ["5.py"])
        self.assertEqual(Generator.generate_parameters(Generator, "[5.]"), ['ERROR: Invalid parameter! See readme file.'])
        self.assertEqual(Generator.generate_parameters(Generator, "[5.py[10.ipynb].py]"), ['ERROR: You need to close square brackets opened!  Ex: [50.py].py'])
        self.assertEqual(Generator.generate_parameters(Generator, "5.py"), ['ERROR: Parameters must be within square brackets! Ex: [50.py][50.xml].py'])
        self.assertEqual(Generator.generate_parameters(Generator, "[5 0].py]"), ['ERROR: Space characters is never permitted in module name!'])

    def test_extract_extension(self):
        self.assertEqual(Generator.extract_extension(Generator, "20.py"), ".py")
        self.assertEqual(Generator.extract_extension(Generator, "20.ipynb"), ".ipynb")
        self.assertEqual(Generator.extract_extension(Generator, "20.xml"), ".xml")
        self.assertEqual(Generator.extract_extension(Generator, "20"), "")

    def test_generate_files(self):
        file_directory = os.path.dirname(os.path.abspath(__file__))
        self.assertEqual(Generator.generate_files(Generator, file_directory, ['3.py', '3.ipynb']), 'The operation was completed successfully!')
        self.assertEqual(Generator.generate_files(Generator, file_directory, ['10.pyX', '10.ipynb']), '01.pyX not finded')
        self.assertEqual(Generator.generate_files(Generator, file_directory, ['ABC.py', 'abc.ipynb']), 'The name of parameter is not numeric!')



if __name__ == "__main__":
    unittest.main()
