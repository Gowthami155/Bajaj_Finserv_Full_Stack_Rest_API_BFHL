# Bajaj_Finserv_Full_Stack_Rest_API_BFHL
This project contains a REST API built with Python and the Flask framework to solve a specific challenge. The API handles a POST request at the /bfhl endpoint, which takes an array of strings as input and processes it to return a structured JSON response.
This repository contains the source code for a RESTful API, the primary objective was to create and deploy an API that can intelligently process an array of mixed data types—numbers, alphabets, and special characters—and return a structured JSON response. The API is designed to be robust and handle various data inputs while adhering to the specified logical and formatting requirements.

Example A


 <img width="931" height="1000" alt="image" src="https://github.com/user-attachments/assets/bb4d3d52-0b2d-418f-b2ca-b29b67f0bbf1" />


 
 JSON Output
 {
    "alphabets": [
        "A",
        "R"
    ],
    "concat_string": "rA",
    "email": "john@xyz.com",
    "even_numbers": [
        "334",
        "4"
    ],
    "is_success": true,
    "odd_numbers": [
        "1"
    ],
    "roll_number": "ABCD123",
    "special_characters": [
        "$"
    ],
    "sum": "339",
    "user_id": "john_doe_17091999"
}



 Example B


 
 <img width="823" height="876" alt="image" src="https://github.com/user-attachments/assets/04b7a62d-8381-48ea-a8c8-57a7a0ca2bde" />



 
 <img width="653" height="447" alt="image" src="https://github.com/user-attachments/assets/80052a6a-a9ed-48f3-ab74-f3234095ecdd" />


 
 JSON Output
 {
    "alphabets": [
        "A",
        "Y",
        "B"
    ],
    "concat_string": "bYa",
    "email": "john@xyz.com",
    "even_numbers": [
        "2",
        "4",
        "92"
    ],
    "is_success": true,
    "odd_numbers": [
        "5"
    ],
    "roll_number": "ABCD123",
    "special_characters": [
        "&",
        "-",
        "*"
    ],
    "sum": "103",
    "user_id": "john_doe_17091999"
}




Example C



<img width="933" height="932" alt="image" src="https://github.com/user-attachments/assets/ca50a7e8-a947-4fcd-93da-de4cfa6cb3a9" />




<img width="918" height="286" alt="image" src="https://github.com/user-attachments/assets/9a52589e-f8a6-44d3-9b72-eaa9cfb290bc" />

JSON output
{
    "alphabets": [
        "A",
        "ABCD",
        "DOE"
    ],
    "concat_string": "doeABCDa",
    "email": "john@xyz.com",
    "even_numbers": [],
    "is_success": true,
    "odd_numbers": [],
    "roll_number": "ABCD123",
    "special_characters": [],
    "sum": "0",
    "user_id": "john_doe_17091999"
}


Preview

<img width="668" height="510" alt="image" src="https://github.com/user-attachments/assets/3b5916fc-8f11-430e-8dbc-a12c4a4b0037" />




