# Content Creator Crew 🎬

AI-powered multi-agent system for automated YouTube content creation using [CrewAI](https://crewai.com).

## What it does

4 AI agents collaborate to create complete YouTube content packages:

| Agent | Role |
|-------|------|
| 🔍 Trend Researcher | Finds viral trending topics |
| ✍️ Script Writer | Writes engaging video scripts |
| 📈 SEO Optimizer | Creates optimized metadata & tags |
| 🎨 Thumbnail Strategist | Generates title & thumbnail concepts |

## Quick Start

```bash
# Install dependencies
pip install uv
crewai install

# Add API keys to .env
GEMINI_API_KEY=your_key
SERPER_API_KEY=your_key

# Configure input parameters in main.py
# Edit the inputs dictionary according to your needs:
# - content_type: Type of content (e.g., "YouTube video")
# - target_audience: Your audience (e.g., "Tech enthusiasts")
# - video_length: Duration in minutes (e.g., "10")
# - tone: Content tone (e.g., "conversational")
# - niche: Content niche (e.g., "AI & Technology")

# Run
crewai run
```

## Project Structure

```
src/content_crew/
├── config/
│   ├── agents.yaml    # Agent definitions
│   └── tasks.yaml     # Task definitions
├── crew.py            # Crew orchestration
├── main.py            # Entry point
└── tools/             # Custom tools
```

## Output

Generates content in `output/` folder:
- Trending topics analysis
- Complete video script
- SEO metadata & tags
- Title variations & thumbnail concepts
