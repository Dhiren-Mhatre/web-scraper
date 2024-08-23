
# Nobero Product Scraper and Web Application

## Overview
This project is a full-stack application that scrapes product data from the Nobero website's men's section and displays it on a ReactJS-based web application. The project is divided into two main parts:

1. **Scraping Data Using Scrapy**: A Scrapy-based spider is used to scrape product details from the men's category of the Nobero website.
2. **Django REST API and ReactJS Application**: The scraped data is loaded into a database and exposed through a Django REST API, which is then consumed by a ReactJS frontend to display the product information.

## Features
- **Data Scraping**: Extracts detailed product information such as title, price, available SKUs, and descriptions from the Nobero website.
- **RESTful API**: Exposes product data through a Django REST Framework API.
- **Responsive UI**: A ReactJS-based frontend that displays the products and their details.
- **Filtering**: Basic filtering capabilities for products in the frontend (can be extended).
- **Scalability**: The Scrapy spider and Django API are designed to be easily extendable to other categories such as the women's section.

## Technologies Used
- **Scrapy**: For web scraping.
- **Django**: As the backend framework to manage the database and expose the RESTful API.
- **Django REST Framework**: For building the API.
- **SQLite**: As the default database for storing scraped data.
- **ReactJS**: As the frontend framework for building the user interface.
- **Axios**: For making HTTP requests from the React frontend to the Django backend.
- **CSS**: For styling the React components.

## Installation and Setup

### Prerequisites
- Python 3.x
- Node.js and npm
- Virtualenv (optional, but recommended)

### Part 1: Scrapy Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/nobero-scraper.git
   cd nobero-scraper
   ```

2. **Set Up Virtual Environment**

   ```bash
   python3 -m venv scraper_env
   source scraper_env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install scrapy
   ```

4. **Navigate to Scrapy Project Directory**

   ```bash
   cd nobero_scraper
   ```

5. **Run the Spider**

   ```bash
   scrapy crawl nobero -o products.json
   ```

   This will scrape the products from the Nobero men's section and save them to `products.json`.

### Part 2: Django REST API

1. **Navigate to Django Project Directory**

   ```bash
   cd ../nobero_api
   ```

2. **Set Up Virtual Environment**

   ```bash
   python3 -m venv api_env
   source api_env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Load Data into Database**

   You can create a custom management command or manually load data from `products.json` to the database using Django ORM.

6. **Run Django Development Server**

   ```bash
   python manage.py runserver
   ```

   The API will be available at [http://localhost:8000/api/products/](http://localhost:8000/api/products/).

### Part 3: ReactJS Application

1. **Navigate to React Project Directory**

   ```bash
   cd ../frontend
   ```

2. **Install Dependencies**

   ```bash
   npm install
   ```

3. **Start the React Application**

   ```bash
   npm start
   ```

   The application will be available at [http://localhost:3000](http://localhost:3000).

## Running the Full Application
1. **Ensure Django Backend is Running**:  
   The Django API should be running on [http://localhost:8000](http://localhost:8000).

2. **Ensure React Frontend is Running**:  
   The ReactJS app should be running on [http://localhost:3000](http://localhost:3000).

3. **Navigate to the React App in Your Browser**:  
   You should see the product listings scraped from the Nobero website, and you can click on products to see more details.
 

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**:  
Replace `yourusername` with your actual GitHub username when you publish the repository. Make sure to customize the repository name and link according to your GitHub repository.
```

You can customize this further according to your project needs.
