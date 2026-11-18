
# Defect BUG02 – Finish Button Not Responding

**Status:** Needs Verification – Not a Confirmed Defect

| Field | Value |
|---|---|
| Defect ID | BUG02 |
| Module | Checkout |
| Test Case | TC08 |
| Severity | Major (Provisional) |
| Priority | High (Provisional) |
| Expected Result | Clicking Finish should complete the order |
| Initial Actual Result | Only hover effect appeared; no action occurred |
| Reproducibility | Initially observed after refreshing and repeating checkout |
| Retest Result | Checkout completed successfully during a subsequent test |

## Steps to Reproduce
1. Login to SauceDemo.
2. Add a product to the cart.
3. Proceed to checkout.
4. Enter valid customer details.
5. Click Continue.
6. Click Finish.

## Initial Observed Result
During the initial test, the Finish button displayed a hover effect but did not respond to clicking. The order confirmation page did not appear.

## Retest Observation
During a subsequent test, the Finish button worked successfully and the application displayed:

"Thank you for your order!"

## Evidence
- Initial observation: Screenshot to be added if available.
- Retest: Screenshot of successful order confirmation, if available.

## Conclusion
The Finish button appeared unresponsive during the initial testing attempt. However, the issue could not be reproduced during subsequent testing because the checkout completed successfully.

Further testing is required to determine whether this was a temporary issue or an application defect.

**Final Classification:** Needs Verification. Not counted as a confirmed defect.
