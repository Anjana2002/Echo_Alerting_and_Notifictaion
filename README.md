# Echo - Real-time Alert & Notification System

Echo is a Django-based alerting and notification system designed to help organizations efficiently deliver critical messages to users and teams. Users can view, snooze, or mark alerts as read, while admins can manage alerts and track delivery status.

---

## Features

- **User Alerts**
  - View active alerts on the dashboard
  - Snooze alerts for a custom duration
  - Mark alerts as read (read alerts are hidden from the dashboard)
  
- **All Notifications Page**
  - Table view of all notifications for a user
  - Displays alert title, message, severity, date/time, and status
  - Mark individual notifications as read
  
- **User Settings**
  - Customize default snooze duration

- **Admin Features**
  - Create, update, and delete alerts
  - Assign alerts to users, teams, or the entire organization
  - Track alert delivery with `NotificationDelivery` logs (status: delivered, read, snoozed)
  - Filter alerts by severity, active status, and time range

- **Real-time Alert Filtering**
  - Only active alerts are shown
  - Snoozed or read alerts are excluded automatically

---


## Models

1. **Alert** – Represents an alert with title, message, severity, start & expiry time, and target users/teams.  
2. **UserAlertPreference** – Tracks snoozed and read status for each user per alert.  
3. **NotificationDelivery** – Logs delivery status of alerts per user (delivered, read, snoozed).  
4. **Team** – Represents a group of users. Alerts can be assigned to entire teams.  
5. **User** – Extends Django’s default user model to manage individual user details.  
6. **UserSettings** – Stores user-specific preferences such as default snooze duration for alerts.
  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Anjana2002/Echo_Alerting_and_Notifictaion.git
cd echo
```

 2. Create a virtual environment and activate it:
 
 ```bash 
 python3 -m venv venv
 source venv/bin/activate  # Linux/macOS
 venv\Scripts\activate     # Windows
 ```

 3. Apply migrations:
 ```bash 
 python manage.py migrate
 ```

 4. Create a superuser for admin access:
```bash 
python manage.py createsuperuser
```

5. Run the development server::
```bash 

python manage.py runserver
```

## Technologies Used

- **Python 3.10**
- **Django 5.x**
- **SQLite** (default) or any Django-supported database
- **HTML, CSS, Django Templates**

## Future Scope

- Email & SMS alert delivery  
- Custom reminder frequency  
- Scheduled alerts at specific times  
- Escalation if alerts not acknowledged  
- Role-based access for Admin features  
- Push notifications

