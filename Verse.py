import requests
import random
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify, url_for, redirect
import json



# Define the API key and Bible ID
API_KEY = '80507ab8dcb312bef4bcbdd4805808a1'
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
    


submissions = {}


@app.route('/submit-form', methods=['POST'])
def submit_form():
    global submissions
    submission_id = len(submissions) + 1  # Creating a unique ID for each submission
    form_data_dict = request.form.to_dict()
    
    submissions[submission_id] = form_data_dict  # Storing the form data under the unique ID
    
    print("Current Submissions:", submissions)  # Debugging: print all submissions

    # Save to file
    with open('submissions.txt', 'w') as file:
        json.dump(submissions, file, indent=4)  # 'indent' for pretty printing

    # Return a JSON response for AJAX
    return jsonify({'message': 'Form submitted successfully', 'submission_id': submission_id})



form_submissions = {}

@app.route('/another-route', methods=['POST'])
def submit_another_form():
    global form_submissions
    submission_id = len(form_submissions) + 1  # Creating a unique ID for each submission

    name = request.form.get('name')
    email = request.form.get('email')
    prayer = request.form.get('prayer')

    if name and email and prayer:
        form_submissions[submission_id] = {
            'name': name,
            'email': email,
            'prayer': prayer
        }
    
        # Debugging: Print the updated form_submissions
        print(json.dumps(form_submissions, indent=4))

        # Write data to a file or process it as needed
        with open('form_submissions.txt', 'w') as file:
            json.dump(form_submissions, file, indent=4)

        return jsonify({'message': 'Form submitted successfully', 'submission_id': submission_id})
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


# if __name__ == '__main__':
#     app.run(debug=True)
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Replace 5001 with any available port number




