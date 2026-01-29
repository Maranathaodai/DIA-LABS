
import os
import random
import asyncio
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour
from dotenv import load_dotenv


from datetime import datetime

class DisasterEnvironment:
    def __init__(self):
        self.zones = ["Zone A", "Zone B", "Zone C", "Zone D"]

    def get_condition(self, zone):
        temperature = random.randint(20, 40)
        humidity = random.randint(30, 100)
        visibility = random.choice(["Clear", "Moderate", "Poor"])

        disaster_types = [None, "Flood", "Earthquake", "Fire"]
        disaster = random.choice(disaster_types)
        severity = None
        if disaster:
            severity = random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])
        return {
            "zone": zone,
            "temperature": temperature,
            "humidity": humidity,
            "visibility": visibility,
            "disaster": disaster,
            "severity": severity,
        }



class SensorAgent(Agent):
    class PerceptionBehaviour(PeriodicBehaviour):
        def __init__(self, env, **kwargs):
            super().__init__(**kwargs)
            self.env = env
            self.cycle = 0
            self.disaster_events = []  # Track all detected disasters

        async def run(self):
            self.cycle += 1
            print("\n" + "#"*60)
            print(f"CYCLE {self.cycle} - SENSOR PERCEPTION CYCLE")
            print("#"*60)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            disaster_detected = False
            for zone in self.env.zones:
                cond = self.env.get_condition(zone)
                print(f"[{self.agent.jid}] {zone}: Temp={cond['temperature']}°C, Humidity={cond['humidity']}%, Visibility={cond['visibility']}")
                if cond["disaster"]:
                    disaster_detected = True
                    affected_population = random.randint(100, 5000)
                    resources_needed = random.randint(1, 20)
                    
                    # Map severity to level number
                    severity_level = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}
                    level = severity_level.get(cond['severity'], 0)
                    
                    # Store event details
                    event = {
                        "timestamp": timestamp,
                        "type": cond['disaster'],
                        "location": zone,
                        "severity": cond['severity'],
                        "level": level,
                        "affected_population": affected_population,
                        "resources_needed": resources_needed
                    }
                    self.disaster_events.append(event)
                    
                    print("!"*20 + " DISASTER DETECTED! " + "!"*20)
                    print(f"Type: {cond['disaster']}")
                    print(f"Location: {zone}")
                    print(f"Severity: {cond['severity']}")
                    print(f"Affected Population: {affected_population} people")
                    print(f"Resources Needed: {resources_needed}")
                    print(f"Timestamp: {timestamp}")
            if not disaster_detected:
                print(f"[{self.agent.jid}] No new disasters detected in this cycle.")
        
        def generate_log_file(self):
            """Generate a formatted disaster event log file"""
            with open("disaster_events.log", "w") as f:
                f.write("DISASTER EVENT LOG\n")
                f.write("="*60 + "\n")
                f.write("SensorAgent ID: SENSOR-001\n")
                f.write(f"Total Events Detected: {len(self.disaster_events)}\n")
                f.write("="*60 + "\n\n")
                
                for idx, event in enumerate(self.disaster_events, 1):
                    f.write(f"Event #{idx}\n")
                    f.write(f"  Timestamp: {event['timestamp']}\n")
                    f.write(f"  Type: {event['type']}\n")
                    f.write(f"  Location: {event['location']}\n")
                    f.write(f"  Severity: {event['severity']} (Level {event['level']})\n")
                    f.write(f"  Affected Population: {event['affected_population']}\n")
                    f.write(f"  Resources Needed: {event['resources_needed']}\n")
                    f.write("-"*60 + "\n\n")
            
            print(f"\n[LOG] Disaster event log saved to disaster_events.log ({len(self.disaster_events)} events)")

    async def setup(self):
        print("\n============================================================")
        print("Lab 2: SENSOR AGENT DEMONSTRATION\nPerception and Environment Modeling")
        print("============================================================\n")
        print("[Environment] Disaster environment initialized\n")
        print(f"[SensorAgent {self.jid}] Initialized")
        env = DisasterEnvironment()
        print(f"[SensorAgent {self.jid}] Monitoring locations: {env.zones}\n")
        print("[System] Starting perception cycles...\n")
        self.perception_behaviour = self.PerceptionBehaviour(env, period=5)
        self.add_behaviour(self.perception_behaviour)


async def main():
    load_dotenv()
    agent_jid = os.getenv("AGENT_JID")
    agent_password = os.getenv("AGENT_PASSWORD")

    agent = SensorAgent(agent_jid, agent_password)
    await agent.start()
    print("SensorAgent is running. Press Ctrl+C to stop.")
    try:
        while agent.is_alive():
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\n[System] Stopping agent...")
        # Generate log file before stopping
        if hasattr(agent, 'perception_behaviour'):
            agent.perception_behaviour.generate_log_file()
        await agent.stop()
        print("[System] Agent stopped successfully.")

if __name__ == "__main__":
    asyncio.run(main())