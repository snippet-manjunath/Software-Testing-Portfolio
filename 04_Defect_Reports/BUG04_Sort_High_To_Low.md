# BUG04 – Price Sorting High to Low Not Working

- **Module:** Product Sorting
- **Test Case:** TC07
- **Severity:** Major (provisional)
- **Priority:** High (provisional)
- **Status:** Failed – Reproduced

## Steps to Reproduce
1. Login to SauceDemo.
2. Open the Products page.
3. Click the sorting dropdown.
4. Select Price (high to low).

## Expected Result
Products should be arranged in descending order of price.

## Actual Result
The application displays: "Sorting is broken! This error has been reported to Backtrace."

## Conclusion
The high-to-low price sorting functionality did not work during testing.
