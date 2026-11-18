
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
| TC02 | Login with incorrect credentials | Error displayed | Username and password do not match | PASS |
| TC03 | Login with empty fields | Validation displayed | Username is required | PASS |
| TC04 | Login with locked-out user | Access denied | Not executed separately | PENDING |
| TC05 | View available products | Products displayed | Names, prices and images visible | PASS |
| TC06 | Sort price low to high | Ascending order | Sorting broken – Backtrace error | FAIL |
| TC07 | Sort price high to low | Descending order | Sorting broken – Backtrace error | FAIL |
| TC08 | Click Finish | Order confirmation displayed | Initially appeared unresponsive; later order completed successfully | NEEDS VERIFICATION |
| TC09 | Add product to cart | Product added | Product added successfully | PASS |
| TC10 | Remove product from cart page | Product removed | Product removed successfully | PASS |
| TC11 | Add multiple products | All products visible | Two products added and visible | PASS |
| TC12 | Checkout with valid details | Overview displayed | Overview opened successfully | PASS |
| TC13 | Missing first name | Validation displayed | First Name is required | PASS |
| TC14 | Missing last name | Validation displayed | Continued without validation | FAIL |
| TC15 | Missing postal code | Validation displayed | Postal Code is required | PASS |
| TC16 | Complete an order | Confirmation displayed | Thank you for your order! | PASS |
| TC17 | Return to products | Products page displayed | Back Home worked correctly | PASS |
| TC18 | Verify cart after checkout | Cart empty | Cart was empty | PASS |
| TC19 | Remove from products page | Product removed | Hover effect appears; click does nothing | FAIL – Provisional |
| TC20 | Login using locked-out user | Access denied | Epic sadface: Sorry, this user has been locked out. | PASS |
| TC21 | Validate postal code length | Accept 6 digits; reject other formats under additional requirement | 5, 6, 7 digits and ABC123 all accepted | FAIL – Requirement-based |

## 2. Postal Code Boundary Test Details

Additional test expectation: Indian six-digit PIN code format.

| Input | Expected Result | Actual Result | Status |
|---|---|---|---|
| 56001 | Reject | Accepted | FAIL |
| 560001 | Accept | Accepted | PASS |
| 5600012 | Reject | Accepted | FAIL |
| ABC123 | Reject | Accepted | FAIL |

**Note:** This is a requirement-based finding. SauceDemo does not necessarily specify Indian PIN code validation as a built-in requirement.

## 3. Execution Summary

| Result | Count |
|---|---:|
| Passed | 14 |
| Failed | 5 |
| Needs Verification | 1 |
| Pending | 1 |
| Total | 21 |

## 4. Observations

1. Login works correctly with valid credentials.
2. Invalid credentials display an appropriate error message.
3. Empty username produces a validation message.
4. Locked-out user is correctly prevented from logging in (TC20).
5. Product names, prices and images are displayed correctly.
6. Both price sorting options display a Backtrace error.
7. Adding products to the cart works.
8. Removing products from the cart page works.
9. Removing products directly from the Products page appears unresponsive.
10. First Name validation works correctly.
11. Last Name validation appears to be missing.
12. Postal Code validation works when the field is empty.
13. Standard user checkout and order completion work.
14. Back Home navigation works correctly.
15. Cart is empty after successful checkout.
16. Postal code accepts 5-digit, 6-digit, 7-digit and alphanumeric values.

## 5. Conclusion

Manual functional testing was performed on the SauceDemo application using 21 test cases.

A total of 14 test cases passed, 5 failed, 1 requires further verification and 1 remains pending.

The main issues observed involved product sorting, last name validation and product removal from the Products page. An additional postal code format test identified a difference against the user-defined six-digit PIN requirement.

The Finish button issue could not be reproduced during subsequent testing, and therefore is not classified as a confirmed defect.

The testing process provided practical experience in test planning, test case design, test execution, boundary value analysis and defect reporting.
