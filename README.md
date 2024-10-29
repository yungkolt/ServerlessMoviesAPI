# Serverless Movies API
**A serverless API that provides movie information and allows users to filter movies by release year. This project is built using AWS serverless services including Lambda, DynamoDB, API Gateway, and S3 for storage.**

## Features
- GetMovies: Retrieves a list of all movies in the database, with details such as title, release year, genre, and cover image.

- GetMoviesByYear: Filters movies by release year, returning only those released in a specified year.

## Architecture
The project uses an AWS serverless stack:

- AWS Lambda: Handles business logic for each API endpoint.

- AWS DynamoDB: Stores movie information in a NoSQL database.

- AWS S3: Stores movie cover images.

- API Gateway: Manages HTTP requests and routes them to the appropriate Lambda functions.

<!-- (optional) Add a diagram if available -->

## API Endpoints
### GetMovies
- Endpoint: /GetMovies
- Method: GET
- Description: Returns a JSON list of all movies.
- Sample Response:
JSON

[
    {
        "title": "Inception",
        "releaseYear": "2010",
        "genre": "Science Fiction, Action",
        "coverUrl": "https://example-bucket.s3.amazonaws.com/inception.jpg"
    },
    {
        "title": "The Dark Knight",
        "releaseYear": "2008",
        "genre": "Action, Crime, Drama",
        "coverUrl": "https://example-bucket.s3.amazonaws.com/dark-knight.jpg"
    }
]
### GetMoviesByYear
- Endpoint: /getmoviesbyyear/{year}
- Method: GET
- Description: Filters movies by the specified release year.
- Path Parameter: year (e.g., 2010)
- Sample Request: GET /getmoviesbyyear/2010
- Sample Response:
JSON

[
    {
        "title": "Inception",
        "releaseYear": "2010",
        "genre": "Science Fiction, Action",
        "coverUrl": "https://example-bucket.s3.amazonaws.com/inception.jpg"
    }
]
## Setup and Installation
### Prerequisites
AWS CLI must be installed and configured with credentials (`aws configure`).
A valid S3 bucket in your AWS account.
Clone the Repository
git clone https://github.com/yourusername/ServerlessMoviesAPI.git
cd ServerlessMoviesAPI

Configure AWS CLI
Make sure to configure your AWS CLI with appropriate credentials:

aws configure

Environment Variables
Set up environment variables in AWS Lambda for your database, S3 bucket, and other configurations.

Deploy Lambda Functions
Deploy Lambda functions through the AWS console or use the AWS SDK for automated deployment.

Create API Gateway Routes
Set up routes in API Gateway to point to each Lambda function.

Add Sample Data to DynamoDB
Populate DynamoDB with sample movie data (title, release year, genre, cover URL).

Usage
Example Curl Requests
GetMovies
curl -X GET https://yourapi.com/GetMovies

GetMoviesByYear
curl -X GET https://yourapi.com/getmoviesbyyear/2010

Testing
You can test the API using tools like Postman or by making requests directly with curl. To validate the data returned from DynamoDB, use the AWS Console to inspect stored items.

Tech Stack
Languages: Python (for Lambda functions)
AWS Services:
DynamoDB - NoSQL database for storing movie data.
S3 - Stores movie cover images.
Lambda - Serverless compute service to run the API logic.
API Gateway - Manages the API endpoints.
Contributing
If you’d like to contribute, please fork the repository and make your changes in a branch. Once you’ve tested your changes, submit a pull request for review.

License
This project is licensed under the MIT License. See LICENSE for more details.
