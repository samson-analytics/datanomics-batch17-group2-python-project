# 6)	You receive log records:
# logs = [
#    {"user": "alice", "action": "login"},
#    {"user": "bob", "action": "login"},
#    {"user": "alice", "action": "purchase"},
#    {"user": "", "action": "login"},
#    {"user": "charlie", "action": None},
#    {"user": "bob", "action": "logout"}
# ]

# Build a program that:
# •	Remove invalid records where:
# o	user is empty OR
# o	action is missing (None)
# o	Count actions per user (dictionary)
# o	Count frequency of each action (dictionary)
# o	Cleaned record count
# o	User activity summary
# o	Most common action


# Expected Output
# Cleaned Records: 4

# User Activity:
# {
#     "alice": 2,
#     "bob": 2,
#     "charlie": 0
# }

# Action Counts:
# {
#     "login": 2,
#     "purchase": 1,
#     "logout": 1
# }

# Most Common Action: login

logs = [
    {"user": "alice", "action": "login"},
    {"user": "bob", "action": "login"},
    {"user": "alice", "action": "purchase"},
    {"user": "", "action": "login"},
    {"user": "charlie", "action": None},
    {"user": "bob", "action": "logout"}
]

cleaned_logs = []
user_activity = {}
action_counts = {}

for log in logs:
    if log["user"] != "":
        user_activity[log["user"]] = 0

for log in logs:
    if log["user"] != "" and log["action"] != None:
        cleaned_logs.append(log)

for log in cleaned_logs:
    user = log["user"]
    user_activity[user] += 1

for log in cleaned_logs:
    action = log["action"]

    if action not in action_counts:
        action_counts[action] = 1
    else:
        action_counts[action] += 1

most_common_action = ""
highest_count = 0

for action, count in action_counts.items():
    if count > highest_count:
        highest_count = count
        most_common_action = action

print("\nCleaned records:", len(cleaned_logs))
print("\nUser Activity:")
print(user_activity)

print("\nAction Counts:")
print(action_counts)

print("\nMost Common Action:", most_common_action)