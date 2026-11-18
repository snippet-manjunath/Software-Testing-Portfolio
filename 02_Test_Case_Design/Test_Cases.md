# Test Case Design – SauceDemo

## Project Information

- **Project:** Software Testing Portfolio
- **Application:** SauceDemo – Online Shopping Application
- **Testing Type:** Functional Testing
- **Browser:** Google Chrome
- **Testing Approach:** Manual Testing

## 1. Login Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC01 | Login with valid credentials | User should log in successfully | PASS |
| TC02 | Login with incorrect username/password | Error message should be displayed | PASS |
| TC03 | Login with empty username and password | Validation message should be displayed | PASS |
| TC04 | Login with locked-out user | Access should be denied | PENDING |

## 2. Product Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC05 | View available products | Products should be displayed correctly | PASS |
| TC06 | Sort products by price low to high | Products should appear in ascending price order | FAIL |
| TC07 | Sort products by price high to low | Products should appear in descending price order | FAIL |

## 3. Shopping Cart Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC09 | Add product to cart | Product should be added successfully | PASS |
| TC10 | Remove product from cart page | Product should be removed successfully | PASS |
| TC11 | Add multiple products | All selected products should appear in cart | PASS |

## 4. Checkout Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC08 | Click Finish on checkout overview | Order confirmation page should appear | NEEDS VERIFICATION |
| TC12 | Checkout with valid details | Checkout overview page should appear | PASS |
| TC13 | Checkout with missing first name | Validation message should appear | PASS |
| TC14 | Checkout with missing last name | Validation message should appear | FAIL |
| TC15 | Checkout with missing postal code | Validation message should appear | PASS |

## 5. Order Module

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC16 | Complete an order | Order confirmation should appear | PASS |
| TC17 | Return to products after order | Products page should appear | PASS |
| TC18 | Verify cart after checkout | Cart should be empty after successful checkout | PASS |

## 6. Additional Test Cases

| ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC19 | Remove product directly from Products page | Product should be removed from cart | FAIL – Provisional |
| TC20 | Login using locked-out user credentials | Access should be denied | PENDING |
| TC21 | Validate postal code length | Six-digit PIN should be accepted if specified by requirements | NEEDS VERIFICATION |

## 7. Testing Techniques

### 7.1 Equivalence Partitioning
- Test valid and invalid login credentials.
- Test empty and non-empty checkout fields.

### 7.2 Boundary Value Analysis
Test postal code inputs with different lengths, including:
- 5 digits
- 6 digits
- 7 digits

Evaluate input validation and acceptance behaviour.

### 7.3 State Transition Testing
- Login and logout.
- Adding and removing products from cart.
- Checkout and order confirmation.

### 7.4 Decision Table Testing
- Valid and missing checkout details.
- Different combinations of customer information.

## 8. Conclusion

The test cases cover login, product display, sorting, shopping cart, checkout and order functionalities of the SauceDemo application. Manual testing is performed to verify expected behaviour, identify potential defects and evaluate application functionality. Additional test cases are included to examine cart removal, locked-out user access and postal code validation.
