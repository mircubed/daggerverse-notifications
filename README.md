# Daggerverse Notifications in Discord

I aimed to receive Discord alerts whenever a new module was added to Daggerverse. Lacking direct engineering support and with only an introductory course in Python as my coding experience, I turned to ChatGPT for assistance.

## Overview

This project demonstrates setting up a system to automatically fetch new module listings from the Daggerverse website and send notifications via Discord when new modules are identified. It was accomplished with minimal prior programming knowledge, highlighting the accessibility of technology and the power of collaboration.

## Process

Here's a summary of our collaborative efforts:

- **Environment Setup**: Installed Python and the necessary libraries (`requests` and `beautifulsoup4`) to facilitate web scraping and HTTP requests.

- **Project Initialization**: Created a new project repository using GitHub Desktop and Visual Studio Code, building on the foundational knowledge from my introductory Python course.

- **Script Development**:
  - Crafted a Python script capable of fetching the current list of modules from Daggerverse.
  - Compared the fetched list against a locally stored list to identify new modules.
  - Updated and saved the list of known modules locally for future reference.

- **Discord Integration**:
  - Implemented Discord notifications using a webhook, allowing for real-time alerts about new modules.
  - Securely stored the Discord webhook URL in GitHub Actions secrets to maintain privacy.

- **Automation with GitHub Actions**:
  - Established a GitHub Actions workflow that runs the script at scheduled intervals.
  - Utilized the Discord webhook secret within the workflow to automate notifications.

## Conclusion

This project not only achieved the initial objective of automating notifications for new Daggerverse modules but also served as a practical introduction to Python scripting, GitHub version control, and workflow automation. It stands as a testament to the accessible nature of technology and the empowering role of guided learning.
