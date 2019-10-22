#%% [markdown]
# # Problem 4: Active Directory
# 
# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
# 
# Write a function that provides an efficient look up of whether the user is in a group.

#%%
class Group(object):
    def __init__(self, _name):
        """
        A group object has a name, list of groups and a list of users.
        """
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        """
        Adds a group to the group list.
        """
        self.groups.append(group)

    def add_user(self, user):
        """
        Adds a user to the user list.
        """
        self.users.append(user)

    def get_groups(self):
        """
        Returns the group list.
        """
        return self.groups

    def get_users(self):
        """
        Returns the user list.
        """
        return self.users

    def get_name(self):
        """
        Returns the name of the group.
        """
        return self.name
    
    def __str__(self):
        """
        String representation of the group.
        """
        s = "Group, name: " + self.name + ", groups: ["
        for group in self.groups:
            s += str(group) + ", "
        s += "], users: "
        for user in self.users:
            s += str(user) + ", "
        s += "]"
        return s


#%%
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited_groups = set()
    groups = [group]
    while len(groups) > 0:
        group = groups.pop(0)
        if group in visited_groups:
            continue
        visited_groups.add(group)
        users = group.get_users()
        if user in users:
            return True
        groups.extend(group.get_groups())
    return False

#%% [markdown]
# # Tests

#%%
# Input: A single group with no groups or users
parent = Group("parent")

# Expected output: False
print(is_user_in_group("sub_child_user", parent))
print(is_user_in_group("kittykat", parent))


#%%
# Add more groups and users
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


#%%
# Expected Output: True
print(is_user_in_group("sub_child_user", parent))


#%%
# Expected Output: False
print(is_user_in_group("kittykat", parent))


#%%
# Input: Extend the network to contain a closed group
sub_child.add_group(parent)


#%%
# Expected Output: True
print(is_user_in_group("sub_child_user", parent))


#%%
# Expected Output: False
print(is_user_in_group("kittykat", parent))


#%%
# Create a new test with a group that has no groups or users
empty_group = Group("nothing here")

# Expected output: False, False
print(is_user_in_group("sub_child_user", empty_group))
print(is_user_in_group("kittykat", empty_group))


