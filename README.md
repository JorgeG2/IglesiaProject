# Church Website for a Local Church in Atlantic City

## Project Overview

This repository contains the source code for a responsive church website designed and developed for a local church in Atlantic City. The website aims to provide a digital platform for the church community, offering easy access to church information, activities, and inspirational content.

## Features

- Responsive Design: Developed using HTML5, CSS3, and JavaScript to ensure compatibility across various devices and screen sizes.
- Interactive Elements: Integration of JavaScript for dynamic content updates and interactive user experience.
- AOS Library: Utilized Animate On Scroll (AOS) library for smooth and visually appealing scroll-based animations.
- Bible API Integration: Daily updates of inspirational Bible verses through API.Bible integration, enhancing user engagement.
- Flexbox and CSS Grid: Implemented advanced CSS layout techniques for a modern and user-friendly interface.

## Technologies Used

- Frontend: HTML5, CSS3, JavaScript
- Animation Library: AOS (Animate On Scroll)
- API: API.Bible for fetching daily Bible verses
- Backend: Flask (Python web framework) for handling server-side logic

## Running the Project

To run the website locally, follow these steps:

1. Clone the Repository: Use Git to clone the project's repository to your local machine. This can be done by executing git clone [repository URL] in your command line or terminal, where [repository URL] is the URL of the Git repository.
2. Set Up a Virtual Environment (Optional but Recommended): Before installing dependencies, it's a good practice to create a virtual environment. This keeps your project's dependencies separate from your global Python environment. In your project directory, run:

```bash
 python -m venv newenv
```

Then activate the virtual environment:

On Windows: newenv\Scripts\activate
On macOS and Linux: source newenv/bin/activate

3. Install Dependencies: Navigate to the directory containing the cloned project. Install Flask and other required dependencies by running:

```bash
pip install -r requirements.txt
```

This command installs all the packages listed in the requirements.txt file of your project.

4.Start the Flask Server: With the dependencies installed, you can start the Flask server. Set the environment variable for Flask by running:

```bash
export FLASK_APP=Verse.py
```

Then, start the Flask server with:

```bash
   flask run
```

This command launches a local web server that hosts the website, allowing you to access it through your web browser at `http://localhost:5000` or a similar URL provided in the terminal.

## How to Contribute

If you would like to contribute to this project, please follow these guidelines:

- Submit pull requests with your proposed changes.
- Adhere to the coding standards and conventions used in the project.
- For any queries or assistance, contact [Your Name] at [Your Email Address].

## Contact

For more information or inquiries about this project, feel free to contact [Your Name] at [Your Email Address].

## Acknowledgments

A heartfelt thank you to the community of the local church in Atlantic City for their support and inspiration in developing this website. Their feedback and insights have been invaluable in shaping this digital platform.
