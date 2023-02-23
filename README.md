# Yacut

Yacut is a link shortening web service that allows users to shorten long URLs into shorter ones. The project is built using Python, Flask, SQLAlchemy, Alembic, HTML, and CSS. It also includes an API for programmatic access to the shortening service.

## Features

- Shorten URLs into shorter, more manageable links.
- Ability to customize the short URL's domain name and path.
- Password-protected links that can only be accessed by those who have the password.
- Optional expiration dates for links.
- API access to the link shortening service.

## Getting Started

To get started with Yacut, follow these instructions:

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. Clone the repository: `git clone https://github.com/PavelFil98/yacut.git`
2. Change into the project directory: `cd yacut`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `.\env\Scripts\activate`
   - On Unix or Linux: `source env/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Create a `.env` file and set the environment variables:
7. Create the database: `flask db upgrade`
8. Start the server: `flask run`
