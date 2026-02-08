from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from content_crew.tools.custom_tool import ScrapingBeeTool
from crewai_tools import FileReadTool, SerperDevTool

@CrewBase
class ContentCrew():
    """Multi-agent crew for automated content creation pipeline"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            verbose=True,
            tools=[ScrapingBeeTool(), SerperDevTool()]
        )

    @agent
    def script_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['script_writer'],
            verbose=True,
            tools=[FileReadTool(root_dir='knowledge')]
        )

    @agent
    def seo_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_optimizer'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def thumbnail_title_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['thumbnail_title_strategist'],
            verbose=True,
            tools=[]
        )

    @task
    def research_trends(self) -> Task:
        return Task(
            config=self.tasks_config['research_trends'],
        )

    @task
    def write_script(self) -> Task:
        return Task(
            config=self.tasks_config['write_script'],
        )

    @task
    def optimize_seo(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_seo'],
        )

    @task
    def create_titles_thumbnails(self) -> Task:
        return Task(
            config=self.tasks_config['create_titles_thumbnails'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ContentCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )