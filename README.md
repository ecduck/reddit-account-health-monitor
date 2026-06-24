# Reddit Account Health Monitor

A read-only utility for checking basic status information for authorized Reddit accounts through Reddit's official OAuth-based API.

## Purpose

This project is intended to help authorized account owners review basic account status information such as OAuth access, public profile availability, karma, email verification status, and recent account activity.

The tool is designed for private account maintenance and transparency. It does not automate posting, commenting, voting, private messages, moderation actions, or engagement.

## What it checks

- OAuth access status
- Basic authenticated account metadata
- Public profile availability
- Link karma and comment karma
- Email verification status when available
- Recent posts made by the authenticated account
- Recent comments made by the authenticated account
- API response status and rate-limit headers

## What it does not do

- Does not post content
- Does not submit comments
- Does not vote
- Does not send private messages
- Does not scrape Reddit outside the official API
- Does not bypass rate limits
- Does not manipulate karma
- Does not access private user data
- Does not infer or expose non-public Reddit internal trust or enforcement systems

## Data handling

API credentials and account tokens must be stored locally in a `.env` file and should never be committed to this repository.

Reports are intended to be stored locally or in a private spreadsheet controlled by the authorized account owner.

## Status

This project is under development and intended for approved API access only.
