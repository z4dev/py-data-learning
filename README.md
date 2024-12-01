### 1. **Python Data Structures:**

- **Lists**: Mutable, allows changes like appending, removing elements, etc.
- **Tuples**: Immutable, can't be modified after creation.
- **Sets**: Unordered collections of unique elements.
- **Dictionaries**: Key-value pairs, useful for mapping related data.

### 2. **Control Flow:**

- **Loops**: `for`, `while`, and list comprehensions.
- **Error Handling**: Using `try`, `except`, and `finally` blocks for runtime errors.
- **Conditional Expressions**: Using `if`, `else`, and `elif` for decision-making.

### 3. **File Handling:**

- **Reading and Writing Files**: Using `open()`, `read()`, `write()`, etc.
- **Working with CSV and JSON**: Using Python's built-in modules to process data.
- **Handling File Paths**: Using `os.path` and methods like `os.remove()` to manage files.

### 4. **Machine Learning Concepts:**

- **Supervised Learning**: Model learns from labeled data.
- **Unsupervised Learning**: Model finds patterns in data without labels.
- **Reinforcement Learning**: Model learns through rewards and penalties.

### 5. **Functions & Modules:**

- **Creating Functions**: Defining and calling functions, passing parameters.
- **Importing Modules**: Using `import` and `from ... import` to use external functions and modules.

### 6. **Pythonic Concepts:**

- **List Comprehension**: More efficient way to create or modify lists.
- **Enumerate**: Useful for iterating over items and tracking index simultaneously.
- **Lambda Functions**: Anonymous functions for short operations.

### 7. **Working with Libraries:**

- **`os`**: For handling file paths, directories, and system operations.
- **`pickle`**: For serializing Python objects to files.
- **`json`**: For reading and writing JSON data.

### 8. **Miscellaneous:**

- **Set Operations**: Union, intersection, and difference for set manipulation.
- **CSV File Handling**: Reading/writing CSV files using Python’s `csv` module.


# Data Frames

---

```python
DataFrame = pd.DataFrame()
```

* Remember:

→

2D data refers to data that is organized in two dimensions, often represented in rows and columns. It can be visualized in a table or matrix format, where each row represents a **record** or observation, and each column represents a feature or attribute of that data.

Here are a few examples of 2D data:

### 1. **Tabular Data (Excel, CSV, Database)**:

This is the most common form of 2D data, where data is organized into rows and columns. Each row represents an individual observation, and each column represents an attribute or variable of the data.

**Example**:


| Name  | Age | Height (cm) | Weight (kg) |
| ----- | --- | ----------- | ----------- |
| Ahmed | 25  | 175         | 70          |
| Ali   | 30  | 180         | 80          |
| Amal  | 22  | 160         | 55          |

* In this table, the **rows** are individual records (people), and the **columns** are the attributes (name, age, height, weight).

### 3. **Matrices (Mathematical Data)**:

Matrices are another form of 2D data commonly used in mathematics, computer science, physics, and engineering.

**Example**: A 3x3 matrix:

```lua
lua
Copy code
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

```

This matrix can represent various data types, such as system of linear equations, transformations, or even image data.

### **mage Data (Grayscale or RGB)**:

Images are another example of 2D data, where each pixel can be represented as a value (or values, for RGB images) in a grid format.

* **Grayscale Image**: Each pixel value represents a single intensity, and the image is a matrix of these intensity values.
  **Example**: An image with a 3x3 grayscale matrix might look like this:

  ```lua
  lua
  Copy code
  [[255, 200, 180],
   [120, 100, 150],
   [75, 85, 90]]

  ```

  Where each number represents the intensity of the pixel (ranging from 0 to 255).
* **RGB Image**: For colored images, each pixel is represented by a tuple of three values (Red, Green, Blue).
  **Example**: A 2x2 RGB image might be represented as:

  ```lua
  lua
  Copy code
  [[[255, 0, 0], [0, 255, 0]],
   [[0, 0, 255], [255, 255, 0]]]

  ```

  Each pixel is represented by three values: one for Red, one for Green, and one for Blue.

```python
import pandas as pd

data = {
    'Name': ['Ahmed', 'Ali', 'Amal'],
    'Age': [25, 30, 22],
    'Height': [175, 180, 160],
    'Weight': [70, 80, 55]
}

df = pd.DataFrame(data)
print(df)

output : 

   Name  Age  Height  Weight
0  Ahmed   25     175      70
1    Ali   30     180      80
2   Amal   22     160      55

```

###
