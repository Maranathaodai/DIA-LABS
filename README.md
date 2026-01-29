# Primary Project: Disaster Response & Relief Coordination System 
## Programming Language: Python 
### Agent Framework: SPADE (Smart Python Agent Development Environment) 
#### Online Laboratory Platform: GitHub Codespaces 
## 1. INTRODUCTION 
This laboratory manual accompanies the course Intelligent Agent Systems and provides structured, 
hands-on experience in the design, modeling, simulation, and implementation of intelligent multi
agent systems using Python. 
All laboratory sessions are delivered through an online development and simulation environment 
based on GitHub Codespaces, ensuring a uniform, browser-accessible, and reproducible setup for all 
students. This approach eliminates local installation inconsistencies while supporting realistic multi
agent execution. 
The laboratories are organized around a single capstone-driven practical project, the Disaster 
Response and Relief Coordination System, which evolves incrementally throughout the semester. 
Each laboratory session introduces specific technical competencies that directly contribute to the 
completion of the final multi-agent system. 
Students will apply: 
• Agent-oriented design principles 
• Belief–Desire–Intention (BDI) style reasoning 
• The Prometheus agent-oriented software engineering methodology 
Progression is from simple autonomous agents to a coordinated, distributed, and evaluated multi
agent system operating under uncertainty. 
 ## 2. LABORATORY OBJECTIVES 
Upon successful completion of the laboratory component, students will be able to: 
1. Implement intelligent software agents using Python and the Smart Python Agent 
Development Environment (SPADE) 
2. Model agent perception, goals, events, and actions within a dynamic environment 
3. Design and execute inter-agent communication using the Foundation for Intelligent Physical 
Agents – Agent Communication Language (FIPA-ACL) 
4. Apply the Prometheus methodology to real-world, distributed problem domains 
5. Build coordinated multi-agent systems for dynamic and uncertain environments 
6. Evaluate agent autonomy, coordination effectiveness, and system robustness 
## 3. TOOLS AND SOFTWARE REQUIREMENTS 
Mandatory Tools (Provided via GitHub Codespaces) 
• Python 3.9 or higher 
• SPADE (Smart Python Agent Development Environment) 
• Extensible Messaging and Presence Protocol (XMPP) Server 
o Prosody XMPP Server or ejabberd XMPP Server 
• Prometheus Design Tool (PDT) 
Supporting Tools 
• Draw.io or StarUML for Agent Unified Modeling Language (AUML) diagrams 
• Git for distributed version control 
• Visual Studio Code or PyCharm (accessed through Codespaces) 
## 4. PROJECT OVERVIEW 
Disaster Response & Relief Coordination System 
Problem Description 
Following a disaster event such as flooding, earthquakes, or fire outbreaks, emergency response 
operations must be coordinated rapidly under conditions of uncertainty, partial information, and 
limited resources. Centralized control systems are often unavailable, unreliable, or overloaded 
during such events. 
This project models a decentralized intelligent multi-agent system in which autonomous agents 
collaborate to: 
• Detect disaster events 
• Assess damage severity 
• Allocate rescue and response tasks 
• Manage limited relief and logistical resources 
The system emphasizes distributed decision-making, coordination, and resilience. 
Core Agent Types and Responsibilities 
Agent 
Responsibility 
SensorAgent 
Detects disaster events and reports environmental 
conditions 
RescueAgent 
LogisticsAgent 
Performs rescue operations 
Manages supplies and relief items 
CoordinatorAgent 
Assigns tasks, sets priorities, and coordinates agents 
## 5. LAB STRUCTURE 
Each laboratory session consists of: 
• Objective 
• Background 
• Practical Tasks 
• Deliverables 
• Assessment Criteria 
## LAB SESSIONS 
### LAB 1: ENVIRONMENT AND AGENT PLATFORM SETUP 
Objective 
To configure the Python agent development environment and deploy a basic agent. 
Background 
The Smart Python Agent Development Environment (SPADE) enables the creation of intelligent 
agents using asynchronous behaviors and message-based interaction over the Extensible Messaging 
and Presence Protocol (XMPP). 
Practical Tasks 
1. Launch the provided GitHub Codespaces environment 
2. Verify Python and SPADE installation 
3. Start the embedded XMPP server 
4. Create agent credentials 
5. Implement and execute a basic SPADE agent 
### Deliverables 
• Screenshot of a running agent in GitHub Codespaces 
• Python source code 
• Environment setup report (½ page) 
### LAB 2: PERCEPTION AND ENVIRONMENT MODELING 
Objective 
To implement agent perception of environmental and disaster-related events. 
Background 
Agents must sense their environment to guide decision-making and react to changes. 
Practical Tasks 
1. Implement a simulated disaster environment 
2. Create a SensorAgent that periodically monitors conditions 
3. Generate and log disaster events such as damage severity levels 
### Deliverables 
• SensorAgent code 
• Event logs 
• Brief explanation of percepts 