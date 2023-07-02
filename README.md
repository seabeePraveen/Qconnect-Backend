# Qconnect API Backend Server
![](static/Qconnect_logo.jpeg)
<p align="center">
<img src="static/Qconnect_logo.jpeg" height=60 width=60> </p>

<h2> This is a chat application backend server built using Django and Django REST Framework. It provides several endpoints to manipulate the data in the database and manage chat functionality.</h2>

---

## Features

- User authentication and authorization
- CRUD operations for messages
- User profile management
- Real-time chat functionality

## Frontend Repository

The frontend application for Qconnect is developed using Flutter and can be found at [Qconnect Frontend](https://github.com/seabeePraveen/Qconnect-App). It provides the user interface for interacting with the Qconnect API backend.

To set up the complete Qconnect application, follow the instructions in the [Qconnect Frontend repository](https://github.com/seabeePraveen/Qconnect-App) for installing and configuring the Flutter frontend application.

## Backend Repository

This repository contains the backend server implementation for Qconnect. For information on setting up and running the backend server, please refer to the instructions in this repository.


## Installation

1. Clone the repository:
  ```shell
  git clone https://github.com/seabeePraveen/Qconnect-Backend.git
  cd Qconnect-Backend
  ```

2. Create and activate a virtual environment:
  ```shell
  python3 -m venv venv
  source venv/bin/activate
  ```

3. Install the dependencies:
  ```shell
  pip install -r requirements.txt
  ```

4. Set up the database:
  ```shell
  python manage.py makemigrations
  python manage.py migrate
  ```

5. Start the Server
  ```shell
  python manage.py runserver
  ```
## API Endpoints

The following API endpoints are available:

- **POST** `/api/login/`: Obtain an access token for authentication (Token-based authentication)
- **POST** `/api/register/`: User registration
- **POST** `/api/update/`: Update current user information based on token
- **POST** `/api/delete/`: Delete current user 
- **POST** `/api/get_user/`: Retrieve current user information based on token
- **POST** `/api/get_user_with_string/`: Retrieve users by starting string (Useful for search functionality)
- **POST** `/api/get_last_messages_of_user_and_details/`: Retrieve last messages of a user and their details
- **POST** `/api/get/`: Get messages of user2 (Retrieve messages between current user and user2)
- **POST** `/api/send/`: Send the entered message and save it in DataBase


## Contributing
Contributions are welcome! If you find any issues or have suggestions, please feel free to create an issue or submit a pull request.
