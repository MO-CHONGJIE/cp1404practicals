"""
project_management
Estimate: 65 minutes
Actual:  minutes
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")

    choice = input(">>> ").lower()

    if choice == "l":
        filename = input("Filename: ")
        projects = load_projects(filename)
        print(f"Loaded {len(projects)} projects from {filename}")

    elif choice == "s":
        filename = input("Filename: ")
        save_projects(projects, filename)
        print(f"Projects saved to {filename}")

    elif choice == "d":
        display_projects(projects)

    elif choice == "f":
        date_str = input("Show projects that start after (dd/mm/yyyy): ")
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        filter_projects(projects, date)

    elif choice == "a":
        new_project = add_project()
        projects.append(new_project)

    elif choice == "u":
        for i, project in enumerate(projects):
            print(f"{i} {project}")
        index = int(input("Project choice: "))
        update_project(projects[index])

    elif choice == "q":
        print("Thank you for using the project manager!")
    else:
        print("Invalid option")


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            projects.append(Project)
    return projects

def save_projects(projects, filename):
    with open(filename, "w") as file:
        file.write("Name, Start Date, Priority, Cost Estimate, Completion Percentage\n")
        for project in projects:
            file.write(f"{project.name}, {project.start_date.strftime('%d/%m/%Y')}"
                       f", {project.priority}, {project.cost_estimate}"
                       f", {project.completion_percentage}\n")

def display_projects(projects):
    """Display project is incomplete or completed, sorted by priority."""
    incomplete = sorted([project for project in projects if not project.is_complete()])
    complete = sorted([project for project in projects if project.is_complete()])

    print("Incomplete projects:")
    for project  in incomplete:
        print(f"  {project }")
    print("Completed projects:")
    for project  in complete:
        print(f"  {project }")