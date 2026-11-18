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
| TC01 | Login with valid credentials | Login successful | User logged in successfully | PASS |
| TC02 | Login with incorrect credentials | Error message displayed | Username and password do not match | PASS |
| TC03 | Login with empty fields | Validation message displayed | Username is required | PASS |
| TC04 | Login with locked-out user | Access denied | Not executed | PENDING |
| TC05 | View available products | Products displayed correctly | Product names, prices and images visible | PASS |
| TC06 | Sort products by price (low to high) | Ascending price order | Error: Sorting is broken! Reported to Backtrace | FAIL |
| TC07 | Sort products by price (high to low) | Descending price order | Error: Sorting is broken! Reported to Backtrace | FAIL |
| TC08 | Click Finish on checkout overview | Order confirmation displayed | Button shows hover effect but does not respond | FAIL – Provisional |
| TC09 | Add product to cart | Product added successfully | Not executed | PENDING |
| TC10 | Remove product from cart | Product removed successfully | Not executed | PENDING |
| TC11 | Add multiple products | All products displayed in cart | Not executed | PENDING |
| TC12 | Checkout with valid details | Checkout overview displayed | Not executed | PENDING |
| TC13 | Checkout with missing first name | Validation displayed | Not executed | PENDING |
| TC14 | Checkout with missing last name | Validation displayed | Not executed | PENDING |
| TC15 | Checkout with missing postal code | Validation displayed | Not executed | PENDING |
| TC16 | Complete an order | Order confirmation displayed | Not executed | PENDING |
| TC17 | Return to products after order | Products page displayed | Not executed | PENDING |
| TC18 | Verify cart after checkout | Cart reflects completed order | Not executed | PENDING |

## 2. Execution Summary

| Result | Count |
|---|---:|
| Total Test Cases | 18 |
| Passed | 4 |
| Failed | 3 (including 1 provisional) |
| Pending | 11 |

## 3. Observations

1. Login works with valid credentials.
2. Invalid login credentials produce an appropriate error message.
3. Empty username produces a validation message.
4. Product names, prices and images are displayed correctly.
5. Sorting products from low to high produces a Backtrace error.
6. Sorting products from high to low also produces a Backtrace error.
7. The checkout Finish button appeared unresponsive during testing and requires further investigation.

## 4. Conclusion

Manual functional testing identified successful login and product display functionality. Two sorting failures were observed, and one potential checkout issue was reproduced. Remaining test cases are pending execution.
