# BUG06 – Last Name Validation Missing During Checkout

- **Defect ID:** BUG06
- **Module:** Checkout
- **Test Case:** TC14
- **Severity:** Major (provisional)
- **Priority:** Medium (provisional)
- **Status:** Failed – Observed

## Steps to Reproduce
1. Login to SauceDemo.
2. Add a product to the cart.
3. Open the shopping cart.
4. Click Checkout.
5. Enter a valid First Name.
6. Leave the Last Name field empty.
7. Enter a valid Postal Code.
8. Click Continue.

## Expected Result
The application should display a validation message indicating that Last Name is required.

## Actual Result
The application allows the user to continue to the checkout overview page without entering a Last Name.

## Conclusion
Last Name validation appears to be missing during checkout. Further investigation is required.
