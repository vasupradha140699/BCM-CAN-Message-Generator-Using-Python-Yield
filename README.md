# BCM CAN Message Generator Using Python Generators

## Project Overview
This project demonstrates how to use Python generators (`yield`) to generate sequential Body Control Module (BCM) CAN messages and validate the received CAN IDs against an expected CAN ID.

## Objectives
- Understand Python generators and the `yield` keyword.
- Generate CAN messages sequentially using a generator function.
- Validate received CAN IDs against the expected CAN ID.
- Identify expected and unexpected CAN messages.
- Display test execution results in the console.

## Technologies Used
- **Programming Language:** Python
- **Concepts:** Classes, methods, generators, `yield`, loops, conditional statements, and string comparison.
- **Automotive Domain:** Body Control Module (BCM) and CAN message validation.

## How It Works
1. The `BCM` class contains the `CAN_Message_Generator()` method.
2. The `yield` keyword generates one CAN ID and CAN data pair at a time.
3. The `for` loop retrieves each generated message.
4. Each CAN ID is compared with the expected CAN ID (`0x120`).
5. If the received CAN ID matches `0x120`, the result is **Expected CAN Message received**.
6. If the CAN ID does not match, the result is **Unexpected CAN message**.
7. The program displays the test execution start and completion messages.

## Sample CAN Messages

| CAN ID | CAN Data | Expected Result |
|---|---|---|
| `0x120` | `01 02 03` | Expected |
| `0x150` | `01 03 03` | Unexpected |
| `0x160` | `01 04 03` | Unexpected |
| `0x140` | `01 02 03` | Unexpected |
| `0x120` | `01 06 03` | Expected |

## Key Learning
- A generator produces values one at a time instead of returning all values at once.
- `yield` preserves the function's state between iterations.
- A generator can be useful for simulating a sequence of CAN messages in an automotive testing exercise.
- Conditional statements can validate whether a generated CAN ID matches the expected ID.

## Note
This is a Python-based CAN message simulation for learning and testing purposes. It does not communicate with a physical CAN bus or validate the actual CAN payload, timing, or message integrity.

- Add PASS/FAIL counters and a final test summary.
- Add test cases for missing, invalid, or unexpected messages.
- Extend the simulation to include CAN message timeouts and diagnostic scenarios.
