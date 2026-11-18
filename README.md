# Software Testing Portfolio – SauceDemo

## 1. Project Overview

This project demonstrates practical experience in **Software Testing** through manual testing and test automation of the SauceDemo online shopping application.

The project focuses on validating application functionality, identifying defects, designing test cases, executing tests and documenting results.

- **Application:** SauceDemo
- **Application URL:** https://www.saucedemo.com/
- **Project Type:** Software Testing Portfolio
- **Testing Approach:** Manual Testing and Automation Testing
- **Automation Tool:** Selenium WebDriver
- **Programming Language:** Python
- **Browser:** Google Chrome
- **Version Control:** Git and GitHub

## 2. Project Objectives

- Understand the software testing life cycle.
- Prepare a structured test plan.
- Design and execute functional test cases.
- Identify and document application defects.
- Perform boundary value analysis and other testing techniques.
- Automate selected test cases using Selenium WebDriver.
- Prepare test execution reports and a final test summary.

## 3. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| SauceDemo | Application under test |
| Selenium WebDriver | Browser automation |
| Python 3.13.11 | Automation programming language |
| Google Chrome | Web browser |
| Python unittest | Automated test execution |
| Git | Version control |
| GitHub | Project repository |
| Markdown | Test documentation |

## 4. Repository Structure

```text
Software-Testing-Portfolio/
│
├── 01_Test_Plan/
│   └── Test_Plan.md
│
├── 02_Test_Case_Design/
│   └── Test_Cases.md
│
├── 03_Test_Execution/
│   └── Test_Execution_Results.md
│
├── 04_Defect_Reports/
│   ├── BUG02_Finish_Button_Not_Responding.md
│   ├── BUG03_Sort_Low_To_High.md
│   ├── BUG04_Sort_High_To_Low.md
│   ├── BUG05_Remove_From_Products_Page.md
│   └── BUG06_Last_Name_Validation_Missing.md
│
├── 05_Test_Automation/
│   ├── saucedemo_automation.py
│   ├── requirements.txt
│   └── Automation_Test_Results.md
│
├── 06_Test_Reports/
│   └── Final_Test_Summary_Report.md
│
├── 07_Screenshots/
│   └── Testing Evidence and Screenshots
│
└── README.md
```

## 5. Testing Scope

The following application functionalities were tested:

- User Login and Authentication
- Product Listing
- Product Sorting
- Add to Cart
- Remove from Cart
- Shopping Cart Verification
- Checkout Process
- Checkout Form Validation
- Order Completion

## 6. Testing Techniques

The following test design techniques were used:

1. **Equivalence Partitioning:** Testing valid and invalid input categories.
2. **Boundary Value Analysis:** Testing different postal code lengths and input formats.
3. **State Transition Testing:** Verifying application behaviour during login, cart operations and checkout.
4. **Decision Table Testing:** Testing combinations of checkout form inputs.

## 7. Manual Testing Summary

A total of **21 manual test cases** were designed and evaluated.

| Test Result | Count |
|---|---:|
| Passed | 14 |
| Failed | 4 |
| Needs Verification | 2 |
| Pending | 1 |
| **Total** | **21** |

### Major Findings

- Price sorting from low to high displayed a Backtrace error.
- Price sorting from high to low displayed a Backtrace error.
- Checkout continued without entering a Last Name.
- The Remove button on the Products page appeared unresponsive and requires further verification.

### Additional Observations

- The Finish button initially appeared unresponsive but worked during a subsequent test.
- Postal code format testing was performed against an additional Indian six-digit PIN code requirement. This is not treated as a confirmed built-in SauceDemo defect.

## 8. Test Automation

### Tools Used

- Selenium WebDriver
- Python 3.13.11
- Google Chrome

### Automated Test Cases

| Test ID | Description | Status |
|---|---|---|
| AT01 | Valid Login | PASS |
| AT02 | Invalid Login | PASS |
| AT03 | Add Product to Cart | PASS |
| AT04 | Verify Cart | PASS |
| AT05 | Remove Product from Cart | PASS |

### Automation Summary

- **Total Tests:** 5
- **Passed:** 5
- **Failed:** 0
- **Execution Time:** 9.769 seconds

### Execution Command

```bash
python -m unittest -v saucedemo_automation.py
```

All five automated test cases executed successfully.

### How to Run Automation Tests

1. Clone the repository:

```bash
git clone https://github.com/snippet-manjunath/Software-Testing-Portfolio.git
```

2. Navigate to the automation folder:

```bash
cd Software-Testing-Portfolio/05_Test_Automation
```

3. Create a Python virtual environment:

```bash
python3 -m venv venv
```

4. Activate the environment on macOS or Linux:

```bash
source venv/bin/activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

6. Execute the automated tests:

```bash
python -m unittest -v saucedemo_automation.py
```

**Prerequisite:** Python and Google Chrome must be installed.

## 9. Defect Summary

The following defects and observations were documented during manual testing:

| Defect ID | Description | Classification |
|---|---|---|
| BUG02 | Finish button initially appeared unresponsive | Needs Verification |
| BUG03 | Price sorting low to high | Observed – Failed |
| BUG04 | Price sorting high to low | Observed – Failed |
| BUG05 | Remove button issue on Products page | Provisional – Needs Further Verification |
| BUG06 | Last Name validation missing | Observed – Failed |

Postal code format observations are documented separately as requirement-based findings and are not included as confirmed application defects.

## 10. Screenshots and Evidence

The `07_Screenshots` folder contains supporting evidence collected during testing, including automation execution evidence.

These screenshots help demonstrate the testing process and observed application behaviour.

## 11. Project Deliverables

- Test Plan
- Test Case Design
- Manual Test Execution Results
- Defect Reports
- Selenium Automation Script
- Automation Test Results
- Testing Screenshots and Evidence
- Final Software Testing Summary Report

## 12. Conclusion

This project provided practical experience in manual testing and browser automation using Selenium WebDriver with Python.

A total of 21 manual test cases were evaluated, and five automated test cases were executed successfully.

The project demonstrates the complete testing workflow, including test planning, test case design, test execution, defect documentation, automation and test reporting.

---

**Repository:** [Software Testing Portfolio – GitHub](https://github.com/snippet-manjunath/Software-Testing-Portfolio)
