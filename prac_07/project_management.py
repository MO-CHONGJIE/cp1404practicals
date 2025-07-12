"""
project_management
Estimate: 65 minutes
Actual:  minutes
"""

from project import Project
from datetime import datetime

FILENAME = "projects.txt"


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            parts = line.strip().split(',')
            projects.append(Project)
    return projects

def display_projects(projects):
    """Display project is incomplete or completed, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project  in incomplete:
        print(f"  {project }")
    print("Completed projects:")
    for project  in complete:
        print(f"  {project }")