# Apache Beam 

📖 **Description**: This project demonstrates Apache Beam, a unified model for building data processing pipelines. It showcases various features like windowing, triggers, custom processing functions, and more using a simulated website log data scenario.

🌟 **Features**:
- Time-windowed data processing
- Use of custom ParDo functions
- Trigger-based data processing
- Identifying user actions within a time window
- Filtering out bot-like behavior

🎯 **Goals**: The primary goals of this project are to provide a practical example of using Apache Beam for data processing and to showcase its key features.

## Scenario

📜 **Scenario**:
Imagine we're analyzing logs from a website. These logs contain user IDs, timestamps, and the type of action they performed (e.g., "login", "view_item", "purchase"). We want to:

1. Count the number of each action type within a certain window.
2. Identify users who did a "login" followed by a "purchase" within 10 minutes.
3. Filter out any bots (let's assume any user with more than 100 actions within a 10-minute window is a bot).

## Usage

📋 **Usage**: The project processes simulated website log data to count action types within time windows and identify users who logged in and made a purchase within 10 minutes.

