import requests

url = "https://api.teamflect.com/api/goal/getGoals"
delete_url = "https://api.teamflect.com/api/goal/deleteGoal"

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NTIyN2FkMDFmYzQ0MTY5MGUxMzRkYzUiLCJpYXQiOjE3MDU1Nzg4MjksImV4cCI6MTcwNTY2NTIyOSwiaXNzIjoiaHR0cHM6Ly90ZWFtZmxlY3QuY29tIn0.5r8A0FlEtqX13zyKvc9_RQkSILNWUBP5wCqguMDTwW0"
}

params = {
    "includeCompleted": "true",
    "startDate": "2024-01-18",
    "endDate": "2024-01-18",
    "isActive": "false",
    "isAll": "true",
    "status": "1",
    "selectedLabels": "",
    "allGoal": "false"
}

# Send GET request
response = requests.get(url, headers=headers, params=params)
data = response.json()

# Check if the GET request was successful
if response.status_code == 200:
    # Loop through the goals and send a DELETE request for each
    goals = data.get("goals", [])
    print(len(goals))
    for goal in data.get("goals", []):
        goal_id = goal.get("_id")
        isPrivate = goal.get("isPrivate")
        if isPrivate == False:
            print(r"Goal with ID {goal_id} is not private")
        # if goal_id:
        #     delete_data = {"goalId": goal_id}
        #     delete_response = requests.post(delete_url, headers=headers, json=delete_data)
        #
        #     # Check if the DELETE request was successful
        #     if delete_response.status_code == 200:
        #         print(r"Goal with ID {goal_id} deleted successfully")
        #     else:
        #         print(r"Failed to delete goal with ID {goal_id}. Status code: {delete_response.status_code}")
else:
    print(r"Failed to retrieve goals. Status code: {response.status_code}")
