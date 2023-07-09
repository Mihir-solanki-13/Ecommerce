# My E-commerce Site

My E-commerce Site is an online shopping platform that allows users to browse and purchase products conveniently. This README provides an overview of the site's features, setup instructions, and important information.

## Features

### Email Authentication
- Users can create an account and log in using their email address and password.
- Password reset functionality is available to help users recover their accounts.

### Coupon Feature
- Users can apply discount coupons during the checkout process to avail discounts on their purchases.
- The site supports various types of coupons, such as percentage-based discounts, fixed amount discounts, or free shipping.

### Seller feature 
The seller feature in My E-commerce Site allows users to become sellers and add their products for verification by the admin. Once verified, sellers can list and sell their products on the platform.

### Razorpay API Integration
- Payment transactions are handled through the Razorpay payment gateway.
- Users can securely complete their payments using various payment methods supported by Razorpay, such as credit/debit cards, net banking, UPI, etc.

### Invoice Feature
- After successfully completing the payment, users will receive a PDF invoice via email.
- The invoice will contain details of the purchased items, payment information, and order summary.
- The PDF invoice is generated dynamically and attached to the email.


## Technologies Used

- Python and Django framework for backend development.
- HTML, CSS, and JavaScript for frontend development.
- Razorpay API for payment gateway integration.
- Database management system (e.g., sqlite) for data storage.

## Setup Instructions

1. Clone the repository:


2. Install the required dependencies:
   install razorpay
   Get its authentication key
   You can find your API keys at <https://dashboard.razorpay.com/#/app/keys>.


3. Configure the environment variables:
- Create a `.env` file in the project's root directory.
- Set the necessary environment variables such as the database connection details, email server configuration, and Razorpay API credentials. Example:
  ```
  SECRET_KEY=your_secret_key
  DATABASE_URL=your_database_url
  EMAIL_HOST=your_email_host
  EMAIL_PORT=your_email_port
  RAZORPAY_KEY_ID=your_razorpay_key_id
  RAZORPAY_KEY_SECRET=your_razorpay_key_secret
  ```

4. Run the database migrations:

5. Start the development server:


6. Access the site in your web browser at `http://localhost:8000`.

## Contribution

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create a new issue or submit a pull request.




