from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data_json = request.get_json()
        input_data = data_json.get('data', [])

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        
        for item in input_data:
            if item.isdigit():
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        concat_string = ""
        for i, char in enumerate(reversed(alphabets)):
            if i % 2 == 0:
                concat_string += char.lower()
            else:
                concat_string += char.upper()
        
        # This is a placeholder; you'll need to use your actual information
        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        response_data = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)