
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
import asyncio
import os
from dotenv import load_dotenv

class BasicAgent(Agent):
    class PrintHelloBehaviour(OneShotBehaviour):
        async def run(self):
            print(f"Agent {self.agent.jid} is now online and ready to serve in the disaster response system.")
            await self.agent.stop()

    async def setup(self):
        print(f"Agent {self.jid} starting...")
        b = self.PrintHelloBehaviour()
        self.add_behaviour(b)

async def main():
    load_dotenv()
    agent_jid = os.getenv("AGENT_JID")
    agent_password = os.getenv("AGENT_PASSWORD")

    agent = BasicAgent(agent_jid, agent_password)
    await agent.start()
    print("Agent is running. Press Ctrl+C to stop.")
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())