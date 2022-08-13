from dataclasses import dataclass


@dataclass
class Employee:
    """Class for keeping track of employee details."""

    name: str
    job_title: str
