import requests
import random
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify, url_for, redirect
import mysql.connector
from config import API_KEY, DB_CONFIG
from mysql.connector.errors import Error
# from dotenv import load_dotenv
# load_dotenv()



# Define the API key and Bible ID
BIBLE_ID = '592420522e16049f-01'

# Define an array of Bible verses
VERSE_ID= [
    'JER.29.11',
    'PSA.23',
    '1COR.4.4-8',
    'PHP.4.13',
    'JHN.3.16',
    'ROM.8.28',
    'ISA.41.10',
    'PSA.46.1',
    'GAL.5.22-23',
    'HEB.11.1',
    '2TI.1.7',
    '1COR.10.13',
    'PRO.22.6',
    'ISA.40.31',
    'JOS.1.9',
    'HEB.12.2',
    'MAT.11.28',
    'ROM.10.9-10',
    'PHP.2.3-4',
    'MAT.5.43-44',
]

# Function to get a random Bible verse
def get_random_verse():
    # Generate a random index to select a verse from the VERSES list
    verse_index = random.randint(0, len(VERSE_ID) - 1)
    NEW_ID = VERSE_ID[verse_index]



    try:
        # Make a GET request to the Bible API to retrieve the verse
        response = requests.get(
            f'https://api.scripture.api.bible/v1/bibles/{BIBLE_ID}/search?query={NEW_ID}',
             headers = {'api-key': API_KEY}
        )

        # Check if the response is successful
        response.raise_for_status()

        # Parse the response data
        data_response = response.json()

        # Print the verse content and reference
        html_passage = data_response["data"]["passages"][0]["content"]


        # New code to parse HTML and extract text
        soup = BeautifulSoup(html_passage, 'lxml')
        text_passage = soup.get_text(separator=' ', strip=True)

        # print("---------------------")
        # print(text_passage)

        # Print the Book 
        book_refernce = data_response["data"]["passages"][0]["reference"]
        # print(book)
        return book_refernce, text_passage

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the API request
        print(f'Error: {e}')

# Call the function to get a random verse
get_random_verse()

# # Good job this actually is a decent project im proud of you -J
# from flask import Flask, render_template

app = Flask(__name__)

#for getting the bible verse and reference
@app.route('/')
def home():
    book_reference, text_passage = get_random_verse()
    if book_reference and text_passage:
        return render_template('index.html', verse=text_passage, reference=book_reference)
    else:
        return render_template('index.html', error="Unable to fetch verse")
    

# ----------------- DATABASE -----------------
submissions = {}


@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    phone = request.form['phone'] 
    email = request.form['email']

    try:
        # Establish a database connection
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # SQL query to insert the new general inquiry
        insert_query = """
        INSERT INTO GeneralInfo (name, email, phone)
        VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (name, email, phone))

        # Commit the transaction
        conn.commit()

        # Close the connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'Form submitted successfully'})
    except Error as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Failed to submit form'})





#PRAYERS 

form_submissions = {}



@app.route('/another-route', methods=['POST'])
def submit_another_form():
    name = request.form.get('name')
    email = request.form.get('email')
    prayer = request.form.get('prayer')

    if name and email and prayer:
        try:
            # Establish a database connection
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()

            # Prepare the INSERT statement
            insert_stmt = (
                "INSERT INTO Prayers (name, email, prayer_request) "
                "VALUES (%s, %s, %s)"
            )
            data = (name, email, prayer)

            # Execute the INSERT statement
            cursor.execute(insert_stmt, data)
            conn.commit()

            # Close the connection
            cursor.close()
            conn.close()

            return jsonify({'message': 'Prayer request submitted successfully'})
        except Error as e:
            print(f"Error: {e}")
            return jsonify({'message': 'Failed to submit prayer request'})
    else:
        return jsonify({'message': 'Empty submission received'})




# render statement page
@app.route('/Statement')
def show_statement():
    return render_template('statement.html')

#render the Prayers page 
@app.route('/Prayers')
def show_prayers():
    return render_template('Prayers.html')

#render the About for hidden page
@app.route('/habout')
def show_statements():
    return render_template('statement.html')

#render the Prayers for hidden page
@app.route('/hprayer')
def show_prayerss():
    return render_template('Prayers.html')
# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=5334)  # Replace 5001 with any available port number




