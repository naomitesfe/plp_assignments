# File Handling & Exception Handling in Python 📝🐍

This Python script demonstrates:

1. **File Handling**  
   - Reading from a file  
   - Writing modified content to a new file  
   - Example modification: converting text to uppercase (can be customized)  

2. **Exception Handling**  
   - Handling `FileNotFoundError` if the file does not exist  
   - Handling `IOError` for read/write issues  
   - Handling unexpected errors gracefully  

---

## 🚀 How to Use

1. Make sure you have a text file ready to read.  
2. Run the Python script:

```bash
python file_handling_exception.py
Enter the filename when prompted.
```
The script will create a new file named modified_<original_filename> with the modified content.

##⚡ Notes
- You can customize the modify_content() function to apply different transformations to the file content.
- The script ensures safe file operations with proper error handling.
