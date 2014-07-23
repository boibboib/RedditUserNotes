RedditUserNotes
===============

Displays wiki/usernotes users and comments and verifies users still exists (not deleted or shadowbanned).


Requirements:

1. PRAW library.
2. Must be a moderator, or have wiki read privileges.


Usage:

1. Edit USERNAME, PASSWORD and SUBREDDIT vars in usernotes.py.
2. Run usernotes.py

The script will retrieve the data from the wiki/usernotes page and display the USERNAMEs and COMMENTs.  Then, attempt to access each username to assess if the account has been deleted or shadowbanned by admin. When complete, the script will print out the usernames that have been deleted or shadowbanned by admin.
