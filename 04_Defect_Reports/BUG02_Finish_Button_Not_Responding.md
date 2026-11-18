# Defect BUG02 – Finish Button Not Responding

**Status:** Fail – Reproduced

| Field | Value |
|---|---|
| Defect ID | BUG02 |
| Module | Checkout |
| Test Case | TC08 |
| Severity | Major (provisional) |
| Priority | High (provisional) |
| Expected Result | Clicking Finish should complete the order |
| Actual Result | Only hover effect appears; no action occurs |
| Reproducibility | Reproduced after refreshing and repeating checkout |

## Steps to Reproduce
1. Login to SauceDemo.
2. Add a product to the cart.
3. Proceed to checkout.
4. Enter valid customer details.
5. Click Continue.
6. Click Finish.

## Observed Result
The Finish button displays a hover effect but does not respond to clicking. The order confirmation page does not appear.

## Evidence
Screenshot: Add screenshot here.

## Conclusion
The checkout Finish button appears to be unresponsive during testing. Further investigation is required to identify the cause.
