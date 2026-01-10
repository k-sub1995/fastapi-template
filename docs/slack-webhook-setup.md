# Slack Incoming Webhook Setup Guide

This guide explains how to set up Slack Incoming Webhook for CI failure notifications.

## Prerequisites

- Slack workspace admin or permission to create apps
- GitHub repository admin access

---

## Step 1: Create a Slack App

1. Go to [Slack API: Applications](https://api.slack.com/apps)
2. Click **"Create New App"**
3. Select **"From scratch"**
4. Enter:
   - **App Name**: `GitHub CI Notifications` (or any name you prefer)
   - **Workspace**: Select your workspace
5. Click **"Create App"**

---

## Step 2: Enable Incoming Webhooks

1. In the app settings, navigate to **"Incoming Webhooks"** (left sidebar)
2. Toggle **"Activate Incoming Webhooks"** to **On**
3. Click **"Add New Webhook to Workspace"** at the bottom
4. Select the channel where you want notifications (e.g., `#ci-alerts`)
5. Click **"Allow"**
6. Copy the **Webhook URL**

> [!CAUTION]
> Keep this URL secret. Anyone with this URL can post messages to your channel.

---

## Step 3: Add Webhook URL to GitHub Secrets

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Enter:
   - **Name**: `SLACK_WEBHOOK_URL`
   - **Secret**: Paste the Webhook URL from Step 2
5. Click **"Add secret"**

---

## Verification

To test your webhook manually:

```bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Hello from CI!"}' \
  YOUR_WEBHOOK_URL
```

---

## Troubleshooting

| Issue | Solution |
| No notification received | Check if `SLACK_WEBHOOK_URL` secret is set correctly |
| `invalid_payload` error | Verify the webhook URL format |
| Notification sent to wrong channel | Create a new webhook for the correct channel |
| Mentions not working | Ensure member ID format is `<@UXXXXXXXX>` |

---

## References

- [Slack: Sending messages using Incoming Webhooks](https://api.slack.com/messaging/webhooks)
- [rtCamp/action-slack-notify](https://github.com/rtCamp/action-slack-notify)
