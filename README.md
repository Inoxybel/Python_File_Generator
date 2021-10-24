# Python-Project-File_Generator
Automatic Copy Files


This module make N copies of specific file(s) of any extension

- First you need to rename original files to 01.extension_of_file
  Ex: 
  
      module.py     -> 01.py
      example.ipynb -> 01.ipynb
      tables.xml    -> 01.xml

  For files without extensions like "hosts" file of Windows S.O.:
  Ex: 
  
      hosts                   -> 01
      file_without_extension  -> 01

How to configure this module to copy from single file:

- Rename module name with pattern: [number_of_copies.format_of_file].py
  Ex: 
  
      [10.py].py    -> Make  9 copies of 01.py file
      [15.ipynb].py -> Make 14 copies of 01.ipynb file
      [12]          -> Make 11 copies of 01 file (no extension file)


How to configure this module to copy multiples files:

- Rename module name with pattern: [number_of_copies.format_of_file][number_of_copies.format_of_file].py
  Ex: 
  
      [20.py][15.ipynb].py      -> Make 19 copies of 01.py file and 14 copies of 01.ipynb file
      [5.py][6.ipynb][3.xml].py -> Make 4 copies of 01.py file, 5 copies of 01.ipynb file and 2 copies of 01.xml file


Wrong configurations:
Ex: 

    [20.py][10.py].py     -> You will make higher number of copies, always

    [20.py[10.ipynb].py   -> You always need to close square brackets opened

    [20.py]10.ipynb.py    -> Only .py files will be copied
    20.py[10.ipynb].py    -> Only .ipynb files will be copied

    [20.py] [10.ipynb].py -> Space characters is never permitted in file name

    [20.].py              -> Invalid extension name

    [ABC.py].py           -> Use only numbers to describe how much copies you need


How to use:

   - Mouse Right Click -> Open With -> Python

   - Execute module file with a terminal 

        

    

