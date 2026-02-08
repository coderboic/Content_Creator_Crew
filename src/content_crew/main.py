#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from content_crew.crew import ContentCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
def run():
    inputs = {
        'content_type': "YouTube video",
        'target_audience': "Tech enthusiasts",
        'video_length': "10",
        'tone': "conversational",
        'niche': "AI & Technology"
    }

    try:
        ContentCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


