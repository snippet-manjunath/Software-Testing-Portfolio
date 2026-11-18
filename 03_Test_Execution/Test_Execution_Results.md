# Test Execution Results

## Project Information

- **Project:** Software Testing Portfolio
- **Application:** SauceDemo – Online Shopping Application
- **Testing Type:** Functional Testing
- **Browser:** Google Chrome
- **Execution Method:** Manual Testing

## 1. Test Execution Details

| Test ID | Test Scenario | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| TC01 | Login with valid credentials | User should log in successfully | User logged in successfully | PASS |
| TC02 | Login with incorrect username/password | Error message should be displayed | Error message: Username and password do not match | PASS |
| TC03 | Login with empty username and password | Validation message should be displayed | Error message: Username is required | PASS |
| TC04 | Login with locked-out user | Access should be denied | Not executed | PENDING |
| TC05 | View available products | Products should be displayed | Not executed | PENDING |
| TC06 | Sort products by price (low to high) | Products should appear in ascending price order | Not executed | PENDING |
| TC07 | Sort products by price (high to low) | Products should appear in descending price order | Not executed | PENDING |
| TC08 | Click Finish on checkout overview | Order confirmation should appear | Button shows hover effect but does not respond to click | FAIL – Provisional |
| TC09 | Add product to cart | Product should be added successfully | Not executed | PENDING |
| TC10 | Remove product from cart | Product should be removed | Not executed | PENDING |
| TC11 | Add multiple products | All selected products should appear in cart | Not executed | PENDING |
| TC12 | Checkout with valid details | Checkout overview should appear | Not executed | PENDING |
| TC13 | Checkout with missing first name | Validation message should appear | Not executed | PENDING |
| TC14 | Checkout with missing last name | Validation message should appear | Not executed | PENDING |
| TC15 | Checkout with missing postal code | Validation message should appear | Not executed | PENDING |
| TC16 | Complete an order | Order confirmation should appear | Not executed | PENDING |
| TC17 | Return to products after order | Products page should appear | Not executed | PENDING |
| TC18 | Verify cart after checkout | Cart should reflect completed order | Not executed | PENDING |

## 2. Execution Summary

| Result | Count |
|---|---:|
| Total Test Cases | 18 |
| Passed | 3 |
| Failed (Provisional) | 1 |
| Pending | 14 |

## 3. Observations

1. Login functionality works correctly with valid credentials.
2. The application displays an appropriate error message for incorrect login credentials.
3. The application displays a validation message when the username is empty.
4. The Finish button appeared unresponsive during checkout testing. The issue was reproduced after refreshing the page and requires further investigation.

## 4. Conclusion

Initial manual testing of the SauceDemo application was performed successfully for three login scenarios. One potential checkout issue was observed and documented. The remaining test cases will be executed to evaluate the application's functionality further.
