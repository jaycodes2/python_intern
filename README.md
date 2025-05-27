
---

# Python & Automation Intern Assignment

## Overview

This project demonstrates automation skills by processing real event data, cleaning it, generating personalized messages, and automating message delivery via Telegram bot.

The workflow covers:

* Data cleaning and normalization
* Personalized message generation based on attendee data
* Optional automation to send messages via Telegram bot

---

## Dataset

The dataset contains over 600 rows with columns such as:

* `name`, `first_name`, `last_name`, `email`, `created_at`
* `approval_status`, `has_joined_event`
* `amount`, `amount_tax`, `amount_discount`, `currency`, `ticket_name`
* `Job Title`, `LinkedIn profile`

---

## Project Structure & Files

| File/Folders          | Description                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| `clean_data.py`       | Script to clean and normalize the dataset according to assignment requirements                       |
| `cleaned_output.csv`  | Output CSV file containing cleaned and flagged data                                                  |
| `auto_msg.py`         | Generates personalized messages for each user based on event attendance and profile data             |
| `custom_messages.csv` | CSV with emails and personalized messages for outreach                                               |
| `user_messages_txt/`  | Folder containing individual `.txt` files with messages per user (optional bonus)                    |
| `user_messages_json/` | Folder containing individual `.json` files with messages per user (optional bonus)                   |
| `telebot.py`          | Script to send messages automatically via Telegram Bot API                                           |
| `.env`                | Environment file storing sensitive variables such as Telegram Bot token and chat ID (ignored by Git) |
| `user_messages.csv`   | Final CSV file used for message sending (can be same as `custom_messages.csv`)                       |
| `user_messages.json`  | JSON file version of messages per user                                                               |

---

## Detailed Explanation

### Step 1: Data Cleaning — `clean_data.py`

This script processes the raw CSV dataset to:

* **Remove duplicate rows** based on the email column, ensuring unique contacts.
* **Normalize** `has_joined_event` values, converting `Yes`/`No` strings to boolean `True`/`False`.
* **Flag incomplete data:**

  * Rows missing or having incomplete LinkedIn profiles
  * Rows with blank or missing job titles

The cleaned data is saved as `cleaned_output.csv` for further use.

---

### Step 2: Auto-Personalized Messaging — `auto_msg.py`

This script reads the cleaned data, then:

* Generates personalized messages depending on:

  * Whether the user joined the event
  * Their job title
  * Their first name
  * Whether they have a LinkedIn profile
* Outputs a CSV file (`custom_messages.csv`) with columns:

  * `email` — recipient's email
  * `message` — the customized message to be sent

**Bonus:** It also saves individual messages in:

* `user_messages_txt/` — text files, one per user
* `user_messages_json/` — JSON files with email and message fields

This modular approach allows easy integration with various messaging platforms.

---

### Step 3 (Bonus): Telegram Bot Automation — `telebot.py`

This script reads the messages and automatically sends them to users via Telegram using the Telegram Bot API.

* Uses sensitive credentials (bot token, chat ID) stored securely in `.env`.
* Can be triggered in batch mode to push messages into a Telegram queue.
* Provides success/failure feedback for each message sent.

---

## Usage Instructions

### 1. Setup environment

* Create a `.env` file at the project root with:

```
BOT_TOKEN=your_telegram_bot_token_here
CHAT_ID=your_chat_id_here
```

* Install Python dependencies (e.g., `requests`, `pandas`) if needed:

```bash
pip install -r requirements.txt
```

*(Add a `requirements.txt` if you want)*

---

### 2. Run data cleaning

```bash
python clean_data.py
```

* Generates `cleaned_output.csv` with cleaned and flagged data.

---

### 3. Generate personalized messages

```bash
python auto_msg.py
```

* Outputs `custom_messages.csv`
* Creates user message files in `user_messages_txt/` and `user_messages_json/`

---

### 4. Send messages via Telegram bot

```bash
python telebot.py
```

* Sends messages using Telegram API based on `custom_messages.csv`
* Make sure `.env` is configured with valid credentials

---

## Important Notes

* The `.env` file is **excluded** from Git to protect sensitive data.
* Use `.env.example` as a template for collaborators to set their own credentials.
* Message templates can be customized inside `auto_msg.py` to fit different contexts or platforms.
* The project can be extended to send emails via SMTP instead of Telegram.

---

## Contact & Support

For any issues or questions, please contact Jayanthan P  at jayanthan1944@gmail.com.

---

# Thank you for reviewing this project!

---

