## [Unreleased]

### Added 

- Added change log : )
- Added support for multiple bots under the same source code.

### Changed

- The `tgbottoken` command which was previously used for updating the token of a bot is now removed. If you need to update the token, you can do so manually from your `credentials.py` file.
- The `tgbotwebhook` command can now change the webhook of any bot. It does not need to be a bot inside the project.

### Fixed

- Given this is an open source project, not having the bot token in the bot webhook URL could have been a security issue. If you knew the domain name the project was deployed on, you could send fake updates to it. This is fixed now by including the bot token in the URL.

