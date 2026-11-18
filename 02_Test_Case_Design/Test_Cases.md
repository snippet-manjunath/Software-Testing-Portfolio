
# Test Case Design – SauceDemo

## Project Information

- **Project:** Software Testing Portfolio
- **Application:** SauceDemo – Online Shopping Application
- **Application URL:** https://www.saucedemo.com/
- **Testing Type:** Functional Testing
- **Browser:** Google Chrome
- **Testing Approach:** Manual Testing

---

## 1. Login Module

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC01 | Login with valid credentials | User should log in successfully | User logged in successfully | PASS |
| TC02 | Login with incorrect username/password | Error message should be displayed | Username and password do not match | PASS |
| TC03 | Login with empty username and password | Validation message should be displayed | Username is required | PASS |
| TC04 | Login with locked-out user | Access should be denied | Covered by TC20 | COVERED |

## 2. Product Module

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC05 | View available products | Products should be displayed correctly | Names, prices and images visible | PASS |
| TC06 | Sort products by price low to high | Products should appear in ascending price order | Sorting broken – Backtrace error displayed | FAIL |
| TC07 | Sort products by price high to low | Products should appear in descending price order | Sorting broken – Backtrace error displayed | FAIL |

## 3. Shopping Cart Module

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC09 | Add product to cart | Product should be added successfully | Product added successfully | PASS |
| TC10 | Remove product from cart page | Product should be removed successfully | Product removed successfully | PASS |
| TC11 | Add multiple products | All selected products should appear in cart | Two products added and visible | PASS |

## 4. Checkout Module

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC08 | Click Finish on checkout overview | Order confirmation page should appear | Initially appeared unresponsive; later order completed successfully | NEEDS VERIFICATION |
| TC12 | Checkout with valid details | Checkout overview page should appear | Overview opened successfully | PASS |
| TC13 | Checkout with missing first name | Validation message should appear | First Name is required | PASS |
| TC14 | Checkout with missing last name | Validation message should appear | Continued without validation | FAIL |
| TC15 | Checkout with missing postal code | Validation message should appear | Postal Code is required | PASS |

## 5. Order Module

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC16 | Complete an order | Order confirmation should appear | Thank you for your order! | PASS |
| TC17 | Return to products after order | Products page should appear | Back Home worked correctly | PASS |
| TC18 | Verify cart after checkout | Cart should be empty after successful checkout | Cart was empty | PASS |

## 6. Additional Test Cases

| ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC19 | Remove product directly from Products page | Product should be removed from cart | Hover effect appears; click does nothing | FAIL – Provisional |
| TC20 | Login using locked-out user credentials | Access should be denied | Epic sadface: Sorry, this user has been locked out. | PASS |
| TC21 | Validate postal code length | Evaluate acceptance of different postal code formats | 5, 6, 7 digits and ABC123 all accepted | NEEDS VERIFICATION |

## 7. Postal Code Boundary Testing

Additional test expectation: Indian six-digit PIN code format.

| Input | Expected Result | Actual Result | Status |
|---|---|---|---|
| 56001 | Reject under additional requirement | Accepted | FAIL – Requirement-based |
| 560001 | Accept | Accepted | PASS |
| 5600012 | Reject under additional requirement | Accepted | FAIL – Requirement-based |
| ABC123 | Reject under additional requirement | Accepted | FAIL – Requirement-based |

**Note:** Indian six-digit PIN validation is an additional testing requirement. SauceDemo does not necessarily specify this as a built-in application requirement.

## 8. Testing Techniques

### 8.1 Equivalence Partitioning

- Test valid and invalid login credentials.
- Test empty and non-empty checkout fields.
- Test different postal code input formats.

### 8.2 Boundary Value Analysis

Test postal code inputs with different lengths, including:

- 5 digits
- 6 digits
- 7 digits

Evaluate input validation and acceptance behaviour.

### 8.3 State Transition Testing

- Login and logout.
- Adding and removing products from cart.
- Checkout and order confirmation.
- Cart state after successful checkout.

### 8.4 Decision Table Testing

- Valid and missing checkout details.
- Different combinations of customer information.
- Login with valid, invalid and locked-out credentials.

## 9. Conclusion

The test cases cover login, product display, sorting, shopping cart, checkout and order functionalities of the SauceDemo application.

A total of 21 test cases were designed and evaluated. Manual testing was performed to verify expected behaviour, identify potential defects and evaluate application functionality.

The testing process identified issues related to product sorting, last name validation and product removal. Additional tests were conducted for locked-out user access and postal code input validation.

Some observations require further verification before they can be classified as confirmed defects.
