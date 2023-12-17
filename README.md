# habit-tracker
A Python application that records time spent doing certain activities, primarily built to keep track of how much time you spend coding each day.


[![Unit Tests](https://github.com/notzune/habit-tracker/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/notzune/habit-tracker/actions/workflows/unit_tests.yml)

---

## Building From Source

### Prerequisites
- Python 3.x installed on your machine.
- Git installed on your machine (for cloning the repository).
- Basic familiarity with using command line interfaces.

### Step-by-Step Instructions

#### Step 1: Clone the Repository
1. **Open your Command Line Interface (CLI)**: This can be Terminal on macOS/Linux or Command Prompt/Powershell on Windows.
2. **Navigate to the Directory** where you want to store the project.
3. **Clone the Repository**:
   ```git clone https://github.com/notzune/habit-tracker.git```
   This command downloads the code to your local machine.

#### Step 2: Set Up a Virtual Environment (Optional but Recommended)
1. **Navigate to the Project Directory**:
   ```cd habit-tracker```
2. **Create a Virtual Environment**:
   ```python -m venv venv```
3. **Activate the Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On MacOS/Linux: `source venv/bin/activate`

#### Step 3: Install Dependencies
1. **Install Required Packages**:
   ```pip install -r requirements.txt```
   This command installs all the necessary Python packages.

#### Step 4: Run the Application
1. **Run the Main Script**:
   ```python main.py```
   This starts the application.

### You're All Set!

Now you should have [habit-tracker](https://github.com/notzune/habit-tracker) running on your machine. If you have any issues or questions, feel free to reach out for support by [opening a ticket](https://github.com/notzune/habit-tracker/issues).

## User Guide for Setting Up Google Calendar API Access

### Introduction
This guide will help you set up access to the Google Calendar API for [habit-tracker](https://github.com/notzune/habit-tracker). You'll create your own Google Cloud project, enable the Google Calendar API, and obtain the credentials needed to run the application.

### Prerequisites
- A Google account.
- Basic familiarity with using web browsers.

### Step-by-Step Instructions

#### Step 1: Create a Google Cloud Project
1. **Open Your Web Browser**: Go to your preferred web browser.
2. **Visit Google Cloud Console**: Click [here](https://console.cloud.google.com/) or type `https://console.cloud.google.com/` in the address bar and press Enter.
3. **Sign In**: Use your Google account to sign in.
4. **Create a New Project**:
   - On the top navigation bar, you'll see a dropdown with the name of a current project (if any). Click on it.
   - In the new window, click the "New Project" button at the top right.
   - Give your project a fun and easy name, like "MyCalendarProject".
   - Click "Create".

#### Step 2: Enable the Google Calendar API
1. **Open the Dashboard**: After creating your project, you'll be taken to the dashboard.
2. **Enable APIs & Services**:
   - Find and click on "Enable APIs and Services" at the top.
   - In the API Library, search for "Google Calendar API".
   - Click on it and then click "Enable" to activate the API for your project.

#### Step 3: Create Credentials
1. **Access Credentials Page**:
   - On the left sidebar, click "Credentials".
   - On the Credentials page, click "Create Credentials" at the top and choose "OAuth client ID".
2. **Configure the OAuth Consent Screen**:
   - Select "External" and click "Create".
   - Fill in the "App name" (like "MyCalendarApp"), your email in "User support email" and "Developer contact information".
   - Click "Save and Continue".
   - Skip the "Scopes" section for now, just click "Save and Continue".
   - In the "Test users" section, click "Add Users" and enter your Google email address. Click "Save and Continue".
3. **Create OAuth Client ID**:
   - Now back in the "Credentials" tab, click "Create Credentials" again and select "OAuth client ID".
   - For "Application type", choose "Web application".
   - Name it (like "MyWebClient").
   - Under "Authorized redirect URIs", click "Add URI" and enter `http://localhost:8080/` (or the redirect URI you plan to use in your app).
   - Click "Create".
4. **Download the Credentials**:
   - After creating your client ID, you'll see a confirmation screen. Click the download icon (looks like a down arrow) next to your new client ID.
   - This downloads a file named `credentials.json`. Keep this file safe; you'll need it for the next step.

#### Step 4: Place `credentials.json` in the Application Folder
1. **Locate the Downloaded File**: Find `credentials.json` in your Downloads folder.
2. **Move the File**: Drag this file into the same folder where you have [habit-tracker](https://github.com/notzune/habit-tracker). This is important for the application to connect to Google Calendar.

#### Step 5: Run the Application
1. **Start [habit-tracker](https://github.com/notzune/habit-tracker)**: Now, when you start the application, it will use these credentials to access your Google Calendar.
2. **Follow Any On-Screen Instructions**: The application might ask you to log in to your Google account and grant access to your Google Calendar.

### You're All Set!
Congratulations! You've successfully set up [habit-tracker](https://github.com/notzune/habit-tracker) with Google Calendar API access. If you have any issues or questions, feel free to reach out for support by [opening a ticket](https://github.com/notzune/habit-tracker/issues).