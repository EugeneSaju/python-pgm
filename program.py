import os

# Set the environment variable
env_var_name = "MY_ENV_VAR"
env_var_value = "HI FROM HWLLO WORLD"
os.environ[env_var_name] = env_var_value

# Get the environment variable value
env_var_value = os.environ.get(env_var_name)

# Check if the environment variable exists
if env_var_value is not None:
    # Write the environment variable to a text file
    with open("env_var.txt", "w") as f:
        f.write(env_var_value)
    print("Environment variable written to env_var.txt")
else:
    print("Environment variable not found.")
