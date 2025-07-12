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