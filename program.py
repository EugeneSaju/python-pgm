import os

# Get the environment variable value directly
env_var_value = os.environ.get("MY_ENV_VAR")

# Check if the environment variable exists
if env_var_value is not None:
    # Write the environment variable to a text file
    with open("env_var.txt", "w") as f:
        f.write(env_var_value)
    print("Environment variable written to env_var.txt")
else:
    print("Environment variable not found.")
