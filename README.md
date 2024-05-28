CT E-Commerce API

**Streamlined Functionality**

The API offers a robust set of features for managing customers, products, orders, and shopping carts, ensuring a smooth and efficient e-commerce experience.

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

**Technical Architecture**



* **Flask:** Leverages the power and flexibility of the Flask web development framework.
* **Flask-SQLAlchemy:** Employs Flask-SQLAlchemy as an Object Relational Mapper (ORM) to streamline database interactions.
* **Marshmallow:** Integrates Marshmallow for robust data validation and serialization, ensuring data integrity within API requests and responses.
* **Secure Authentication (Flask-JWT-Extended):** Implements a secure JSON Web Token (JWT) based authentication system using Flask-JWT-Extended (or a similar library).
* **Performance Optimization (Flask-Limiter & Flask-Caching):** Optimizes performance through rate limiting with Flask-Limiter to prevent abuse and caching with Flask-Caching for frequently accessed data.
* **Cross-Origin Communication (Flask-Cors):** Enables Cross-Origin Resource Sharing (CORS) via Flask-Cors for seamless communication between the frontend and backend applications.
* **Unit Testing (with unittest):** Employs a unit testing suite implemented with the unittest framework to ensure the reliability and robustness of individual API functionalities through isolated test cases.