# write a working pythob class that has methods and attributes
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year =year

    def display_info(self):
        print(f"car: {self.make} {self.model} {self.year}")

#use the same class to iplement an object.
my_car = Car("toyota", "corolla", 2023)
print(my_car.model)
print(my_car.make)
print(my_car.year)
my_car.display_info()


#how to use github as a team.


# Create or Import Repositories: Create new repositories for your projects or import existing ones into your 
# organization. You can do this directly from the GitHub website or using Git commands on your local machine.

# Add Team Members: Invite team members to join your organization and grant them appropriate permissions to 
# access repositories. You can manage permissions at the organization level and for each repository.

# Collaborate on Code: Team members can collaborate on code by cloning repositories to their local machines, 
# making changes, and pushing those changes back to GitHub. They can create branches, pull requests, review code, 
# and merge changes into the main branch.

# Use Branches: Encourage the use of feature branches for development work. Each feature or bug fix should 
# have its own branch. This helps isolate changes, facilitates code reviews, and prevents conflicts.

# Code Reviews: Use GitHub's pull request feature for code reviews. Team members can review each other's 
# code, provide feedback, and discuss changes before merging them into the main branch.

# Project Management: Use GitHub's built-in project management features like Issues, Projects, and Milestones 
# to track tasks, organize work, and plan releases. You can link issues to pull requests and track their status.

# Continuous Integration and Deployment (CI/CD): Set up CI/CD pipelines using GitHub Actions or third-party 
# integrations like Travis CI or CircleCI. Automate testing, code quality checks, and deployment processes to 
# ensure a smooth development workflow.

# Documentation: Maintain project documentation using GitHub's Wiki feature or by adding Markdown files to your
#  repositories. Document project guidelines, coding standards, and any other relevant information to help team members understand and contribute to the project.

# Communicate: Encourage communication within the team using GitHub's built-in features like comments, discussions, and notifications. You can also integrate GitHub with communication tools like Slack for real-time collaboration.