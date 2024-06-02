## E-Commerce API using CI/CD

This project implements Continuous Integration and Continuous Deployment (CI/CD) for the e-commerce API. The API runs on a MySQL database in development and on a PostgreSQL database on Render in production. This is the live production swagger link:

https://advanced-ecommerce-api.onrender.com/api/docs

This repository contains a *main.yaml* file with build, test and deploy steps for the GitHub workflow. Any development change that is pushed to this repository will automatically be deployed to render, provided that the build and test steps pass (i.e. dev changes will not be deployed to production if a unit test fails).

### Technologies Used:
* **psycopg2:** Leverages a database adapter for Python to interact with the PostgreSQL hosted on Render.
* **Swagger:** Used for comprehensive API documentation. This human-readable and machine-readable documentation provides a clear understanding of the API's functionalities, including endpoints, request parameters, response structures, and error codes.
* **Flask:** Leverages the power and flexibility of the Flask web development framework.
* **Flask-SQLAlchemy:** Used as an Object Relational Mapper (ORM) to streamline database interactions.
* **Marshmallow:** Used for robust data validation and serialization, ensuring data integrity within API requests and responses.
* **Flask-JWT-Extended:** Used to implement a secure JSON Web Token (JWT) based authentication system.
* **Flask-Limiter:** Optimizes performance through rate limiting.
* **Flask-Caching:** Used to cache frequently accessed data.
* **Flask-Cors:** Enables Cross-Origin Resource Sharing (CORS) for seamless communication between the frontend and backend applications.
* **unittest:** Employs a unit testing suite implemented to ensure the reliability and robustness of individual API functionalities through isolated test cases.
* **Gunicorn:** High-performance WSGI server used to deploy the Flask application in a production environment.

### API Features:

**Customer Management**
* **Comprehensive CRUD Operations:** Effortlessly create, retrieve (with pagination), update, and delete customer accounts.
* **Secure Authentication:** Implement a robust login system with role-based authorization for granular access control.

**Product Management**
* **Seamless Product Creation & Administration:** Add and manage product listings efficiently (requires admin role).
* **Optimized Retrieval with Pagination & Search:** Retrieve all products with pagination for better performance and search functionality for ease of use.
* **Detailed Product Updates & Removal:** Update product information and remove items from the store as needed (requires admin role).

**Order Processing**
* **Simplified Order Creation:** Create new orders with a user-friendly process (requires customer login).
* **Comprehensive Order Management:** Retrieve all orders (requires admin role) for comprehensive oversight.
* **In-depth Order Details:** Obtain detailed information for specific orders.
* **Order Tracking Integration:** Implement order tracking functionality for authenticated customers to monitor order status (order must belong to the customer).

**Shopping Cart Management**
* **Convenient Item Addition:** Add items to the shopping cart for a seamless purchasing experience (requires customer login).
* **Complete Cart Overview:** View all items currently in a customer's cart.
* **Granular Item Removal:** Remove specific items from the cart for order customization.
* **Cart Emptying Functionality:** Completely empty the cart for a fresh start.