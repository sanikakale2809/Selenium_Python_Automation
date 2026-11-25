from datetime import datetime



print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

print("--")

test_name="TC3"
current_time="21-11-2026_07_22_10"

screenshot_path = f".\\Screenshots\\{test_name}_{current_time}.png"

print(screenshot_path)
