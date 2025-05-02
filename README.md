# SeleniumDragDropRandomizer

## Overview

**Name**: SeleniumDragDropRandomizer  
**Author**: Suman Gangopadhyay  
**Date**: 2-May-2025  
**Description**: This program uses Selenium to automate random drag-and-drop actions, moving capital cities to their corresponding countries on the demo page at [http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html](http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html). It shuffles the order of actions for each run and uses Explicit Waits for reliability.  
**Email**: linuxgurusuman@gmail.com

This Python script leverages Selenium WebDriver to interact with a web-based drag-and-drop interface, randomly dragging capital cities (e.g., Oslo, Stockholm) to their respective countries (e.g., Norway, Sweden). The program is structured with a `Data` class for configuration and a `SumanDragDrop` class for the drag-and-drop logic, ensuring modularity and reusability.

## Features
- Randomizes the order of drag-and-drop actions for each run.
- Uses Selenium's Explicit Waits to ensure elements are interactable, improving reliability.
- Handles errors gracefully with detailed logging (e.g., timeouts, missing elements).
- Automatically installs ChromeDriver using `webdriver_manager`.
- Modular design with separate data and logic classes.

## Prerequisites
- **Python**: Version 3.6 or higher.
- **Selenium**: Python package for browser automation.
- **webdriver_manager**: Simplifies ChromeDriver installation.
- **Google Chrome**: Required for the WebDriver to function.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/SeleniumDragDropRandomizer.git
   cd SeleniumDragDropRandomizer
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install selenium webdriver-manager
   ```

4. **Ensure Google Chrome is Installed**:
   - The script uses ChromeDriver, which requires Google Chrome. Download it from [https://www.google.com/chrome/](https://www.google.com/chrome/) if not already installed.

## Usage

1. **Run the Script**:
   ```bash
   python RandomDragDrop.py
   ```
   - The script will:
     - Open a Chrome browser.
     - Navigate to the demo page.
     - Randomly drag each capital to its corresponding country.
     - Print success or error messages for each action.
     - Close the browser after completion.

2. **Example Output**:
   ```
   Successfully dragged Berlin to its country
   Successfully dragged Oslo to its country
   Successfully dragged Madrid to its country
   Successfully dragged Helsinki to its country
   Successfully dragged London to its country
   Successfully dragged Stockholm to its country
   Successfully dragged Washington to its country
   All drag-and-drop actions completed successfully!
   ```
   - The order of capitals will vary each run due to randomization.

## File Structure
```
SeleniumDragDropRandomizer/
├── RandomDragDrop.py       # Main script with drag-and-drop logic
├── README.md          # This file
```

## Code Structure
- **Data Class**:
  - Stores the demo page URL and a dictionary mapping capitals to their HTML element IDs (`capital_id` and `country_id`).
  - Example: `{"Oslo": {"capital_id": "box1", "country_id": "box101"}}`.
- **SumanDragDrop Class**:
  - Inherits from `Data`.
  - Initializes the Selenium WebDriver and ActionChains.
  - Implements the `drag_and_drop` method to perform randomized drag-and-drop actions.
- **Main Block**:
  - Entry point that creates a `SumanDragDrop` instance and calls `drag_and_drop`.

## Troubleshooting
- **ChromeDriver Issues**:
  - Ensure ChromeDriver matches your Chrome version (check in `chrome://settings/help`).
  - The `webdriver_manager` should automatically download the correct version, but verify it works.
- **Timeout Errors**:
  - If the demo page loads slowly, increase the `WebDriverWait` timeout in `drag_drop.py`:
    ```python
    WebDriverWait(self.driver, 15).until(...)  # Change 10 to 15
    ```
- **Element Not Found**:
  - Inspect the demo page with Chrome Developer Tools (F12) to confirm element IDs (`box1`, `box101`, etc.).
  - Update the `capital_to_country` dictionary in `drag_drop.py` if IDs have changed.
- **Network Issues**:
  - Ensure the demo page ([http://www.dhtmlgoodies.com](http://www.dhtmlgoodies.com)) is accessible.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details (create a `LICENSE` file if needed).

## Contact
For questions or feedback, contact Suman Gangopadhyay at [linuxgurusuman@gmail.com](mailto:linuxgurusuman@gmail.com).
