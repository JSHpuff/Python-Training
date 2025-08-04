# 1.
first_name = 'John'
last_name = 'Doe'
s = F'Hello, {first_name} {last_name}!'
print(s)

# 2.
s = F'Hello, {" ".join((first_name, last_name))}!'
print(s)

# 3.
name = 'John'
website = 'PythonTutorial.net'
message = (
    f'Hello {name}.'
    f"You're learning Python at {website}"
)
print(message)

# 4.
message = f'Hello {name}. ' \
          f"You're learning Python at {website}."
print(message)

# 5.
message = f"""Hello {name}.
You're learning Python at {website}."""
print(message)