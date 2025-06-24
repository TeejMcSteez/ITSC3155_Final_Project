### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
### Customer Needs
Online Restaurant Ordering System
Customer Needs:
As a forward-thinking restaurant owner, I recognize the growing trend towards online food ordering. I
want to provide my customers with a seamless online ordering experience to increase sales and enhance
customer satisfaction. I decide to hire a team of software engineers to develop an Online Restaurant
Ordering System that will enable customers to order food from my restaurant through an API.
- Increase Revenue: The primary objective of implementing the Online Restaurant Ordering System
is to boost revenue by tapping into the growing market of online food ordering. We aim to provide
customers with a convenient and user-friendly platform to order our restaurant's dishes.
- Enhance Customer Experience: We want to create a seamless and enjoyable experience for our
customers. This includes
+ Taking order as guest without making account (Customer names, phone and address on
each order)
+ Easy menu creation and exploration Including dishes, ingredients, price, calories, food
category (spicy, kids, vegetarian, low fat, etc.)
+ Efficient order placement (order tracking number, take out/delivery.)
+ Payment processing: different payment methods.
+ Real-time order tracking by order number (order status).
- Improve Operational Efficiency: OROS should help streamline our restaurant's operations. It
should facilitate order management, reduce errors, and make it easier for our staff to process
orders efficiently (different way of seeing data for staff, customer, chef, …).
- Gather Customer Feedback: We aim to gather feedback from customers through reviews and
ratings, allowing us to continuously improve our menu and service quality.
- Promotion and Marketing: The system should enable us to run promotions and generate promo
codes for customers.
- Data Analysis and Decision-Making: We want to collect and analyze data over time about
customer preferences, order trends, order status, and sales. This data will inform business
decisions and help us tailor our offerings to customer demands.
- Documentation and Training: We need comprehensive documentation for the system to
facilitate future enhancements and provide training materials for staff.