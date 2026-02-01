# 🤖 Dispatch: An Agent Starter Pack

> A lightweight, local-first agentic framework for HuggingFace models with built-in tool calling

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ✨ Features

- 🏠 **100% Local** - BYOK (Bring Your Own Keys)
- 🛠️ **Easy Tool Integration** - Add custom tools in minutes
- 🔄 **Multi-Tool Support** - Handle multiple tool calls per turn
- 💻 **Code Execution** - Built-in sandboxed code runner using apptainer.
- 🎯 **Simple API** - Get started with 3 lines of code
- 📢 **ntfy.sh Integration** - Real-time pub/sub messaging for multi-agent coordination
- 🔗 **Agent Communication** - Send commands, receive status updates, and sync across agents
- ⚡ **Priority-Based Commands** - Route external commands by priority level (high/normal/low)


## � Communication & Notifications

Dispatch agents can communicate with each other and external systems via **ntfy.sh**, a free real-time notification service.

### Key Channels

| Channel | Purpose |
|---------|---------|
| `agent_commands` | External commands to agents with priority levels |
| `agent_sync` | Multi-agent coordination and status updates |
| `agent_emergencies` | Critical alerts and error notifications |
| `agent_{name}_tasks` | Per-agent task delegation |

### Configuration

All channel names and ntfy settings are configurable via `.env` file:

```env
NTFY_COMMANDS_CHANNEL=agent_commands
NTFY_SYNC_CHANNEL=agent_sync
NTFY_EMERGENCIES_CHANNEL=agent_emergencies
NTFY_BASE_URL=https://ntfy.sh
NTFY_TIMEOUT=10
```

### Built-in Tools

- **`read_ntfy_messages(channel, limit=10)`** - Fetch recent messages from a channel
- **`post_ntfy_message(channel, message, title)`** - Publish messages to a channel
- **`notify_external_system(agent_id, status, message)`** - Send structured status updates

### Agent Identification

Each agent gets a unique ID at startup in format: `{AgentName}_{UUID_prefix}`

```python
AGENT_ID = f"{AGENT_NAME}_{AGENT_UUID[:8]}"
```

This allows external systems to route commands to specific agents and track responses.

MIT