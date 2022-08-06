# 0x00. AirBnB clone - The console

## Resources

- [Python packages](https://alx-intranet.hbtn.io/concepts/66)
- [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)
- [cmd module](https://docs.python.org/3.8/library/cmd.html)
- [packages concept page](https://docs.python.org/3.4/tutorial/modules.html#packages)
- [uuid module](https://docs.python.org/3.8/library/uuid.html)
- [datetime](https://docs.python.org/3.8/library/datetime.html)
- [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Objectives

Learn:

- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Features

### Console

#### Description

The Console manages the whole application's functionality from the command line. Some of these commands perform the following:

- Creating a new object.
- Storing and retrieving an object from a file or database.
- Executing operations on objects. e.g. count.
- Updating object's attributes.
- Destroying an object.

`console.py` file contains the entry point of the command interpreter.

#### Usage

To launch the console application in interactive mode simply run:

`./console.py`

To run in the non-interactive mode:

`echo "your-command-goes-here" | ./console.py `

#### Commands

| Commands          | Description                                                                                                                                             | Usage                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **help** or **?** | Displays documented commands.                                                                                                                           | **help**                                     |
| **quit**          | Exits the program.                                                                                                                                      | **quit**                                     |
| **EOF**           | Ends the program. Used when files are passed into the program.                                                                                          | N/A                                          |
| **create**        | Creates a new instance of the \<class_name\>. Stores in a JSON file, the object's serialized string representation and prints the id of created object. | **create** \<class_name\>                    |
| **show**          | Prints the string representation of an instance based on the class name and id.                                                                         | **show** \<class_name class_id\>             |
| **destroy**       | Deletes and instance base on the class name and id.                                                                                                     | **destroy** \<class_name class_id\>          |
| **all**           | Prints all string representation of all instances based or not on the class name                                                                        | **all** or **all** \<class_name class_id\>   |
| **update**        | Updates an instance based on the class name and id by adding or updating attribute from a dictionary or without a dictionary                            | **update** \<class_name class_id key value\> |

### Models

- `models/` directory contains classes used for this project:
- The class `BaseModel` defines all common attributes/methods for other classes and is the base class for the project.
- Other classes that inherit from the `BaseModel` class include:
  - `User`
  - `Place`
  - `City`
  - `Amenity`
  - `State`
  - `Review`
- The `FileStorage` class serializes instances of all the classes above to a JSON file and also deserializes JSON file to instances.

### Tests

All tests of the application are located in the `tests/` folder.
To execute all unit tests, run:
`python3 -m unittest discover tests `
from the root directory. Adding option `-v` reduces verbosity of the results

## File Descriptions

### console, model and storage

- [console.py](console.py) - the console contains the entry point of the command interpreter.
- [base_model.py](models/base_model.py) - The BaseModel class from which future classes will be derived
- [file_storage.py](models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
- [amenity.py](models/amenity.py) - class that inherits from BaseModel class.
- [city.py](models/city.py) - class that inherits from BaseModel class.
- [place.py](models/place.py) - class that inherits from BaseModel class.
- [review.py](models/review.py) - class that inherits from BaseModel class.
- [state.py](models/state.py) - class that inherits from BaseModel class.
- [user.py](models/user.py) - class that inherits from BaseModel class.

### Tests

- [test_console.py](tests/test_console.py) - Contains tests for the console module.
- [test_base_model.py](tests/test_models/test_base_model.py) - Contains the tests for the BaseModel class
- [test_file_storage.py](tests/test_models/test_file_storage.py) - Contains the tests of the FileStorage class
- [test_amenity.py](tests/test_models/test_amenity.py) - Contains the tests for the Amenity class
- [test_city.py](tests/test_models/test_city.py) - Contains the tests for the City class:
- [test_place.py](tests/test_models/test_place.py) - Contains the tests for the Place class
- [test_review.py](tests/test_models/test_review.py) - Contains the tests for the Review class
- [test_state.py](tests/test_models/test_state.py) - Contains the tests for the State class
- [test_user.py](tests/test_models/test_user.py) - Contains the tests for the User class

## Authors

- Brian Kiprotich
- Brenda Jelimo

## Bugs

- No known bugs.
