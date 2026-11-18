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
| TC06 | Sort products by price (low to high) | Ascending price order | Sorting is broken! Error reported to Backtrace | FAIL |
| TC07 | Sort products by price (high to low) | Descending price order | Sorting is broken! Error reported to Backtrace | FAIL |
| TC08 | Click Finish on checkout overview | Order confirmation displayed | Button shows hover effect but does not respond | FAIL – Provisional |
| TC09 | Add product to cart | Product added successfully | Product added successfully | PASS |
| TC10 | Remove product from cart page | Product removed successfully | Product removed successfully | PASS |
| TC11 | Add multiple products | All products displayed in cart | Two products added and visible | PASS |
| TC12 | Checkout with valid details | Checkout overview displayed | Not executed | PENDING |
| TC13 | Checkout with missing first name | Validation displayed | Error: First Name is required | PASS |
| TC14 | Checkout with missing last name | Validation displayed | Application continues to checkout overview | FAIL |
| TC15 | Checkout with missing postal code | Validation displayed | Error: Postal Code is required | PASS |
| TC16 | Complete an order | Order confirmation displayed | Not executed | PENDING |
| TC17 | Return to products after order | Products page displayed | Not executed | PENDING |
| TC18 | Verify cart after checkout | Cart reflects completed order | Not executed | PENDING |
| TC19 | Remove product from products page | Product removed and cart count updated | Hover effect appears, but clicking Remove does nothing | FAIL – Provisional |

## 2. Execution Summary

| Result | Count |
|---|---:|
| Total Test Cases | 19 |
| Passed | 9 |
| Failed | 6 |
| Pending | 4 |

## 3. Observations

1. Login functionality works correctly with valid credentials.
2. Invalid login credentials produce an appropriate error message.
3. Empty username produces a validation message.
4. Product names, prices and images are displayed correctly.
5. Both price sorting options display a Backtrace error.
6. Adding products to the cart works correctly.
7. Removing products from the cart page works correctly.
8. Removing products directly from the Products page appears unresponsive.
9. Checkout validation works for missing First Name.
10. Checkout allows continuation when Last Name is empty.
11. Checkout validation works for missing Postal Code.
12. The Finish button appeared unresponsive during testing.

## 4. Conclusion

Manual functional testing was performed on the SauceDemo online shopping application. Several functionalities, including login, product display and cart operations, worked as expected. Potential defects were observed in product sorting, checkout validation and certain cart operations. Further testing is required to complete the remaining test cases and verify all observed issues.
