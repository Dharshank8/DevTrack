
class Project:
    def __init__(self, project_id, project_name, description):
        self.project_id = project_id
        self.project_name = project_name
        self.description = description

    def display_project(self):
        print("Project ID:", self.project_id)
        print("Project Name:", self.project_name)
        print("Description:", self.description)


project1 = Project(
    101,
    "DevTrack",
    "Project and Issue Management System"
)

project1.display_project()
