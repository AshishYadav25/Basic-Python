name = "      Ash   ish     "
dots = "......."

print(name + dots)
print(name.lstrip() + dots) # lstrip() method to remove left side space

print(name.rstrip() + dots) # rstrip() method to remove right side space

print(name.strip() + dots)  # strip() method to remove both left & right side space

# Strip method does not remove in between space, to do that we need to use replace argument

print(name.replace(" ","")) # replace ()
