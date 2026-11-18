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
| TC04 | Login with locked-out user | Access denied | Not executed | PENDING |
| TC05 | View available products | Products displayed | Names, prices and images visible | PASS |
| TC06 | Sort price low to high | Ascending order | Sorting broken – Backtrace error | FAIL |
| TC07 | Sort price high to low | Descending order | Sorting broken – Backtrace error | FAIL |
| TC08 | Click Finish | Order confirmation displayed | Initially appeared unresponsive; later successful order completed | NEEDS VERIFICATION |
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
| TC20 | Locked-out user | Access denied | Not executed | PENDING |
| TC21 | Validate postal code length | Six-digit PIN accepted, if required | Accepts varying lengths; detailed boundary tests pending | NEEDS VERIFICATION |

## 2. Execution Summary

| Result | Count |
|---|---:|
| Passed | 12 |
| Failed | 4 |
| Needs Verification | 2 |
| Pending | 2 |
| Total | 20 + 1 additional test |

## 3. Observations

1. Login works correctly with valid credentials.
2. Invalid credentials display an error message.
3. Empty username displays a validation message.
4. Product names, prices and images are visible.
5. Both price sorting options display a Backtrace error.
6. Adding products to the cart works.
7. Removing products from the cart page works.
8. Removing products from the Products page appears unresponsive.
9. First Name validation works correctly.
10. Last Name validation appears to be missing.
11. Postal Code validation works when the field is empty.
12. Standard user checkout and order completion work.
13. Back Home navigation works correctly.
14. Cart is empty after successful checkout.
15. Postal code length validation requires further investigation.

## 4. Conclusion

Manual functional testing was performed on the SauceDemo online shopping application. Login, product display, cart operations and checkout were tested. Potential defects were observed in sorting, last name validation and product removal from the Products page. Additional verification is required for the Finish button and postal code length behaviour.
