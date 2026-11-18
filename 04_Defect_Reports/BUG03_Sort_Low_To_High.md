# BUG03 – Price Sorting Low to High Not Working

- **Module:** Product Sorting
- **Test Case:** TC06
- **Severity:** Major (provisional)
- **Priority:** High (provisional)
- **Status:** Failed – Reproduced

## Steps to Reproduce
1. Login to SauceDemo.
2. Open the Products page.
3. Click the sorting dropdown.
4. Select Price (low to high).

## Expected Result
Products should be arranged in ascending order of price.

## Actual Result
The application displays: "Sorting is broken! This error has been reported to Backtrace."

## Conclusion
The low-to-high price sorting functionality did not work during testing.
